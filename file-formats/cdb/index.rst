CDB
===

Description
-----------

``.cdb`` is the conversation database format used by LevelEdit and runtime
conversation systems.

The default global conversation database path in LevelEdit is
``Presets\\conv10.cdb``.

References
----------

* `Tools/LevelEdit/FileLocations.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/FileLocations.h>`_
* `Tools/LevelEdit/ConversationEditorMgr.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/ConversationEditorMgr.cpp>`_
* `Combat/conversationmgr.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/conversationmgr.cpp>`_
* `Combat/combatchunkid.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Combat/combatchunkid.h>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Container model
~~~~~~~~~~~~~~~

``.cdb`` uses ``chunkio`` chunks/micro-chunks.

Top-level subsystem chunk
~~~~~~~~~~~~~~~~~~~~~~~~~

Saved via ``SaveLoadSystemClass`` as the conversation subsystem chunk:

* ``CHUNKID_CONVERSATION_MGR``.

Conversation manager chunks
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within the conversation manager payload:

* ``CHUNKID_VARIABLES``
  * Micro-chunks for next active/global/level conversation ids.
* ``CHUNKID_CONVERSATION_CATEGORY``
  * Stores category id, then repeated ``CHUNKID_CONVERSATION`` entries.
* Repeated ``CHUNKID_ACTIVE_CONVERSATION`` entries.

Editor usage
~~~~~~~~~~~~

LevelEdit global conversation database operations:

* Save global DB: sets category to ``CATEGORY_GLOBAL`` and saves ``_ConversationMgrSaveLoad``.
* Load global DB: loads with ``SaveLoadSystemClass::Load``.
