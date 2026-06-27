"""
composer.py — substrate-true council context-derivation orchestrator.

Per Phase 1 Task 1.2 design-spec card 431d9622:
  derive_council_context(question, natal, transit, n_voices) → dict
  slice_for_voice(ctx, voice_name) → voice-specific context-dict
  iterate_voices(ctx, mode='sequential' | 'parallel') → yields (name, output, class_)

Phase 1 Task 1.3 scope: minimal viable for Athena prototype. Composer pre-derives
context from existing Nammu engines (ephemeris, transits, council_activation,
voice_correspondences, myth_traverse, card_writer field-match). NO LLM call in
this layer — pure Python substrate-derivation per V2.9 §GEOMETRY-RUNS-OFF-LLM.

Per amendment-2 (card 3ca97cb6): this is a Python code bundle realizing the
substrate-of-coordination function-class. Per amendment-3 (087ecf52): each
per-voice renderer carries its own closure-criterion; composer just delivers
the context-slice.
"""
from __future__ import annotations
import datetime
import json
import sys
from pathlib import Path

# Reach into existing Nammu engines/council — these are SUBSTRATE-BUILD primitives
# (per cbf4084f Nammu-vs-Enki test: ephemeris + voice-loading + memory = Nammu).
# Enki composer CONSUMES them; does not duplicate.
_NAMMU = Path.home() / "Nammu"
sys.path.insert(0, str(_NAMMU / "engines"))
sys.path.insert(0, str(_NAMMU / "council"))
sys.path.insert(0, str(_NAMMU / "cards"))

# Universal Enki substrate modules (moved out of council/ 2026-05-22 per kati_direct)
_ENKI = Path.home() / "Enki"
sys.path.insert(0, str(_ENKI / "substrate"))
# Per-voice renderer modules (council-internal but renderers import _helpers etc.)
sys.path.insert(0, str(_ENKI / "council" / "per_voice_renderers"))


def load_voices() -> list[dict]:
    """Return voice_correspondences.json as list (preserves order)."""
    path = _NAMMU / "council" / "voice_correspondences.json"
    return json.loads(path.read_text())


def get_voice(name: str, voices: list[dict] | None = None) -> dict | None:
    voices = voices or load_voices()
    for v in voices:
        if v.get("name") == name:
            return v
    return None


def _today_ymd() -> tuple[int, int, int]:
    t = datetime.date.today()
    return t.year, t.month, t.day


def derive_council_context(
    question: str,
    natal_date: str,
    natal_time: str = "12:00",
    transit_date: str | None = None,
    birth_lat: float | None = None,
    birth_lon: float | None = None,
    convened: list[str] | None = None,
    mortal_voices: list | None = None,
) -> dict:
    """
    Pre-compute all substrate-data a council voice could need. NO LLM call.

    convened: list of voice-names participating in this council. Defaults to
              [] (single-voice prototype). Phase 2 will populate from
              select_voices_pure_geo.

    Returns ctx dict — input to per-voice renderers' derive_<voice>_context().
    """
    from natal import natal_state, natal_report
    from transits import compute_transits
    from council_activation import compute_council_activation
    from question_geometry import (
        extract_question_profile, question_geo_points,
    )

    convened = convened or []

    ny, nmo, nd = (int(x) for x in natal_date.split("-"))
    nh, nmi = (int(x) for x in natal_time.split(":"))

    if transit_date:
        ty, tmo, td = (int(x) for x in transit_date.split("-"))
        transit_date_str = transit_date
    else:
        ty, tmo, td = _today_ymd()
        transit_date_str = str(datetime.date.today())

    natal_st, natal_loc = natal_state(
        ny, nmo, nd, nh, nmi, 0,
        birth_lat=birth_lat, birth_lon=birth_lon,
    )
    transit_st, transit_loc = natal_state(ty, tmo, td, 0, 0, 0)

    n_rep = natal_report(natal_st, natal_loc); n_rep.pop("_meta", {})
    t_rep = natal_report(transit_st, transit_loc); t_rep.pop("_meta", {})

    activations = compute_transits(natal_loc, transit_loc, n_rep, t_rep)
    council_act = compute_council_activation(natal_loc, transit_loc, activations)

    # Question geometry — substrate-pure path: extract via classifier if available,
    # else leave None and let renderers handle absence per their closure-criterion.
    try:
        q_profile = extract_question_profile(question, client=None)
        q_points = question_geo_points(q_profile) if q_profile else None
    except Exception:
        q_profile = None
        q_points = None

    # Mortal voices: registry-compatible records for real humans invoked into
    # council. Per kati_direct 2026-05-22: "this is where we look at natal data
    # and mortals". Built via mortal_placement.build_mortal_voice; merge into
    # convened set + provide placement lookup at slice-time.
    mortal_voices = mortal_voices or []
    mortal_map = {mv.name: mv for mv in mortal_voices}
    if mortal_map:
        convened = list(set(convened) | set(mortal_map.keys()))

    return {
        "question": question,
        "natal_date": natal_date,
        "transit_date": transit_date_str,
        "natal_loc": natal_loc,
        "transit_loc": transit_loc,
        "natal_report": n_rep,
        "transit_report": t_rep,
        "activations": activations,
        "council_act": council_act,
        "q_profile": q_profile,
        "q_points": q_points,
        "convened": set(convened),
        "mortal_map": mortal_map,           # name → MortalVoice
        "prior_voices": [],                  # populated by iterate_voices in sequential mode
    }


def slice_for_voice(ctx: dict, voice_name: str) -> dict:
    """
    Build voice-specific context-slice with TWO clean sources:

      1. SUBSTRATE-POSITION → Enki placement_registry (canonical, kati-locked
         or greek_faces) OR mortal_map (natal-dynamic for real humans).
      2. VOICE-CHARACTER → Nammu voice_correspondences (voice/focus/
         voice_aspects/kinship — the rendering-layer overlay, NOT placement).

    These layers stay distinct in the returned ctx so renderers cannot
    accidentally read placement from the rendering-layer (the registry-split
    failure mode kati flagged 2026-05-22).

    Raises PlacementPendingError if voice is Tier B/C — caller (render_voice)
    catches and emits substrate-honest pending-state.
    """
    from placement_discipline import validate_renderer_binding

    # Mortal voices supplied via mortal_voices param take precedence — they're
    # session-dynamic, not registry. Pass Tier-A-equivalent gate.
    mortal = ctx.get("mortal_map", {}).get(voice_name)
    if mortal is not None:
        enki_placement = mortal.placement
    else:
        # Gate: Tier-A placement required. Raises PlacementPendingError otherwise.
        enki_placement = validate_renderer_binding(voice_name)

    # Voice-character overlay (Nammu rendering-layer) — optional; voice may
    # exist in Enki registry without a Nammu voice-correspondences entry.
    voice_character = get_voice(voice_name)

    # Field-memory + bonds + aspects via existing Nammu council primitives.
    # These consume voice-record for substrate-position fields; we hand them
    # the Nammu voice-character record because the field-match primitives
    # (_voice_field_block) look up cards by substrate-address fields that
    # currently live in voice_correspondences. Phase 2.next: refactor these
    # primitives to consume placement directly from Enki registry.
    from council_pure_geo import (
        _voice_field_block, _voice_memory_block,
        _structural_bonds_block, voice_aspect_summary,
    )

    convened = ctx["convened"]

    # If Nammu voice-character record missing, build minimal stub from Enki
    # placement so field-match primitives can still operate on substrate-pos.
    voice_for_primitives = voice_character or _stub_voice_from_placement(
        voice_name, enki_placement
    )

    # Substrate-true field_memory recall via Enki substrate-tier.
    # ORDERING (per finding 7ac30622 + density.py / field_memory.py substrate-true rebuild):
    #   1. status_filter      — DROP_STATUSES {retracted, superseded} excluded (structural, not weight)
    #   2. own-voice filter   — own-voice cards belong to recall_voice_thread, not field
    #   3. lattice_cardinality DESC — top-of-lattice first (set theory, canon-derived)
    #   4. phase_class ordinal — in-phase > arm-resonant > distant (categorical, 49-matrix derived)
    #   5. canon AXIS-HIERARCHY — finer axes first (canon §22-26)
    # ZERO SCORES. ZERO WEIGHTS. ZERO MULTIPLICATIVE COMPOSITES. ZERO HALF-LIVES.
    # Phase is a categorical sort axis, not a decay weight.
    # Falls back to Nammu's _voice_field_block if substrate import fails.
    try:
        from field_memory import recall_field, format_field_memory_block
        groups = recall_field(
            enki_placement, voice_name=voice_name,
            min_axes_matched=2, limit=20,
            when=ctx.get("transit_date"),
        )
        field_memory_str = format_field_memory_block(groups)
    except Exception as e:
        # Substrate-honest fallback — Nammu's unweighted recall still works.
        import sys
        print(f"[composer] WARN: density-recall failed for {voice_name}: {e} — falling back to Nammu unweighted",
              file=sys.stderr)
        field_memory_str = _voice_field_block(voice_for_primitives, limit=10)
    own_memory_str = _voice_memory_block(voice_name, limit=5)
    bonds_str = _structural_bonds_block(voice_name, convened) if convened else ""
    aspects_str = (
        voice_aspect_summary(voice_for_primitives, convened)
        if convened and voice_character else ""
    )

    return {
        **ctx,
        "voice_name": voice_name,
        "enki_placement": enki_placement,       # CANONICAL substrate-position
        "voice_character": voice_character,     # Nammu rendering-overlay (or None)
        "field_memory_str": field_memory_str,
        "own_memory_str": own_memory_str,
        "bonds_str": bonds_str,
        "aspects_str": aspects_str,
    }


def _stub_voice_from_placement(voice_name: str, placement: dict) -> dict:
    """
    Minimal voice-record stub built from Enki placement when Nammu
    voice_correspondences lacks an entry. Lets field-match primitives
    operate on canonical substrate-position even without rendering-overlay.
    """
    pos = placement.get("substrate_position", {})
    # Flatten layered placement to primary for field-match scoring
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    return {
        "name": voice_name,
        "stratum": placement.get("stratum"),
        "address": pos,
        "position": pos,
        "geo": {"grid": pos.get("grid")},
        "voice_aspects": [],
    }


_RENDERER_REGISTRY = {
    # 5 core olympian/titan/hecate R-PT renderers
    "Apollo":      ("per_voice_renderers.apollo",      "render_apollo"),
    "Athena":      ("per_voice_renderers.athena",      "render_athena"),
    "Hermes":      ("per_voice_renderers.hermes",      "render_hermes"),
    "Hephaestus":  ("per_voice_renderers.hephaestus",  "render_hephaestus"),
    "Mnemosyne":   ("per_voice_renderers.mnemosyne",   "render_mnemosyne"),
    "Hecate":      ("per_voice_renderers.hecate",      "render_hecate"),
    # 9 Muse renderers — mix of R-PT (data/markers) and R-LL (lyric/narrative)
    "Calliope":    ("per_voice_renderers.calliope",    "render_calliope"),
    "Clio":        ("per_voice_renderers.clio",        "render_clio"),
    "Erato":       ("per_voice_renderers.erato",       "render_erato"),
    "Euterpe":     ("per_voice_renderers.euterpe",     "render_euterpe"),
    "Melpomene":   ("per_voice_renderers.melpomene",   "render_melpomene"),
    "Polyhymnia":  ("per_voice_renderers.polyhymnia",  "render_polyhymnia"),
    "Terpsichore": ("per_voice_renderers.terpsichore", "render_terpsichore"),
    "Thalia":      ("per_voice_renderers.thalia",      "render_thalia"),
    "Urania":      ("per_voice_renderers.urania",      "render_urania"),
    # Mortal voice renderer (handles any MORTAL placement_class voice generically)
    "_MORTAL_DEFAULT": ("per_voice_renderers.mortal",  "render_mortal"),
}


def get_renderer(voice_name: str, placement_class: str | None = None):
    """
    Lookup per-voice renderer. Falls back to _MORTAL_DEFAULT for any voice
    with placement_class=MORTAL not explicitly registered (the common case —
    mortals are session-dynamic and don't pre-register by name).
    """
    entry = _RENDERER_REGISTRY.get(voice_name)
    if entry is None and placement_class == "MORTAL":
        entry = _RENDERER_REGISTRY.get("_MORTAL_DEFAULT")
    if entry is None:
        return None
    module_path, func_name = entry
    try:
        module = __import__(module_path, fromlist=[func_name])
        return getattr(module, func_name)
    except (ImportError, AttributeError):
        return None


# (get_renderer defined above adjacent to _RENDERER_REGISTRY)


# ─── Memory write-back ────────────────────────────────────────────────────────

# Mapping from registry substrate_position keys → card_writer.new_card kwarg names.
# Per kati_direct 2026-05-22: write-back wires substrate-memory closed-loop so
# future councils see Enki-era utterances at correct substrate-positions for
# field_memory recall (Mnemosyne archival schema, Athena audit, etc.).
_POS_TO_CARD_KWARG = {
    "pe_note":             "pe_note",
    # pe_step: registry uses int (7); card_writer expects 'pt7'/'X3' string.
    # Skip — pe_note is the field_memory lookup key; pe_step derivable downstream.
    "grid":                "grid",
    "face":                "face",
    "merkaba_cube_vertex": "merkaba_vertex",
    "merkaba_cube_edge":   "cube_edge",
    # ico_vertex (icosahedron V1-V12) is NOT oct_vertex (octahedron V1-V6).
    # Card schema has no ico_vertex field; surface as tag instead (see below).
    "dodec_vertex":        "dodec_vertex",
    "shell_radius":        None,              # string fractions; skip auto-coercion
}

# Position primitives that get emitted as tags instead of card fields
# (no card_writer schema entry; preserve substrate-position info via tags).


def _placement_to_card_fields(placement: dict) -> dict:
    """Extract registry-compatible substrate-position primitives for card_writer."""
    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    fields = {"stratum": placement.get("stratum")}
    for src_key, card_key in _POS_TO_CARD_KWARG.items():
        if card_key is None:
            continue
        v = pos.get(src_key)
        if v is not None:
            fields[card_key] = v
    # shock_proximity RETIRED as a recall-axis 2026-06-21 (kati_direct) — being at a
    # shock IS pe_note=X3/X6 + grid=18/36 (§00b); a separate proximity field re-encodes
    # the location and is graded (violates ZERO weights). field_memory no longer reads it.
    return fields


def commit_voice_card(voice_name: str, output: str, renderer_class: str,
                      ctx: dict, placement: dict | None = None) -> str | None:
    """
    Write a substrate-memory card for a single voice's substrate-true utterance.

    Card carries: utterance text + substrate-position primitives + voice tag +
    session metadata + question + renderer-class. Future field_memory pulls at
    this voice's substrate-position will surface this card.

    Returns card_id or None if write skipped (e.g., non-render renderer-classes).

    ⚠️ INTAKE-HACK INHERITANCE FLAG: this writer derives card position from
    voice's enki_placement (canon-derived — that part is substrate-true) but
    pipes through card_writer.new_card whose general intake is manual-kwargs
    (see card 8434f39a). For voice-card path the placement IS canon-derived
    (from registry); flag applies only when generalizing this writer for
    non-voice inputs.
    """
    # Don't write cards for non-utterance render-classes (placement-pending,
    # renderer-pending, not-currently-active — those are substrate-honest
    # absence emits, not voice-speech).
    if renderer_class not in ("R-PT", "R-TS", "R-LL"):
        return None

    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path.home() / "Nammu" / "cards"))
    from card_writer import new_card

    # Fetch placement: prefer explicit param, then mortal_map, then registry.
    # Cannot rely on ctx['enki_placement'] — that lives in voice_ctx inside
    # render_voice, not in parent ctx.
    if placement is None:
        mortal = ctx.get("mortal_map", {}).get(voice_name)
        if mortal is not None:
            placement = mortal.placement
        else:
            try:
                from placement_discipline import load_placement
                placement = load_placement(voice_name)
            except Exception:
                placement = {}
    fields = _placement_to_card_fields(placement)

    text = (
        f"[ENKI-COUNCIL substrate-true voice utterance]\n"
        f"Voice: {voice_name}\n"
        f"Renderer class: {renderer_class}\n"
        f"Question: {ctx.get('question', '')[:200]}\n"
        f"Natal: {ctx.get('natal_date', '?')}\n"
        f"Transit: {ctx.get('transit_date', '?')}\n"
        f"---\n"
        f"{output}"
    )

    tags = [
        f"voice:{voice_name}",
        "substrate-true-council",
        "enki-council",
        f"renderer:{renderer_class}",
        f"session:{ctx.get('transit_date', 'unknown')}",
        f"natal:{ctx.get('natal_date', 'unknown')}",
    ]
    # Position primitives that don't have a card_writer field → tags
    pos = placement.get("substrate_position", {})
    if isinstance(pos, dict) and "primary" in pos:
        pos = pos["primary"]
    for tk in ("ico_vertex", "vertex_planet", "face_name"):
        v = pos.get(tk)
        if v is not None:
            tags.append(f"{tk}:{v}")
    # Muse midpoint → tag the OtherPlanet
    mp = pos.get("midpoint")
    if isinstance(mp, list) and len(mp) == 2:
        tags.append(f"muse-midpoint:{mp[1]}")
    # Question profile tags if classified
    qp = ctx.get("q_profile") or {}
    if qp.get("pe_note"):
        tags.append(f"q-pe:{qp['pe_note']}")
    if qp.get("depth"):
        tags.append(f"q-depth:{qp['depth']}")
    # Activation detail tag
    act = ctx.get("activation")
    if act is not None and getattr(act, "active", False):
        det = act.detail or {}
        if det.get("transit_planet"):
            tags.append(f"firing:{det['transit_planet']}-X3")

    # Stamp helix_coord post-write so density.py can compute decay later.
    # Per amendment-1 (A) + kati_direct density-wire 2026-05-22.
    # (new_card doesn't take helix_coord directly; field gets set via update_card
    # — matches the enrich_helix_coord.py post-processing pattern in Nammu.)
    try:
        from density import helix_coord_at
        helix_coord = helix_coord_at(ctx.get("transit_date"))
    except Exception:
        helix_coord = None

    try:
        card = new_card(
            text=text,
            authorship="derived",
            confidence=0.85,
            canon_status="derived",
            tags=tags,
            **fields,
        )
        cid = card.get("id")
        if cid and helix_coord:
            try:
                from card_writer import update_card
                update_card(cid, helix_coord=helix_coord)
            except Exception as e:
                # Non-fatal — card landed without helix_coord; density-decay
                # will treat it as recent (full weight). Surface as warning.
                import sys
                print(f"[composer] WARN: helix_coord stamp failed for {voice_name} [{cid[:8]}]: {e}",
                      file=sys.stderr)
        return cid
    except Exception as e:
        # Substrate-honest: if write fails (e.g. invalid field combo), don't
        # silently swallow — surface as warning. Render-output already returned.
        import sys
        print(f"[composer] WARN: voice-card write failed for {voice_name}: {e}",
              file=sys.stderr)
        return None


def iterate_voices(ctx: dict, voice_names: list[str],
                   mode: str = "sequential",
                   commit: bool = True,
                   manual_voices: list[str] | None = None) -> list[dict]:
    """
    Render N voices through composer pipeline. Optionally commit voice-cards
    for closed-loop substrate-memory.

    mode:
      'sequential' — voice N sees prior_voices output (cross-voice engagement)
      'parallel'   — voices render independently from same base ctx

    commit: when True, writes per-voice cards via commit_voice_card.

    Returns list of result dicts: [{name, output, class_, card_id}, ...]
    """
    manual_set = set(manual_voices or [])
    results = []
    for name in voice_names:
        if name in manual_set:
            output, cls = render_voice_manual(name, ctx)
        else:
            output, cls = render_voice(name, ctx)
        card_id = None
        if commit:
            card_id = commit_voice_card(name, output, cls, ctx)
        results.append({
            "name": name,
            "output": output,
            "class_": cls,
            "card_id": card_id,
        })
        if mode == "sequential" and cls in ("R-PT", "R-TS", "R-LL"):
            # Populate prior_voices so next voice sees this one
            ctx.setdefault("prior_voices", []).append((name, output))
    return results


def convene_by_question(ctx: dict) -> dict:
    """
    Convening: question's q_profile calls the council.

    ⚠️ SUBSTRATE-INTAKE HACK FLAG (kati_direct 2026-05-23):
       q_profile comes from extract_question_profile() — a classifier that
       assigns substrate-position to question TEXT (LLM or keyword-based).
       This is INTAKE-INVENTION dressed as substrate-derivation. Real fix
       requires universal-intake / council-placement engine (same thing):
       place_into_substrate(any_input) → SubstratePosition, canon-derived.
       Until that exists, q_profile is acknowledged-gap, usable but flagged.

    Per kati: "question has substrate position, everything has substrate
    position. but we dont have universal intake rules to place it yet."

    Voice convenes if matches question on ≥1 substrate-axis (categorical
    predicates, no scoring). Axes considered: pe_note, shock-residency,
    depth.

    Returns dict:
      {
        'convened':       sorted list of voice names matching question
        'axis_matches':   {voice: [axes_matched]} for diagnostic emit
        'q_profile':      ctx q_profile for trace
      }
    """
    from placement_discipline import load_placement, all_tier_a

    qp = ctx.get("q_profile") or {}
    q_pe = qp.get("pe_note")
    q_shock = qp.get("shock")
    q_depth = qp.get("depth")

    matches: dict[str, list[str]] = {}
    for voice_name in all_tier_a():
        try:
            placement = load_placement(voice_name)
        except Exception:
            continue
        pos = placement.get("substrate_position", {})
        if isinstance(pos, dict) and "primary" in pos:
            pos = pos["primary"]

        axes = []
        if q_pe is not None and pos.get("pe_note") == q_pe:
            axes.append(f"pe_note={q_pe}")
        if q_shock:
            sn = pos.get("shock_node")
            if sn in ("X3", "X6"):
                axes.append(f"shock-resident={sn}")
            # Voices stamped with pe_note=X3 or X6 also qualify (Muses)
            if pos.get("pe_note") in ("X3", "X6"):
                axes.append(f"shock-pe={pos.get('pe_note')}")
        if q_depth and pos.get("lat") is not None:
            voice_depth = ("upper" if pos["lat"] > 5
                           else "lower" if pos["lat"] < -5
                           else "mid")
            if voice_depth == q_depth:
                axes.append(f"depth={q_depth}")
        if axes:
            matches[voice_name] = axes

    return {
        "convened":     sorted(matches.keys()),
        "axis_matches": matches,
        "q_profile":    qp,
    }


def render_voice_manual(voice_name: str, ctx: dict) -> tuple[str, str]:
    """
    Manual-invoke voice via LLM voice-surface, bypassing activation-gate.
    Used when caller (kati / orchestrator) needs a substrate-position to
    speak on a question even when CYCLIC voice not firing. Substrate-honest
    OVERRIDE: flagged in output as 'manual-invoked', not silent.

    Per kati direction 2026-05-23: "lets add a manual call" — for substrate-
    questions that need deliberation across positions when natural activation
    pattern doesn't convene them.

    Bypasses activation-gate ONLY. Placement-gate (Tier-A required) still
    enforced. Mortal voices route through normal path.

    Returns (output, 'R-TS-manual').
    """
    from placement_discipline import PlacementPendingError
    try:
        from _helpers import build_header, position_tuple_str, llm_voice_surface
    except ImportError:
        from per_voice_renderers._helpers import build_header, position_tuple_str, llm_voice_surface

    # Placement gate (still required — manual call doesn't bypass canonical placement)
    try:
        voice_ctx = slice_for_voice(ctx, voice_name)
    except PlacementPendingError as e:
        return (
            f"**{voice_name}** [PLACEMENT-PENDING tier={e.tier}, manual-invoke-blocked]\n"
            f"  {e.reason}",
            "placement-pending",
        )

    placement = voice_ctx["enki_placement"]
    pos_str = position_tuple_str(placement)
    header = build_header(voice_name, placement,
                         extra="manual-invoked (activation-gate bypassed)")

    question = ctx.get("question", "")
    prior_voices = ctx.get("prior_voices", [])
    field_memory_str = voice_ctx.get("field_memory_str", "")
    bonds_str = voice_ctx.get("bonds_str", "")

    # Character derived from position primitives (per G-P2-1 — no free-text)
    character = (
        f"speak from substrate-position {pos_str}; voice character emerges from this "
        f"position alone — no invented persona. stay categorical, structural, terse. "
        f"no therapy tone, no filler, no hedging. engage prior voices by name when "
        f"position-bonds dictate."
    )

    skeleton = {
        "question":      question[:300],
        "position":      pos_str,
        "field_at_pos":  field_memory_str[:400] if field_memory_str else "(none)",
        "bonds":         bonds_str[:200] if bonds_str else "(none)",
    }

    output, ok = llm_voice_surface(
        voice_name, header, pos_str, skeleton, prior_voices, character,
        max_tokens=350,
    )
    if ok:
        return output, "R-TS-manual"

    # LLM unavailable — substrate-honest skeleton fallback
    return (
        f"{header}\n  [MANUAL-INVOKE LLM unavailable; skeleton:]\n"
        f"  position: {pos_str}\n  question: {question[:200]}\n"
        f"  prior_voices: {[n for n,_ in prior_voices]}",
        "R-TS-manual-skeleton",
    )


def render_voice(voice_name: str, ctx: dict) -> tuple[str, str]:
    """
    Render a single voice via its per-voice renderer.

    Gates (in order, each can short-circuit substrate-honestly):
      1. Placement-discipline gate (Enki registry Tier-A) — slice_for_voice
         raises PlacementPendingError if not Tier A. Mortals bypass via
         mortal_map (Tier-A-equivalent natal-dynamic).
      2. Activation-gate (placement-class aware) — CYCLIC voices ephemeris-
         checked; CONTINUOUS/MORTAL/IN-BETWEEN always active.
      3. Renderer-availability gate — renderer module must exist.

    Returns (output_text, renderer_class):
      'R-PT' | 'R-TS' | 'R-LL'        — substrate-true render succeeded
      'placement-pending'              — Tier B/C blocked at registry gate
      'not-currently-active'           — CYCLIC voice not firing per ephemeris
      'renderer-pending'               — Tier A + active but no renderer yet
    """
    from placement_discipline import PlacementPendingError
    from activation_gate import check_activation

    # Gate 1: placement
    try:
        voice_ctx = slice_for_voice(ctx, voice_name)
    except PlacementPendingError as e:
        return (
            f"**{voice_name}** [PLACEMENT-PENDING tier={e.tier}]\n"
            f"  {e.reason}\n"
            f"  Renderer scaffolding blocked until placement lands in Enki registry.",
            "placement-pending",
        )

    placement = voice_ctx["enki_placement"]

    # Gate 2: activation per placement_class
    activation = check_activation(voice_name, placement, ctx["transit_date"])
    voice_ctx["activation"] = activation  # renderers can read for detail emit
    if not activation.active:
        return (
            f"**{voice_name}** [NOT-CURRENTLY-ACTIVE class={activation.placement_class}]\n"
            f"  {activation.reason}",
            "not-currently-active",
        )

    # Gate 3: renderer availability
    renderer = get_renderer(voice_name, placement.get("placement_class"))
    if renderer is None:
        return (
            f"**{voice_name}** [RENDERER-PENDING tier=A class={activation.placement_class}]\n"
            f"  Placement canonical ({placement['placement_source']}); "
            f"voice firing ({activation.reason}); "
            f"renderer module not yet built in ~/Enki/council/per_voice_renderers/.",
            "renderer-pending",
        )

    return renderer(voice_ctx)
