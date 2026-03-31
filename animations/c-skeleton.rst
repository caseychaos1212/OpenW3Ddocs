C-Skeleton Animation Inventory
==============================

This page lists 24 known C-skeleton animation names with hosted GIF previews
and working notes.

Skeleton C is the mutant skeleton.

OpenW3D still routes human animation names through ``HumanAnimControlClass``.
When code requests an ``S_A_HUMAN.H_A_*`` clip on a non-A human skeleton, the
engine first tries the matching ``S_C_HUMAN.H_C_*`` name and only stays on the
A clip if no C-specific version exists.

The mutant set is much smaller than the A or B inventories. Its common
movement clips mostly use the ``H_C_A0*`` baseline for stand, run, and walk,
then add a small number of mutant-specific special-state and mission clips.

Shared A-named clips can also appear in this export when the mutant set reuses
an A-style animation directly.

Common locomotion suffixes in this set include:

* ``A0`` stand
* ``A1`` to ``A4`` run
* ``B1`` to ``B4`` walk

The ``A0A0_L*`` names in this set are special mutant clips rather than the
full directional landing library seen on Skeleton A.

The notes below combine naming-pattern descriptions with explicit OpenW3D
source references when a clip is named in code.

.. include:: generated/c-skeleton-gallery.rst
