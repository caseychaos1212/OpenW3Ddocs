# Source review — 2026-09-14

This review compares the documentation with OpenW3D's headers and relevant
load/save code. It corrects verified discrepancies and refreshes the generated
script reference. It is not an exhaustive validation of every game variant,
script behavior, or animation preview.

## Sources

The main reference is [OpenW3D at `dbd77b7`](https://github.com/w3dhub/OpenW3D/tree/dbd77b71a57f19dfc2618babb6df989954f2651a),
the current `main` commit when reviewed. The comparison also consulted the
documentation's cited headers:

- [TT max2w3d at `d89e338`](https://github.com/w3dhub/max2w3d/blob/d89e338a4d09f9e65baf1381edc0e5bd2e757308/scripts/w3d.h)
  and [its obsolete declarations](https://github.com/w3dhub/max2w3d/blob/d89e338a4d09f9e65baf1381edc0e5bd2e757308/scripts/w3dobsolete.h).
- [EA Generals/Zero Hour at `0a05454`](https://github.com/electronicarts/CnC_Generals_Zero_Hour/blob/0a05454d8574207440a5fb15241b98ad0b435590/GeneralsMD/Code/Libraries/Source/WWVegas/WW3D2/w3d_file.h).
  The emitter follow-up checked all six `w3d_file.h` copies: the runtime,
  `Tools/WW3D/max2w3d`, and `Tools/WW3D/pluglib` headers in both `Generals`
  and `GeneralsMD`.
- [OpenSAGE's emitter enum at `588ac47`](https://github.com/OpenSAGE/OpenSAGE/blob/588ac477367a0022adf29f20a084e8873014e6ce/src/OpenSage.FileFormats.W3d/W3dChunkType.cs#L119-L132),
  compared with [its published chunk table](https://opensage.readthedocs.io/file-formats/w3d/#w3d-chunk-type).
- [w3d2ply at the already cited `ecd8302`](https://github.com/mikolalysenko/w3d2ply/blob/ecd8302b6cfd0578ab249cb95c8b70636c4609bc/w3d_file.h).
- [libw3d at the already cited `fb547b2`](https://github.com/feliwir/libw3d/blob/fb547b28c91f17070d65ba24edf7a5294a0554d9/include/libw3d/types.hpp).

Declarations describe fields; the corresponding reader/writer establishes what
OpenW3D actually consumes. Extensions and obsolete declarations are not evidence
of runtime support.

## W3D corrections

| Area | Correction | Evidence |
| --- | --- | --- |
| Index notation | Index triplets are stored as `I, J, K`. `Vector3i` uses signed 32-bit integers; `Vector3i16` uses unsigned 16-bit integers, with `K` at byte 4. Coordinate vectors remain `X, Y, Z`. No `J, K, I` storage reorder was found. | [vector3i.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwmath/vector3i.h) |
| Triangle indices | Three indices identify the triangle's three vertices, rather than separate normal/UV/color streams. OpenW3D maps `Vindex[0..2]` to `I, J, K`. | [meshgeometry.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/meshgeometry.cpp) |
| UV index stream | One 12-byte triplet per triangle, not 4 bytes. The runtime checks the length and skips these indices. UV-coordinate count comes from the UV chunk length. | [meshmdlio.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/meshmdlio.cpp) |
| Chunk IDs | Spot-light info is `0x462`. Emitter rotation/frame/blur keys remain documented at `0x50A/0x50B/0x50C`, with extra info at `0x50D`. Removed only the additional `0x510/0x511/0x512` assignments inherited from OpenSAGE's documentation; see the emitter follow-up below. | [w3d_file.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/w3d_file.h) |
| Vertex material | Opacity and translucency start at bytes 24 and 28, after shininess at 20. | `W3dVertexMaterialStruct` in the same header |
| Hierarchy | Header center is 12 bytes. The root is pivot 0; `0xffffffff` means no parent. Quaternion components map to `X, Y, Z, W`; the base transform uses the quaternion rather than Euler angles. | [htree.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/htree.cpp), [quat.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/wwmath/quat.h) |
| Bit animation | Round bit storage up to whole bytes; bits run from least to most significant within each byte. | [motchan.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/motchan.cpp), [motchan.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/motchan.h) |
| Compressed animation | Corrected time-coded word counts, the one-byte adaptive flags field, and the compressed visibility header/32-bit data records. Added enum values 11–14 while documenting that runtime dispatch uses base values 0/1/2/6. | [w3d_file.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/w3d_file.h), [hcanim.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/hcanim.cpp) |
| Emitter user data | Replaced the bare-string claim with OpenW3D's struct-then-string layout, including the legacy placeholder and alignment caveat. | [part_ldr.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/part_ldr.cpp) |
| Emitter structures | Corrected velocity/acceleration offsets, RGBA color types, V2 offsets, property-header offsets, and reserved-array lengths. Kept the Generals extra-info layout distinct from OpenW3D's declaration. | `W3dEmitter*` declarations in the checked headers |
| Aggregate structures | Fixed the 32-character base name, four-byte flags, and texture-replacer records: two 15×32-character paths, two 260-character filenames, and texture parameters. | `W3dAggregate*` and `W3dTextureReplacer*` in `w3d_file.h` |
| Sphere/ring effects | Corrected alpha and subsequent ring offsets, the four-byte integer tile count, the ring definition chunk name, and the boundaries of per-key micro-chunks. | [sphereobj.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/sphereobj.h), [ringobj.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/ringobj.h), [prim_anim.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/prim_anim.h) |
| Other records | Fixed the null-object version width; documented trailing alignment in HModel and LOD headers. The collection object-name description now refers to render objects. | `w3d_file.h`, [hmdldef.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/hmdldef.cpp), [distlod.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/distlod.cpp) |
| Generals shade indices | The shader-submesh shade stream is one `UINT32` per vertex, not a float coordinate vector. | `W3D_CHUNK_SHDSUBMESH_VERTEX_SHADE_INDICES` in the EA Generals header |
| Obsolete formats | Restored `NumPovTris`, corrected `FutureCounts[5]` and subsequent old-mesh offsets, changed map frame rate and HModel LOD limits to floats, and corrected `FutureUse[32]` to 128 bytes. | [w3d_obsolete.h](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/w3d_obsolete.h) |
| Skin support | Distinguished the declared multi-bone layouts from the reviewed runtime paths, which retain a single bone and do not load the extended chunk. | [meshgeometry.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/meshgeometry.cpp), [meshmdlio.cpp](https://github.com/w3dhub/OpenW3D/blob/dbd77b71a57f19dfc2618babb6df989954f2651a/Code/ww3d2/meshmdlio.cpp) |

## Emitter follow-up

The Zero Hour runtime header does contain later emitter declarations, and all
of these chunk types and their descriptions are retained. Its enum starts at
`0x500` and increments without reassignment through extra info at `0x50D`:
line properties `0x509`, rotation keys `0x50A`, frame keys `0x50B`, blur-time
keys `0x50C`, and extra info `0x50D`.

| EA header copy | Emitter declarations |
| --- | --- |
| `Generals/Code/Libraries/Source/WWVegas/WW3D2/w3d_file.h` | Through frame keys (`0x50B`) |
| `GeneralsMD/Code/Libraries/Source/WWVegas/WW3D2/w3d_file.h` | Through extra info (`0x50D`), including blur-time keys |
| Both games' `Code/Tools/WW3D/max2w3d/w3d_file.h` | Through frame keys (`0x50B`) |
| Both games' `Code/Tools/WW3D/pluglib/w3d_file.h` | No emitter chunk declarations |

None of these six copies assigns the disputed `0x510/0x511/0x512` values.
OpenSAGE's published documentation lists those values, but its source enum
uses `0x50A/0x50B/0x50C`, matching OpenW3D and the Zero Hour runtime header.
The W3D page now explains this source/documentation discrepancy and the
differences between the bundled header copies. These declaration checks do
not establish runtime support in each game.

## Other pages and generated references

- Checked the MIX header, directory/name tables, CRC lookup, and 8-byte alignment
  against `wwlib/mixfile.cpp`; the documented layout agrees.
- Checked the LVL/LSD/LDD top-level save/load flows, and the DDB/CDB/TDB subsystem
  descriptions against their linked implementations. Clarified that runtime DDB
  saves can contain only definitions, and that the conversation-ID micro-chunks
  depend on the saved category. Fixed nested-list rendering and literal paths.
- Checked mapper argument keys against `ww3d2/mapper.cpp` and mapper selection
  against `vertmaterial.cpp`; the documented key list agrees.
- Fixed the generator's comment handling and regenerated the catalog: **1,639
  entries across 41 files**, down from 1,655. Sixteen commented registrations
  were incorrectly indexed, including two duplicate Mission04 entries. The
  scanner now ignores commented callbacks/commands and preprocessor directives,
  preserves quoted strings and source line numbers, and does not treat a disabled
  script block as documentation for the next class. Retained registrations keep
  their parameter descriptions. Source-line references and detected summaries,
  callbacks, and command lists were refreshed. These are scanner results, not a
  manual behavior review of every script.
- Added optional `--source-revision` provenance to the generator. Clarified the
  limits of its preprocessor model and that source inventory differs from the
  CMake build's compiled script set.
- Checked the human animation naming and skeleton-remapping code. Corrected
  landing names to the state-specific `S_A_HUMAN.H_A_A0L0`–`A0L4` pattern. Kept
  existing inventory and preview descriptions as working notes.

## Verification and remaining gaps

The HTML documentation builds with the repository's pinned Sphinx 7.1.2 and
theme dependencies, using warnings as errors. Fixed the existing TDB indentation
error, malformed W3D references/tables, and the invalid Sphinx language setting.
Build files and included gallery fragments are excluded as standalone pages.
Seven focused generator regression tests pass, covering commented registrations,
callbacks, directives and braces, quoted comment delimiters, continued line
comments, and disabled scripts incorrectly used as source notes. The regenerated
catalog was checked for duplicate entries and unchanged parameter descriptions
among the retained registrations.

This review does not establish binary compatibility from real game files. The
Earth & Beyond parser and its exclusive variants, complete SAGE shader/property
payloads, BFME compressed-motion payloads, and detailed audio-definition
micro-chunks still need targeted reader/writer and sample-file checks. Existing
TODOs and unknown fields in those areas remain unresolved. Hosted/embedded GIF
content and every inferred animation description were not visually reviewed.

To repeat the script generation, use the reviewed source checkout:

```text
python tools/generate_openw3d_scripts_reference.py --source-root <OpenW3D>/Code/Scripts --source-revision dbd77b71a57f19dfc2618babb6df989954f2651a
python -m unittest discover -s tools/tests -v
python -m sphinx -b html -W --keep-going . build/html
```
