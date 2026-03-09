LVL
===

Description
-----------

``.lvl`` is the LevelEdit project file format.

In OpenW3D, ``LevelEdit`` saves/loads ``.lvl`` through ``EditorSaveLoadClass``.

References
----------

* `Tools/LevelEdit/EditorSaveLoad.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/EditorSaveLoad.cpp>`_
* `Tools/LevelEdit/EditorSaveLoad.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/EditorSaveLoad.h>`_
* `Tools/LevelEdit/EditorChunkIDs.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/EditorChunkIDs.h>`_
* `Tools/LevelEdit/lightsolvesavesystem.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/lightsolvesavesystem.h>`_
* `Tools/LevelEdit/lightsolvesavesystem.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/lightsolvesavesystem.cpp>`_
* `Tools/LevelEdit/LevelEditDoc.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/LevelEditDoc.cpp>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Container model
~~~~~~~~~~~~~~~

``.lvl`` is chunk-based and uses the same chunk/micro-chunk primitives as
other SaveLoad-backed files.

Top-level layout
~~~~~~~~~~~~~~~~

Current format writes two wrapper chunks:

* ``CHUNKID_LVL_DATA`` (value ``304021447``)
* ``CHUNKID_LIGHT_SOLVE`` (value ``304021448``)

The loader peeks the first chunk:

* If first chunk is ``CHUNKID_LVL_DATA``, it loads both wrappers as modern format.
* Otherwise it falls back to legacy single-stream SaveLoad data.

``CHUNKID_LVL_DATA`` content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Save_Level_Data`` writes these SaveLoad subsystems in order:

* ``_PhysStaticDataSaveSystem``
* ``_TheNodeMgr``
* ``_TheEditorSaveLoadSubsystem``
* ``_TheBackgroundMgr``
* ``_TheWeatherMgr``
* ``_TheMapMgrSaveLoadSubsystem``
* ``_TheHeightfieldMgrSaveLoadSubsystem``
* ``_ConversationMgrSaveLoad`` (category set to level)

``CHUNKID_LIGHT_SOLVE`` content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``Save_Light_Solve`` writes ``_TheLightSolveSaveSystem`` (chunk id
``CHUNKID_EDITOR_LIGHT_SOLVE_SAVELOAD``). Its internal records include:

* ``LSS_CHUNKID_OBJECT_LIGHT_SOLVE`` (``30102537``)
* ``LSS_CHUNKID_OBJECT_VARIABLES``
* ``LSS_CHUNKID_OBJECT_LIGHTING``

Object variables are stored as micro-chunks:

* Object ID
* Render object class ID
* Sub-object count
