B-Skeleton Animation Inventory
==============================

This page lists 158 known B-skeleton animation names with hosted GIF previews
and working notes.

Skeleton B is the default female human skeleton.

OpenW3D's normal human locomotion is state-driven in ``HumanStateClass``
rather than hardcoded clip-by-clip in mission scripts. The engine builds the
common B-skeleton movement set with the same hold-style and leg-style naming
pattern used on Skeleton A, typically in the form ``H_B_<holdstyle><legsuffix>``.

When code requests an ``S_A_HUMAN.H_A_*`` clip on a non-A human skeleton,
``HumanAnimControlClass`` first tries the matching B-skeleton name. If a
B-specific clip is missing, playback falls back to the original A clip.

This export mostly covers stand, run, walk, pose, and mission-specific
cinematic clips rather than the full A-skeleton state set.

Common hold-style families in this set include:

* ``A0`` hands down, empty hands, C4, and beacon baseline
* ``B0`` at chest or relaxed
* ``C1`` to ``C3`` shoulder hold, looking down to up
* ``D1`` to ``D3`` hip hold, looking down to up
* ``F1`` to ``F3`` handgun hold, looking down to up

Common leg-style suffixes in this set include:

* ``A0`` stand
* ``A1`` to ``A4`` run
* ``B1`` to ``B4`` walk

Numbered suffixes such as ``_02`` or ``_14`` usually indicate alternate takes
or pose variants on the same base locomotion name.

The notes below combine naming-pattern descriptions with explicit OpenW3D
source references when a clip is named in code.

.. include:: generated/b-skeleton-gallery.rst
