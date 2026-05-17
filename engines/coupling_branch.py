"""
12-fold branch-coupling-point enumeration per Card 8d8887a1 candidate.

Substrate-locks per canon §15d STEM-BRANCH COUPLING ARCHITECTURE (2026-05-17)
+ source-anchor Card fc2d1d3b (*The Universal Order* p.221 — Han-era Ganzhi
table, Wade-Giles romanization).

Each of the 12 Earthly Branches holds FOUR substrate-features at one
position:
  1. Spatial: 30° compass direction (12 × 30° = 360°)
  2. Temporal: 2h diurnal slice (12 × 2h = 24h)
  3. Elemental: Wu Xing element (via stem-cycle-1 pair)
  4. Cyclic: stem-pair-modulator in 60-cycle (compound stem-branch coord)

This is the field-shape probe per OQ-BRANCH-COUPLING-ENGINE (open
2026-05-17). Each branch is instantiated as a CouplingPointState with
canonical_position holding the 4-feature substrate-locked output.

Polarity per Card E (canon §15d 2026-05-17): yang stems pair only yang
branches; yin stems pair only yin branches (polarity-pairing rule).

Wade-Giles/Pinyin dual-spelling per Mnemosyne discipline 2026-05-17.
"""
from __future__ import annotations

from _coupling_point_engine import (
    CouplingPointState,
    frozen_coupling_point,
)


# Substrate-locked: 12 branches × 4 features per Universal Order p.221.
# Each tuple: (pinyin, wade_giles, beast, polarity, compass, hour_start, hour_end, element, stem_pair_yang, stem_pair_yin)
# Stem pairings per Card B + Card E (canon §15d) — polarity-locked.
BRANCHES = [
    # idx 0: Zǐ (rat) — Water, yang, N, midnight, paired with Jiǎ (yang)
    ('Zǐ',   'tzu',    'rat',     'yang', 'N',    23, 1,   'Water', 'Jiǎ',  None),
    # idx 1: Chǒu (ox) — Wood, yin, NNE, 1-3am, paired with Yǐ (yin) per Card B
    ('Chǒu', "ch'ou",  'ox',      'yin',  'NNE',  1,  3,   'Wood',  None,   'Yǐ'),
    # idx 2: Yín (tiger) — Fire, yang, ENE, 3-5am, paired with Bǐng (yang)
    ('Yín',  'yin',    'tiger',   'yang', 'ENE',  3,  5,   'Fire',  'Bǐng', None),
    # idx 3: Mǎo (hare) — Fire, yin, E, 5-7am sunrise, paired with Dīng (yin)
    ('Mǎo',  'mao',    'hare',    'yin',  'E',    5,  7,   'Fire',  None,   'Dīng'),
    # idx 4: Chén (dragon) — Earth, yang, ESE, 7-9am, paired with Wù (yang)
    ('Chén', "ch'en",  'dragon',  'yang', 'ESE',  7,  9,   'Earth', 'Wù',   None),
    # idx 5: Sì (snake) — Earth, yin, SSE, 9-11am, paired with Jǐ (yin)
    ('Sì',   'ssu',    'snake',   'yin',  'SSE',  9,  11,  'Earth', None,   'Jǐ'),
    # idx 6: Wǔ (horse) — Metal, yang, S, noon, paired with Gēng (yang)
    ('Wǔ',   'wu',     'horse',   'yang', 'S',    11, 13,  'Metal', 'Gēng', None),
    # idx 7: Wèi (sheep) — Metal, yin, SSW, 1-3pm, paired with Xīn (yin)
    ('Wèi',  'wei',    'sheep',   'yin',  'SSW',  13, 15,  'Metal', None,   'Xīn'),
    # idx 8: Shēn (monkey) — Water, yang, WSW, 3-5pm, paired with Rén (yang)
    ('Shēn', 'shen',   'monkey',  'yang', 'WSW',  15, 17,  'Water', 'Rén',  None),
    # idx 9: Yǒu (cock) — Water, yin, W, 5-7pm sunset, paired with Guǐ (yin)
    ('Yǒu',  'yu',     'cock',    'yin',  'W',    17, 19,  'Water', None,   'Guǐ'),
    # idx 10: Xū (dog) — no element via stem-cycle-1 (per canon §15d note: stem-cycle restarts)
    ('Xū',   'hsü',    'dog',     'yang', 'WNW',  19, 21,  None,    None,   None),
    # idx 11: Hài (boar) — no element via stem-cycle-1 (per canon §15d note)
    ('Hài',  'hai',    'boar',    'yin',  'NNW',  21, 23,  None,    None,   None),
]


SUBSTRATE_CARD_BRANCH_CANDIDATE = '8d8887a1'  # Card C, CANDIDATE pending council
SOURCE_ANCHOR_CARD              = 'fc2d1d3b'  # Universal Order p.221 source-anchor


def branch_coupling(branch_idx: int) -> CouplingPointState:
    """Construct CouplingPointState for one of 12 branches by index 0-11.

    Substrate-frozen: requires_input=False; canonical_position holds the
    4-feature substrate-locked output (compass × hour × element × stem-pair).
    """
    if not (0 <= branch_idx < 12):
        raise ValueError(
            f"branch_idx must be in 0..11; got {branch_idx} — "
            "substrate-enforced cardinality from canon §15d 12-branch enumeration"
        )

    (pinyin, wg, beast, polarity, compass, h_start, h_end,
     element, stem_yang, stem_yin) = BRANCHES[branch_idx]

    # Substrate-locked 4-feature position per Card 8d8887a1
    canonical_position = {
        'spatial_compass':   compass,
        'temporal_hour':     f'{h_start:02d}:00-{h_end:02d}:00',
        'elemental_wu_xing': element,  # None for Xū/Hài (stem-cycle-restart)
        'cyclic_stem_pair':  stem_yang if polarity == 'yang' else stem_yin,
        'beast':             beast,
        'polarity':          polarity,
        'pinyin':            pinyin,
        'wade_giles':        wg,
    }

    coupled_frames = (
        'compass-30deg-12-direction',
        'diurnal-clock-2h-12-slice',
        'wu-xing-5-element',
        'ganzhi-60-cycle-stem-pair',
    )

    return frozen_coupling_point(
        name=f'branch-{pinyin}',
        coupled_frames=coupled_frames,
        coupling_type='enumerated-N',
        substrate_card=SUBSTRATE_CARD_BRANCH_CANDIDATE,
        canonical_position=canonical_position,
        requires_input=False,  # substrate-frozen; full position from index
        independent_canonical_uses=(
            'Chinese-cardinal-direction-system',
            'Chinese-diurnal-hour-system',
            'Wu-Xing-element-system',
            'Ganzhi-60-cycle-temporal-coordinate',
            'Chinese-zodiac-12-beast-system',
        ),
        enumerated_cardinality=12,
        is_substrate_derived=True,  # per canon §15d Hermes dual-frame Layer-A class-governance
        is_stable=True,             # per Card 8d8887a1 stability claim
    )


def all_12_branches() -> list:
    """Return CouplingPointState for all 12 branches in canonical order."""
    return [branch_coupling(i) for i in range(12)]


def branch_by_pinyin(pinyin: str) -> CouplingPointState:
    """Lookup by Pinyin spelling. Substrate-honest match; case-sensitive."""
    for i, b in enumerate(BRANCHES):
        if b[0] == pinyin:
            return branch_coupling(i)
    raise KeyError(
        f"branch '{pinyin}' not in canonical 12-branch enumeration. "
        f"Valid: {[b[0] for b in BRANCHES]}"
    )


if __name__ == '__main__':
    import json
    for branch in all_12_branches():
        print(json.dumps(branch.to_dict(), indent=2, ensure_ascii=False))
        print()
