.. _presets-and-definitions:

Presets and definitions
=======================

A preset is the editor's named entry for a definition. The definition stores
the settings used to create an object; the object is an individual instance
in the editor or game. Understanding these three layers explains how a DDB
database becomes usable content, and why copying a preset involves more
than copying its name.

This chapter follows OpenW3D revision
``dbd77b71a57f19dfc2618babb6df989954f2651a``. Editor behavior refers to the
original ``Code/Tools/LevelEdit`` implementation in that snapshot. Other
editors and TT branches need their own comparison. The paths below were
checked against source; the examples have not been exercised in LevelEdit
or round-tripped through sample game files.

See :doc:`/file-formats/ddb/index` for the database container and file locations.

The three layers
----------------

.. list-table::
   :header-rows: 1
   :widths: 20 35 45

   * - Layer
     - Main types
     - Responsibility
   * - Editor preset
     - ``PresetClass``, ``PresetMgrClass``
     - Editor tree placement, parent relationship, comments, temporary status,
       manual file dependencies, and embedded editor nodes.
   * - Definition
     - ``DefinitionClass``, ``DefinitionMgrClass`` and concrete subclasses
     - Named configuration with a definition ID, a class ID, persistence
       methods, and a virtual ``Create()`` method.
   * - Instance
     - For example, ``SoldierGameObj`` or an editor ``ObjectNodeClass``
     - An individual object created using that configuration. Several
       instances can use the same definition.

``PresetClass::Get_ID()``, ``Get_Name()``, and ``Get_Class_ID()`` obtain their
values from the associated definition. The preset caches a definition ID
for loading. Its name is not a separate editor-only identifier.
``Set_Definition()`` also stores an in-memory back-reference to the preset
in the definition's generic user-data field.

At runtime, ``BaseGameObj::Init()`` keeps a pointer to its definition, while
derived initialization code applies settings to the object. Definitions
therefore need to remain available while their instances use them.
Sources: `Preset accessors`_, `Preset implementation`_, `Definition interface`_,
and `Base game object`_.

.. code-block:: text

   LevelEdit preset ---- definition ID ----> SoldierGameObjDef
        |                                       |
        +-- parent preset ID                    +-- PhysDefID --> physics definition
        +-- comments                            |
        +-- manual dependencies                 +-- Create() --> SoldierGameObj
                                                                      |
                                                            physics object

IDs and names
-------------

Several different identifiers appear in the same save/load path:

.. list-table::
   :header-rows: 1
   :widths: 24 36 40

   * - Identifier
     - Example or accessor
     - Meaning
   * - Definition class ID
     - ``Get_Class_ID()``; ``CLASSID_GAME_OBJECT_DEF_SOLDIER = 0x3001``
     - The concrete kind of definition. All soldier definitions share this
       class ID.
   * - Definition ID / preset ID
     - ``Get_ID()``
     - Identifies one configuration record. This is the ID stored in preset
       links and fields that reference another definition.
   * - Definition name / preset name
     - ``Get_Name()``
     - A configuration's lookup name, such as a custom soldier preset name.
       The definition factory's display label ``Soldier`` names the type.
   * - Persistence chunk ID
     - ``Get_Factory().Chunk_ID()``;
       ``CHUNKID_GAME_OBJECT_DEF_SOLDIER``
     - Selects the loader for a serialized record. A soldier instance has a
       separate ``CHUNKID_GAME_OBJECT_SOLDIER`` persistence type.
   * - Preset parent ID
     - ``PresetClass::m_ParentID``
     - Another preset's definition ID. Zero is the initial no-parent value.
   * - Serialized pointer identity
     - ``SIMPLEFACTORY_CHUNKID_OBJPOINTER``
     - SaveLoad's object-remapping identity. It is separate from the
       definition ID and is not a file offset.

Superclass IDs group definition types into ranges of ``0x1000``.
``CLASSID_GAME_OBJECTS`` is ``0x3000``; soldier definitions occupy the next
class ID, ``0x3001``. Use ``SuperClassID_From_ClassID()`` for this grouping.
This arithmetic applies to **class IDs**, not preset IDs.
Sources: `Definition class IDs`_, `Combat class and chunk IDs`_,
`Soldier definition`_, and `Persistence factory`_.

Allocating definition IDs
~~~~~~~~~~~~~~~~~~~~~~~~~

The regular editor creation path calls
``DefinitionMgrClass::Get_New_ID(class_id)``. Its allocation range begins at::

   range_start = (class_id - 0x1000) * 10000

The initial candidate is ``range_start + 1``; the allocator then examines
loaded definitions for an available value. For soldier class ``0x3001``,
the initial candidate is decimal ``81930001``. This is an illustration of
the allocator, not an ID to hard-code into a new preset. Imported databases
and temporary definitions need not follow that allocation convention.

Temporary presets use ``Get_Next_Temp_ID()`` instead. The original editor
keeps its next value in the Windows application profile/registry and starts
at decimal ``1000000000``. That counter does not itself inspect another
database for collisions. When combining content from different editor
profiles, check definition IDs and the references to them together.

``Register_Definition()`` requires a nonzero ID and an unregistered object.
The database loader takes a separate path: it appends loaded definitions
and sorts them by ID. Do not rely on loading to resolve duplicate IDs or to
provide a documented "last database wins" rule.
Sources: `Definition manager`_, `Preset manager`_, and `Temporary ID allocator`_.

Creating a preset and creating an object
----------------------------------------

There are three different factory operations:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Operation
     - Result
   * - ``DefinitionFactoryClass::Create()``
     - A new definition populated by its C++ constructor defaults. The
       ``SimpleDefinitionFactoryClass`` implementation returns ``new T``.
   * - ``PersistFactoryClass::Load()``
     - An object reconstructed from saved data. A simple persistence
       factory allocates ``T``, calls its ``Load()``, and registers its
       old-to-new identity mapping.
   * - ``DefinitionClass::Create()``
     - An instance initialized from an existing definition. For example,
       ``SoldierGameObjDef::Create()`` allocates ``SoldierGameObj`` and
       calls ``Init(*this)``.

Definition factories register with ``DefinitionFactoryMgrClass`` during
construction. Persistence factories register separately with
``SaveLoadSystemClass``. ``soldier.cpp`` provides a concrete example of both
registrations; adding a definition type requires the relevant registration
code to be linked into the application.
Sources: `Definition factory registration`_, `Simple definition factory`_,
`Persistence factory`_, and `Soldier definition`_.

The editor's Add path
~~~~~~~~~~~~~~~~~~~~~

``PresetsFormClass::Add_New_Preset()`` performs the following sequence:

1. Obtain the selected definition factory and optional parent preset.
2. Call ``PresetMgrClass::Create_Preset()`` to create a definition, assign
   an ID, and associate it with a new ``PresetClass``.
3. Set the parent and copy its properties when a parent is selected.
4. Accept the supplied name or show the properties dialog.
5. Add the accepted preset to ``PresetMgrClass``, register its definition
   with ``DefinitionMgrClass``, and add its ID to the parent's child list.

``PresetMgrClass::Create_Preset()`` alone does not perform those final
registrations. Code using that helper directly needs to account for them.

The editor's Make action follows a different path. It asks the scene editor
to create a node from the preset. ``PresetClass::Create()`` validates the
configuration and selects an editor node type from the definition's class
or superclass, such as ``ObjectNodeClass`` or ``SoundNodeClass``.
Sources: `Preset creation in LevelEdit`_, `Preset manager`_, and
`Preset implementation`_.

Editable parameters and persistence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The editor discovers fields through ``Get_Parameter_Count()`` and
``Lock_Parameter()``. Macros such as ``EDITABLE_PARAM`` and
``MODEL_DEF_PARAM`` expose member variables through that interface when
``PARAM_EDITING_ON`` is enabled. This metadata supplies field types and
names for property editing, copying, and the dependency collection below.

Exposing a parameter does not automatically serialize it. The concrete
definition's ``Save()`` and ``Load()`` methods handle its chunks. For
example, ``SoldierGameObjDef`` exposes ``JumpVelocity`` as an editable
float and separately writes and reads its jump-velocity micro-chunk.
Sources: `Editable parameter metadata`_, `Soldier definition`_, and
`Soldier persistence`_.

.. _preset-inheritance:

Parents, copying, and propagation
---------------------------------

A child preset has its own definition. On creation,
``PresetClass::Copy_Properties()`` copies editable values into that
definition through ``Copy_Definition()``. The definition ID and name remain
those of the new entry. Soldier dialogue and preset transition data have
additional copy handling.

Model/physics settings need special treatment. For a
``TYPE_MODELDEFINITIONID`` parameter, ``Copy_Definition()`` follows the
referenced definition and copies its settings. If the destination has no
referenced definition, the editor creates and registers one with a new ID.
Other parameter types use their ``Copy_Value()`` implementations. This is
why copying a preset can also create an additional definition record.
Sources: `Preset implementation`_ and `Definition copy utilities`_.

The parent relationship is stored by the editor preset. The base
``DefinitionClass`` payload writes the definition's own ID and name;
its old ``XXX_VARID_PARENTID`` declaration is not saved or loaded by the
reviewed implementation. Runtime definition loading does not reconstruct
settings by walking the editor's parent tree.

The original editor provides an explicit **Propagate** action in the preset
properties dialog. It lets the user select descendant presets and parameter
values to copy. For matching parameter names and types, selected values
replace the destination values, including values that previously differed.
Model-definition parameters are traversed recursively when the referenced
classes match. Soldier dialogue has a separate propagation option.

For example, suppose a child soldier has ``JumpVelocity = 3`` and its parent
is changed to ``4``. Choosing that child and ``JumpVelocity`` in Propagate
copies ``4`` into the child's definition. Leaving the child out of the
selection leaves its value unchanged. This example describes the copy
operation, not a persistent per-field inheritance flag.

The source also contains older equality-based helpers named
``Build_Inherited_Param_List()`` and ``Compare_Derived_Parameters()``. No
caller of ``Build_Inherited_Param_List()`` was found in the reviewed
LevelEdit source; its presence does not establish automatic propagation
on every parent edit.
Sources: `Definition persistence`_, `Preset properties dialog`_,
`Explicit propagation`_, and `Legacy propagation helpers`_.

Dependencies and what gets saved
--------------------------------

Two dependency lists serve different purposes:

* **Definition records:** ``PresetClass::Collect_Definitions()`` includes
  the preset's definition and uses ``Build_Embedded_Definition_List()`` to
  gather embedded definitions. That helper recurses through
  ``TYPE_MODELDEFINITIONID`` and adds directly referenced
  ``TYPE_PHYSDEFINITIONID`` records. It does not traverse every possible
  definition-reference parameter.
* **Asset filenames:** ``Get_All_Dependencies()`` combines manually listed
  files with filenames discovered from editable parameters.
  ``Add_Definition_Dependencies()`` examines ``TYPE_FILENAME`` and
  ``TYPE_SOUND_FILENAME``, validates their paths through the editor file
  manager, and recurses through ``TYPE_MODELDEFINITIONID``. This is not a
  complete dependency scan of scripts, referenced W3D contents, or all
  other definitions.

A manual file dependency does not create or register a missing definition.
Likewise, having the definition record does not by itself guarantee that
all referenced assets are available.
Sources: `Preset implementation`_ and `Definition copy utilities`_.

Saving an editor database
~~~~~~~~~~~~~~~~~~~~~~~~~

``PresetsFormClass::Save_Presets()`` filters presets by its class and
temporary/global selection. It temporarily disables saving for all
definitions, then enables the records collected for the remaining presets.
It writes ``_TheDefinitionMgr`` first and ``_ThePresetMgr`` second, restores
the removed presets, and re-enables definition saving.

The order matters to this reader: ``PresetClass::Load_Variables()`` resolves
its definition ID immediately using
``Find_Definition(m_DefinitionID, false)``. It resolves its parent preset ID
later in ``On_Post_Load()`` and rebuilds the parent's child list.
Sources: `Editor database save`_ and `Preset implementation`_.

.. code-block:: text

   Editor DDB
   +-- Definition manager subsystem
   |   +-- Objects
   |       +-- Concrete definition persistence chunk
   |           +-- Simple-factory remapping identity
   |           +-- Concrete definition data
   |               +-- Class-specific fields and base-class data
   |                   +-- DefinitionClass: definition ID and name
   +-- Preset manager subsystem
       +-- Presets
       |   +-- Preset persistence chunk
       |       +-- Simple-factory remapping identity
       |       +-- Preset data: comments, definition ID, parent ID, ...
       +-- Embedded editor node data

The diagram shows the main ownership boundaries, not every chunk.
Class-specific ``CHUNKID_DEF_PARENT`` containers represent **C++ base-class
data**; they are unrelated to the parent preset in the editor tree.
``DefinitionMgrClass::Load_Objects()`` selects persistence factories by
chunk ID and sorts the resulting definitions by definition ID. Unknown
factory chunk IDs are skipped in that loop, so a successful outer load is
not proof that every record was reconstructed.
Sources: `Definition manager`_, `Persistence factory`_, `Base game object`_,
and `Preset manager`_.

Runtime databases and objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``SaveGameManager::Save_Definitions()`` writes only the definition subsystem.
An editor DDB can also contain preset metadata, but the runtime creation
path below uses ``DefinitionMgrClass``. The shared SaveLoad reader dispatches
top-level chunks to registered subsystems, processes pointer remaps, and
runs post-load callbacks when requested.
Sources: `Runtime definition save/load`_ and `SaveLoad dispatch`_.

A soldier creation request by name follows this path:

1. ``ObjectLibraryManager::Create_Object(name)`` looks up the name through
   ``Find_Typed_Definition(name, CLASSID_GAME_OBJECTS)``.
2. The object library calls ``Is_Valid_Config()`` and, if valid, the
   definition's ``Create()`` method.
3. ``SoldierGameObjDef::Create()`` allocates and initializes the soldier.
4. Physical-object initialization resolves ``PhysDefID`` to a physics
   definition and creates the physics object from that definition.

The string passed to this object-library path is a definition/preset name,
not a W3D filename or the name of a C++ definition factory. The object
library targets game-object definitions; sound, physics, and other kinds
have their own consumers.
Sources: `Object library`_, `Soldier definition`_, and `Physical object setup`_.

Lookup behavior and twiddlers
-----------------------------

``Find_Definition(id)`` searches by definition ID.
``Find_Named_Definition(name)`` compares names without case sensitivity.
``Find_Typed_Definition(name, class_id)`` additionally accepts either an
exact class ID or a superclass ID; for example, ``CLASSID_GAME_OBJECTS``
can select a soldier definition. Avoid names that become ambiguous within
the requested category.

These lookup methods default to ``twiddle = true``. A ``TwiddlerClass`` is
a definition that chooses an entry from its list of definition IDs.
Looking up a twiddler can therefore return a selected target definition
instead of the twiddler record itself. Pass ``false`` when inspecting or
editing the stored record, as ``PresetClass`` does while linking a preset
to its definition. An empty or unresolved selection can produce ``nullptr``.
Sources: `Definition manager`_ and `Twiddler implementation`_.

Troubleshooting
---------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Symptom
     - Check
   * - A preset exists in the tree, but Make fails.
     - Check its definition, ``Is_Valid_Config()`` result, and whether
       ``PresetClass::Create()`` supports placing that class.
   * - A game object cannot be created by name.
     - Check the loaded definition name and game-object class category,
       configuration validation, and any twiddler target.
   * - A copied soldier has missing model/physics settings.
     - Follow its ``PhysDefID`` and confirm that the referenced definition
       was created, registered, saved, and loaded with it.
   * - Changing a parent does not update a child.
     - Inspect the child's stored values and the explicit Propagate
       selection. Changing the tree relationship does not copy values.
   * - Definitions disappear when reading a database.
     - Check the concrete persistence chunk IDs against the factories
       registered in the reading executable, and check for duplicate IDs.
   * - Loading reports a missing definition or requests a re-export.
     - Compare the object's saved definition ID with the loaded DDB.
       ``BaseGameObj::Load()`` resolves that ID; renaming alone cannot
       repair a broken numeric reference.

When adding a new definition type in C++, use an existing type as a guide:
assign its class and persistence IDs, register both factories, expose its
editable parameters where needed, implement its save/load and creation
methods, and ensure its registration code is linked. A factory declaration
in an unlinked source file cannot make that type available to a reader.

.. _Preset accessors: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/Preset.h
.. _Preset implementation: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/Preset.cpp
.. _Preset manager: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/PresetMgr.cpp
.. _Definition interface: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/definition.h
.. _Definition persistence: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/definition.cpp
.. _Definition manager: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/definitionmgr.cpp
.. _Definition class IDs: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/definitionclassids.h
.. _Combat class and chunk IDs: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/combatchunkid.h
.. _Soldier definition: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/soldier.cpp#L119-L169
.. _Base game object: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/basegameobj.cpp
.. _Persistence factory: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/persistfactory.h
.. _Definition factory registration: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/definitionfactory.cpp
.. _Simple definition factory: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/simpledefinitionfactory.h
.. _Editable parameter metadata: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/editable.h
.. _Soldier persistence: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/soldier.cpp#L196-L280
.. _Temporary ID allocator: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/Utils.cpp#L2029-L2051
.. _Preset creation in LevelEdit: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/PresetsLibForm.cpp#L1511-L1601
.. _Definition copy utilities: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/DefinitionUtils.cpp
.. _Preset properties dialog: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/PresetPropSheet.cpp#L142-L172
.. _Explicit propagation: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/ParameterInheritanceDialog.cpp#L601-L800
.. _Legacy propagation helpers: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/PresetsLibForm.cpp#L1991-L2171
.. _Editor database save: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Tools/LevelEdit/PresetsLibForm.cpp#L1343-L1420
.. _Runtime definition save/load: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/savegame.cpp#L504-L557
.. _SaveLoad dispatch: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/saveload.cpp
.. _Object library: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/objlibrary.cpp
.. _Physical object setup: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/Combat/physicalgameobj.cpp#L328-L359
.. _Twiddler implementation: https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwsaveload/twiddler.cpp
