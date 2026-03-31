Test_RMV.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``19``
* Source: ``Code/Scripts/Test_RMV.cpp``

M00_C130_Dropoff_RMV
--------------------

M00_C130_Dropoff_RMV in Test_RMV.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; creates or destroys objects; controls animation playback.

* Source line: ``56``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Start_Timer``, ``Create_Explosion_At_Bone``, ``Create_Object_At_Bone``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   ObjToCreate=:string

M00_Commando_Death_Taunt
------------------------

M00_Commando_Death_Taunt in Test_RMV.cpp reacts to destruction state.

* Source line: ``94``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Get_Random``, ``Create_Sound``
* Summary source: ``heuristic``

M00_Damaged_Warning
-------------------

M00_Damaged_Warning in Test_RMV.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``116``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Create_Sound``, ``Set_Display_Color``, ``Display_Text``, ``Start_Timer``
* Summary source: ``heuristic``

M00_Destroyed_Turret
--------------------

M00_Destroyed_Turret in Test_RMV.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``466``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

M00_Ion_Cannon_Sound
--------------------

M00_Ion_Cannon_Sound in Test_RMV.cpp initializes behavior when the object is created.

* Source line: ``603``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Number=0:int

M00_Put_Script_On_Commando
--------------------------

M00_Put_Script_On_Commando in Test_RMV.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``149``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_A_Star``, ``Get_Position``, ``Attach_Script``
* Summary source: ``heuristic``

Poke_And_Play_Cinematic
-----------------------

Poke_And_Play_Cinematic in Test_RMV.cpp handles player poke interaction; creates or destroys objects.

* Source line: ``592``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Text_File:string, Location=0 0 0:vector3

RMV_Camera_Behavior
-------------------

RMV_Camera_Behavior in Test_RMV.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``229``
* Event hooks: ``Created``, ``Killed``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Get_Position``, ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``, ``Stop_Sound``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Angle:float, Alarm_ID=0:int, Is_Gun=0:int, Delay=0.0:float

RMV_Cinematic_Position
----------------------

RMV_Cinematic_Position in Test_RMV.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``447``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Bone_Position``, ``Debug_Message``
* Summary source: ``heuristic``

Parameter Description::

   Bone:string

RMV_Engine_Sound
----------------

RMV_Engine_Sound in Test_RMV.cpp initializes behavior when the object is created; reacts to destruction state; plays sounds.

* Source line: ``477``
* Event hooks: ``Created``, ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``, ``Stop_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string, Bone:string

RMV_Home_Point
--------------

RMV_Home_Point in Test_RMV.cpp initializes behavior when the object is created.

* Source line: ``209``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Radius:float

RMV_Hostage_Rescue_Point
------------------------

RMV_Hostage_Rescue_Point in Test_RMV.cpp watches enter or exit events; sends custom events.

* Source line: ``184``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``
* Summary source: ``heuristic``

RMV_Test_Damage
---------------

RMV_Test_Damage in Test_RMV.cpp initializes behavior when the object is created; handles player poke interaction.

* Source line: ``626``
* Event hooks: ``Created``, ``Damaged``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Shield_Strength``, ``Get_Max_Health``, ``Get_Health``, ``Set_Health``, ``Debug_Message``, ``Set_Shield_Strength``
* Summary source: ``heuristic``

RMV_Test_Facing
---------------

RMV_Test_Facing in Test_RMV.cpp implements script callbacks.

* Source line: ``217``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Facing``
* Summary source: ``heuristic``

RMV_Test_Script
---------------

RMV_Test_Script in Test_RMV.cpp implements script callbacks.

* Source line: ``48``
* Event hooks: ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``
* Summary source: ``heuristic``

RMV_Test_Stealth
----------------

RMV_Test_Stealth in Test_RMV.cpp initializes behavior when the object is created.

* Source line: ``666``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Stealth``
* Summary source: ``heuristic``

RMV_Transport_Evac
------------------

RMV_Transport_Evac in Test_RMV.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback.

* Source line: ``499``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Get_Position``, ``Set_Model``, ``Set_Facing``, ``Get_Facing``, ``Set_Animation``, ``Attach_To_Object_Bone``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Number:int, Nod=0:int

RMV_Trigger_Killed
------------------

RMV_Trigger_Killed in Test_RMV.cpp reacts to destruction state; sends custom events.

* Source line: ``195``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   ID:int, Type:int, Param:int

RMV_Trigger_Poked_2
-------------------

RMV_Trigger_Poked_2 in Test_RMV.cpp handles player poke interaction; sends custom events; creates or destroys objects.

* Source line: ``613``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Target:int, Type:int, Param:int
