LDD
===

Description
-----------

``.ldd`` stores dynamic save-game state.

In OpenW3D code, the same chunk layout is also used for ``.sav`` files
written by the in-game save system.

At runtime it is paired with:

* ``.lsd`` for static level state.
* ``.ddb`` for definitions.

References
----------

* `Combat/savegame.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/savegame.h>`_
* `Combat/savegame.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/savegame.cpp>`_
* `Tools/LevelEdit/Export.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/Export.cpp>`_
* `Commando/combatgmode.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Commando/combatgmode.cpp>`_
* `Commando/dlgsavegame.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Commando/dlgsavegame.cpp>`_
* `Commando/dlgloadspgame.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Commando/dlgloadspgame.cpp>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Container model
~~~~~~~~~~~~~~~

``.ldd`` uses ``chunkio`` chunks/micro-chunks.

Top-level chunks
~~~~~~~~~~~~~~~~

``SaveGameManager::Save_Game`` writes:

* ``CHUNKID_LEVEL_INFO`` (``1011991648`` in normal builds, ``1011991650`` in BETACLIENT builds).
* ``CHUNKID_LEVEL_DATA`` (next enum value).

This structure is extension-agnostic in code: both map dynamic files (commonly
``.ldd``) and user save files (commonly ``.sav``) are written through the same
function.

``CHUNKID_LEVEL_INFO`` payload
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Micro-chunks:

* ``MICROCHUNKID_MAP_FILENAME`` (map/level filename string).
* ``MICROCHUNKID_DESCRIPTION`` (wide description string).
* ``MICROCHUNKID_MISSION_DESCRIPTION`` (mission description id).

``CHUNKID_LEVEL_DATA`` payload
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contains SaveLoad subsystem chunks, including:

* ``_CombatSaveLoad``
* ``_ConversationMgrSaveLoad`` (level category)
* ``_PhysDynamicSaveSystem``
* ``_TheEncyclopediaMgrSaveLoadSubsystem``
* ``_DynamicAudioSaveLoadSubsystem``
* ``_TheMapMgrSaveLoadSubsystem``
* Optional additional subsystems passed via varargs

Load flow
~~~~~~~~~

On load, runtime reads level info from ``.ldd``, derives ``<map>.ddb``, loads definitions,
loads ``.lsd`` static data, then loads ``CHUNKID_LEVEL_DATA`` dynamic state.

Save-game naming in practice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Observed names in OpenW3D code:

* ``save\\autosave.sav``
* ``save\\quicksaveA.sav``
* ``save\\quicksaveB.sav``
* Slot saves like ``save\\savegameNN.sav``
