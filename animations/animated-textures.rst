.. _animated-textures:

Animated textures
=================

OpenW3D animates ordinary mesh textures with **texture mappers**. A mapper
changes the texture coordinates used to sample an image as engine time
advances. A grid mapper steps through frames packed into one image; other
mappers scroll, rotate, or oscillate the coordinates over an image.
These effects do not need a skeletal animation or a sequence of texture files.

This guide follows OpenW3D revision
``8f4d7aad6a58e5f91667454b1d6813e53b179d36``, specifically the material
loader and ``ww3d2`` mapper implementation. The examples are derived from
source and have not been tested in a running game or exporter. The
:ref:`derivative comparison <animated-texture-derivatives>` identifies a
separate Zero Hour implementation; its additional options are not OpenW3D
options. Particle frame keys are a separate system and are outside this guide.

Where the settings live
-----------------------

A vertex material selects one mapping mode for each texture stage. OpenW3D
loads stages 0 and 1 separately, so each stage can have its own mapper and
arguments. The mode is stored in the vertex material's ``Attributes`` field;
the argument text is stored in ``W3D_CHUNK_VERTEX_MAPPER_ARGS0`` or
``W3D_CHUNK_VERTEX_MAPPER_ARGS1``. The texture filename belongs to the
separate texture record.

In a W3D material editor, select the mapping mode for the stage that uses
the texture, then enter its arguments as one ``key=value`` per line. The
original OpenW3D Max exporter exposes a mapping selector and argument box
for each stage in the vertex material controls. Do not add an ``[Args]``
heading: the runtime loader adds it before parsing the text as INI data.

An argument only has an effect if the selected mapper reads it. For example,
entering ``FPS=8`` while leaving the stage on ordinary UV mapping does not
animate anything. Selecting Grid and Rotate together does not compose two
effects: the mapping bits select one mode per stage.

Sources: `Material loader`_ and `Exporter vertex material controls`_. See
:ref:`w3d-mapper-arguments` for the complete OpenW3D argument-key list.

Making a grid animation
-----------------------

The plain ``GridTextureMapperClass`` uses an atlas with the same number of
columns and rows. Each side has ``2 ** Log2Width`` cells. The texture's pixel
dimensions do not come from ``Log2Width``; that setting describes the cell
layout within the image.

.. list-table:: Grid sizes
   :header-rows: 1
   :widths: 25 35 40

   * - ``Log2Width``
     - Columns x rows
     - Available frames
   * - ``1``
     - 2 x 2
     - 4
   * - ``2``
     - 4 x 4
     - 16
   * - ``3``
     - 8 x 8
     - 64
   * - ``4``
     - 16 x 16
     - 256

For a 16-frame example:

1. Pack 16 images into a 4 x 4 atlas. A 512 x 512 image would give each
   frame a 128 x 128 cell.
2. Put frame 0 in the cell at the UV origin, then arrange frames along
   increasing U, followed by the next row along increasing V. Verify the
   image orientation in your exporter; image editors and UV editors may
   display the vertical axis differently.
3. Map the mesh to the first cell: U and V each cover ``0.0`` to ``0.25``
   in the exported UVs. **The plain grid mapper only adds an offset; it
   does not shrink a full 0-to-1 UV layout to one cell.**
4. Assign the atlas to the desired texture stage, select Grid mapping,
   and enter:

   .. code-block:: text

      FPS=8
      Log2Width=2
      Last=16

5. Export the mesh and make the atlas available through the game's normal
   texture lookup. The mapper samples that same image throughout playback.

At eight frames per second, this example completes a loop in two seconds.
Its frame layout in UV space is:

.. code-block:: text

                    increasing U -->
                  +----+----+----+----+
   UV origin      |  0 |  1 |  2 |  3 |
                  +----+----+----+----+
   increasing V   |  4 |  5 |  6 |  7 |
         |        +----+----+----+----+
         v        |  8 |  9 | 10 | 11 |
                  +----+----+----+----+
                  | 12 | 13 | 14 | 15 |
                  +----+----+----+----+

For grid width ``N`` and frame ``f`` within the atlas, the mapper adds::

   U offset = (f % N) / N
   V offset = floor(f / N) / N

For frame 6 in the example, the offset is ``(0.5, 0.25)``. It translates
the original first-cell UVs to the third column of the second row.
Adding ``UScale`` or ``VScale`` to Grid's arguments will not fix oversized
UVs, because this mapper does not read those keys.
Source: `OpenW3D mapper implementation`_, ``GridTextureMapperClass``.

Grid arguments and playback
---------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 15 67

   * - Key
     - Default
     - Meaning
   * - ``FPS``
     - ``1.0``
     - Requested frames per second. Positive values advance forward;
       negative values request reverse playback. Zero initializes at
       frame 0 and stops automatic advancement.
   * - ``Log2Width``
     - ``1``
     - Base-2 logarithm of the number of cells along each side.
   * - ``Last``
     - ``0``
     - Number of frames in the loop. Zero selects every cell in the grid.
       Otherwise use a count from 1 through ``N * N``.

Despite its name, ``Last`` is a **count**, not the last frame's index.
``Last=10`` plays frames 0 through 9; ``Last=16`` plays 0 through 15.
For a partly filled 4 x 4 atlas, use ``Last=10`` to skip the six unused
cells at the end. The grid dimensions stay 4 x 4.

The mapper measures elapsed milliseconds using ``WW3D::Get_Sync_Time()``
when it is applied for rendering. It accumulates the elapsed time, advances
by the number of complete frame intervals, and retains the remainder. A
slow render frame can therefore skip animation frames. A mapper that has
not been applied for a while catches up on its next application, unless
it has been reset in between.

For nonzero ``FPS``, the frame interval is an unsigned integer calculated
as ``1000 / abs(FPS)``, with the fractional part discarded. For example,
``FPS=30`` gives 33 milliseconds per frame, approximately 30.3 frames per
second. Use finite, practical rates no greater than 1000 in magnitude;
higher rates can produce a zero interval and division by zero. The loader
also does not validate the grid dimensions or frame count for you.

The normal grid path loops by reducing the frame number modulo ``Last``.
It has no mapper argument for playing once, ping-pong playback, start
delay, or interpolation between frame images. These options cannot be
enabled with the similarly named texture-info fields described below.

.. note::

   Reverse playback needs extra care with a shortened loop in this
   OpenW3D revision. Initialization starts at ``Last - 1``, but ``Reset()``
   starts at the final cell of the full grid. The update also uses an
   unsigned ``LastFrame`` in its modulo expression, so a negative frame
   value does not reliably wrap to the expected frame for non-power-of-two
   counts. Prefer positive FPS for a partially filled atlas; verify reverse
   playback and resets in the target engine before relying on them.

Source: `OpenW3D mapper implementation`_, ``initialize()``, ``Reset()``,
and ``update_temporal_state()``.

Scrolling and rotating a texture
--------------------------------

Select **Linear Offset** mapping for a continuous scrolling effect, such
as a conveyor belt or flowing surface. Example arguments:

.. code-block:: text

   UPerSec=0.25
   VPerSec=0.0
   UScale=1.0
   VScale=1.0

``UPerSec`` and ``VPerSec`` default to zero and specify motion in UV units
per second. Both scales default to one. OpenW3D preserves a legacy sign
convention: the sampling-coordinate offset changes by the **negative** of
the supplied rate. Thus ``UPerSec=0.25`` subtracts 0.25 from the U offset
per second, wrapping the offset into the range from zero to less than one.
With a repeating texture, one complete scroll takes four seconds. The
visible direction on the mesh also depends on its UV orientation.

For a spinning pattern, select **Rotate** mapping and use:

.. code-block:: text

   Speed=0.25
   UCenter=0.5
   VCenter=0.5
   UScale=1.0
   VScale=1.0

``Speed`` is revolutions per second, so this example makes one revolution
in four seconds. Its default is ``0.1``; the default center is ``(0, 0)``,
so explicitly use ``(0.5, 0.5)`` when rotating around the texture's center.

Other time-varying choices include Sine Linear Offset for oscillation,
Step Linear Offset for discrete UV steps, and Zigzag Linear Offset for
back-and-forth motion. Grid Classic Environment and Grid Environment
combine grid frame offsets with generated environment coordinates. Their
coordinate generation differs from the plain Grid example above.
Source: `OpenW3D mapper implementation`_.

Timing belongs to the material mapper
-------------------------------------

Each mapper keeps its own playback state. Two materials can use the same
texture image with different mapping settings; the image filename does
not define a global animation clock. Objects that share a material mapper
also share that mapper's state. Do not assume that spawning another object
automatically starts its texture animation at frame 0.

For engine-side control, ``GridTextureMapperClass`` exposes ``Set_Frame()``,
``Set_Frame_Per_Second()``, and ``Reset()``. Setting the rate reinitializes
playback; setting a frame alone does not stop time-based advancement. To
hold a frame, set the rate to zero and then set the desired valid frame.
These are C++ methods, not mapper argument keys or gameplay-script commands.

``Reset_All_Texture_Mappers(robj, make_unique)`` traverses a render object
and resets its time-varying material mappers. Its ``make_unique`` path
makes mesh and vertex material data unique before resetting. This is
relevant when a reset should affect one object instead of shared material
state. Cloning a grid mapper also resets its playback state.
Sources: `Mapper interface`_, `OpenW3D mapper implementation`_, and
`Material loader`_ (material copy and apply methods).

Texture-info animation fields
------------------------------

The W3D format separately declares ``AnimType``, ``FrameCount``, and
``FrameRate`` in ``W3dTextureInfoStruct``. The declared animation modes are
Loop, Ping-pong, Once, and Manual. These are alternative mode values, not
independent flags to combine.

In the reviewed OpenW3D ``Load_Texture()`` path, the loader reads the
structure but uses its texture attributes for mipmaps, texture type, and
addressing. It does not use those three animation fields to create a
frame sequence. Changing them does not configure a grid mapper or make
numbered image files play as an animation. Configure the vertex material
mapper and its arguments instead.

Sources: `W3D declarations`_ and `Texture loader`_. See
:ref:`w3d-texture-info` for the binary record layout.

.. _animated-texture-derivatives:

Differences in other W3D derivatives
------------------------------------

The released **Generals: Zero Hour** runtime source at revision
``0a05454d8574207440a5fb15241b98ad0b435590`` has a related grid mapper.
It reads ``FPS``, ``Log2Width``, and ``Last`` with the same defaults, and
also reads ``Offset`` (default zero). It reduces ``Offset`` modulo the
frame count and starts at that offset for forward or stopped playback,
or at ``Last - 1 - Offset`` for reverse playback. Its reset uses the same
starting-frame rule.

The Zero Hour plain grid transform also only translates UVs, so it still
expects UVs sized to one cell. OpenW3D's reviewed grid constructor does
not read ``Offset``. An argument accepted by one derivative should not be
assumed to work in another. This comparison covers the cited runtime
mapper source; it does not establish compatibility with every exporter,
TT/Scripts release, or other SAGE game.
Sources: `Zero Hour mapper implementation`_ and `OpenW3D mapper implementation`_.

Troubleshooting
---------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Symptom
     - Check
   * - The entire atlas is visible.
     - Fit the exported UVs into one cell. Grid adds offsets without
       scaling the UVs; ``UScale`` and ``VScale`` are not Grid options.
   * - The texture stays still.
     - Check the selected stage and mapping mode, the argument spelling,
       and whether ``FPS=0`` or ``Last=1`` is intentional.
   * - Empty cells appear during playback.
     - Set ``Last`` to the number of populated cells, arranged consecutively
       from frame 0. Zero uses the entire grid.
   * - A frame is missing at the end.
     - Use a frame count for ``Last``. Sixteen frames require ``Last=16``.
   * - Adjacent frames bleed into the image.
     - Filtering and mipmaps can sample across cell boundaries. As an
       authoring precaution, inset UVs and provide matching edge padding
       within each cell. Test at the distances and mip levels used in game.
       Clamping the texture addresses clamps the whole atlas, not each cell.
   * - Scrolling stretches at the edge.
     - Check the texture's U/V addressing. A seamless scrolling surface
       generally needs repeat addressing and an image that tiles.
   * - Several objects restart together.
     - Check whether they share material mapper state before resetting it.
   * - Settings work in a derivative but not OpenW3D.
     - Check that the target mapper reads those keys. For example,
       OpenW3D's reviewed Grid mapper does not read Zero Hour's ``Offset``.

.. _OpenW3D mapper implementation: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/ww3d2/mapper.cpp
.. _Mapper interface: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/ww3d2/mapper.h
.. _Material loader: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/ww3d2/vertmaterial.cpp
.. _Exporter vertex material controls: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/Tools/max2w3d/GameMtlVertexMaterialDlg.cpp
.. _W3D declarations: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/ww3d2/w3d_file.h
.. _Texture loader: https://github.com/w3dhub/OpenW3D/blob/8f4d7aad6a58e5f91667454b1d6813e53b179d36/Code/ww3d2/texture.cpp
.. _Zero Hour mapper implementation: https://github.com/electronicarts/CnC_Generals_Zero_Hour/blob/0a05454d8574207440a5fb15241b98ad0b435590/GeneralsMD/Code/Libraries/Source/WWVegas/WW3D2/mapper.cpp
