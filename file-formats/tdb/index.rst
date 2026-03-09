TDB
===

Description
-----------

``.tdb`` is the translation database format (for example ``strings.tdb``).

LevelEdit saves/loads this through ``TranslateDBClass`` using the SaveLoad system.

References
----------

* `Tools/LevelEdit/FileLocations.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/FileLocations.h>`_
* `Tools/LevelEdit/stringsmgr.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/stringsmgr.cpp>`_
* `wwtranslatedb/translatedbids.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwtranslatedb/translatedbids.h>`_
* `wwtranslatedb/translatedb.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwtranslatedb/translatedb.h>`_
* `wwtranslatedb/translatedb.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwtranslatedb/translatedb.cpp>`_
* `wwlib/chunkio.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/chunkio.h>`_

Specification
-------------

Container model
~~~~~~~~~~~~~~~

``.tdb`` uses ``chunkio`` chunks/micro-chunks.

Top-level subsystem chunk
~~~~~~~~~~~~~~~~~~~~~~~~~

Saved via ``SaveLoadSystemClass`` as:

* ``CHUNKID_TRANSLATE_DB`` (from ``translatedbids.h``).

Translate DB internal chunks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``TranslateDBClass`` writes:

* ``CHUNKID_VARIABLES``
  * Micro-chunks:
    * ``VARID_VERSION_NUMBER``
    * ``VARID_LANGUAGE_ID``
* ``CHUNKID_CATEGORIES``
  * Repeated category persist chunks.
* ``CHUNKID_OBJECTS``
  * Repeated translation object persist chunks.

Typical file path
~~~~~~~~~~~~~~~~~

LevelEdit default path:

* ``Always\\TranslationDB\\strings.tdb``.
