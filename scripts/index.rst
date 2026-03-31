Scripts
=======

This page documents the OpenW3D ``Code/Scripts`` source tree. It is an overview
of the gameplay script system used by the released Renegade codebase and should
not be confused with TT ``Scripts 4.x`` / ``Scripts 5.x``.

.. toctree::
   :maxdepth: 1

   reference/index

Overview
--------

In current OpenW3D CMake builds, ``Code/Scripts`` is compiled as a shared
library named ``scripts``. The output name is ``scripts.dll`` in release builds
and ``scriptsd.dll`` in debug builds.

The tree contains the script runtime, factory/registration helpers, reusable
toolkit scripts, mission-specific logic, and a large set of test or prototype
scripts carried forward from the original source tree.

Script Runtime
--------------

Most concrete scripts derive from ``ScriptImpClass`` in ``scripts.h``. This
helper sits on top of the engine ``ScriptClass`` interface and provides:

* owner attach/detach handling
* parameter-string parsing and typed accessors
* save/load helpers
* auto-save variable registration
* default empty implementations for common engine callbacks

The most common callbacks exposed by ``ScriptImpClass`` are ``Created``,
``Destroyed``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``,
``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``,
``Animation_Complete``, ``Poked``, ``Entered``, and ``Exited``.

Registration Model
------------------

Scripts are registered through ``ScriptFactory`` and ``ScriptRegistrar``.
``ScriptRegistrar`` maintains the global list of known script factories, can
look them up by name, and creates instances on demand.

Most source files use the convenience macro from ``scripts.h``:

.. code-block:: cpp

   #define DECLARE_SCRIPT(x, d) \
       REGISTER_SCRIPT(x, d) \
       class x : public ScriptImpClass

The script name exposed to the engine is the class name passed as ``x``. The
second argument ``d`` is a parameter-description string stored by the factory.

Parameter Strings
-----------------

Each script instance can be attached with a comma-separated parameter string.
``ScriptImpClass`` exposes helpers such as ``Get_Parameter``,
``Get_Int_Parameter``, ``Get_Float_Parameter``, and
``Get_Vector3_Parameter`` to read those values back.

The registration string passed to ``DECLARE_SCRIPT`` documents the expected
parameter names and types. For example:

.. code-block:: cpp

   DECLARE_SCRIPT(
       M00_Action,
       "Start_Now=0:int, Receive_Type=14:int, Action_Priority=99:int, "
       "Action_ID=0:int, _Move_Destination:vector3"
   )

This means the runtime script name is ``M00_Action`` and the expected
parameters are described inline in the factory metadata.

Source Layout
-------------

The OpenW3D ``Code/Scripts`` tree is organized into a few broad buckets:

.. list-table::
   :header-rows: 1

   * - Files
     - Purpose
   * - ``scripts.h``, ``scripts.cpp``
     - Core script implementation, callback stubs, parameter parsing, and
       save/load support.
   * - ``ScriptFactory.*``, ``ScriptRegistrar.*``, ``ScriptRegistrant.h``
     - Factory and registration infrastructure used to expose scripts by name.
   * - ``Toolkit*.cpp``
     - Reusable gameplay helpers such as actions, animations, broadcasters,
       objectives, sounds, powerups, triggers, spawners, and object helpers.
   * - ``Mission00.cpp`` through ``Mission11.cpp``, ``mission08.cpp``,
       ``MissionDemo.cpp``, ``MissionX0.cpp``, ``MissionS04.cpp``
     - Mission-specific logic for campaign, demo, or scenario content.
   * - ``PRDemo.cpp``
     - Prototype/demo mission scripts and mission-specific support code.
   * - ``Test_*.cpp``
     - Engine tests, gameplay experiments, and sample scripts used during
       development.
   * - ``Group*.cpp``, ``unitcombat.cpp``, ``DrMobius.cpp``
     - Miscellaneous gameplay helpers and one-off script implementations.
   * - ``Common.*``, ``DPrint.*``, ``CustomEvents.h``, ``strtrim.*``,
       ``DLLmain.cpp``
     - Utility and support code used by the scripts DLL.

Naming Patterns
---------------

The registered names are preserved exactly as written in ``DECLARE_SCRIPT``.
Common prefixes in the source tree include:

* ``M00_`` for general-purpose Renegade mission or toolkit scripts
* ``M01_`` through ``M11_`` for mission-specific logic
* ``MPR_`` for the ``PRDemo.cpp`` prototype/demo scripts
* ``Test_`` or author-tagged names such as ``BMG_``, ``DME_``, ``RAD_``,
  ``JDG_``, and ``RMV_`` for test, prototype, or contributor-specific work

Scope
-----

This page is intentionally an overview of the script system and source layout.
The generated per-script reference lives under ``scripts/reference`` and is
produced from active ``DECLARE_SCRIPT`` registrations in the local OpenW3D
source tree. It combines:

* manual summaries from ``scripts/openw3d-script-overrides.json``
* nearby source comments when they exist
* heuristic summaries derived from callback overrides and ``Commands->`` usage

The machine-readable export for future LevelEditQt integration is
``scripts/openw3d-script-catalog.json``.

To regenerate the catalog and RST pages, run::

   python tools/generate_openw3d_scripts_reference.py
