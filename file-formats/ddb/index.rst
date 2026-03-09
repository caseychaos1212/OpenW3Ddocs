DDB
===

Description
-----------

``.ddb`` files are definition database files used by the game runtime and
LevelEdit tooling.

In OpenW3D, ``.ddb`` is written/read through the shared SaveLoad framework and
stores definition data plus preset data.

References
----------

* `wwsaveload/saveload.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwsaveload/saveload.cpp>`_
* `wwsaveload/saveloadids.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwsaveload/saveloadids.h>`_
* `wwsaveload/definitionmgr.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwsaveload/definitionmgr.h>`_
* `Tools/LevelEdit/EditorChunkIDs.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/EditorChunkIDs.h>`_
* `Tools/LevelEdit/PresetsLibForm.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/PresetsLibForm.cpp>`_
* `Tools/LevelEdit/PresetMgr.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/PresetMgr.cpp>`_
* `Tools/LevelEdit/Preset.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/Preset.cpp>`_
* `Tools/LevelEdit/FileLocations.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/FileLocations.h>`_
* `Combat/savegame.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/savegame.cpp>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Container model
~~~~~~~~~~~~~~~

``.ddb`` uses the same chunk container used by the SaveLoad system:

* Chunk header: ``uint32 ChunkType`` + ``uint32 ChunkSize``.
* ``ChunkSize`` MSB indicates sub-chunks.
* Micro-chunks use 1-byte type + 1-byte size.

SaveLoad writes one top-level chunk per subsystem using that subsystem's
``Chunk_ID()``.

Top-level content in OpenW3D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LevelEdit preset save calls write two main subsystems:

* ``_TheDefinitionMgr`` (chunk id ``CHUNKID_SAVELOAD_DEFMGR`` from ``saveloadids.h``).
* ``_ThePresetMgr`` (chunk id ``CHUNKID_PRESETMGR`` from ``EditorChunkIDs.h``).

Within ``PresetMgrClass``
~~~~~~~~~~~~~~~~~~~~~~~~~

``PresetMgrClass`` stores:

* ``CHUNKID_PRESETS``: each preset saved under its persist factory chunk id.
* ``CHUNKID_EMBEDDED_NODE_DATA``:
  * ``CHUNKID_PRESET_ID``
  * ``CHUNKID_NODE_LIST``

``PresetClass`` payloads include:

* ``CHUNKID_COMMENTS`` string chunk.
* ``CHUNKID_VARIABLES`` micro-chunks such as definition ID, temporary flag,
  parent ID, and manual dependency strings.

Typical file locations and usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Global editor DB: ``presets\\objects.ddb``.
* Temp editor DB: ``Presets\\temps20.ddb``.
* Exported per-map DB: ``<map>.ddb``.
* Runtime load path derives ``<map>.ddb`` from map name and loads definitions before level data.
