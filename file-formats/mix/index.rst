MIX
===

Description
-----------

``.mix`` is the archive/container format used by OpenW3D runtime and tools for
packaged game content.

This is not a ``chunkio`` format. It uses its own header + file table layout.

References
----------

* `wwlib/mixfile.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/mixfile.h>`_
* `wwlib/mixfile.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/mixfile.cpp>`_
* `wwlib/realcrc.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/wwlib/realcrc.h>`_
* `Tools/LevelEdit/Export.cpp <https://github.com/w3dhub/OpenW3D/blob/main/Code/Tools/LevelEdit/Export.cpp>`_

Specification
-------------

Header
~~~~~~

OpenW3D writer emits a ``MIX1`` file with this leading data:

======  =====  ====================
Offset  Bytes  Field
======  =====  ====================
0       4      Signature (``MIX1``)
4       4      HeaderOffset
8       4      NamesOffset
12      4      Reserved/unused
======  =====  ====================

File data area
~~~~~~~~~~~~~~

Embedded file bytes are written before the directory tables.

* Each stored file is padded to 8-byte alignment.
* Directory ``Offset`` values point into this file data area.

Directory table at ``HeaderOffset``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

====  =====  =================
Seq   Bytes  Field
====  =====  =================
1     4      FileCount
N     12     File entry x N
====  =====  =================

Each file entry:

* ``uint32 CRC`` (case-insensitive CRC of stored filename).
* ``uint32 Offset`` (archive-relative file start).
* ``uint32 Size`` (file size in bytes).

Entries are sorted by CRC and looked up with binary search.

Name table at ``NamesOffset``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

====  =====  ==========================
Seq   Bytes  Field
====  =====  ==========================
1     4      FileCount
N     1+L    Name record x N
====  =====  ==========================

Each name record:

* ``uint8 NameLength``.
* ``char Name[NameLength]`` (includes null terminator in writer output).

Runtime lookup
~~~~~~~~~~~~~~

``MixFileFactoryClass::Get_File`` computes ``CRC_Stringi(filename)`` and binary-searches
the file table. On hit, it returns a biased file view into the archive data.
