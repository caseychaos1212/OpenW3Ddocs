A-Skeleton Animation Inventory
==============================

This page lists 581 known A-skeleton animation names with hosted GIF previews
and working notes.

Skeleton A is the default male skeleton. Other skeletons can fall back to
Skeleton A animations when a more specific clip does not exist.

These entries are documented as general A-skeleton animations and are not
treated here as character-specific.

OpenW3D's normal human locomotion is state-driven in ``HumanStateClass``
rather than hardcoded clip-by-clip in mission scripts. The engine combines a
torso or weapon-hold family with a leg-style suffix to build the common
movement clips, typically in the form ``H_A_<holdstyle><legsuffix>``.

Common hold-style families include:

* ``A0`` hands down, empty hands, C4, and beacon baseline
* ``B0`` at chest or relaxed
* ``C1`` to ``C3`` shoulder hold, looking down to up
* ``D1`` to ``D3`` hip hold, looking down to up
* ``E2`` launcher hold
* ``F1`` to ``F3`` handgun hold, looking down to up

Common leg-style suffixes include:

* ``A0`` stand
* ``A1`` to ``A4`` run
* ``B1`` to ``B4`` walk
* ``C0`` to ``C6`` crouch and crouch-move
* ``J0`` to ``J4`` jump

Landings use a separate state-specific naming pattern:
``S_A_HUMAN.H_A_A0L0`` through ``S_A_HUMAN.H_A_A0L4``. The engine does not
append ``A0L0`` to a hold-style prefix.

Special states such as ladder, dive, wounded, death, fire or chem or electric
damage, hostage sequences, and mission cinematics can force specific
``H_A_*`` clips directly.

The notes below combine the inventory naming from the animation catalog with
explicit references found in the local OpenW3D source tree when a clip is
named in code.

Source review: `HumanStateClass naming and landing selection <https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/humanstate.cpp>`_
and `HumanAnimControlClass skeleton remapping <https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/animcontrol.cpp>`_.

.. include:: generated/a-skeleton-gallery.rst
