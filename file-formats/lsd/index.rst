LSD
===

Description
-----------

``.lsd`` files store static level state used at runtime.

In OpenW3D, ``SaveGameManager`` uses ``.lsd`` for static world data and pairs it
with ``.ldd`` (dynamic save data) and ``.ddb`` (definitions).

References
----------

* `Combat/savegame.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/savegame.h>`_
* `Combat/savegame.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/savegame.cpp>`_
* `Tools/LevelEdit/Export.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/Export.cpp>`_
* `Commando/modpackage.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Commando/modpackage.cpp>`_
* `wwsaveload/saveload.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwsaveload/saveload.cpp>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Write path
~~~~~~~~~~

During level export, LevelEdit does:

* ``SaveGameManager::Set_Map_Filename("<name>.lsd")``
* ``SaveGameManager::Save_Level()``

``Save_Level`` writes SaveLoad subsystem chunks to the ``.lsd`` file:

* ``_PhysStaticDataSaveSystem``
* ``_PhysStaticObjectsSaveSystem``
* ``_StaticAudioSaveLoadSubsystem``
* ``_TheBackgroundMgr``
* ``_TheWeatherMgr``
* ``_TheMapMgrSaveLoadSubsystem``

Read/load path
~~~~~~~~~~~~~~

``Pre_Load_Game`` resolves file pairing:

* ``.mix`` input maps to ``<root>.ldd`` plus ``<root>.lsd``.
* ``.lsd`` input implies ``<root>.ldd`` for dynamic data.

While loading a game:

* ``.ldd`` level-info chunk provides map filename.
* Runtime loads ``<map>.ddb`` definitions.
* Runtime then loads static level data from ``.lsd`` via ``Load_Level()``.

Packaging
~~~~~~~~~

``ModPackageClass::Build_Level_List`` identifies levels in a package by finding
``.lsd`` entries.
