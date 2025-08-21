W3D
===

Description
-----------

``.w3d`` files were used in the following games to store 3D models:

* C&C Renegade
* Earth & Beyond
* C&C Generals
* Zero Hour
* BFME I
* BFME II

Later SAGE games (C&C3 and RA3) used an XML-based evolution of the w3d format called w3x.

This document was adapted from the OPENSAGE READTHEDOCS It was added to by Casey Williams for use for Renegade based W3D projects.

Because of this some of the information may be diffrent for SAGE games especially BFME I and II. 

References
----------

* `w3d2ply/w3d_file.h <https://github.com/mikolalysenko/w3d2ply/blob/ecd8302b6cfd0578ab249cb95c8b70636c4609bc/w3d_file.h>`_
* `libw3d/types.hpp <https://github.com/feliwir/libw3d/blob/fb547b28c91f17070d65ba24edf7a5294a0554d9/include/libw3d/types.hpp>`_
* `OpenW3D/w3d_file.h <https://github.com/w3dhub/OpenW3D/blob/main/Code/ww3d2/w3d_file.h>`_
* `max2w3d/scripts <https://github.com/w3dhub/max2w3d/blob/master/scripts/w3d.h>`_  
* `GeneralsMD/w3d_file.h <https://github.com/electronicarts/CnC_Generals_Zero_Hour/blob/main/GeneralsMD/Code/Libraries/Source/WWVegas/WW3D2/w3d_file.h>`_
* `therealKyp/Earth-and-Beyond-server <https://github.com/therealKyp/Earth-and-Beyond-server/tree/master/trunk/Net7Tools/W3D%20Parser>`_

Specification
-------------

Chunks
~~~~~~

``.w3d`` files can contain mesh data, animation data, bone transforms for placing meshes into a hierarchy and doing skinned animations, mesh bounding box information, and even particle emitter definitions. Skinned models are usually split over several files, with each animation chunk placed in a separate file. There is no technical need for this; it was presumably done for maintainability and / or runtime memory efficiency.

``.w3d`` is a chunk-based binary format. A ``.w3d`` file can (and usually does) contain multiple chunks. Every chunk starts with a chunk header:

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

* **ChunkType**: A value from the `W3D_CHUNK_TYPE`_ enumeration.
* **ChunkSize**: MSB is 1 if the chunk contains sub-chunks, otherwise it's 0. Lower 31 bits are the chunk size, not including this chunk header.

Some chunks, depending on the value of **ChunkType** in the chunk header, have sub-chunks. If there are sub-chunks, then the Most Significant Bit (MSB) of the **ChunkSize** field will be ``1``.

Note that the indentation denotes the chunk hierarchy, with nested chunk types appearing as sub-chunks of the parent chunk.

MicroChunk
~~~~~~~~~~

Instead of filling the contents of a
chunk with data, you can fill it with "micro-chunks" which contain a single byte
id and a single byte size.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       1      UINT8    MicroChunkType
1       1      UINT8    MicroChunkSize
======  =====  =======  ===========

* **MicroChunkType**: These are dependent on the parent definition.
* **MicroChunkSize**: Can't contain Subchunks.


W3D_CHUNK_TYPE
~~~~~~~~~~~~~~

==========  ==========================
Value       Name
==========  ==========================
0x0         `W3D_CHUNK_MESH`_
0x1         `W3D_CHUNK_MESH_HEADER`_
0x2         `W3D_CHUNK_VERTICES`_
0x3         `W3D_CHUNK_VERTEX_NORMALS`_
0x4         `W3D_CHUNK_SURRENDER_NORMALS`_
0x5         `W3D_CHUNK_TEXCOORDS`_
0x6         `O_W3D_CHUNK_MATERIALS`_
0x7         `O_W3D_CHUNK_TRIANGLES`_
0x8         `O_W3D_CHUNK_QUADRANGLES`_ 
0x9         `O_W3D_CHUNK_SURRENDER_TRIANGLES`_
0xA         `O_W3D_CHUNK_POV_TRIANGLES`_
0xB         `O_W3D_CHUNK_POV_QUADRANGLES`_
0xC         `W3D_CHUNK_MESH_USER_TEXT`_
0xD         `W3D_CHUNK_VERTEX_COLORS`_
0xE         `W3D_CHUNK_VERTEX_INFLUENCES`_
0xF         `W3D_CHUNK_DAMAGE`_
0x10        `W3D_CHUNK_DAMAGE_HEADER`_
0x11        `W3D_CHUNK_DAMAGE_VERTICES`_
0x12        `W3D_CHUNK_DAMAGE_COLORS`_
0x13        `W3D_CHUNK_DAMAGE_MATERIALS`_
0x14        `O_W3D_CHUNK_MATERIALS2`_
0x15        `W3D_CHUNK_MATERIALS3`_
0x16        `W3D_CHUNK_MATERIAL3`_
0x17        `W3D_CHUNK_MATERIAL3_NAME`_
0x18        `W3D_CHUNK_MATERIAL3_INFO`_
0x19        `W3D_CHUNK_MATERIAL3_DC_MAP`_
0x1A        `W3D_CHUNK_MAP3_FILENAME`_
0x1B        `W3D_CHUNK_MAP3_INFO`_
0x1C        `W3D_CHUNK_MATERIAL3_DI_MAP`_
0x1D        `W3D_CHUNK_MATERIAL3_SC_MAP`_
0x1E        `W3D_CHUNK_MATERIAL3_SI_MAP`_
0x1F        `W3D_CHUNK_MESH_HEADER3`_
0x20        `W3D_CHUNK_TRIANGLES`_
0x21        `W3D_CHUNK_PER_TRI_MATERIALS`_
0x22        `W3D_CHUNK_VERTEX_SHADE_INDICES`_
0x23        `W3D_CHUNK_PRELIT_UNLIT`_
0x24        `W3D_CHUNK_PRELIT_VERTEX`_
0x25        `W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_PASS`_
0x26        `W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_TEXTURE`_
0x28        `W3D_CHUNK_MATERIAL_INFO`_
0x29        `W3D_CHUNK_SHADERS`_
0x2A        `W3D_CHUNK_VERTEX_MATERIALS`_
0x2B        `W3D_CHUNK_VERTEX_MATERIAL`_
0x2C        `W3D_CHUNK_VERTEX_MATERIAL_NAME`_
0x2D        `W3D_CHUNK_VERTEX_MATERIAL_INFO`_
0x2E        `W3D_CHUNK_VERTEX_MAPPER_ARGS0`_
0x2F        `W3D_CHUNK_VERTEX_MAPPER_ARGS1`_
0x30        `W3D_CHUNK_TEXTURES`_
0x31        `W3D_CHUNK_TEXTURE`_
0x32        `W3D_CHUNK_TEXTURE_NAME`_
0x33        `W3D_CHUNK_TEXTURE_INFO`_
0x38        `W3D_CHUNK_MATERIAL_PASS`_
0x39        `W3D_CHUNK_VERTEX_MATERIAL_IDS`_
0x3A        `W3D_CHUNK_SHADER_IDS`_
0x3B        `W3D_CHUNK_DCG`_
0x3C        `W3D_CHUNK_DIG`_
0x3E        `W3D_CHUNK_SCG`_
0x3F        `W3D_CHUNK_SHADER_MATERIAL_ID`_
0x48        `W3D_CHUNK_TEXTURE_STAGE`_
0x49        `W3D_CHUNK_TEXTURE_IDS`_
0x4A        `W3D_CHUNK_STAGE_TEXCOORDS`_
0x4B        `W3D_CHUNK_PER_FACE_TEXCOORD_IDS`_
0x50        `W3D_CHUNK_SHADER_MATERIALS`_
0x51        `W3D_CHUNK_SHADER_MATERIAL`_
0x52        `W3D_CHUNK_SHADER_MATERIAL_HEADER`_
0x53        `W3D_CHUNK_SHADER_MATERIAL_PROPERTY`_
0x58        `W3D_CHUNK_DEFORM`_
0x59        `W3D_CHUNK_DEFORM_SET`_
0x5A        `W3D_CHUNK_DEFORM_KEYFRAME`_
0x5B        `W3D_CHUNK_DEFORM_DATA`_
0x60        `W3D_CHUNK_TANGENTS`_
0x61        `W3D_CHUNK_BITANGENTS`_
0x80        `W3D_CHUNK_PS2_SHADERS`_
0x90        `W3D_CHUNK_AABTREE`_
0x91        `W3D_CHUNK_AABTREE_HEADER`_
0x92        `W3D_CHUNK_AABTREE_POLYINDICES`_
0x93        `W3D_CHUNK_AABTREE_NODES`_
0x100       `W3D_CHUNK_HIERARCHY`_
0x101       `W3D_CHUNK_HIERARCHY_HEADER`_
0x102       `W3D_CHUNK_PIVOTS`_
0x103       `W3D_CHUNK_PIVOT_FIXUPS`_
0x104       `W3D_CHUNK_PIVOT_UNKNOWN1`_
0x200       `W3D_CHUNK_ANIMATION`_
0x201       `W3D_CHUNK_ANIMATION_HEADER`_
0x202       `W3D_CHUNK_ANIMATION_CHANNEL`_
0x203       `W3D_CHUNK_BIT_CHANNEL`_
0x280       `W3D_CHUNK_COMPRESSED_ANIMATION`_
0x281       `W3D_CHUNK_COMPRESSED_ANIMATION_HEADER`_
0x282       `W3D_CHUNK_COMPRESSED_ANIMATION_CHANNEL`_
0x283       `W3D_CHUNK_COMPRESSED_BIT_CHANNEL`_
0x284       `W3D_CHUNK_COMPRESSED_ANIMATION_MOTION_CHANNEL`_
0x2C0       `W3D_CHUNK_MORPH_ANIMATION`_
0x2C1       `W3D_CHUNK_MORPHANIM_HEADER`_
0x2C2       `W3D_CHUNK_MORPHANIM_CHANNEL`_
0x2C3       `W3D_CHUNK_MORPHANIM_POSENAME`_
0x2C4       `W3D_CHUNK_MORPHANIM_KEYDATA`_
0x2C5       `W3D_CHUNK_MORPHANIM_PIVOTCHANNELDATA`_
0x300       `W3D_CHUNK_HMODEL`_
0x301       `W3D_CHUNK_HMODEL_HEADER`_
0x302       `W3D_CHUNK_NODE`_
0x303       `W3D_CHUNK_COLLISION_NODE`_
0x304       `W3D_CHUNK_SKIN_NODE`_
0x305       `OBSOLETE_W3D_CHUNK_HMODEL_AUX_DATA`_
0x306       `OBSOLETE_W3D_CHUNK_SHADOW_NODE`_
0x400       `W3D_CHUNK_LODMODEL`_
0x401       `W3D_CHUNK_LODMODEL_HEADER`_
0x402       `W3D_CHUNK_LOD`_
0x420       `W3D_CHUNK_COLLECTION`_
0x421       `W3D_CHUNK_COLLECTION_HEADER`_
0x422       `W3D_CHUNK_COLLECTION_OBJ_NAME`_
0x423       `W3D_CHUNK_PLACEHOLDER`_
0x424       `W3D_CHUNK_TRANSFORM_NODE`_
0x440       `W3D_CHUNK_POINTS`_
0x460       `W3D_CHUNK_LIGHT`_
0x461       `W3D_CHUNK_LIGHT_INFO`_
0x452       `W3D_CHUNK_SPOT_LIGHT_INFO`_
0x463       `W3D_CHUNK_NEAR_ATTENUATION`_
0x464       `W3D_CHUNK_FAR_ATTENUATION`_
0x465       `W3D_CHUNK_SPOT_LIGHT_INFO_5_0`_
0x466       `W3D_CHUNK_PULSE`_
0x500       `W3D_CHUNK_EMITTER`_
0x501       `W3D_CHUNK_EMITTER_HEADER`_
0x502       `W3D_CHUNK_EMITTER_USER_DATA`_
0x503       `W3D_CHUNK_EMITTER_INFO`_
0x504       `W3D_CHUNK_EMITTER_INFOV2`_
0x505       `W3D_CHUNK_EMITTER_PROPS`_
0x506       `OBSOLETE_W3D_CHUNK_EMITTER_COLOR_KEYFRAME`_
0x507       `OBSOLETE_W3D_CHUNK_EMITTER_OPACITY_KEYFRAME`_
0x508       `OBSOLETE_W3D_CHUNK_EMITTER_SIZE_KEYFRAME`_   
0x509       `W3D_CHUNK_EMITTER_LINE_PROPERTIES`_
0x50A       `W3D_CHUNK_EMITTER_ROTATION_KEYFRAMES`_
0x50B       `W3D_CHUNK_EMITTER_FRAME_KEYFRAMES`_
0x50C       `W3D_CHUNK_EMITTER_BLUR_TIME_KEYFRAMES`_
0x50D       `W3D_CHUNK_EMITTER_EXTRA_INFO`_
0x510       `W3D_CHUNK_EMITTER_ROTATION_KEYFRAMES`_
0x511       `W3D_CHUNK_EMITTER_FRAME_KEYFRAMES`_
0x512       `W3D_CHUNK_EMITTER_BLUR_TIME_KEYFRAMES`_
0x600       `W3D_CHUNK_AGGREGATE`_
0x601       `W3D_CHUNK_AGGREGATE_HEADER`_
0x602       `W3D_CHUNK_AGGREGATE_INFO`_
0x603       `W3D_CHUNK_TEXTURE_REPLACER_INFO`_
0x604       `W3D_CHUNK_AGGREGATE_CLASS_INFO`_
0x700       `W3D_CHUNK_HLOD`_
0x701       `W3D_CHUNK_HLOD_HEADER`_
0x702       `W3D_CHUNK_HLOD_LOD_ARRAY`_
0x703       `W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER`_
0x704       `W3D_CHUNK_HLOD_SUB_OBJECT`_
0x705       `W3D_CHUNK_HLOD_AGGREGATE_ARRAY`_
0x706       `W3D_CHUNK_HLOD_PROXY_ARRAY`_
0x707       `W3D_CHUNK_HLOD_LIGHT_ARRAY`_
0x740       `W3D_CHUNK_BOX`_
0x741       `W3D_CHUNK_SPHERE`_
0x742       `W3D_CHUNK_RING`_
0x750       `W3D_CHUNK_NULL_OBJECT`_ 
0x800       `W3D_CHUNK_LIGHTSCAPE`_
0x801       `W3D_CHUNK_LIGHTSCAPE_LIGHT`_
0x802       `W3D_CHUNK_LIGHT_TRANSFORM`_
0x900       `W3D_CHUNK_DAZZLE`_
0x901       `W3D_CHUNK_DAZZLE_NAME`_
0x902       `W3D_CHUNK_DAZZLE_TYPENAME`_
0xA00       `W3D_CHUNK_SOUNDROBJ`_
0xA01       `W3D_CHUNK_SOUNDROBJ_HEADER`_
0xA02       `W3D_CHUNK_SOUNDROBJ_DEFINITION`_
0xB00       `W3D_CHUNK_SHDMESH`_
0xB01       `W3D_CHUNK_SHDMESH_NAME`_
0xB02       `W3D_CHUNK_SHDMESH_HEADER`_
0xB03       `W3D_CHUNK_SHDMESH_USER_TEXT`_
0xB20       `W3D_CHUNK_SHDSUBMESH`_
0xB21       `W3D_CHUNK_SHDSUBMESH_HEADER`_
0xB40       `W3D_CHUNK_SHDSUBMESH_SHADER`_
0xB41       `W3D_CHUNK_SHDSUBMESH_SHADER_CLASSID`_
0xB42       `W3D_CHUNK_SHDSUBMESH_SHADER_DEF`_
0xB43       `W3D_CHUNK_SHDSUBMESH_VERTICES`_
0xB44       `W3D_CHUNK_SHDSUBMESH_VERTEX_NORMALS`_
0xB45       `W3D_CHUNK_SHDSUBMESH_TRIANGLES`_
0xB46       `W3D_CHUNK_SHDSUBMESH_VERTEX_SHADE_INDICES`_
0xB47       `W3D_CHUNK_SHDSUBMESH_UV0`_
0xB48       `W3D_CHUNK_SHDSUBMESH_UV1`_
0xB49       `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_S`_
0xB4A       `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_T`_
0xB4B       `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_SXT`_
0xB4C       `W3D_CHUNK_SHDSUBMESH_VERTEX_COLOR`_
0xB4D       `W3D_CHUNK_SHDSUBMESH_VERTEX_INFLUENCES`_
0xC00       `W3D_CHUNK_SECONDARY_VERTICES`_
0xC01       `W3D_CHUNK_SECONDARY_VERTEX_NORMALS`_
0xC02       `W3D_CHUNK_LIGHTMAP_UV`_
==========  ==========================

Chunks and sub-chunks appear in ``.w3d`` files in the following hierarchy:

* `W3D_CHUNK_MESH`_
  
  * `W3D_CHUNK_VERTICES`_
  * `W3D_CHUNK_SECONDARY_VERTICES`_
  * `W3D_CHUNK_VERTEX_NORMALS`_
  * `W3D_CHUNK_SECONDARY_VERTEX_NORMALS`_
  * `W3D_CHUNK_MESH_USER_TEXT`_
  * `W3D_CHUNK_VERTEX_INFLUENCES`_
  * `W3D_CHUNK_MESH_HEADER3`_
  * `W3D_CHUNK_TRIANGLES`_
  * `W3D_CHUNK_VERTEX_SHADE_INDICES`_
  * `W3D_CHUNK_PRELIT_UNLIT`_
  * `W3D_CHUNK_PRELIT_VERTEX`_
  * `W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_PASS`_
  * `W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_TEXTURE`_
  * `W3D_CHUNK_MATERIAL_INFO`_
  * `W3D_CHUNK_SHADERS`_
  * `W3D_CHUNK_VERTEX_MATERIALS`_

    * `W3D_CHUNK_VERTEX_MATERIAL`_

      * `W3D_CHUNK_VERTEX_MATERIAL_NAME`_
      * `W3D_CHUNK_VERTEX_MATERIAL_INFO`_
      * `W3D_CHUNK_VERTEX_MAPPER_ARGS0`_
      * `W3D_CHUNK_VERTEX_MAPPER_ARGS1`_

  * `W3D_CHUNK_TEXTURES`_

    * `W3D_CHUNK_TEXTURE`_

      * `W3D_CHUNK_TEXTURE_NAME`_
      * `W3D_CHUNK_TEXTURE_INFO`_

  * `W3D_CHUNK_MATERIAL_PASS`_

    * `W3D_CHUNK_VERTEX_MATERIAL_IDS`_
    * `W3D_CHUNK_SHADER_IDS`_
    * `W3D_CHUNK_DCG`_
    * `W3D_CHUNK_DIG`_
    * `W3D_CHUNK_SCG`_
    * `W3D_CHUNK_SHADER_MATERIAL_ID`_

    * `W3D_CHUNK_TEXTURE_STAGE`_

      * `W3D_CHUNK_TEXTURE_IDS`_
      * `W3D_CHUNK_STAGE_TEXCOORDS`_
      * `W3D_CHUNK_PER_FACE_TEXCOORD_IDS`_

  * `W3D_CHUNK_SHADER_MATERIALS`_

    * `W3D_CHUNK_SHADER_MATERIAL`_

      * `W3D_CHUNK_SHADER_MATERIAL_HEADER`_
      * `W3D_CHUNK_SHADER_MATERIAL_PROPERTY`_

  * `W3D_CHUNK_DEFORM`_

    * `W3D_CHUNK_DEFORM_SET`_
    
      * `W3D_CHUNK_DEFORM_KEYFRAME`_
    
        * `W3D_CHUNK_DEFORM_DATA`_

  * `W3D_CHUNK_TANGENTS`_
  * `W3D_CHUNK_BITANGENTS`_
  * `W3D_CHUNK_PS2_SHADERS`_
  * `W3D_CHUNK_AABTREE`_

    * `W3D_CHUNK_AABTREE_HEADER`_
    * `W3D_CHUNK_AABTREE_POLYINDICES`_
    * `W3D_CHUNK_AABTREE_NODES`_

* `W3D_CHUNK_HIERARCHY`_
    
  * `W3D_CHUNK_HIERARCHY_HEADER`_
  * `W3D_CHUNK_PIVOTS`_
  * `W3D_CHUNK_PIVOT_FIXUPS`_
  * `W3D_CHUNK_PIVOT_UNKNOWN1`_

* `W3D_CHUNK_ANIMATION`_

  * `W3D_CHUNK_ANIMATION_HEADER`_
  * `W3D_CHUNK_ANIMATION_CHANNEL`_
  * `W3D_CHUNK_BIT_CHANNEL`_

* `W3D_CHUNK_COMPRESSED_ANIMATION`_

  * `W3D_CHUNK_COMPRESSED_ANIMATION_HEADER`_
  * `W3D_CHUNK_COMPRESSED_ANIMATION_CHANNEL`_
  * `W3D_CHUNK_COMPRESSED_BIT_CHANNEL`_
  * `W3D_CHUNK_COMPRESSED_ANIMATION_MOTION_CHANNEL`_

* `W3D_CHUNK_MORPH_ANIMATION`_

  * `W3D_CHUNK_MORPHANIM_HEADER`_
  * `W3D_CHUNK_MORPHANIM_CHANNEL`_

    * `W3D_CHUNK_MORPHANIM_POSENAME`_
    * `W3D_CHUNK_MORPHANIM_KEYDATA`_

  * `W3D_CHUNK_MORPHANIM_PIVOTCHANNELDATA`_

* `W3D_CHUNK_HMODEL`_

  * `W3D_CHUNK_HMODEL_HEADER`_
  * `W3D_CHUNK_NODE`_
  * `W3D_CHUNK_COLLISION_NODE`_
  * `W3D_CHUNK_SKIN_NODE`_
  * `OBSOLETE_W3D_CHUNK_HMODEL_AUX_DATA`_
  * `OBSOLETE_W3D_CHUNK_SHADOW_NODE`_

* `W3D_CHUNK_LODMODEL`_
  
  * `W3D_CHUNK_LODMODEL_HEADER`_
  * `W3D_CHUNK_LOD`_

* `W3D_CHUNK_COLLECTION`_

  * `W3D_CHUNK_COLLECTION_HEADER`_
  * `W3D_CHUNK_COLLECTION_OBJ_NAME`_
  * `W3D_CHUNK_PLACEHOLDER`_
  * `W3D_CHUNK_TRANSFORM_NODE`_

* `W3D_CHUNK_POINTS`_

* `W3D_CHUNK_LIGHT`_

  * `W3D_CHUNK_LIGHT_INFO`_
  * `W3D_CHUNK_SPOT_LIGHT_INFO`_
  * `W3D_CHUNK_NEAR_ATTENUATION`_
  * `W3D_CHUNK_FAR_ATTENUATION`_
  * `W3D_CHUNK_SPOT_LIGHT_INFO_5_0`_
  * `W3D_CHUNK_PULSE`_


* `W3D_CHUNK_EMITTER`_

  * `W3D_CHUNK_EMITTER_HEADER`_
  * `W3D_CHUNK_EMITTER_USER_DATA`_
  * `W3D_CHUNK_EMITTER_INFO`_
  * `W3D_CHUNK_EMITTER_INFOV2`_
  * `W3D_CHUNK_EMITTER_PROPS`_
  * `OBSOLETE_W3D_CHUNK_EMITTER_COLOR_KEYFRAME`_
  * `OBSOLETE_W3D_CHUNK_EMITTER_OPACITY_KEYFRAME`_
  * `OBSOLETE_W3D_CHUNK_EMITTER_SIZE_KEYFRAME`_
  * `W3D_CHUNK_EMITTER_LINE_PROPERTIES`_
  * `W3D_CHUNK_EMITTER_ROTATION_KEYFRAMES`_
  * `W3D_CHUNK_EMITTER_FRAME_KEYFRAMES`_
  * `W3D_CHUNK_EMITTER_BLUR_TIME_KEYFRAMES`_
  * `W3D_CHUNK_EMITTER_EXTRA_INFO`_

* `W3D_CHUNK_AGGREGATE`_

  * `W3D_CHUNK_AGGREGATE_HEADER`_

    * `W3D_CHUNK_AGGREGATE_INFO`_

  * `W3D_CHUNK_TEXTURE_REPLACER_INFO`_
  * `W3D_CHUNK_AGGREGATE_CLASS_INFO`_

* `W3D_CHUNK_HLOD`_

  * `W3D_CHUNK_HLOD_HEADER`_
  * `W3D_CHUNK_HLOD_LOD_ARRAY`_

    * `W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER`_
    * `W3D_CHUNK_HLOD_SUB_OBJECT`_

  * `W3D_CHUNK_HLOD_AGGREGATE_ARRAY`_
  * `W3D_CHUNK_HLOD_PROXY_ARRAY`_
  * `W3D_CHUNK_HLOD_LIGHT_ARRAY`_


* `W3D_CHUNK_BOX`_

* `W3D_CHUNK_SPHERE`_

* `W3D_CHUNK_RING`_

* `W3D_CHUNK_NULL_OBJECT`_

* `W3D_CHUNK_LIGHTSCAPE`_

  * `W3D_CHUNK_LIGHTSCAPE_LIGHT`_

    * `W3D_CHUNK_LIGHT_TRANSFORM`_

* `W3D_CHUNK_DAZZLE`_

  * `W3D_CHUNK_DAZZLE_NAME`_
  * `W3D_CHUNK_DAZZLE_TYPENAME`_

* `W3D_CHUNK_SHDMESH`_
 
   * `W3D_CHUNK_SHDMESH_NAME`_
   * `W3D_CHUNK_SHDMESH_HEADER`_
   * `W3D_CHUNK_SHDMESH_USER_TEXT`_
   * `W3D_CHUNK_SHDSUBMESH`_

      * `W3D_CHUNK_SHDSUBMESH_HEADER`_
      * `W3D_CHUNK_SHDSUBMESH_SHADER`_

        * `W3D_CHUNK_SHDSUBMESH_SHADER_CLASSID`_
        * `W3D_CHUNK_SHDSUBMESH_SHADER_DEF`_
      
      * `W3D_CHUNK_SHDSUBMESH_VERTICES`_
      * `W3D_CHUNK_SHDSUBMESH_VERTEX_NORMALS`_
      * `W3D_CHUNK_SHDSUBMESH_TRIANGLES`_
      * `W3D_CHUNK_SHDSUBMESH_VERTEX_SHADE_INDICES`_
      * `W3D_CHUNK_SHDSUBMESH_UV0`_
      * `W3D_CHUNK_SHDSUBMESH_UV1`_
      * `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_S`_
      * `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_T`_
      * `W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_SxT`_
      * `W3D_CHUNK_SHDSUBMESH_VERTEX_COLOR`_
      * `W3D_CHUNK_SHDSUBMESH_VERTEX_INFLUENCES`_

W3D_CHUNK_MESH
~~~~~~~~~~~~~~

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

This is the root mesh definition chunk. It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_MESH_HEADER3
* W3D_CHUNK_VERTICES
* W3D_CHUNK_VERTEX_NORMALS
* W3D_CHUNK_MESH_USER_TEXT
* W3D_CHUNK_VERTEX_INFLUENCES
* W3D_CHUNK_TRIANGLES
* W3D_CHUNK_VERTEX_SHADE_INDICES
* W3D_CHUNK_PRELIT_UNLIT
* W3D_CHUNK_PRELIT_VERTEX
* W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_PASS
* W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_TEXTURE
* W3D_CHUNK_MATERIAL_INFO
* W3D_CHUNK_SHADERS
* W3D_CHUNK_VERTEX_MATERIALS
* W3D_CHUNK_TEXTURES
* W3D_CHUNK_MATERIAL_PASS
* W3D_CHUNK_TEXTURE_STAGE
* W3D_CHUNK_DEFORM
* W3D_CHUNK_TANGENTS
* W3D_CHUNK_BITANGENTS
* W3D_CHUNK_SHADER_MATERIALS
* W3D_CHUNK_PS2_SHADERS
* W3D_CHUNK_AABTREE
* W3D_CHUNK_SECONDARY_VERTICES
* W3D_CHUNK_SECONDARY_VERTEX_NORMALS


W3D_CHUNK_MESH_HEADER3
~~~~~~~~~~~~~~~~~~~~~~

The mesh header contains general info about the mesh.

======  =====  ===============  ====================
Offset  Bytes  Type             Name
======  =====  ===============  ====================
0       4      UINT32           Version
4       4      UINT32           MeshFlags
8       16     CHAR[16]         MeshName
24      16     CHAR[16]         ContainerName
40      4      UINT32           NumTriangles
44      4      UINT32           NumVertices
48      4      UINT32           NumMaterials
52      4      UINT32           NumDamageStages
56      4      SINT32           SortLevel
60      4      UINT32           PrelitVersion
64      4      UINT32           FutureCounts
68      4      UINT32           VertexChannels
72      4      UINT32           FaceChannels
76      12     `W3D_VECTOR3`_   BoundingBoxMin
88      12     `W3D_VECTOR3`_   BoundingBoxMax
100     12     `W3D_VECTOR3`_   BoundingSphereCenter
112     4      FLOAT32          BoundingSphereRadius
======  =====  ===============  ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **MeshFlags**: bitwise-or'd collection of `W3D_MESH_FLAGS`_ values.
* **MeshName**: 16 Byte field for the name of the mesh.
* **ContainerName**: 16 Byte Field for the name of the file.
* **NumTriangles**: Number of triangles.
* **NumVertices**: Number of unique vertices.
* **NumMaterials**: Number of unique materials.
* **NumDamageStages**: Number of damage offset chunks.
* **SortLevel**: Static sorting level of this mesh.
* **PrelitVersion**: Mesh generated by this version of Lightmap Tool (Lightscape).
* **FutureCounts**: Reserved for future use.
* **VertexChannels**: bitwise-or'd collection of `W3D_VERTEX_CHANNELS`_ values.
* **FaceChannels**: bitwise-or'd collection of `W3D_FACE_CHANNELS`_ values.
* **BoundingBoxMin**: Min corner of the bounding box.
* **BoundingBoxMax**: Max corner of the bounding box.
* **BoundingSphereCenter**: Center of bounding sphere.
* **BoundingSphereRadius**: Bounding sphere radius.

W3D_VERTEX_CHANNELS
~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x1         Location                    Object-space location of the vertex
0x2         Normal                      Object-space normal for the vertex
0x4         TexCoord                    Texture coordinate
0x8         Color                       Vertex color
0x10        BoneId                      Per-vertex bone id for skins
==========  ==========================  ==============

W3D_FACE_CHANNELS
~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x1         Face                        Basic face info, W3dTriStruct...
==========  ==========================  ==============

W3D_MESH_FLAGS
~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x0         None                        Plain old normal mesh
0x1         CollisionBox                (obsolete as of 4.1) Mesh is a collision box (should be 8 verts, should be hidden, etc)
0x2         Skin                        (obsolete as of 4.1) Skin mesh 
0x4         Shadow                      (obsolete as of 4.1) Intended to be projected as a shadow
0x8         Aligned                     (obsolete as of 4.1) Always aligns with camera
0xFF0       CollisionTypeMask           Mask for the collision type bits
0x10        CollisionTypePhysical       Physical collisions
0x20        CollisionTypeProjectile     Projectiles (rays) collide with this
0x40        CollisionTypeVis            Vis rays collide with this mesh
0x80        CollisionTypeCamera         Camera rays/boxes collide with this mesh
0x100       CollisionTypeVehicle        Vehicles collide with this mesh (and with physical collision meshes)
0x1000      Hidden                      This mesh is hidden by default
0x2000      TwoSided                    Render both sides of this mesh
0x4000      ObsoleteLightMapped         Obsolete lightmapped mesh
0x8000      CastShadow                  This mesh casts shadows. Retained for backwards compatibility - use W3D_MESH_FLAG_PRELIT_* instead
0xFF0000    GeometryTypeMask            (introduced with 4.1)
0x0         GeometryTypeNormal          (4.1+) Normal mesh geometry
0x10000     GeometryTypeCameraAligned   (4.1+) camera aligned mesh
0x20000     GeometryTypeSkin            (4.1+) skin mesh
0x30000     ObsoleteGeometryTypeShadow  (4.1+) shadow mesh OBSOLETE!
0x40000     GeometryTypeAAbox           (4.1+) aabox OBSOLETE!
0x50000     GeometryTypeOBBox           (4.1+) obbox OBSOLETE!
0x60000     GeometryTypeCameraOriented  (4.1+) Camera oriented mesh (points *towards* camera)
0xF000000   PrelitMask                  (4.2+) 
0x1000000   PrelitUnlit                 Mesh contains an unlit material chunk wrapper
0x2000000   PrelitVertex                Mesh contains a precalculated vertex-lit material chunk wrapper
0x4000000   PrelitLightMapMultiPass     Mesh contains a precalculated multi-pass lightmapped material chunk wrapper
0x8000000   PrelitLightMapMultiTexture  Mesh contains a precalculated multi-texture lightmapped material chunk wrapper
0x10000000  Shatterable                 This mesh is shatterable
0x20000000  NPatchable                  It is okay to NPatch this mesh
==========  ==========================  ==============

W3D_CHUNK_VERTICES
~~~~~~~~~~~~~~~~~~

Array of vertices.

======  ======  =================  ====================
Offset  Bytes   Type               Name
======  ======  =================  ====================
0       12 * N  `W3D_VECTOR3`_[N]  Vertices
======  ======  =================  ====================

``N`` is the number of vertices specified in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

* **Vertices**: Each Vertex in the mesh.

W3D_CHUNK_VERTEX_NORMALS
~~~~~~~~~~~~~~~~~~~~~~~~

Array of normals.

======  ======  =================  ====================
Offset  Bytes   Type                Name
======  ======  =================  ====================
0       12 * N  `W3D_VECTOR3`_[N]   Normals
======  ======  =================  ====================

``N`` is the number of vertices specified in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

* **Normals**: Each Normal in the mesh.

W3D_CHUNK_MESH_USER_TEXT
~~~~~~~~~~~~~~~~~~~~~~~~

Text from the MAX comment field (null-terminated string).

======  ==========  ======================  ====================
Offset  Bytes       Type                    Name
======  ==========  ======================  ====================
0       ChunkSize   CHAR[N]                  UserText
======  ==========  ======================  ====================

* **UserText**: Arbitrary length based on user input within 3dsMAX.

W3D_CHUNK_VERTEX_INFLUENCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mesh deformation vertex connections.

For Each Vertex specifed in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       2       UINT16        BoneIndex
2       6       UINT8[6]      Padding
======  ======  ============  ====================

* **BoneIndex**: ID of the bone in which the vertex is influenced.
* **Padding**: Evens out the data structure.

WWSKIN only allows 1 bone per vertex.

**TODO**: Does BFME have a second bone index, and bone weights?

TT_W3D_VERTEX_INFLUENCE
~~~~~~~~~~~~~~~~~~~~~~~

TT: Added Max Skin Support which now allows two bone weights

For Each Vertex specifed in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4       UINT16[2]        BoneIndex
4       4       UINT16[2]        Weight
======  ======  ============  ====================

* **BoneIndex**: ID of the bone in which the vertex is influenced up to two Bones.
* **Weight**: Weight of each bone on the vertex.


W3D_CHUNK_TRIANGLES
~~~~~~~~~~~~~~~~~~~

Array of Triangles

For Each Triangle specifed in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

======  =====  ==============  ====================
Offset  Bytes  Type            Name
======  =====  ==============  ====================
0       12     UINT32[3]       VertexIndex
12      4      UINT32          SurfaceType
16      12     `W3D_VECTOR3`_  Normal
28      4      FLOAT32         Distance
======  =====  ==============  ====================

* **VertexIndex**: Three vertex indexes: normal, texcoord and color indices.
* **SurfaceType**: A value from the `W3D_SURFACE_TYPE`_ enumeration.
* **Normal**: plane normal.
* **Distance**: plane distance.



W3D_SURFACE_TYPE
~~~~~~~~~~~~~~~~

==========  ==========================
Value       Name
==========  ==========================
0           LightMetal
1           HeavyMetal
2           Water
3           Sand
4           Dirt
5           Mud
6           Grass
7           Wood
8           Concrete
9           Flesh
10          Rock
11          Snow
12          Ice
13          Default
14          Glass
15          Cloth
16          TiberiumField
17          FoliagePermeable
18          GlassPermeable
19          IcePermeable
20          ClothPermeable
21          Electrical
22          Flammable
23          Steam
24          EletricalPermeable
25          FlammablePermeable
26          SteamPermeable
27          WaterPermeable
28          TiberiumWater
29          TiberiumWaterPermeable
30          UnderwaterDirt
31          UnderwaterTiberiumDirt
==========  ==========================

W3D_CHUNK_VERTEX_SHADE_INDICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Shade indexes for each vertex.

These are in relation to 3ds max smoothing groups.

Later w3d engine games ignore these.

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4 * N  UINT32       ShadeIndices
======  =====  ===========  ====================

``N`` is the number of vertices specified in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

* **ShadeIndices**: Data Derived from 3ds max smoothing groups.

W3D_CHUNK_PRELIT_UNLIT
~~~~~~~~~~~~~~~~~~~~~~~

Optional unlit material chunk wrapper this was mostly used in renegade buildings using the lightscape tool.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

W3D_CHUNK_PRELIT_VERTEX
~~~~~~~~~~~~~~~~~~~~~~~

Optional vertex-lit material chunk wrapper this was mostly used in renegade buildings using the lightscape tool.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========


W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_PASS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional lightmapped multi-pass material chunk wrapper this was mostly used in renegade buildings using the lightscape tool.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

W3D_CHUNK_PRELIT_LIGHTMAP_MULTI_TEXTURE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional lightmapped multi-texture material chunk wrapper this was mostly used in renegade buildings using the lightscape tool.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

W3D_CHUNK_MATERIAL_INFO
~~~~~~~~~~~~~~~~~~~~~~~

Declares the number of material passes, vertex materials, shaders, and textures that will be found in subsequent chunks.

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       PassCount
4       4      UINT32       VertexMaterialCount
8       4      UINT32       ShaderCount
12      4      UINT32       TextureCount
======  =====  ===========  ====================

* **PassCount**: How many material passes this render object uses
* **VertexMaterialCount**: How many vertex materials are used
* **ShaderCount**: How many shaders are used
* **TextureCount**: How many textures are used

W3D_CHUNK_SHADERS
~~~~~~~~~~~~~~~~~

Container chunk for an array of `W3D_SHADER`_ structures.
The number of shaders is contained in the **ShaderCount** field in the `W3D_CHUNK_MATERIAL_INFO`_ chunk.

W3D_SHADER
~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       1      UINT8        DepthCompare
1       1      UINT8        DepthMask
2       1      UINT8        ColorMask
3       1      UINT8        DestBlend
4       1      UINT8        FogFunc
5       1      UINT8        PrimaryGradient
6       1      UINT8        SecondaryGradient
7       1      UINT8        SrcBlend
8       1      UINT8        Texturing
9       1      UINT8        DetailColorFunc
10      1      UINT8        DetailAlphaFunc
11      1      UINT8        ShaderPreset
12      1      UINT8        AlphaTest
13      1      UINT8        PostDetailColorFunc
14      1      UINT8        PostDetailAlphaFunc
15      1      UINT8        [Padding]
======  =====  ===========  ====================

* **DepthCompare**: A value from the `W3D_SHADER_DEPTH_COMPARE`_ enumeration.
* **DepthMask**: A value from the `W3D_SHADER_DEPTH_MASK`_ enumeration.
* **ColorMask**: Now obsolete and ignored.
* **DestBlend**: A value from the `W3D_SHADER_DEST_BLEND_FUNC`_ enumeration.
* **FogFunc**: Now obsolete and ignored.
* **PrimaryGradient**: A value from the `W3D_SHADER_PRIMARY_GRADIENT`_ enumeration.
* **SecondaryGradient**: A value from the `W3D_SHADER_SECONDARY_GRADIENT`_ enumeration.
* **SrcBlend**: A value from the `W3D_SHADER_SRC_BLEND_FUNC`_ enumeration.
* **Texturing**: A value from the `W3D_SHADER_TEXTURING`_ enumeration.
* **DetailColorFunc**: A value from the `W3D_SHADER_DETAIL_COLOR_FUNC`_ enumeration.
* **DetailAlphaFunc**: A value from the `W3D_SHADER_DETAIL_ALPHA_FUNC`_ enumeration.
* **ShaderPreset**: Now obsolete and ignored.
* **AlphaTest**: A value from the `W3D_SHADER_ALPHA_TEST`_ enumeration.
* **PostDetailColorFunc**: A value from the `W3D_SHADER_DETAIL_COLOR_FUNC`_ enumeration.
* **PostDetailAlphaFunc**: A value from the `W3D_SHADER_DETAIL_ALPHA_FUNC`_ enumeration.
* **Padding**: Evens out the data structure.

W3D_SHADER_DEPTH_COMPARE
~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           PassNever                   Pass never (i.e. always fail depth comparison test)
1           PassLess                    Pass if incoming less than stored
2           PassEqual                   Pass if incoming equal to stored
3           PassLEqual                  Pass if incoming less than or equal to stored (default)
4           PassGreater                 Pass if incoming greater than stored
5           PassNotEqual                Pass if incoming not equal to stored
6           PassGEqual                  Pass if incoming greater than or equal to stored
7           PassAlways                  Pass always
==========  ==========================  ==============

W3D_SHADER_DEPTH_MASK
~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           WriteDisable                Disable depth buffer writes 
1           WriteEnable                 Enable depth buffer writes (default)
==========  ==========================  ==============

W3D_SHADER_DEST_BLEND_FUNC
~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Zero                        Destination pixel doesn't affect blending (default)
1           One                         Destination pixel added unmodified
2           SrcColor                    Destination pixel multiplied by fragment RGB components
3           OneMinusSrcColor            Destination pixel multiplied by one minus (i.e. inverse) fragment RGB components
4           SrcAlpha                    Destination pixel multiplied by fragment alpha component
5           OneMinusSrcAlpha            Destination pixel multiplied by fragment inverse alpha
6           SrcColorPreFog              Destination pixel multiplied by fragment RGB components prior to fogging
==========  ==========================  ==============

W3D_SHADER_PRIMARY_GRADIENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     Disable primary gradient (same as OpenGL 'decal' texture blend)
1           Modulate                    Modulate fragment ARGB by gradient ARGB (default)
2           Add                         Add gradient RGB to fragment RGB, copy gradient A to fragment A
3           BumpEnvMap                  Environment-mapped bump mapping
==========  ==========================  ==============

W3D_SHADER_SECONDARY_GRADIENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     Don't draw secondary gradient (default)
1           Enable                      Add secondary gradient RGB to fragment RGB 
==========  ==========================  ==============

W3D_SHADER_SRC_BLEND_FUNC
~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Zero                        Fragment not added to color buffer
1           One                         Fragment added unmodified to color buffer (default)
2           SrcAlpha                    Fragment RGB components multiplied by fragment A
3           OneMinusSrcAlpha            Fragment RGB components multiplied by fragment inverse (one minus) A
==========  ==========================  ==============

W3D_SHADER_TEXTURING
~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     No texturing (treat fragment initial color as 1,1,1,1) (default)
1           Enable                      Enable texturing
==========  ==========================  ==============

W3D_SHADER_DETAIL_COLOR_FUNC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     Local (default)
1           Detail                      Other
2           Scale                       Local * Other
3           InvScale                    ~(~Local * ~Other) = Local + (1-Local)*Other
4           Add                         Local + Other
5           Sub                         Local - Other
6           SubR                        Other - Local
7           Blend                       (LocalAlpha)*Local + (~LocalAlpha)*Other
8           DetailBlend                 (OtherAlpha)*Local + (~OtherAlpha)*Other
==========  ==========================  ==============

W3D_SHADER_DETAIL_ALPHA_FUNC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     Local (default)
1           Detail                      Other
2           Scale                       Local * Other
3           InvScale                    ~(~Local * ~Other) = Local + (1-Local)*Other
==========  ==========================  ==============

W3D_SHADER_ALPHA_TEST
~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           Disable                     Disable alpha testing (default)
1           Enable                      Enable alpha testing
==========  ==========================  ==============

W3D_CHUNK_VERTEX_MATERIALS
~~~~~~~~~~~~~~~~~~~~~~~~~~

Wraps the vertex materials.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_VERTEX_MATERIAL



W3D_CHUNK_VERTEX_MATERIAL
~~~~~~~~~~~~~~~~~~~~~~~~~

Vertex material wrapper.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_VERTEX_MATERIAL_NAME
* W3D_CHUNK_VERTEX_MATERIAL_INFO
* W3D_CHUNK_VERTEX_MAPPER_ARGS0
* W3D_CHUNK_VERTEX_MAPPER_ARGS1

W3D_CHUNK_VERTEX_MATERIAL_NAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vertex material name (null-terminated string)

======  ==========  =======  ===========
Offset  Bytes       Type     Name
======  ==========  =======  ===========
0       ChunkSize   CHAR[N]  Material Name
======  ==========  =======  ===========

* **Material Name**: Name of the Material

W3D_CHUNK_VERTEX_MATERIAL_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vertex material info.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4       UINT32        MaterialFlags
4       4       `W3D_RGB`_    Ambient
8       4       `W3D_RGB`_    Diffuse
12      4       `W3D_RGB`_    Specular
16      4       `W3D_RGB`_    Emissive
20      4       FLOAT32       Shininess
20      4       FLOAT32       Opacity
20      4       FLOAT32       Translucency
======  ======  ============  ====================

* **MaterialFlags**: bitwise-or'd collection of `W3D_VERTEX_MATERIAL_FLAGS`_ values.
* **Ambient**: Ambient Color values in RGB.
* **Diffuse**: Diffuse Color values in RGB
* **Specular**: Specular Color values in RGB
* **Emissive**: Emissive Color values in RGB
* **Shininess**: How tight the specular highlight will be, 1 - 1000 (default = 1).
* **Opacity**: How opaque the material is, 0.0 = invisible, 1.0 = fully opaque (default = 1).
* **Translucency**: How much light passes through the material. (default = 0).

W3D_VERTEX_MATERIAL_FLAGS
~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==============================================  ==============
Value       Name                                            Description
==========  ==============================================  ==============
0x1         W3DVERTMAT_USE_DEPTH_CUE                       
0x2         W3DVERTMAT_ARGB_EMISSIVE_ONLY 
0x4         W3DVERTMAT_COPY_SPECULAR_TO_DIFFUSE                       
0x8         W3DVERTMAT_DEPTH_CUE_TO_ALPHA                     


0xFF0000    W3DVERTMAT_STAGE0_MAPPING_MASK          
0x0         W3DVERTMAT_STAGE0_MAPPING_UV      
0x10000     W3DVERTMAT_STAGE0_MAPPING_ENVIRONMENT     
0x20000     W3DVERTMAT_STAGE0_MAPPING_CHEAP_ENVIRONMENT            
0x30000     W3DVERTMAT_STAGE0_MAPPING_SCREEN         
0x40000     W3DVERTMAT_STAGE0_MAPPING_LINEAR_OFFSET       
0x50000     W3DVERTMAT_STAGE0_MAPPING_SILHOUETTE                  
0x60000     W3DVERTMAT_STAGE0_MAPPING_SCALE                    
0x70000     W3DVERTMAT_STAGE0_MAPPING_GRID         
0x80000     W3DVERTMAT_STAGE0_MAPPING_ROTATE                  
0x90000     W3DVERTMAT_STAGE0_MAPPING_SINE_LINEAR_OFFSET         
0xA0000     W3DVERTMAT_STAGE0_MAPPING_STEP_LINEAR_OFFSET          
0xB0000     W3DVERTMAT_STAGE0_MAPPING_ZIGZAG_LINEAR_OFFSET   
0xC0000     W3DVERTMAT_STAGE0_MAPPING_WS_CLASSIC_ENV          
0xD0000     W3DVERTMAT_STAGE0_MAPPING_WS_ENVIRONMENT  
0xE0000     W3DVERTMAT_STAGE0_MAPPING_GRID_CLASSIC_ENV          
0xF0000     W3DVERTMAT_STAGE0_MAPPING_GRID_ENVIRONMENT          
0x100000    W3DVERTMAT_STAGE0_MAPPING_RANDOM  
0x110000    W3DVERTMAT_STAGE0_MAPPING_EDGE                 
0x120000    W3DVERTMAT_STAGE0_MAPPING_BUMPENV               

0xFF00      W3DVERTMAT_STAGE1_MAPPING_MASK             
0x0         W3DVERTMAT_STAGE1_MAPPING_UV
0x100       W3DVERTMAT_STAGE1_MAPPING_ENVIRONMENT 
0x200       W3DVERTMAT_STAGE1_MAPPING_CHEAP_ENVIRONMENT             
0x300       W3DVERTMAT_STAGE1_MAPPING_SCREEN           
0x400       W3DVERTMAT_STAGE1_MAPPING_LINEAR_OFFSET
0x500       W3DVERTMAT_STAGE1_MAPPING_SILHOUETTE
0x600       W3DVERTMAT_STAGE1_MAPPING_SCALE 
0x700       W3DVERTMAT_STAGE1_MAPPING_GRID 
0x800       W3DVERTMAT_STAGE1_MAPPING_ROTATE
0x900       W3DVERTMAT_STAGE1_MAPPING_SINE_LINEAR_OFFSET
0xA00       W3DVERTMAT_STAGE1_MAPPING_ZIGZAG_LINEAR_OFFSET
0xB00       W3DVERTMAT_STAGE1_MAPPING_ZIGZAG_LINEAR_OFFSET
0xC00       W3DVERTMAT_STAGE1_MAPPING_WS_CLASSIC_ENV
0xD00       W3DVERTMAT_STAGE1_MAPPING_WS_ENVIRONMENT 
0xE00       W3DVERTMAT_STAGE1_MAPPING_GRID_CLASSIC_ENV 
0xF00       W3DVERTMAT_STAGE1_MAPPING_GRID_ENVIRONMENT
0x1000      W3DVERTMAT_STAGE1_MAPPING_RANDOM
0x1100      W3DVERTMAT_STAGE1_MAPPING_EDGE 
0x1200      W3DVERTMAT_STAGE1_MAPPING_BUMPENV 

0xFF000000  W3DVERTMAT_PSX_MASK
0x7000000   W3DVERTMAT_PSX_TRANS_MASK
0x0         W3DVERTMAT_PSX_TRANS_NONE
0x1000000   W3DVERTMAT_PSX_TRANS_100
0x2000000   W3DVERTMAT_PSX_TRANS_50
0x3000000   W3DVERTMAT_PSX_TRANS_25 
0x4000000   W3DVERTMAT_PSX_TRANS_MINUS_100 
0x8000000   W3DVERTMAT_PSX_NO_RT_LIGHTING
==========  ==============================================  ==============

W3D_CHUNK_VERTEX_MAPPER_ARGS0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arguments for the first stage mapping (null-terminated, line-break-separated string).

======  ==========  =======  ===========
Offset  Bytes       Type     Name
======  ==========  =======  ===========
0       ChunkSize   CHAR[N]  ARGS0
======  ==========  =======  ===========

* **ARGS0**: Argument for the first texture stage.

W3D_CHUNK_VERTEX_MAPPER_ARGS1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Arguments for the second stage mapping (null-terminated, line-break-separated string).

======  ==========  =======  ===========
Offset  Bytes       Type     Name
======  ==========  =======  ===========
0       ChunkSize   CHAR[N]  ARGS1
======  ==========  =======  ===========

* **ARGS1**: Argument for the second texture stage.


W3D_CHUNK_TEXTURES
~~~~~~~~~~~~~~~~~~

Wraps all of the texture info.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_TEXTURE

W3D_CHUNK_TEXTURE
~~~~~~~~~~~~~~~~~

Wraps a texture definition.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_VERTEX_TEXTURE_NAME
* W3D_CHUNK_VERTEX_TEXTURE_INFO

W3D_CHUNK_TEXTURE_NAME
~~~~~~~~~~~~~~~~~~~~~~

Texture filename (null-terminated string).

======  ==========  =======  ===========
Offset  Bytes       Type     Name
======  ==========  =======  ===========
0       ChunkSize   CHAR[N]  Texture Name
======  ==========  =======  ===========

* **Texture Name**: Name of the Texture

W3D_CHUNK_TEXTURE_INFO
~~~~~~~~~~~~~~~~~~~~~~

Optional texture info.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       2       UINT16        TextureFlags
2       2       UINT16        AnimType
4       4       UINT32        FrameCount
8       4       FLOAT32       FrameRate
======  ======  ============  ====================

* **TextureFlags**: bitwise-or'd collection of `W3D_TEXTURE_FLAGS`_ values.
* **AnimType**: bitwise-or'd collection of `W3D_TEXTURE_ANIMATION_FLAGS`_ values.
* **FrameCount**: Number of frames (1 if not animated).
* **FrameRate**: Frame rate, frames per second in floating point.


W3D_TEXTURE_FLAGS
~~~~~~~~~~~~~~~~~~~

==========  ===========================  ==============
Value       Name                          Description
==========  ===========================  ==============
0x1         W3DTEXTURE_PUBLISH            this texture should be "published" (indirected so its changeable in code)
0x2         W3DTEXTURE_RESIZE_OBSOLETE    this texture should be resizeable (OBSOLETE!!!)
0x4         W3DTEXTURE_NO_LOD             this texture should not have any LOD (mipmapping or resizing)
0x8         W3DTEXTURE_CLAMP_U            this texture should be clamped on U
0x10        W3DTEXTURE_CLAMP_V            this texture should be clamped on V
0x20        W3DTEXTURE_ALPHA_BITMAP       this texture's alpha channel should be collapsed to one bit
                                        
0xc0        W3DTEXTURE_MIP_LEVELS_MASK  
0x0         W3DTEXTURE_MIP_LEVELS_ALL     generate all mip-level
0x40        W3DTEXTURE_MIP_LEVELS_2       generate up to 2 mip-levels (NOTE: use W3DTEXTURE_NO_LOD to generate just 1 mip-level)
0x80        W3DTEXTURE_MIP_LEVELS_3       generate up to 3 mip-levels
0xc0        W3DTEXTURE_MIP_LEVELS_4       generate up to 4 mip-levels
                                          Hints to describe the intended use of the various passes / stages
8           W3DTEXTURE_HINT_SHIFT         number of bits to shift up
0xff00      W3DTEXTURE_HINT_MASK          mask for shifted hint value

0x0         W3DTEXTURE_HINT_BASE          base texture
0x100       W3DTEXTURE_HINT_EMISSIVE      emissive map
0x200       W3DTEXTURE_HINT_ENVIRONMENT   environment/reflection map
0x300       W3DTEXTURE_HINT_SHINY_MASK    shinyness mask map

0x1000      W3DTEXTURE_TYPE_MASK
0x0         W3DTEXTURE_TYPE_COLORMAP      Color map.
0x1000      W3DTEXTURE_TYPE_BUMPMAP       Grayscale heightmap (to be converted to bumpmap).
==========  ===========================  ==============

W3D_TEXTURE_ANIMATION_FLAGS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x0         W3DTEXTURE_ANIM_LOOP
0x1         W3DTEXTURE_ANIM_PINGPONG
0x2         W3DTEXTURE_ANIM_ONCE
0x3         W3DTEXTURE_ANIM_MANUAL
==========  ==========================  ==============

W3D_CHUNK_MATERIAL_PASS
~~~~~~~~~~~~~~~~~~~~~~~

Wraps the information for a single material pass.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_VERTEX_MATERIAL_IDS
* W3D_CHUNK_SHADER_IDS
* W3D_CHUNK_DCG
* W3D_CHUNK_DIG
* W3D_CHUNK_SCG
* W3D_CHUNK_SHADER_MATERIAL_ID
* W3D_CHUNK_TEXTURE_STAGE
* W3D_CHUNK_TANGENTS
* W3D_CHUNK_BITANGENTS

W3D_CHUNK_VERTEX_MATERIAL_IDS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single or per-vertex array of UINT32 vertex material indices.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4 * N   UINT32          Vertex Material Index
======  ======  =============  ====================

``N`` is the number of Vertex Material count specified in the `W3D_CHUNK_MATERIAL_INFO`_ chunk.

* **Vertex Material Index**: Index value for the Material


W3D_CHUNK_SHADER_IDS
~~~~~~~~~~~~~~~~~~~~

Single or per-triangle array of UINT32 shader indices.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4 * N   UINT32          Shader Index
======  ======  =============  ====================

``N`` is the number of Shader count specified in the `W3D_CHUNK_MATERIAL_INFO`_ chunk.

* **Shader Index**: Index value for the Shader

W3D_CHUNK_DCG
~~~~~~~~~~~~~

Per-vertex diffuse color values.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4 * N   `W3D_RGBA`_   DCG
======  ======  ============  ====================

``N`` is the number of Vertices with DCG values.

* **DCG**: Diffuse Color.

W3D_CHUNK_DIG
~~~~~~~~~~~~~

Per-vertex diffuse illumination values.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4 * N   `W3D_RGB`_    DIG
======  ======  ============  ====================

``N`` is the number of Vertices with DIG values.

* **DIG**: Diffuse Illumination.

W3D_CHUNK_SCG
~~~~~~~~~~~~~

Per-vertex specular color values.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4 * N   `W3D_RGB`_    SCG
======  ======  ============  ====================

``N`` is the number of Vertices with SCG values.

* **SCG**: Specular color.


W3D_CHUNK_SHADER_MATERIAL_ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single or per-tri array of uint32 fx shader indices
Index into the array of shader materials in the `W3D_CHUNK_SHADER_MATERIAL`_ chunk.
Also Known as: W3D_CHUNK_FXSHADER_IDS

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4 * N   UINT32        FX Shader Index
======  ======  ============  ====================

BFMEII:
TODO: Dig Deeper here
``N`` is the number of triangles in shader materials in `W3D_CHUNK_SHADER_MATERIAL`_

* **FX Shader Index**: FX Shader Index

W3D_CHUNK_TEXTURE_STAGE
~~~~~~~~~~~~~~~~~~~~~~~

Wrapper around a texture stage.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_TEXTURE_IDS
* W3D_CHUNK_STAGE_TEXCOORDS
* W3D_CHUNK_PER_FACE_TEXCOORD_IDS


W3D_CHUNK_TEXTURE_IDS
~~~~~~~~~~~~~~~~~~~~~

Single or per-triangle array of UINT32 texture indices.

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4 * N   UINT32        Texture Index
======  ======  ============  ====================

TODO: Dig Deeper here

``N`` is the number of triangles in 

* **Texture Index**: Texture Index

W3D_CHUNK_STAGE_TEXCOORDS
~~~~~~~~~~~~~~~~~~~~~~~~~

Per-vertex texture coordinates.

======  ======  ===============    ====================
Offset  Bytes   Type                Name
======  ======  ===============    ====================
0       8 * N   `W3D_TEXCOORD`_      Vertex UV
======  ======  ===============    ====================


``N`` is the number of vertices in `W3D_CHUNK_MESH_HEADER3`_.

* **Vertex UV**: UV data for texture mapping.

W3D_CHUNK_PER_FACE_TEXCOORD_IDS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Indices to `W3D_CHUNK_STAGE_TEXCOORDS`_.

======  ======  ===============  ====================
Offset  Bytes   Type              Name
======  ======  ===============  ====================
0       4 * N   `W3D_VECTOR3i`_   Face UV Indices
======  ======  ===============  ====================

TODO: Dig Deeper here

``N`` is the number of Triangles in 

* **Face UV Indices**: 

W3D_CHUNK_SHADER_MATERIALS
~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapper around an array of shader materials.

Also known as: W3D_CHUNK_FX_SHADERS

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_SHADER_MATERIAL


W3D_CHUNK_SHADER_MATERIAL
~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapper that stores material properties for use in conjunction with a specific pixel shader.
Also Known as: W3D_CHUNK_FX_SHADER

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_SHADER_MATERIAL_HEADER
* W3D_CHUNK_SHADER_MATERIAL_PROPERTY


W3D_CHUNK_SHADER_MATERIAL_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Stores the shader information.
Also Known as: W3D_CHUNK_FX_SHADER_INFO

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       1      UINT8        Version
1       32     CHAR[32]     ShaderName
33      1      UINT8        Technique
34      3      UINT8[3]     Pading
======  =====  ===========  ====================

TODO: Dig Deeper here

* **Version**: W3D Format `W3D_VERSION`_ .
* **ShaderName**: 
* **Technique**: 
* **Pading**: 

W3D_CHUNK_SHADER_MATERIAL_PROPERTY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A single shader material property with a type and value.
Also known as: W3D_CHUNK_FX_SHADER_CONSTANT

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       Type
4       4      UINT32       NameLength
8       N      CHAR[N]      ConstantName
======  =====  ===========  ====================

``N`` is equal to the value of NameLength

* **Type**: collection of `W3D_SHADER_MATERIAL_FLAGS`_ values.
* **NameLength**: Length of the name.
* **ConstantName**: Actual name.



W3D_SHADER_MATERIAL_FLAGS
~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x1         CONSTANT_TYPE_TEXTURE       Texture
0x2         CONSTANT_TYPE_FLOAT1        Float
0x3         CONSTANT_TYPE_FLOAT2        Vector2
0x4         CONSTANT_TYPE_FLOAT3        Vector3
0x5         CONSTANT_TYPE_FLOAT4        Vector4
0x6         CONSTANT_TYPE_INT           Int
0x7         CONSTANT_TYPE_BOOL          Bool
==========  ==========================  ==============


W3D_CHUNK_DEFORM
~~~~~~~~~~~~~~~~~~
Mesh deform or 'damage' information.
Appears in the Generals 3dsMAX Exporter code
Appears in the Earth & Beyond W3D Parser code

**Generals / Zero Hour payload:**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       SetCount
4       4      UINT32       AlphaPasses
======  =====  ===========  ====================

* **SetCount**: The amount of sets in this deform object.
* **AlphaPasses**: The total number of alpha passes in the deform set.


**Earth & Beyond payload:**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       SetCount
4       4      UINT32       AlphaPasses
8       L-8    UINT8[8]     Reserved (skip)
======  =====  ===========  ====================

``L`` is the chunk's payload length. E&B code reads the 8-byte header, 
then consumes the remainder of this chunk's payload as reserved.

* **SetCount**: The amount of sets in this deform object.
* **AlphaPasses**: The total number of alpha passes in the deform set.



W3D_CHUNK_DEFORM_SET
~~~~~~~~~~~~~~~~~~~~
Set of deform information
Appears in the Generals 3dsMAX Exporter code
Appears in the Earth & Beyond W3D Parser code

**Generals / Zero Hour payload:**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       KeyframeCount
4       4      UINT32       Flags
======  =====  ===========  ====================

* **KeyframeCount**: The amount of keyframes in this deformation set.
* **Flags**: Any flags / attributes associated with this set.

**Earth & Beyond payload:**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       KeyframeCount
4       4      UINT32       Flags
8       4      UINT32       Reserved
======  =====  ===========  ====================

* **KeyframeCount**: The amount of keyframes in this deformation set.
* **Flags**: Any flags / attributes associated with this set.

W3D_CHUNK_DEFORM_KEYFRAME
~~~~~~~~~~~~~~~~~~~~~~~~~
A keyframe of deform information in the set
Appears in the Generals 3dsMAX Exporter code
Appears in the Earth & Beyond W3D Parser code

**Generals / Zero Hour payload:**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      DeformPercent
4       4      UINT32       DataCount
======  =====  ===========  ====================

* **DeformPercent**: The percentage of deformation for this keyframe.
* **DataCount**: The amount of data for this keyframe.

**Earth & Beyond payload (adds reserved[2]):**

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      DeformPercent
4       4      UINT32       DataCount
8       8      UINT32[2]    Reserved
======  =====  ===========  ====================

* **DeformPercent**: The percentage of deformation for this keyframe.
* **DataCount**: The amount of data for this keyframe.

W3D_CHUNK_DEFORM_DATA
~~~~~~~~~~~~~~~~~~~~~
Deform information about a single vertex
Appears in the Generals 3dsMAX Exporter code
Appears in the Earth & Beyond W3D Parser code

**Generals / Zero Hour entry layout (20 bytes per entry):**

======  =====  ============  ====================
Offset  Bytes  Type          Name
======  =====  ============  ====================
0       4      UINT32        VertexIndex
4       12     FLOAT32[3]    Position (X,Y,Z)
16      4      UINT8[4]      Color (R,G,B,A)
======  =====  ============  ====================

* **VertexIndex**: The vertex index for this data to be appliced too.
* **Position (X,Y,Z)**: The vector position of this data.
* **Color (R,G,B,A)**: The color assosicated with the deform data.

**Earth & Beyond entry layout (28 bytes per entry; adds reserved[2]):**

======  =====  ============  ====================
Offset  Bytes  Type          Name
======  =====  ============  ====================
0       4      UINT32        VertexIndex
4       12     FLOAT32[3]    Position (X,Y,Z)
16      4      UINT8[4]      Color (R,G,B,A)
20      8      UINT32[2]     Reserved
======  =====  ============  ====================

* **VertexIndex**: The vertex index for this data to be appliced too.
* **Position (X,Y,Z)**: The vector position of this data.
* **Color (R,G,B,A)**: The color assosicated with the deform data.


W3D_CHUNK_TANGENTS
~~~~~~~~~~~~~~~~~~

Array of tangent vectors.

======  ======  =================  ====================
Offset  Bytes   Type                  Name
======  ======  =================  ====================
0       12 * N  `W3D_VECTOR3`_[N]     Tangent
======  ======  =================  ====================

``N`` is the number of vertices specified in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

* **Tangent**: Tangent Coordinates.

W3D_CHUNK_BITANGENTS
~~~~~~~~~~~~~~~~~~~~

Array of bitangent vectors.
Also Known as W3D_CHUNK_BINORMALS

======  ======  =================  ====================
Offset  Bytes   Type               Name
======  ======  =================  ====================
0       12 * N  `W3D_VECTOR3`_[N]  Binormal
======  ======  =================  ====================

``N`` is the number of vertices specified in the `W3D_CHUNK_MESH_HEADER3`_ chunk.

* **Binormal**: Binormal Coordinates.

W3D_CHUNK_PS2_SHADERS
~~~~~~~~~~~~~~~~~~~~~

Shader info specific to the PlayStation 2.

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       1      UINT8        DepthCompare
1       1      UINT8        DepthMask
2       1      UINT8        PrimaryGradient
3       1      UINT8        Texturing
4       1      UINT8        AlphaTest
5       1      UINT8        AParam
6       1      UINT8        BParam
7       1      UINT8        CParam
8       1      UINT8        DParam
9       3      UINT8[3]     Padding
======  =====  ===========  ====================

TODO: Add rest of the PS2 enum logic

* **DepthCompare**: A value from the `W3D_SHADER_DEPTH_COMPARE`_ enumeration.
* **DepthMask**: A value from the `W3D_SHADER_DEPTH_MASK`_ enumeration.
* **PrimaryGradient**: A value from the `W3D_SHADER_PRIMARY_GRADIENT`_ enumeration.
* **Texturing**: A value from the `W3D_SHADER_TEXTURING`_ enumeration.
* **AlphaTest**: A value from the `W3D_SHADER_ALPHA_TEST`_ enumeration.
* **PostDetailColorFunc**: A value from the `W3D_SHADER_DETAIL_COLOR_FUNC`_ enumeration.
* **PostDetailAlphaFunc**: A value from the `W3D_SHADER_DETAIL_ALPHA_FUNC`_ enumeration.
* **Padding**: Evens out the data structure.

W3D_CHUNK_AABTREE
~~~~~~~~~~~~~~~~~

Wrapper for Axis-Aligned Box Tree for hierarchical polygon culling.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_AABTREE_HEADER
* W3D_CHUNK_AABTREE_POLYINDICES
* W3D_CHUNK_AABTREE_NODES

W3D_CHUNK_AABTREE_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~

Catalog of the contents of the AABTree.

Each mesh can have an associated Axis-Aligned-Bounding-Box tree
which is used for collision detection and certain rendering algorithms.

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32        NodeCount
4       4      UINT32        PolyCount
8       24     UINT32[6]     Padding
======  =====  ===========  ====================

* **NodeCount**: Number of calculated AAB nodes.
* **PolyCount**: Number of triangles within the `W3D_CHUNK_MESH_HEADER3`_.
* **Padding**: Evens out the data structure.


W3D_CHUNK_AABTREE_POLYINDICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Array of UINT32 polygon indices with count=mesh.PolyCount.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4 * N   UINT32         Polygon Index
======  ======  =============  ====================

``N`` is the number of Polygons specified in the `W3D_CHUNK_AABTREE_HEADER`_ chunk.

* **Polygon Index**: 

W3D_CHUNK_AABTREE_NODES
~~~~~~~~~~~~~~~~~~~~~~~


This is a node in the AABTree.
If the MSB of FrontOrPoly0 is 1, then the node is a leaf and contains Poly0 and PolyCount
else, the node is not a leaf and contains indices to its front and back children.  This matches
the format used by AABTreeClass in WW3D.

For each Node specified in the `W3D_CHUNK_AABTREE_HEADER`_ chunk.

======  ======  ===============  ====================
Offset  Bytes   Type              Name
======  ======  ===============  ====================
0       12      `W3D_VECTOR3`_    Min
12      12      `W3D_VECTOR3`_    Max
24      4       UINT32            FrontorPoly0
28      4       UINT32            BackOrPolyCount
======  ======  ===============  ====================

* **Min**: Min corner of the box. 
* **Max**: Max corner of the box.
* **FrontorPoly0**: Index of the front child or poly0 (if MSB is set, then leaf and poly0 is valid).
* **BackOrPolyCount**: Index of the back child or polycount.

W3D_CHUNK_HIERARCHY
~~~~~~~~~~~~~~~~~~~

Wrapper for Hierarchy tree.

	WHT ( Westwood Hierarchy Tree )

	A hierarchy tree defines a set of coordinate systems which are connected
	hierarchically.  The header defines the name, number of pivots, etc.  
	The pivots chunk will contain a W3dPivotStructs for each node in the
	tree.  
	
	The W3dPivotFixupStruct contains a transform for each MAX coordinate
	system and our version of that same coordinate system (bone).  It is 
	needed when the user exports the base pose using "Translation Only".
	These are the matrices which go from the MAX rotated coordinate systems
	to a system which is unrotated in the base pose.  These transformations
	are needed when exporting a hierarchy animation with the given hierarchy
	tree file.

	Another explanation of these kludgy "fixup" matrices:

	What are the "fixup" matrices?  These are the transforms which
	were applied to the base pose when the user wanted to force the
	base pose to use only matrices with certain properties.  For 
	example, if we wanted the base pose to use translations only,
	the fixup transform for each node is a transform which when
	multiplied by the real node's world transform, yeilds a pure
	translation matrix.  Fixup matrices are used in the mesh
	exporter since all vertices must be transformed by their inverses
	in order to make things work.  They also show up in the animation
	exporter because they are needed to make the animation work with
	the new base pose.

Hierarchy tree definition.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HIERARCHY_HEADER
* W3D_CHUNK_PIVOTS
* W3D_CHUNK_PIVOT_FIXUP
* W3D_CHUNK_PIVOT_UNKNOWN1

W3D_CHUNK_HIERARCHY_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~

Hierarchy header contains general info about the hierarchy.

======  ======  ==============  ====================
Offset  Bytes   Type            Name
======  ======  ==============  ====================
0       4       UINT32          Version
4       16      CHAR[16]        Name
20      4       UINT32          NumPivots
24      4       `W3D_VECTOR3`_  Center
======  ======  ==============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte Field for the name of the file.
* **NumPivots**: Number of Pivots
* **Center**: 

W3D_CHUNK_PIVOTS
~~~~~~~~~~~~~~~~

Contains a Pivot Structure for each node in the tree.

Contains a ROOTRANSFORM node at index -1: 
0xffffffff = root pivot; no parent

======  ======  =================  ====================
Offset  Bytes   Type                Name
======  ======  =================  ====================
0       16      CHAR[16]            Name
16      4       UINT32              ParentIDx
20      12      `W3D_VECTOR3`_      Translation
32      12      `W3D_VECTOR3`_      EulerAngles
44      16      `W3D_QUATERNION`_   Rotation
======  ======  =================  ====================

* **Name**: 16 Byte Field for the name of the node
* **ParentIDx**: Id of Parent.
* **Translation**: Translation to pivot point.
* **EulerAngles**: Orientation of the pivot point.
* **Rotation**: Orientation of the pivot point.

W3D_CHUNK_PIVOT_FIXUPS
~~~~~~~~~~~~~~~~~~~~~~

Only needed by the 3ds Max exporter. Doesn't seem to be used at runtime.
Matrix transforms from its original Max orientation to the simplified "translation-only" base pose used during export.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       48      FLOAT32[4][3]  Transform X, Row Y
======  ======  =============  ====================

* **Transform X, Row Y**: This is a direct dump of a MAX 3x4 matrix


W3D_CHUNK_PIVOT_UNKNOWN1
~~~~~~~~~~~~~~~~~~~~~~~~

Possibly used by Earth & Beyond

W3D_CHUNK_ANIMATION
~~~~~~~~~~~~~~~~~~~

Hierarchy animation data.

	WHA (Westwood Hierarchy Animation)

	A Hierarchy Animation is a set of data defining deltas from the base 
	position of a hierarchy tree.  Translation and Rotation channels can be
	attached to any node of the hierarchy tree which the animation is 
	associated with.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_ANIMATION_HEADER
* W3D_CHUNK_ANIMATION_CHANNEL
* W3D_CHUNK_BIT_CHANNEL


W3D_CHUNK_ANIMATION_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~

Animation header contains general info about the hierarchy

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      16      CHAR[16]       HierarchyName
36      4       UINT32         NumFrames
40      4       UINT32         FrameRate
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.
* **HierarchyName**: 16 Byte field for the name of the Skeleton.
* **NumFrames**: Number of frames in the animation.
* **FrameRate**: Frame Rate of the animation.

W3D_CHUNK_ANIMATION_CHANNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Channel of vectors. 

There will be one Channel Type for each type of animation per frame.


======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       2       UINT16         FirstFrame
2       2       UINT16         LastFrame
4       2       UINT16         VectorLen
6       2       UINT16         Flags
8       2       UINT16         Pivot
10      2       UINT16         Padding
12      4 * N   FLOAT32        Data
======  ======  =============  ====================

``N`` = (LastFrame - FirstFrame + 1) * VectorLen

* **FirstFrame**: Starting Frame.
* **LastFrame**: Last Frame.
* **VectorLen**: length of each vector in this channel.
* **Flags**: `W3D_ANIMATION_CHANNEL_FLAGS`_ values.
* **Pivot**: Pivot affected by this channel.
* **Padding**: Evens out the data structure.
* **Data**: The data for the transform or rotation.


W3D_CHUNK_BIT_CHANNEL
~~~~~~~~~~~~~~~~~~~~~

Channel of boolean values (e.g. visibility).

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       2       UINT16         FirstFrame
2       2       UINT16         LastFrame
4       2       UINT16         Flags
6       2       UINT16         Pivot
8       1       UINT8          DefaultVal
9       1 * N   UINT8[N]       Data
======  ======  =============  ====================

``N`` = (LastFrame - FirstFrame + 1) / 8 

* **FirstFrame**: Starting Frame.
* **LastFrame**: Last Frame.
* **Flags**:  Either 0 = Visibility or 1 = Timecoded Visibility
* **Pivot**: Pivot affected by this channel.
* **DefaultVal**: Default state when outside valid range.
* **Data**: Visibility Booleon.

W3D_CHUNK_COMPRESSED_ANIMATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compressed hierarchy animation data.

======  =====  =======  ===========
Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_COMPRESSED_ANIMATION_HEADER
* W3D_CHUNK_COMPRESSED_ANIMATION_CHANNEL
* W3D_CHUNK_COMPRESSED_BIT_CHANNEL
* W3D_CHUNK_COMPRESSED_ANIMATION_MOTION_CHANNEL

W3D_CHUNK_COMPRESSED_ANIMATION_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Describes playback rate, number of frames, and type of compression.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      16      CHAR[16]       HierarchyName
36      4       UINT32         NumFrames
40      2       UINT16         FrameRate
42      2       UINT16         Flavor
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.
* **HierarchyName**: 16 Byte field for the name of the Skeleton.
* **NumFrames**: Number of frames in the animation.
* **FrameRate**: Frame Rate of the animation.
* **Flavor**:   0 = ANIM_FLAVOR_TIMECODED or 1 = ANIM_FLAVOR_ADAPTIVE_DELTA
                

W3D_CHUNK_COMPRESSED_ANIMATION_CHANNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compressed channel, format dependent on type of compression.

A time code is a uint32 that prefixes each vector
the MSB is used to indicate a binary (non interpolated) movement

**Time Coded**

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         NumTimeCodes
4       2       UINT16         Pivot
6       1       UINT8          VectorLen
7       1       UINT8          Flags
8       2 * N   UINT32[N]      Data
======  ======  =============  ====================

``N`` = (NumTimeCodes * ((VectorLen * sizeof(uint32)) + sizeof(uint32)))

* **NumTimeCodes**: Number of time coded entries.
* **Pivot**: Pivot affected by this channel.
* **VectorLen**: length of each vector in this channel.
* **Flags**: `W3D_ANIMATION_CHANNEL_FLAGS`_ values.
* **Data**: The data for the transform or rotation.

**Adaptive Delta**

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         NumFrames
4       2       UINT16         Pivot
6       1       UINT8          VectorLen
7       2       UINT8          Flags
8       4       FLOAT32        Scale
12      4 * N   UINT32[N]      Data
======  ======  =============  ====================

* **NumFrames**: Number of frames in the animation.
* **Pivot**: Pivot affected by this channel.
* **VectorLen**: Number of Channels.
* **Flags**: `W3D_ANIMATION_CHANNEL_FLAGS`_ values.
* **Scale**: Filter Table Scale.
* **Data**: OpCode Data Stream.

W3D_CHUNK_COMPRESSED_BIT_CHANNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compressed bit stream channel, format dependent on type of compression.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       2       UINT32         NumTimeCodes
2       2       UINT16         Pivot
4       2       UINT8          Flags
6       1       UINT8          DefaultVal
7       1 * N   UINT8[N]       Data
======  ======  =============  ====================

``N`` = (NumTimeCodes * sizeof(uint32))

* **NumTimeCodes**: Number of time coded entries.
* **Pivot**: Pivot affected by this channel.
* **Flags**:  Either 0 = Visibility or 1 = Timecoded Visibility
* **DefaultVal**: Default state when outside valid range.
* **Data**: Visibility Booleon.

W3D_CHUNK_COMPRESSED_ANIMATION_MOTION_CHANNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added in BFME II.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       1       UINT8          Zero
1       1       UINT8          Flavor
2       1       UINT8          VectorLen
3       1       UINT8          Flags
4       2       UINT16         NumTimeCodes
6       2       UINT16         Pivot
======  ======  =============  ====================

* **Zero**: 
* **Flavor**: 0 = TIMECODED, 1 = Adaptive Delta 4, 2 = Adaptive Delta 8 
* **VectorLen**: 
* **Flags**: `W3D_ANIMATION_CHANNEL_FLAGS`_ values.
* **NumTimeCodes**: 
* **Pivot**: 

W3D_ANIMATION_CHANNEL_FLAGS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0           X                           X Translation (scalar)
1           Y                           Y Translation (scalar)
2           Z                           Z Translation (scalar)
3           RX                          X Rotation (scalar)
4           RY                          Y Rotation (scalar)
5           RZ                          Z Rotation (scalar)
6           Q                           Quaternion (4 floats per frame)
7           TimeCoded X                 X Translation (scalar)
8           TimeCoded Y                 Y Translation (scalar)
9           TimeCoded Z                 Z Translation (scalar)
10          TimeCoded Q                 Quaternion (4 floats per frame)
==========  ==========================  ==============

W3D_CHUNK_MORPH_ANIMATION
~~~~~~~~~~~~~~~~~~~~~~~~~

Hierarchy morphing animation data (morphs between poses, for facial animation)

	This is an animation format which describes morphs between poses in another
	animation.  It is used for Renegade's facial animation system.  There is
	a normal anim which defines the pose for each phoneme and then a "Morph Anim"
	which defines the transitions between phonemes over time.  In addition there
	is the concept of multiple morph channels in a morph anim.  Each "channel"
	controls a set of pivots in the skeleton and has its own set of morph keys
	and poses.  This lets us have one set of poses for expressions and another
	for phonemes (a bone is only moved in one or the other anims though)



Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_MORPHANIM_HEADER
* W3D_CHUNK_MORPHANIM_CHANNEL
* W3D_CHUNK_MORPHANIM_PIVOTCHANNELDATA


W3D_CHUNK_MORPHANIM_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~

W3dMorphAnimHeaderStruct describes playback rate, number of frames, and type of compression.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      16      CHAR[16]       HierarchyName
36      4       UINT32         FrameCount
40      4       FLOAT32        FrameRate
44      4       UINT32         ChannelCount
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **Name**: 16 Byte field for the name of the file.
* **HierarchyName**: 16 Byte field for the name of the Skeleton.
* **FrameCount**: The number of frames in the animation.
* **FrameRate**: Frame rate of the animation.
* **ChannelCount**: The number of channels. 

W3D_CHUNK_MORPHANIM_CHANNEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wrapper for a channel

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_MORPHANIM_POSENAME
* W3D_CHUNK_MORPHANIM_KEYDATA

W3D_CHUNK_MORPHANIM_POSENAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Name of the other anim which contains the poses for this morph channel (String)

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        PoseName
======  =========  =============  ====================

* **PoseName**: Name of the other anim which contains the poses for this morph channel.

W3D_CHUNK_MORPHANIM_KEYDATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Morph key data for this channel

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         MorphFrame
4       4       UINT32         PoseFrame
======  ======  =============  ====================

* **MorphFrame**: 
* **PoseFrame**: 

W3D_CHUNK_MORPHANIM_PIVOTCHANNELDATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

uin32 per pivot in the htree,  indicating which channel controls the pivot

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4 * N     UINT32[N]    Pivot
======  ======  =============  ====================

``N`` = The number of pivots in the htree

* **Pivot**: 


W3D_CHUNK_HMODEL
~~~~~~~~~~~~~~~~
	HModel - Hiearchical Model

Blueprint for a hierarchy model

	A Hierarchy Model is a set of render objects which should be attached to 
	bones in a hierarchy tree.  There can be multiple objects per node
	in the tree.  Or there may be no objects attached to a particular bone.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HMODEL_HEADER
* W3D_CHUNK_NODE
* W3D_CHUNK_COLLISION_NODE
* W3D_CHUNK_SKIN_NODE
* OBSOLETE_W3D_CHUNK_HMODEL_AUX_DATA
* OBSOLETE_W3D_CHUNK_SHADOW_NODE

W3D_CHUNK_HMODEL_HEADER
~~~~~~~~~~~~~~~~~~~~~~~

Header for the hierarchy model

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      16      CHAR[16]       HierarchyName
36      2       UINT16         NumConnections
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.
* **HierarchyName**: 16 Byte field for the name of the hierarchy tree this model uses
* **NumConnections**: Number of connected nodes


W3D_CHUNK_NODE
~~~~~~~~~~~~~~

Render objects connected to the hierarchy

For the number of render objects connected to the hierarchy

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       16      CHAR[16]       RenderObjname
16      2       UINT16         PivotIDx
======  ======  =============  ====================



* **RenderObjname**: 16 Byte field for the name of the RenderObjname
* **PivotIDx**: Pivot ID of the Node


W3D_CHUNK_COLLISION_NODE
~~~~~~~~~~~~~~~~~~~~~~~~

Collision meshes connected to the hierarchy

For the the number of collision meshes connected to the hierarchy

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       16      CHAR[16]       CollisionMeshName
16      2       UINT16         PivotIDx
======  ======  =============  ====================

* **CollisionMeshName**: 16 Byte field for the name of the CollisionMeshName
* **PivotIDx**: Pivot ID of the Node

W3D_CHUNK_SKIN_NODE
~~~~~~~~~~~~~~~~~~~

Skins connected to the hierarchy

For the number of skins connected to the hierarchy

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       16      CHAR[16]       SkinMeshName
16      2       UINT16         PivotIDx
======  ======  =============  ====================

* **SkinMeshName**: 16 Byte field for the name of the SkinMeshName
* **PivotIDx**: Pivot ID of the Node


W3D_CHUNK_LODMODEL
~~~~~~~~~~~~~~~~~~
Blueprint for an LOD model.  This is simply a collection of 'n' render objects,  
ordered in terms of their expected rendering costs. (highest is first)

	(LODModel - Level-Of-Detail Model)

	An LOD Model is a set of render objects which are interchangeable and
	designed to be different resolution versions of the same object.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_LODMODEL_HEADER
* W3D_CHUNK_LOD


W3D_CHUNK_LODMODEL_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~

Header for the LOD model

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      2       UINT16         NumLODs
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the LOD model
* **NumLODs**: Number of LOD's

W3D_CHUNK_LOD
~~~~~~~~~~~~~

LOD Data

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       32      CHAR[32]       RenderObjname
32      4       FLOAT32        LODMin
36      4       FLOAT32        LODMax
======  ======  =============  ====================

* **RenderObjname**: 32 Byte field for Render Object. 
* **LODMin**: Minimum screen size before switching lod
* **LODMax**: Maximum screen size before switching lod

W3D_CHUNK_COLLECTION
~~~~~~~~~~~~~~~~~~~~

Collection of render object names

	Collection

	A collection chunk is generated when the user exports a bunch of meshes.
	The collection will be named with the root name of the w3d file and will
	contain a string chunk for the name of each render object in the collection.
	A collection may also contain a "Snap Points" chunk.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_COLLECTION_HEADER
* W3D_CHUNK_COLLECTION_OBJ_NAME
* W3D_CHUNK_PLACEHOLDER
* W3D_CHUNK_TRANSFORM_NODE

W3D_CHUNK_COLLECTION_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
20      4       UINT32         RenderObjectCount
24      8       UINT32[2]      Padding
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.
* **RenderObjectCount**: Number of Child Render Objects.
* **Padding**: Evens out the data structure.

W3D_CHUNK_COLLECTION_OBJ_NAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Contains a string which is the name of a render object

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        RenderObjectName
======  =========  =============  ====================

* **RenderObjectName**: Name of the other anim which contains the poses for this morph channel.

W3D_CHUNK_PLACEHOLDER
~~~~~~~~~~~~~~~~~~~~~

Contains information about a 'dummy' object that will be instanced later

Placeholder chunks.  Also known as "PROXIES".  These are used by the Renegade
level editor to instruct the editor to instance a particular named object

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       48      FLOAT32[4][3]  Transform
52      4       UINT32         NameLength
56      N       CHAR[N]        Name
======  ======  =============  ====================

``N`` = NameLength

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Transform**: this is a direct dump of a MAX 3x4 matrix.
* **NameLength**: Length of the name.
* **Name**: specifies the name of the placeholder object in Commando-level editor.

W3D_CHUNK_TRANSFORM_NODE
~~~~~~~~~~~~~~~~~~~~~~~~

Contains the filename of another w3d file that should be transformed by this node

Transform chunks.  These chunks refer to other W3D files which should be transformed by
this file.  This feature is used to allow user to (for example) lightmap the interior
of a building once and then just transform that into all of our levels that use it.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       48      FLOAT32[4][3]  Transform
52      4       UINT32         NameLength
56      N       CHAR[N]        Name
======  ======  =============  ====================

``N`` = NameLength
* **Version**: W3D Format `W3D_VERSION`_ . 
* **Transform**: this is a direct dump of a MAX 3x4 matrix
* **NameLength**: Length of the name.
* **Name**: specifies the name of the file to apply the transform to.



W3D_CHUNK_POINTS
~~~~~~~~~~~~~~~~

May appear in meshes, hmodels, lodmodels, or collections.

  This is used to implement "snap points"
	for the level editor.  It is just an array of points that were found in
	the max scene (helper object->point).  We make these points co-incide in
	the level editor to snap objects together.  This chunk can occur inside a 
	mesh, hmodel, or collection chunk.  When it does, the points should simply 
	be associated with the model being defined.

======  ======  ==============  ====================
Offset  Bytes   Type            Name
======  ======  ==============  ====================
0       12      `W3D_VECTOR3`_  Point
======  ======  ==============  ====================


* **Point**: 3dxMax Helper Object (Point)

W3D_CHUNK_LIGHT
~~~~~~~~~~~~~~~

Description of a light

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_LIGHT_INFO
* W3D_CHUNK_SPOT_LIGHT_INFO
* W3D_CHUNK_NEAR_ATTENUATION
* W3D_CHUNK_FAR_ATTENUATION
* W3D_CHUNK_LIGHT_TRANSFORM
* W3D_CHUNK_SPOT_LIGHT_INFO_5_0
* W3D_CHUNK_PULSE


W3D_CHUNK_LIGHT_INFO
~~~~~~~~~~~~~~~~~~~~

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         LightFlags
4       4       UINT32         Unused
8       4       `W3D_RGB`_      Ambient
12      4       `W3D_RGB`_      Diffuse
16      4       `W3D_RGB`_      Specular
20      4       FLOAT32        Intensity
======  ======  =============  ====================

* **LightFlags**: bitwise-or'd collection of `W3D_LIGHT_FLAGS`_ values.
* **Ambient**: Ambient RGB Colors.
* **Diffuse**: Diffuse RGB Colors.
* **Specular**: Specular RGB Colors.
* **Intensity**: 


W3D_LIGHT_FLAGS
~~~~~~~~~~~~~~~

==========  ================================  ==============
Value       Name                              Description
==========  ================================  ==============
0xFF        W3D_LIGHT_ATTRIBUTE_TYPE_MASK                   
0x1         W3D_LIGHT_ATTRIBUTE_POINT                     
0x2         W3D_LIGHT_ATTRIBUTE_DIRECTIONAL                 
0x3         W3D_LIGHT_ATTRIBUTE_SPOT                   
0x100       W3D_LIGHT_ATTRIBUTE_CAST_SHADOWS                     
==========  ================================  ==============

W3D_CHUNK_SPOT_LIGHT_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~

Extra spot light parameters

======  ======  ==============  ====================
Offset  Bytes   Type            Name
======  ======  ==============  ====================
0       12      `W3D_VECTOR3`_  SpotDirection
12      4       FLOAT32         SpotAngle
16      4       FLOAT32         SpotExponent
======  ======  ==============  ====================

* **SpotDirection**: 
* **SpotAngle**: 
* **SpotExponent**: 


W3D_CHUNK_NEAR_ATTENUATION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional near attenuation parameters

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        Start
4       4       FLOAT32        End
======  ======  =============  ====================

* **Start**: 
* **End**: 


W3D_CHUNK_FAR_ATTENUATION
~~~~~~~~~~~~~~~~~~~~~~~~~~

Optional far attenuation parameters

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        Start
4       4       FLOAT32        End
======  ======  =============  ====================

* **Start**: 
* **End**: 

W3D_CHUNK_SPOT_LIGHT_INFO_5_0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TT: extra spot light parameters (new in 5.0)

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        SpotOuterAngle
4       4       FLOAT32        SpotInnerAngle
======  ======  =============  ====================

* **SpotOuterAngle**: 
* **SpotInnerAngle**: 

W3D_CHUNK_PULSE
~~~~~~~~~~~~~~~

TT: pulse data (5.0)

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        MinIntensity
4       4       FLOAT32        MaxIntensity
8       4       FLOAT32        IntensityTime
12      4       FLOAT32        IntensityTimeRandom
16      4       FLOAT32        IntensityAdjust
20      1       CHAR[1]        IntensityStopsAtMax
21      1       CHAR[1]        IntensityStopsAtMin
======  ======  =============  ====================

* **MinIntensity**: 
* **MaxIntensity**: 
* **IntensityTime**: 
* **IntensityTimeRandom**: 
* **IntensityAdjust**: 
* **IntensityStopsAtMax**: 
* **IntensityStopsAtMin**: 

W3D_CHUNK_EMITTER
~~~~~~~~~~~~~~~~~

Description of a particle emitter.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_EMITTER_HEADER
* W3D_CHUNK_EMITTER_USER_DATA
* W3D_CHUNK_EMITTER_INFO
* W3D_CHUNK_EMITTER_INFOV2
* W3D_CHUNK_EMITTER_PROPS
* OBSOLETE_W3D_CHUNK_EMITTER_COLOR_KEYFRAME
* OBSOLETE_W3D_CHUNK_EMITTER_OPACITY_KEYFRAME
* OBSOLETE_W3D_CHUNK_EMITTER_SIZE_KEYFRAME
* W3D_CHUNK_EMITTER_LINE_PROPERTIES
* W3D_CHUNK_EMITTER_ROTATION_KEYFRAMES
* W3D_CHUNK_EMITTER_FRAME_KEYFRAMES
* W3D_CHUNK_EMITTER_BLUR_TIME_KEYFRAMES
* W3D_CHUNK_PULSE
* W3D_CHUNK_EMITTER_EXTRA_INFO


W3D_CHUNK_EMITTER_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~

General information such as name and version.

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       UINT32         Version
4       16      CHAR[16]       Name
======  ======  =============  ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.

W3D_CHUNK_EMITTER_USER_DATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~

User-defined data that specific loaders can switch on. (STRING)

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        User Data
======  =========  =============  ====================

* **User Data**: User-defined data

W3D_CHUNK_EMITTER_INFO
~~~~~~~~~~~~~~~~~~~~~~

Generic particle emitter definition.

======  ======  ==============  ====================
Offset  Bytes   Type            Name
======  ======  ==============  ====================
0       260     CHAR[260]       TextureFilename
260     4       FLOAT32         StartSize
264     4       FLOAT32         EndSize
268     4       FLOAT32         Lifetime
272     4       FLOAT32         EmissionRate
276     4       FLOAT32         MaxEmissions
280     4       FLOAT32         VelocityRandom
284     4       FLOAT32         PositionRandom
288     4       FLOAT32         FadeTime
292     4       FLOAT32         Gravity
296     4       FLOAT32         Elasticity
308     12      `W3D_VECTOR3`_  Velocity
320     12      `W3D_VECTOR3`_  Acceleration
324     4       `W3D_RGB`_      StartColor
328     4       `W3D_RGB`_      EndColor
======  ======  ==============  ====================

* **TextureFilename**:
* **StartSize**:
* **EndSize**:
* **Lifetime**:
* **EmissionRate**:
* **MaxEmissions**:
* **VelocityRandom**:
* **PositionRandom**:
* **FadeTime**:
* **Gravity**:
* **Elasticity**:
* **Velocity**:
* **Acceleration**:
* **StartColor**:
* **EndColor**:

W3D_CHUNK_EMITTER_INFOV2
~~~~~~~~~~~~~~~~~~~~~~~~

General particle emitter definition (version 2.0).

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            BurstSize
4       32      W3D_VOLUME_RNG    CreationVolume
36      32      W3D_VOLUME_RNG    VelRandom
68      4       FLOAT32           OutwardVel
72      4       FLOAT32           VelInherit
72      16      W3D_SHADER        Shader
72      4       UINT32            RenderMode
72      4       UINT32            FrameMode
72      24      UINT32[6]         Reserved
======  ======  ===============   ====================       

* **BurstSize**:
* **CreationVolume**:
* **VelRandom**:
* **OutwardVel**:
* **VelInherit**:
* **Shader**: 
* **RenderMode**:
* **FrameMode**:
* **FadeTime**:
* **Reserved**:



W3D_CHUNK_EMITTER_PROPS
~~~~~~~~~~~~~~~~~~~~~~~

Key-frameable properties.

Contains a W3dEmitterPropertyStruct followed by a number of color keyframes, 
opacity keyframes, and size keyframes

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            ColorKeyframes
4       4       UINT32            OpacityKeyframes
12      4       UINT32            SizeKeyframes
16      4       `W3D_RGBA`_        ColorRandom
20      4       FLOAT32           OpacityRandom
24      4       FLOAT32           SizeRandom
28      16      UINT32[4]         Reserved
======  ======  ===============   ====================

* **ColorKeyframes**:
* **OpacityKeyframes**:
* **SizeKeyframes**:
* **ColorRandom**:
* **OpacityRandom**:
* **SizeRandom**:
* **Reserved**:

W3D_CHUNK_EMITTER_LINE_PROPERTIES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Line properties, used by line rendering mode.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            EmitterLineFlags
4       4       UINT32            SubdivisionLevel
8       4       FLOAT32           NoiseAmplitude
12      4       FLOAT32           MergeAbortFactor
16      4       FLOAT32           TextureTileFactor
20      4       FLOAT32           UPerSec
24      4       FLOAT32           VPerSec
28      36      UINT32            Reserved
======  ======  ===============   ====================

* **EmitterLineFlags**: bitwise-or'd collection of `W3D_EMITTER_LINE_FLAGS`_ values.
* **SubdivisionLevel**:
* **NoiseAmplitude**:
* **MergeAbortFactor**:
* **TextureTileFactor**:
* **UPerSec**:
* **VPerSec**:
* **Reserved**:

W3D_EMITTER_LINE_FLAGS
~~~~~~~~~~~~~~~~~~~~~~~

==========  ====================================    ==============
Value       Name                                      Description
==========  ====================================    ==============
0x1         W3D_ELINE_MERGE_INTERSECTIONS           Merge intersections     
0x2         W3D_ELINE_FREEZE_RANDOM                 Freeze random (note: offsets are in camera space)       
0x4         W3D_ELINE_DISABLE_SORTING               Disable sorting (even if shader has alpha-blending)      
0x8         W3D_ELINE_END_CAPS                      Draw end caps on the line
0xFF000000  W3D_ELINE_TEXTURE_MAP_MODE_MASK         Draw end caps on the line
24          W3D_ELINE_TEXTURE_MAP_MODE_OFFSET       By how many bits do I need to shift the texture mapping mode?
0x0         W3D_ELINE_UNIFORM_WIDTH_TEXTURE_MAP     Entire line uses one row of texture (constant V)
0x1         W3D_ELINE_UNIFORM_LENGTH_TEXTURE_MAP    Entire line uses one row of texture stretched length-wise  
0x2         W3D_ELINE_TILED_TEXTURE_MAP             Tiled continuously over line                 
==========  ====================================    ==============

W3D_ELINE_DEFAULT_BITS =	(W3D_ELINE_MERGE_INTERSECTIONS | (W3D_ELINE_UNIFORM_WIDTH_TEXTURE_MAP << W3D_ELINE_TEXTURE_MAP_MODE_OFFSET))

W3D_CHUNK_EMITTER_ROTATION_KEYFRAMES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rotation keys for the particles.

Contains a W3dEmitterRotationHeaderStruct followed by a number of
rotational velocity keyframes.  

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            KeyframeCount
4       4       FLOAT32           Random
8       4       FLOAT32           OrientationRandom
12      4       UINT32            Reserved     
======  ======  ===============   ====================

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
16       4      FLOAT32           Time
20       4      FLOAT32           Rotation
======  ======  ===============   ====================

* **KeyframeCount**:
* **Random**:
* **OrientationRandom**:
* **Reserved**:    
* **Time**:
* **Rotation**:


W3D_CHUNK_EMITTER_FRAME_KEYFRAMES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Frame keys (u-v based frame animation).
Contains a W3dEmitterFrameHeaderStruct followed by a number of
frame keyframes (sub-texture indexing)

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            KeyframeCount
4       4       FLOAT32           Random
8       8       UINT32[2]         Reserved   
======  ======  ===============   ====================

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
16       4      FLOAT32           Time
20       4      FLOAT32           Frame
======  ======  ===============   ====================

* **KeyframeCount**:
* **Random**:
* **Reserved**:    
* **Time**:
* **Frame**:

W3D_CHUNK_EMITTER_BLUR_TIME_KEYFRAMES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Length of tail for line groups.
Contains a W3dEmitterFrameHeaderStruct followed by a number of
frame keyframes (sub-texture indexing)

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            KeyframeCount
4       4       FLOAT32           Random
8       4       UINT32            Reserved   
======  ======  ===============   ====================

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
12       4      FLOAT32           Time
16       4      FLOAT32           BlurTime
======  ======  ===============   ====================


* **KeyframeCount**:
* **Random**:
* **Reserved**:    
* **Time**:
* **BlurTime**:

W3D_CHUNK_EMITTER_EXTRA_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Defined in Generals code also in Earth & Beyond

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       FLOAT32           FutureStartTime
4       36      UINT32            Padding[9]
======  ======  ===============   ====================

* **FutureStartTime**:
* **Padding**: Evens out the data structure.

W3D_CHUNK_AGGREGATE
~~~~~~~~~~~~~~~~~~~

Description of an aggregate object.


Aggregate objects

The following structs are used to define aggregates in the w3d file.  An
'aggregate' is simply a 'shell' that contains references to a hierarchy
model and subobjects to attach to its bones.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_AGGREGATE_HEADER
* W3D_CHUNK_AGGREGATE_INFO
* W3D_CHUNK_TEXTURE_REPLACER_INFO
* W3D_CHUNK_AGGREGATE_CLASS_INFO


W3D_CHUNK_AGGREGATE_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~

General information such as name and version.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       16      CHAR[16]          Name
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **Name**: 16 Byte field for the name of the file.

W3D_CHUNK_AGGREGATE_INFO
~~~~~~~~~~~~~~~~~~~~~~~~

References to 'contained' models

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       32      CHAR[16]          BaseModelName
32      4       UINT32            SubobjectCount
======  ======  ===============   ====================

For Each SubobjectCount:
======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
36      32      CHAR[32]          SubobjectName
68      32      CHAR[32]          BoneName
======  ======  ===============   ====================

* **BaseModelName**: 32 byte field of the BaseModelName. 
* **SubobjectCount**: Number of sub objects.
* **SubobjectName**: 32 byte field of the sub object name.
* **BoneName**: 32 byte field of the bone name.

W3D_CHUNK_TEXTURE_REPLACER_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Information about which meshes need textures replaced

======  ======  =========================   ====================
Offset  Bytes   Type                        Name
======  ======  =========================   ====================
0       4       UINT32                      ReplacedTextureCount
======  ======  =========================   ====================

======  ======  =========================   ====================
Offset  Bytes   Type                        Name
======  ======  =========================   ====================
X       32      CHAR[32]                    MeshPath[0]
X       32      CHAR[32]                    MeshPath[14]
X       32      CHAR[32]                    BonePath[0]
X       32      CHAR[32]                    BonePath[14]
X       260     CHAR[260]                   OldTextureName
X       260     CHAR[260]                   NewTextureName
X       12      `W3D_CHUNK_TEXTURE_INFO`_   TextureParams
======  ======  =========================   ====================

* **ReplacedTextureCount**: 
* **MeshPath**: 
* **BonePath**: 
* **OldTextureName**: 
* **NewTextureName**:
* **TextureParams**:

W3D_CHUNK_AGGREGATE_CLASS_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Information about the original class that created this aggregate.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            OriginalClassID
4       8       UINT32            Flags
8       12      UINT32[3]         Reserved
======  ======  ===============   ====================

* **OriginalClassID**: 
* **Flags**: 0x1 = W3D_AGGREGATE_FORCE_SUB_OBJ_LOD is the only flag.
* **Reserved**:

W3D_CHUNK_HLOD
~~~~~~~~~~~~~~

Description of an HLOD object.

	HLod (Hierarchical LOD Model)

	This is a hierarchical model which has multiple arrays of models which can
	be switched for LOD purposes.
	An HLOD is the basic hierarchical model format used by W3D.  It references
	an HTree for its hierarchical structure and animation data and several arrays
	of sub-objects; one for each LOD in the model.  In addition, it can contain
	an array of "aggregates" which are references to external W3D objects to
	be automatically attached into it.  And it can have a list of "proxy" objects
	which can be used for application purposes such as instantiating game objects
	at the specified transform. 

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HLOD_HEADER
* W3D_CHUNK_HLOD_LOD_ARRAY
* W3D_CHUNK_HLOD_AGGREGATE_ARRAY
* W3D_CHUNK_HLOD_PROXY_ARRAY
* W3D_CHUNK_HLOD_LIGHT_ARRAY

W3D_CHUNK_HLOD_HEADER
~~~~~~~~~~~~~~~~~~~~~

General information such as name and version.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       4       UINT32            LodCount
8       16      CHAR[16]          Name
24      16      CHAR[16]          HierarchyName
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **LodCount**: 
* **Name**: 16 Byte field for the name of the file.
* **HierarchyName**: 16 Byte field for the name of the Hierarchy Tree.


W3D_CHUNK_HLOD_LOD_ARRAY
~~~~~~~~~~~~~~~~~~~~~~~~

Wrapper around the array of objects for each level of detail.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER
* W3D_CHUNK_HLOD_SUB_OBJECT


W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Info on the objects in this level of detail array.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            ModelCount
4       4       FLOAT32           MaxScreenSize
======  ======  ===============   ====================

* **ModelCount**:  Number of models
* **MaxScreenSize**: If model is bigger than this, switch to higher lod.

W3D_CHUNK_HLOD_SUB_OBJECT
~~~~~~~~~~~~~~~~~~~~~~~~~

An object in this level of detail array.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            BoneIndex
4       32      CHAR[32]          Name
======  ======  ===============   ====================

* **BoneIndex**:  Index ID of Bone 
* **Name**: 32 Byte name of sub object "Filename"."Meshname"


W3D_CHUNK_HLOD_AGGREGATE_ARRAY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER
* W3D_CHUNK_HLOD_SUB_OBJECT

W3D_CHUNK_HLOD_PROXY_ARRAY
~~~~~~~~~~~~~~~~~~~~~~~~~~

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER
* W3D_CHUNK_HLOD_SUB_OBJECT

W3D_CHUNK_HLOD_LIGHT_ARRAY
~~~~~~~~~~~~~~~~~~~~~~~~~~

TT: array of lights, used for application-defined purposes, provides a name and a bone. (5.0)

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_HLOD_SUB_OBJECT_ARRAY_HEADER
* W3D_CHUNK_HLOD_SUB_OBJECT


W3D_CHUNK_BOX
~~~~~~~~~~~~~

Defines an collision box render object.

	Collision Boxes

	Collision boxes are meant to be used for, you guessed it, collision detection.
	For this reason, they only contain a minimal amount of rendering information
	(a color).  

	Axis Aligned - This is a bounding box which is *always* aligned with the world 
	coordinate system.  So, the center point is to be transformed by whatever
	transformation matrix is being used but the extents always point down the
	world space x,y, and z axes.  (in effect, you are translating the center).

	Oriented - This is an oriented 3D box.  It is aligned with the coordinate system
	it is in.  So its extents always point along the local coordinate system axes.

  
======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       4       UINT32            BoxFlags
8       32      CHAR[32]          Name
40      4       `W3D_RGB`_         Color
44      12      `W3D_VECTOR3`_     Center
56      12      `W3D_VECTOR3`_     Extent
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **BoxFlags**: bitwise-or'd collection of `W3D_BOX_FLAGS`_ values.
* **Name**: Name is in the form containername.boxname
* **Color**: color to use when drawing the box
* **Center**: center of the box
* **Extent**: extent of the box


W3D_BOX_FLAGS
~~~~~~~~~~~~~~

==========  ============================================  ===========================================
Value       Name                                          Description
==========  ============================================  ===========================================
0x1         W3D_BOX_ATTRIBUTE_ORIENTED                    WorldBox                         
0x2         W3D_BOX_ATTRIBUTE_ALIGNED                     Bounding Box                
0xFF0       W3D_BOX_ATTRIBUTE_COLLISION_TYPE_MASK         Mask for the collision type bits                
4           W3D_BOX_ATTRIBUTE_COLLISION_TYPE_SHIFT        Shifting to get to the collision type bits                 
0x10        W3D_BOX_ATTRIBTUE_COLLISION_TYPE_PHYSICAL     Physical collisions                   
0x20        W3D_BOX_ATTRIBTUE_COLLISION_TYPE_PROJECTILE   Projectiles (rays) collide with this
0x40        W3D_BOX_ATTRIBTUE_COLLISION_TYPE_VIS          Vis rays collide with this mesh
0x80        W3D_BOX_ATTRIBTUE_COLLISION_TYPE_CAMERA       Cameras collide with this mesh   
0x100       W3D_BOX_ATTRIBTUE_COLLISION_TYPE_VEHICLE      Vehicles collide with this mesh
==========  ============================================  ===========================================

W3D_CHUNK_SPHERE
~~~~~~~~~~~~~~~~~

Primative Sphere

These are created in W3dviewer to make visual effects. 
They use Microchunk formating which makes the structure different from standard chunks.

The Header information will be nested into a SubChunk "CHUNKID_SPHERE_DEF" Which is displayed as 0x1
While the Color, Alpha, Scale, and Vector will each have it's own subchunk as well:

These will overlap with standard chunk ID's so care must be made to read these correctly.

==========  ==========================  ==========================
Value       Name                        Description
==========  ==========================  ==========================
0x1         CHUNKID_SPHERE_DEF          Contains Header Information
0x2         CHUNKID_COLOR_CHANNEL       Wrapper for CHUNKID_VARIABLES
0x3         CHUNKID_ALPHA_CHANNEL       Wrapper for CHUNKID_VARIABLES
0x4         CHUNKID_SCALE_CHANNEL       Wrapper for CHUNKID_VARIABLES
0x5         CHUNKID_VECTOR_CHANNEL      Wrapper for CHUNKID_VARIABLES
==========  ==========================  ==========================

Each of the Channels will wrap another subchunk:

CHUNKID_VARIABLES = 0x3150809

Which will then contain the Micochunks.

**CHUNKID_SPHERE_DEF**

======  ======  ====================     ====================
Offset  Bytes   Type                      Name
======  ======  ====================     ====================
0       4       UINT32                    Version
4       4       UINT32                    SphereFlags
8       32      CHAR[32]                  Name
40      12      `W3D_VECTOR3`_            Center
52      12      `W3D_VECTOR3`_            Extent
64      4       FLOAT32                   AnimDuration
68      12      `W3D_VECTOR3`_            DefaultColor
72      4       FLOAT32                   DefaultAlpha
84      12      `W3D_VECTOR3`_            DefaultScale
96      20      `W3D_ALPHA_VECTOR`_       DefaultVector
116     32      CHAR[32]                  TextureName
148     16      `W3D_SHADER`_             Shader
======  ======  ====================     ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **SphereFlags**: bitwise-or'd collection of `W3D_SPHERE_FLAGS`_ values.
* **Name**: 32 Byte Field for the name of the file.
* **Center**: 
* **Extent**: 
* **AnimDuration**: 
* **DefaultColor**: 
* **DefaultAlpha**: 
* **DefaultScale**: 
* **DefaultVector**: 
* **TextureName**: 
* **Shader**: 


**CHUNKID_COLOR_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Value
12      4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_ALPHA_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       FLOAT32           Value
4       4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_SCALE_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Value
12      4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_VECTOR_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===================     ====================
Offset  Bytes   Type                      Name
======  ======  ===================     ====================
0       20      `W3D_ALPHA_VECTOR`_      Value
20      4       FLOAT32                   Time                      
======  ======  ===================     ====================


W3D_SPHERE_FLAGS
~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============
0x1         SPHERE_ALPHA_VECTOR         
0x2         SPHERE_CAMERA_ALIGNED                      
0x4         SPHERE_INVERT_EFFECT                    
0x8         SPHERE_LOOPING                      
==========  ==========================  ==============


W3D_CHUNK_RING
~~~~~~~~~~~~~~

Primative Ring

These are created in W3dviewer to make visual effects. 
They use Microchunk formating which makes the structure different from standard chunks.

The Header information will be nested into a SubChunk "CHUNKID_SPHERE_DEF" Which is displayed as 0x1
While the Color, Alpha, Inner Scale and Outer Scale will each have it's own subchunk as well:

These will overlap with standard chunk ID's so care must be made to read these correctly.

==========  ===========================    ==========================
Value       Name                            Description
==========  ===========================    ==========================
0x1         CHUNKID_RING_DEF                Contains Header Information
0x2         CHUNKID_COLOR_CHANNEL           Wrapper for CHUNKID_VARIABLES
0x3         CHUNKID_ALPHA_CHANNEL           Wrapper for CHUNKID_VARIABLES
0x4         CHUNKID_INNER_SCALE_CHANNEL     Wrapper for CHUNKID_VARIABLES
0x5         CHUNKID_OUTER_SCALE_CHANNEL     Wrapper for CHUNKID_VARIABLES
==========  ===========================    ==========================

Each of the Channels will wrap another subchunk:

CHUNKID_VARIABLES = 0x3150809

Which will then contain the Micochunks.

**CHUNKID_RING_DEF**

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       4       UINT32            RingFlags
8       32      CHAR[32]          Name
40      12      `W3D_VECTOR3`_     Center
52      12      `W3D_VECTOR3`_     Extent
64      4       FLOAT32           AnimDuration
68      12      `W3D_VECTOR3`_     DefaultColor
72      4       FLOAT32           DefaultAlpha
76      8       `W3D_VECTOR2`_     DefaultInnerScale
84      8       `W3D_VECTOR2`_     DefaultOuterSCale
92      8       `W3D_VECTOR2`_     InnerExtent
100     8       `W3D_VECTOR2`_     OuterExtent
108     32      CHAR[32]          TextureName
140     16      `W3D_SHADER`_     Shader
156     16      UINT16            TextureTileCount
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ . 
* **RingFlags**: bitwise-or'd collection of `W3D_RING_FLAGS`_ values.
* **Name**: 32 Byte Field for the name of the file.
* **Center**: 
* **Extent**: 
* **AnimDuration**: 
* **DefaultColor**: 
* **DefaultAlpha**: 
* **DefaultInnerScale**: 
* **DefaultOuterScale**: 
* **InnerExent**:
* **OuterExent**: 
* **TextureName**:
* **Shader**: 
* **TextureTileCount**:

**CHUNKID_COLOR_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_     Value
12      4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_ALPHA_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       FLOAT32           Value
4       4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_INNER_SCALE_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       8       `W3D_VECTOR2`_     Value
8       4       FLOAT32           Time                      
======  ======  ===============   ====================

**CHUNKID_OUTER_SCALE_CHANNEL**

CHUNKID_VARIABLES		= 0x03150809

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       8       `W3D_VECTOR2`_    Value
8       4       FLOAT32           Time                      
======  ======  ===============   ====================

W3D_RING_FLAGS
~~~~~~~~~~~~~~~~

==========  ==========================  ==============
Value       Name                        Description
==========  ==========================  ==============        
0x1         RING_CAMERA_ALIGNED                                         
0x2         RING_LOOPING                      
==========  ==========================  ==============


W3D_CHUNK_NULL_OBJECT
~~~~~~~~~~~~~~~~~~~~~

Defines a NULL object

	NULL Objects

	Null objects are used by the LOD system to make meshes dissappear at lower
	levels of detail.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       8       UINT32            Version
4       4       UINT32            Attributes   
8       8       UINT32[2]         Padding         
16      32      CHAR[32]          Name        
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **Attributes**:
* **Padding**: Evens out the data structure.
* **Name**: 32 Byte Field for the name of the file.

W3D_CHUNK_LIGHTSCAPE
~~~~~~~~~~~~~~~~~~~~

Wrapper for lights created with Lightscape.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_LIGHTSCAPE_LIGHT


W3D_CHUNK_LIGHTSCAPE_LIGHT
~~~~~~~~~~~~~~~~~~~~~~~~~~

Definition of a light created with Lightscape.

W3D_CHUNK_LIGHT_TRANSFORM
~~~~~~~~~~~~~~~~~~~~~~~~~

Position and orientation, defined as right-handed 4x3 matrix transform.

This chunk is found in the `W3D_CHUNK_LIGHT`_ wrapper as well.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       48      FLOAT32[3][4]     Transform
======  ======  ===============   ====================

* **Transform**:

W3D_CHUNK_DAZZLE
~~~~~~~~~~~~~~~~

	Dazzle Objects

	The only data needed to instantiate a dazzle object is the type-name of
	the dazzle to use.  The dazzle is always assumed to be at the pivot point
	of the bone it is attached to (you should enable Export_Transform) for 
	dazzles.  If the dazzle-type (from dazzle.ini) is directional, then the 
	coordinate-system of the bone will define the direction.

Wrapper for a glare object.  Creates halos and flare lines seen around a bright light source

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_DAZZLE_NAME
* W3D_CHUNK_DAZZLE_TYPENAME

W3D_CHUNK_DAZZLE_NAME
~~~~~~~~~~~~~~~~~~~~~

Mull-terminated string,  name of the dazzle

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        DazzleName
======  =========  =============  ====================

* **DazzleName**: Name of Dazzle


W3D_CHUNK_DAZZLE_TYPENAME
~~~~~~~~~~~~~~~~~~~~~~~~~

Null-terminated string,  type of dazzle (from dazzle.ini)

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        DazzleType
======  =========  =============  ====================

* **DazzleType**: Type of Dazzle

W3D_CHUNK_SOUNDROBJ
~~~~~~~~~~~~~~~~~~~

Sound render objects

These objects are used to trigger a sound effect in the world.  When the object
is shown, its associated sound is added to the world and played, when the object
is hidden, the associated sound is stopped and removed from the world.


Description of a sound render object

W3D_CHUNK_SOUNDROBJ_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~

General information such as name and version.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       16      CHAR[16]          Name
20      4       UINT32            SoundRobjFlags
24      32      UINT32[8]         Padding
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **Name**: 16 Byte Field for the name of the file.
* **SoundRobjFlags**: 
* **Padding**: Evens out the data structure.

W3D_CHUNK_SOUNDROBJ_DEFINITION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chunk containing the definition of the sound that is to play

They use Microchunk formating which makes the structure different from standard chunks.

The Sound Render Object Definition has an odd strucure where the first several varibles are nested
under a 0x100 CHUNKID_VARIABLES chunk while the last few are nested under a 0x100 CHUNKID_VARIABLES
chunk which is then nested into a CHUNKID_BASE_CLASS Chunk.

These will overlap with standard chunk ID's so care must be made to read these correctly.

==========  ==========================    ==========================
Value       Name                          Description
==========  ==========================    ==========================
0x100         CHUNKID_VARIABLES           Wrapper for VARIABLES
0x200         CHUNKID_BASE_CLASS          Wrapper for CHUNKID_VARIABLES
==========  ==========================    ==========================

**CHUNKID_VARIABLES**

MicroChunks
The number of these is variable.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       FLOAT32           m_Priority
4       4       FLOAT32           m_Volume
8       4       FLOAT32           m_Pan
12      4       UINT32            m_loopCount
16      4       FLOAT32           m_DropoffRadius
20      4       FLOAT32           m_MaxVoLRadius
24      4       UINT32            m_Type
28      1       UINT8             m_is3DSound
29      N       CHAR[N]           m_Filename
29+N    M       CHAR[M]           m_DisplayText
33+N+M  4       FLOAT32           m_StartOffset
37+N+M  4       FLOAT32           m_PitchFactor
41+N+M  4       FLOAT32           m_PitchFactorRandomizer
45+N+M  4       FLOAT32           m_VolumeRandomizer
49+N+M  4       UINT32            m_VirtualChannel
53+N+M  4       UINT32            m_LogicalType
57+N+M  4       FLOAT32           m_LogicalNotifDelay
58+N+M  1       UINT8             m_CreateLogicalSound
62+N+M  4       FLOAT32           m_LogicalDropofRadius
74+N+M  12      `W3D_VECTOR3`_     m_SphereColor   
======  ======  ===============   ====================

* **m_Priority**:
* **m_Volume**:
* **m_Pan**:
* **m_loopCount**:
* **m_DropoffRadius**:
* **m_MaxVoLRadius**:
* **m_Type**:
* **m_is3DSound**:
* **m_Filename**:
* **m_DisplayText**:
* **m_StartOffset**:
* **m_PitchFactor**:
* **m_PitchFactorRandomizer**:
* **m_VolumeRandomizer**:
* **m_VirtualChannel**:
* **m_LogicalType**:
* **m_LogicalNotifDelay**:
* **m_CreateLogicalSound**:
* **m_LogicalDropofRadius**:
* **m_SphereColor**:

**CHUNKID_BASE_CLASS**

  **CHUNKID_VARIABLES**

MicroChunks

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            m_ID
4       N       CHAR[N]           m_Name 
======  ======  ===============   ====================

* **m_ID**:
* **m_Name**:


W3D_CHUNK_SHDMESH
~~~~~~~~~~~~~~~~~

GENERALS: "Shader mesh" Mesh with multiple sub-meshes that use the scaleable shader system

	ShdMesh Render Objects

	Used to define a ShdMesh in a w3d file.  This class
	is the mesh class used with the scaleable shader system.  It contains a number
	of sub-meshes; each which use a single shader.

	NOTE: ShdMeshes re-use the following chunks from regular meshes:

  	`W3D_CHUNK_VERTICES`_
		`W3D_CHUNK_VERTEX_NORMALS`_  	 
    `W3D_CHUNK_VERTICES`_
		`W3D_CHUNK_TRIANGLES`_
		`W3D_CHUNK_MESH_USER_TEXT`_
		`W3D_CHUNK_VERTEX_INFLUENCES`_
		`W3D_CHUNK_VERTEX_SHADE_INDICES`_
		`W3D_CHUNK_AABTREE`_

These are also seen in the Renegade 2 assets.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_SHDMESH_NAME
* W3D_CHUNK_SHDMESH_HEADER
* W3D_CHUNK_SHDMESH_USER_TEXT

W3D_CHUNK_SHDMESH_NAME
~~~~~~~~~~~~~~~~~~~~~~~

Name

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        Name
======  =========  =============  ====================

* **Name**: Name of the mesh in Filename.Meshname

W3D_CHUNK_SHDMESH_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            Version
4       4       UINT32            MeshFlags
8       4       UINT32            NumTriangles
12      4       UINT32            NumVertices
16      4       UINT32            NumSubMeshes
20      20      UINT32[5]         FutureCounts
40      12      `W3D_VECTOR3`_     BoxMin
52      12      `W3D_VECTOR3`_     BoxMax 
64      12      `W3D_VECTOR3`_     SphCenter 
76      4       FLOAT32           SphRadius 
======  ======  ===============   ====================

* **Version**: W3D Format `W3D_VERSION`_ .
* **MeshFlags**:
* **NumTriangles**:
* **NumVertices**:
* **NumSubMeshes**:
* **FutureCounts**: Reserved for future use.
* **BoxMin**:
* **BoxMax**:
* **SphCenter**: 
* **SphRadius**:


W3D_CHUNK_SHDMESH_USER_TEXT
~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: Text from the MAX comment field (Null terminated string)

======  =========  =============  ====================
Offset  Bytes      Type           Name
======  =========  =============  ====================
0       ChunkSize  CHAR[N]        User Text
======  =========  =============  ====================

* **User Text**: Text from the MAX comment field.

W3D_CHUNK_SHDSUBMESH
~~~~~~~~~~~~~~~~~~~~
GENERALS: wrapper around an individual sub-mesh.

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_SHDSUBMESH_HEADER
* W3D_CHUNK_SHDSUBMESH_SHADER
* W3D_CHUNK_SHDSUBMESH_VERTICES
* W3D_CHUNK_SHDSUBMESH_VERTEX_NORMALS
* W3D_CHUNK_SHDSUBMESH_TRIANGLES
* W3D_CHUNK_SHDSUBMESH_VERTEX_SHADE_INDICES
* W3D_CHUNK_SHDSUBMESH_UV0
* W3D_CHUNK_SHDSUBMESH_UV1
* W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_S
* W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_T
* W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_SxT
* W3D_CHUNK_SHDSUBMESH_VERTEX_COLOR
* W3D_CHUNK_SHDSUBMESH_VERTEX_INFLUENCES


W3D_CHUNK_SHDSUBMESH_HEADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Header for a sub-mesh inside an ShdMesh

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            NumTriangles
4       4       UINT32            NumVertices
8       8       UINT32[2]         FutureCounts
16      12      `W3D_VECTOR3`_     BoxMin
28      12      `W3D_VECTOR3`_     BoxMax 
40      12      `W3D_VECTOR3`_     SphCenter 
52      4       FLOAT32           SphRadius 
======  ======  ===============   ====================

* **NumTriangles**:
* **NumVertices**:
* **FutureCounts**: Reserved for future use.
* **BoxMin**:
* **SphCenter**:
* **SphRadius**:

W3D_CHUNK_SHDSUBMESH_SHADER
~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: wrapper around a Shader

Offset  Bytes  Type     Name
======  =====  =======  ===========
0       4      UINT32   ChunkType
4       4      UINT32   ChunkSize
======  =====  =======  ===========

It is a container chunk that can contain these sub-chunks:

* W3D_CHUNK_SHDSUBMESH_SHADER_CLASSID
* W3D_CHUNK_SHDSUBMESH_SHADER_DEF


W3D_CHUNK_SHDSUBMESH_SHADER_CLASSID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Also Known As W3D_CHUNK_SHDSUBMESH_SHADER_TYPE

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            ShaderClass 
======  ======  ===============   ====================

* **ShaderClass**:

W3D_CHUNK_SHDSUBMESH_SHADER_DEF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Also Known as W3D_CHUNK_SHDSUBMESH_SHADER_DATA

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       4       UINT32            ShaderDefinition
======  ======  ===============   ====================

* **ShaderDefinition**:

W3D_CHUNK_SHDSUBMESH_VERTICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: Array of vertices 

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Vertices 
======  ======  ===============   ====================    

* **Vertices**:

W3D_CHUNK_SHDSUBMESH_VERTEX_NORMALS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: array of normals.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Normals 
======  ======  ===============   ====================

* **Normals**:

W3D_CHUNK_SHDSUBMESH_TRIANGLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: array of 16bit int triplets (vertex indices for each triangle)

======  ======  =================   ====================
Offset  Bytes   Type                  Name
======  ======  =================   ====================
0       6       `W3D_VECTOR3i16`_     Triangles
======  ======  =================   ====================

* **Triangles**:

W3D_CHUNK_SHDSUBMESH_VERTEX_SHADE_INDICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: shade indexes for each vertex.

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_     Indices 
======  ======  ===============   ====================

* **Indices**:

W3D_CHUNK_SHDSUBMESH_UV0
~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex texture coordinates

======  ======  ===============    ====================
Offset  Bytes   Type                Name
======  ======  ===============    ====================
0       8 * N   `W3D_TEXCOORD`_      Vertex UV
======  ======  ===============    ====================

* **Vertex UV**:

W3D_CHUNK_SHDSUBMESH_UV1
~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex texture coordinates

======  ======  ===============    ====================
Offset  Bytes   Type                Name
======  ======  ===============    ====================
0       8 * N   `W3D_TEXCOORD`_     Vertex UV
======  ======  ===============    ====================

* **Vertex UV**:

W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_S
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex tangent basis S vectors

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Tangents
======  ======  ===============   ====================

* **Tangents**:

W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_T
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex tangent basis T vectors

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_    Tangents
======  ======  ===============   ====================

* **Tangents**:

W3D_CHUNK_SHDSUBMESH_TANGENT_BASIS_SXT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex tangent basis SxT vectors

======  ======  ===============   ====================
Offset  Bytes   Type              Name
======  ======  ===============   ====================
0       12      `W3D_VECTOR3`_     Tangents
======  ======  ===============   ====================

* **Tangents**:


W3D_CHUNK_SHDSUBMESH_VERTEX_COLOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: per-vertex color

W3D_CHUNK_SHDSUBMESH_VERTEX_INFLUENCES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GENERALS: byte-per-vertex, WWSkin support

W3D_CHUNK_SECONDARY_VERTICES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unknown purpose - added in BFME. Contained vertices are very similar to,
but not the same as, the vertices in W3D_CHUNK_VERTICES.

Also Known as W3D_CHUNK_VERTICES_COPY

======  ======  =================     ====================
Offset  Bytes   Type                  Name
======  ======  =================     ====================
0       12 * N  `W3D_VECTOR3`_[N]     Vertices
======  ======  =================     ====================

* **Vertices**:

W3D_CHUNK_SECONDARY_VERTEX_NORMALS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unknown purpose - added in BFME. Contained normals are very similar to,
but not the same as, the normals in W3D_CHUNK_NORMALS.

Also Known as W3D_CHUNK_VERTEX_NORMALS_COPY

======  ======  =================     ====================
Offset  Bytes   Type                  Name
======  ======  =================     ====================
0       12 * N  `W3D_VECTOR3`_[N]     Normals
======  ======  =================     ====================

* **Normals**:

W3D_CHUNK_LIGHTMAP_UV
~~~~~~~~~~~~~~~~~~~~~
BFME II: 



OBSOLETE:
---------

These Are defined in the renegade source but were depreciated before release
Documented for historical reasons.

W3D_CHUNK_MESH_HEADER
~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: header for a mesh version 1

======  ======  ===============  ====================
Offset  Bytes   Type              Name
======  ======  ===============  ====================
0       4       UINT32           Version
4       16      CHAR[16]         MeshName
20      4       UINT32           Attributes
24      4       UINT32           NumTriangles
28      4       UINT32           NumQuads
32      4       UINT32           NumSrTris
36      4       UINT32           NumPovQuads
40      4       UINT32           NumVertices
44      4       UINT32           NumNormals
48      4       UINT32           NumSrNormals
52      4       UINT32           NumTexCoords
56      4       UINT32           NumMaterials
60      4       UINT32           NumVertColors
64      4       UINT32           NumVertInfluences
68      4       UINT32           NumDamageStages
72      32      UINT32[8]        FutureCounts
104     4       FLOAT32          LODMin
108     4       FLOAT32          LODMax
112     12      `W3D_VECTOR3`_   Min
124     12      `W3D_VECTOR3`_   Max
136     12      `W3D_VECTOR3`_   SphCenter
148      4      FLOAT32          SphRadius
152     12      `W3D_VECTOR3`_   Translation
164     36      FLOAT32[9]       Rotation
200     12      `W3D_VECTOR3`_   MassCenter
212     36      FLOAT32[9]       Inertia
248     4       FLOAT32          Volume
252     16      CHAR[16]         HierarchyTreeName
268     16      CHAR[16]         HierarchyModelName
284     96      UINT32[24]       FutureUse
======  ======  ===============  ====================



W3D_CHUNK_SURRENDER_NORMALS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of surrender normals (one per vertex as req. by surrender)

======  ======  ==============  ====================
Offset  Bytes   Type            Name
======  ======  ==============  ====================
0       12      `W3D_VECTOR3`_  SrNormals
======  ======  ==============  ====================

W3D_CHUNK_TEXCOORDS
~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of texture coordinates

======  ======  ===============    ====================
Offset  Bytes   Type                Name
======  ======  ===============    ====================
0       8 * N   `W3D_TEXCOORD`_     TexCoord
======  ======  ===============    ====================

O_W3D_CHUNK_MATERIALS
~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of materials version 1

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       16      CHAR[16]      MaterialName 
16      16      CHAR[16]      PrimaryName
32      16      CHAR[16]      SecondaryName
48       4      UINT32        RenderFlags
52       1      UINT8         Red 
53       1      UINT8         Green 
54       1      UINT8         Blue 
======  ======  ============  ====================


O_W3D_CHUNK_TRIANGLES
~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of triangles

O_W3D_CHUNK_QUADRANGLES
~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of quads

O_W3D_CHUNK_SURRENDER_TRIANGLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of surrender format tris

======  ======  ==================        ====================
Offset  Bytes   Type                      Name
======  ======  ==================        ====================
0       12      UINT32[3]                  VIndex 
12      24      `W3D_TEXCOORD`_[3]         TexCoord
36      4       UINT32                     MaterialIDx
40      12      `W3D_VECTOR3`_             Normal
52      4       UINT32                     Atributes 
56      12      `W3D_RGB`_ [3]             Gouraud
======  ======  ==================        ====================


O_W3D_CHUNK_POV_TRIANGLES
~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: POV format triangles 

O_W3D_CHUNK_POV_QUADRANGLES
~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: POV format quads

W3D_CHUNK_VERTEX_COLORS
~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Pre-set vertex coloring

======  ======  ============    ====================
Offset  Bytes   Type            Name
======  ======  ============    ====================
0       4       `W3D_RGB`_      Vertex RGB
======  ======  ============    ====================

W3D_CHUNK_DAMAGE
~~~~~~~~~~~~~~~~

OBSOLETE: Mesh damage, new set of materials, vertex positions, vertex colors

Mesh Damage.  This can include a new set of materials for the mesh,
new positions for certain vertices in the mesh, and new vertex
colors for certain vertices.

W3D_CHUNK_DAMAGE_HEADER
~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Header for the damage data, tells what is coming

======  ======  ============    ====================
Offset  Bytes   Type            Name
======  ======  ============    ====================
0       4       UINT32          NumDamageMaterials
4       4       UINT32          NumDamageVerts
8       4       UINT32          NumDamageColors
12      4       UINT32          DamageIndex
16      16      UINT32[4]       FutureUse
======  ======  ============    ====================


W3D_CHUNK_DAMAGE_VERTICES
~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Array of modified vertices (W3dMeshDamageVertexStruct's)

======  ======  ==============    ====================
Offset  Bytes   Type                Name
======  ======  ==============    ====================
0       4       UINT32              VertexIndex
4       12      `W3D_VECTOR3`_    NewVertex
======  ======  ==============    ====================

W3D_CHUNK_DAMAGE_COLORS
~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Array of modified vert colors (W3dMeshDamageColorStruct's)

======  ======  ============    ====================
Offset  Bytes   Type            Name
======  ======  ============    ====================
0       4       UINT32          VertexIndex
4       4       `W3D_RGB`_       NewColor
======  ======  ============    ====================


W3D_CHUNK_DAMAGE_MATERIALS
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE:

O_W3D_CHUNK_MATERIALS2
~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: array of these are found inside the W3D_CHUNK_MATERIALS2 chunk. Version 2

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       16      CHAR[16]      MaterialName 
16      16      CHAR[16]      PrimaryName
32      16      CHAR[16]      SecondaryName
48       4      UINT32        RenderFlags
52       1      UINT8         Red 
53       1      UINT8         Green 
54       1      UINT8         Blue 
55       1      UINT8         Alpha
56       2      UINT16        PrimaryNumFrames
58       2      UINT16        SecondaryNumFrames
60       12     CHAR[12]      Padding
======  ======  ============  ====================



W3D_CHUNK_MATERIALS3
~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Version 3 wrapper


W3D_CHUNK_MATERIAL3
~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Each version 3 material wrapped with this chunk ID


W3D_CHUNK_MATERIAL3_NAME
~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Name of the material (array of chars, null terminated)

W3D_CHUNK_MATERIAL3_INFO
~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: contains a W3dMaterial3Struct, general material info

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4       UINT32        Material3Flags
4       4       `W3D_RGB`_     DiffuseColor
8       4       `W3D_RGB`_     SpecularColor
12      4       `W3D_RGB`_     EmissiveCoefficients
16      4       `W3D_RGB`_     AmbientCoefficients
20      4       `W3D_RGB`_     DiffuseCoefficients
24      4       `W3D_RGB`_     SpecularCoefficients
28      4       FLOAT32       Shininess
32      4       FLOAT32       Opacity
36      4       FLOAT32       Translucency
40      4       FLOAT32       FogCoeff
======  ======  ============  ====================

* **Material3Flags**: bitwise-or'd collection of `W3D_MATERIAL3_FLAGS`_ values.

W3D_MATERIAL3_FLAGS
~~~~~~~~~~~~~~~~~~~~

==========  ==========================================  ==============
Value       Name                                        Description
==========  ==========================================  ==============
0x1         W3DMATERIAL_USE_ALPHA
0x2         W3DMATERIAL_USE_SORTING 
0x10        W3DMATERIAL_HINT_DIT_OVER_DCT 
0x20        W3DMATERIAL_HINT_SIT_OVER_SCT
0x40        W3DMATERIAL_HINT_DIT_OVER_DIG
0x80        W3DMATERIAL_HINT_SIT_OVER_SIG 
0x100       W3DMATERIAL_HINT_FAST_SPECULAR_AFTER_ALPHA    
0xFF000000  W3DMATERIAL_PSX_MASK
0x7000000   W3DMATERIAL_PSX_TRANS_MASK
0x0         W3DMATERIAL_PSX_TRANS_NONE
0x1000000   W3DMATERIAL_PSX_TRANS_100 
0x2000000   W3DMATERIAL_PSX_TRANS_50
0x3000000   W3DMATERIAL_PSX_TRANS_25 
0x4000000   W3DMATERIAL_PSX_TRANS_MINUS_100
0x8000000   W3DMATERIAL_PSX_NO_RT_LIGHTING
==========  ==========================================  ==============

W3D_CHUNK_MATERIAL3_DC_MAP
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: wraps the following two chunks, diffuse color texture

W3D_CHUNK_MAP3_FILENAME
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: filename of the texture

String

W3D_CHUNK_MAP3_INFO
~~~~~~~~~~~~~~~~~~~~~~~~~~

A map, only occurs as part of a material, will be preceeded by its name.

OBSOLETE: a W3dMap3Struct

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       2       UINT16        MappingType
2       2       UINT16        FrameCount
4       4       UINT32        FrameRate
======  ======  ============  ====================


W3D_CHUNK_MATERIAL3_DI_MAP
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: diffuse illimination map, same format as other maps

W3D_CHUNK_MATERIAL3_SC_MAP
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: specular color map, same format as other maps

W3D_CHUNK_MATERIAL3_SI_MAP
~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: specular illumination map, same format as other maps

W3D_CHUNK_PER_TRI_MATERIALS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: Multi-Mtl meshes - An array of uint16 material id's

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       2       UINT16        Triangle Material Idx
======  ======  ============  ====================


OBSOLETE_W3D_CHUNK_HMODEL_AUX_DATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: extension of the hierarchy model header

HModels had this extra chunk defining the counts of individual
types of objects to be found in the model and some obsolete distance-based LOD settings.
As changes were made to the ww3d library, all of this became useles so the chunk was
"retired".

======  ======  ============  ====================
Offset  Bytes   Type          Name
======  ======  ============  ====================
0       4       UINT32        Attributes
4       4       UINT32        MeshCount
8       4       UINT32        CollisionCount
12      4       UINT32        SkinCount
16      4       UINT32        ShadowCount
20      4       UINT32        NullCount
24      24      UINT32[6]     FutureCounts
48      4       UINT32        LODMin
52      4       UINT32        LODMax
56      4       UINT32[32]    FutureUse
======  ======  ============  ====================

OBSOLETE_W3D_CHUNK_SHADOW_NODE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: shadow object connected to the hierarchy

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       16      CHAR[16]       ShadowMeshName
16      2*N     UINT16[N]      PivotIDx
======  ======  =============  ====================

``N`` = the number of Shadows connected to the hierarchy

OBSOLETE_W3D_CHUNK_EMITTER_COLOR_KEYFRAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: structure defining a single color keyframe

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        Time 
4       4       `W3D_RGBA`_       Color
======  ======  =============  ====================

OBSOLETE_W3D_CHUNK_EMITTER_OPACITY_KEYFRAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: structure defining a single opacity keyframe

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        Time 
4       4       FLOAT32        Opacity
======  ======  =============  ====================

OBSOLETE_W3D_CHUNK_EMITTER_SIZE_KEYFRAME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OBSOLETE: structure defining a single size keyframe

======  ======  =============  ====================
Offset  Bytes   Type           Name
======  ======  =============  ====================
0       4       FLOAT32        Time 
4       4       FLOAT32        Size
======  ======  =============  ====================

Structures
----------

W3D_VECTOR3
~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      X
4       4      FLOAT32      Y
8       4      FLOAT32      Z
======  =====  ===========  ====================


W3D_VECTOR2
~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      X
4       4      FLOAT32      Y
======  =====  ===========  ====================


W3D_VERSION
~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4       UINT32      Version
======  =====  ===========  ====================

**Version**: Each Major chunk type will contain a "header" as its first
sub-chunk.  The first member of this header will be a Version
number formatted so that its major revision number is the
high two bytes and its minor revision number is the lower two
bytes. Example: 01 00 04 00 = 4.1 

W3D_VECTOR3i
~~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      UINT32       I
4       4      UINT32       J
8       4      UINT32       K 
======  =====  ===========  ====================

W3D_VECTOR3i16
~~~~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       2      UINT16       I
2       2      UINT16       J
2       2      UINT16       K 
======  =====  ===========  ====================

W3D_ALPHA_VECTOR
~~~~~~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      AngleX
4       4      FLOAT32      AngleY
8       4      FLOAT32      AngleZ
12      4      FLOAT32      AngleW
16      4      FLOAT32      Intensity
======  =====  ===========  ====================


W3D_RGB
~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       1      UINT8        Red
1       1      UINT8        Green
2       1      UINT8        Blue
3       1      UINT8        Padding
======  =====  ===========  ====================

W3D_RGBA
~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       1      UINT8        Red
1       1      UINT8        Green
2       1      UINT8        Blue
3       1      UINT8        Alpha
======  =====  ===========  ====================

W3D_TEXCOORD
~~~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       4      FLOAT32      U
4       4      FLOAT32      V
======  =====  ===========  ====================

W3D_QUATERNION
~~~~~~~~~~~~~~~

======  =====  ===========  ====================
Offset  Bytes  Type         Name
======  =====  ===========  ====================
0       16      FLOAT32[4]  Q
======  =====  ===========  ====================