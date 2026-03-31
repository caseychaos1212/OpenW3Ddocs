Toolkit_Sounds.cpp
==================

* Category: ``toolkit``
* Active scripts: ``11``
* Source: ``Code/Scripts/Toolkit_Sounds.cpp``

M00_BuildingStateSoundController
--------------------------------

M00_BuildingStateSoundController in Toolkit_Sounds.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``920``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   BuildingSpeaker_ID:int

M00_BuildingStateSoundSpeaker
-----------------------------

Building State Sound System - Plays sounds at a simple object location. Requires Building controller ID to switch sound from normal to destroyed state.

* Source line: ``772``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_ID``, ``Attach_Script``, ``Get_Random``, ``Start_Timer``, ``Get_Position``, ``Debug_Message``, ``Create_Sound``
* Summary source: ``source comment``

Parameter Description::

   3,Offset_Randomness_Destroyed:vector3,Frequency_Min_Destroyed=-1:float,Frequency_Max_Destroyed:float, 
   Explosion_Name:string

Source Notes::

   Building State Sound System - Plays sounds at a simple object location.  Requires Building
   controller ID to switch sound from normal to destroyed state.

   Requires one script attached to the speaker object and the ID of the building controller.
   On Created, the speaker finds the building controller and attaches a script with the speaker's
   ID as a param.  The script attached to the building sends a custom back to each individual
   speaker on events.

   There is a one-to-one ratio of scripts attached to the building controller and speakers
   placed for the building.

M00_Sound_Building_Ambient_RAD
------------------------------

This script handles all ambient sound effects for standard buildings. It is placed on an object that is located where the Master Control Terminal for the building is. For those

* Source line: ``608``
* Event hooks: none detected
* Persistence hooks: none detected
* Key engine calls: none detected
* Summary source: ``source comment``

Parameter Description::

   Building_ID=0:int, Building_Type=0:int, Building Facing=0:int

Source Notes::

   M00_Sound_Building_Ambient_RAD

     This script handles all ambient sound effects for standard buildings. It is placed on an
     object that is located where the Master Control Terminal for the building is. For those
     buildings with no MCT, the object is located at the approximate center of the building
     (this mainly applies to the Guard Tower and Tiberium Silo).

     When the script is created, the building is assumed to start at full power. We can adjust
     this later through other means - this script is only reactive, meaning its output only
     plays sound effects and does not control other objects.

     When a building is active, all sound effects for the building are played normally at
     appropriate positions. Some may be on a timer basis, which is also handled here.

     When a building is destroyed, the main ambient sounds are deactivated, and the power-down
     sound sequence is played. This is another set of sounds played at preset locations.

     When the power-down sequence completes, the power-down sound effects are deactivated and
     the destroyed building sound effects commence, if the building is destroyed and has not
     merely lost power.

     When the building is repaired, the destroyed building sound effects cease, and a power-up
     sequence is played.

     When the power-up sequence completes, the power-up sound effects are stopped, and the
     standard ambient sounds are reinstated.

     When the building loses power, the power-down sound effects are played, and all power-loss
     sounds are started.

     In essence, there are several points throughout each building where standard sounds will
     be played. Each location plays one sound at a time, and may or may not loop.


     Parameters:

     Building_ID =		Which building this script is associated with.
     Building_Type =	A number indicating which type of building this is.
     Building_Facing = Which cardinal direction the building is facing.

     Building Type Numbers:

     01 = NOD Tiberium Refinery
     02 = NOD Communications Center
     03 = NOD Power Plant
     04 = NOD Airfield
     05 = NOD Construction Yard
     06 = NOD Guard Tower
     07 = NOD Hand of Nod
     08 = NOD Landing Pad
     09 = NOD Obelisk of Light
     10 = NOD Repair Facility
     11 = NOD Tiberium Silo

     21 = GDI Tiberium Refinery
     22 = GDI Communications Center
     23 = GDI Power Plant
     24 = GDI Weapons Factory
     25 = GDI Construction Yard
     26 = GDI Guard Tower
     27 = GDI Infantry Barracks
     28 = GDI Landing Pad
     29 = GDI Advanced Guard Tower
     30 = GDI Repair Facility
     31 = GDI Tiberium Silo

     Cardinal Direction Numbers:

     0 = North
     1 = East
     2 = South
     3 = West

M00_Sound_Play_2D_RAD
---------------------

Plays a configured 2D sound immediately or in response to a custom event, with optional repeats and delays.

* Source line: ``79``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``
* Summary source: ``manual``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Sound_Effect:string, Play_Count=1:int, Sound_Delay_Min=0.1:float, Sound_Delay_Max=0.1:float, 
   Debug_Mode=0:int

Source Notes::

   M00_Sound_Play_2D_RAD

     Play a 2D sound one or more times, with a delay factor in between.

     Parameters:

     Sound_Effect		= The 2D sound effect to play.
     Play_Count		= How many times the sound should play.
     Sound_Delay_Min	= The minimum wait before playing the sound.
     Sound_Delay_Max	= The maximum wait before playing the sound.

M00_Sound_Play_3D_At_Bone_RMV
-----------------------------

Play a 3D sound one or more times, with a delay factor in between, on an object.

* Source line: ``433``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Get_Bone_Position``, ``Get_Random``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Object_ID:int, 
   Bone_Name:string, Sound_Effect:string, Play_Count=1:int, Sound_Delay_Min=0.1:float, 
   Sound_Delay_Max=0.1:float, Debug_Mode=0:int

Source Notes::

   M00_Sound_Play_3D_At_Bone_RMV

     Play a 3D sound one or more times, with a delay factor in between, on an object.

     Parameters:

     Object_ID			= The ID of the object to play the sound on.
     Bone_Name			= The bone at which to play the sound.
     Sound_Effect		= The sound effect to play.
     Play_Count		= The number of times to play the sound.
     Sound_Delay_Min	= The minimum delay before playing the sound.
     Sound_Delay_Max	= The maximum delay before playing the sound.

M00_Sound_Play_3D_At_Location_RMV
---------------------------------

Play a 3D sound one or more times, with a delay factor in between, at this location.

* Source line: ``331``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Sound_Effect:string, Play_Count=1:int, Sound_Delay_Min=0.1:float, Sound_Delay_Max=0.1:float, 
   Origin:vector3, Debug_Mode=0:int

Source Notes::

   M00_Sound_Play_3D_At_Location_RMV

     Play a 3D sound one or more times, with a delay factor in between, at this location.

     Parameters:

     Sound_Effect		= The sound effect to be played.
     Play_Count		= The number of times to play the sound.
     Sound_Delay_Min	= The minimum delay before playing the sound.
     Sound_Delay_Max	= The maximum delay before playing the sound.
     Origin			= The Vector3 coordinate to play the sound at.

M00_Sound_Play_3D_On_Object_RAD
-------------------------------

Play a 3D sound one or more times, with a delay factor in between, on an object.

* Source line: ``185``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Get_Position``, ``Get_Random``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Object_ID:int, 
   Sound_Effect:string, Play_Count=1:int, Sound_Delay_Min=0.1:float, Sound_Delay_Max=0.1:float, 
   Debug_Mode=0:int

Source Notes::

   M00_Sound_Play_3D_On_Object_RAD

     Play a 3D sound one or more times, with a delay factor in between, on an object.

     Parameters:

     Object_ID			= The ID of the object to play the sound on.
     Sound_Effect		= The sound effect to play.
     Play_Count		= The number of times to play this effect.
     Sound_Delay_Min	= The minimum delay until the sound is played.
     Sound_Delay_Max	= The maximum delay until the sound is played.

     Special Information:

     Object_ID of 0	= Play on self.
     Play_Count of 0	= Play an endless loop.

RMV_Audio_Sound_Player_Preset
-----------------------------

RMV_Audio_Sound_Player_Preset in Toolkit_Sounds.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``689``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Preset_Name:string, Custom_Type=0:int, Custom_Param=0:int, Sound_Origin:vector3

RMV_Audio_Sound_Player_WAV
--------------------------

RMV_Audio_Sound_Player_WAV in Toolkit_Sounds.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``659``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_WAV_Sound_At_Bone``, ``Create_2D_WAV_Sound``
* Summary source: ``heuristic``

Parameter Description::

   WAV_File:string, Is_3D=1:int, Custom_Type=0:int, Custom_Param=0:int

RMV_Audio_Timer_Delay
---------------------

RMV_Audio_Timer_Delay in Toolkit_Sounds.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``613``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Start_Timer``, ``Get_Random``
* Summary source: ``heuristic``

Parameter Description::

   Target_ID:int, Custom_Type=0:int, Custom_Param=0:int, Delay_Min=0.0:float, Delay_Max=0.0:float, 
   Timer_ID=0:int, Repeat=1:int, Randomize_Each_Time=1:int

RMV_Sound_Play_Near_Player
--------------------------

RMV_Sound_Play_Near_Player in Toolkit_Sounds.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``712``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Get_Position``, ``Get_Random``, ``Create_Sound``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Receive_Type:int, Receive_Param:int, Max_Offset:vector3, Sound_Preset:string, Frequency_Min:float, 
   Frequency_Max=0.0:float
