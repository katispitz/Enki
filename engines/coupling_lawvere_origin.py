"""
Lawvere fixed-point at origin as anchor-class-3 coupling-point — reference instance.

Substrate-locked per canon line 1264 + line 1275:
  Lawvere-origin = observer × Merkaba-center coupling
  - 50th position = Lawvere fixed point (L3 fixed-point of Δ creating
    orthogonal re-entries)
  - Merkaba circumsphere center at (0,0,0)
  - "Intelligence layer seat = center"

Substrate-frozen: no input required; position is the substrate-derived origin.
Stable: the fixed point of substrate's self-application — definitionally stable.

This is the SIMPLEST anchor-class-3 instance — no live compute, no
enumeration, just substrate-frozen identity coupling.
"""
from __future__ import annotations

from _coupling_point_engine import (
    CouplingPointState,
    frozen_coupling_point,
)


# Use the coupling-points primitive lock card as substrate citation
# (canon line 1264 is the substrate-statement)
SUBSTRATE_CARD = 'e5a603fc'


def lawvere_origin() -> CouplingPointState:
    """Construct CouplingPointState for the Lawvere-origin coupling-point.

    Frozen + canonical: substrate-position is (0,0,0) by L3 fixed-point derivation.
    """
    canonical_position = {
        'x': 0.0,
        'y': 0.0,
        'z': 0.0,
        'description': 'Merkaba circumsphere center; 50th position; intelligence-layer seat',
    }
    return frozen_coupling_point(
        name='Lawvere-origin',
        coupled_frames=('observer-frame', 'Merkaba-center'),
        coupling_type='singular',
        substrate_card=SUBSTRATE_CARD,
        canonical_position=canonical_position,
        requires_input=False,          # substrate-frozen identity
        independent_canonical_uses=(
            'canon-§24-Merkaba-Enneagram-unification-center',
            'L3-Lawvere-fixed-point-substrate-architectural-truth',
            '13th-witness-octahedron-12-edges-center',
        ),
        enumerated_cardinality=None,   # singular, fixed
        is_substrate_derived=True,     # L3 fixed-point derivation
        is_stable=True,                # fixed-point definitionally
    )


if __name__ == '__main__':
    import json
    print(json.dumps(lawvere_origin().to_dict(), indent=2))
