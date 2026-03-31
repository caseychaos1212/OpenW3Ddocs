Test_DLS.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``58``
* Source: ``Code/Scripts/Test_DLS.cpp``

DLS_ActionComplete_Test
-----------------------

DLS_ActionComplete_Test in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1381``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Debug_Message``
* Summary source: ``heuristic``

DLS_Artillery_Test
------------------

DLS_Artillery_Test in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``1401``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``
* Summary source: ``heuristic``

DLS_Blink
---------

DLS_Blink in Test_DLS.cpp initializes behavior when the object is created; creates or destroys objects.

* Source line: ``1662``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

DLS_Camera_Test
---------------

DLS_Camera_Test in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``171``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Find_Object``, ``Action_Attack``, ``Start_Timer``, ``Get_ID``, ``Create_Sound``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Pan_Loc1_ID=0:int, Pan_Loc2_ID=0:int, Debug_Mode=0:int

DLS_Cargo_Plane_Test
--------------------

DLS_Cargo_Plane_Test in Test_DLS.cpp creates or destroys objects.

* Source line: ``943``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Get_Position``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

DLS_Cinematic_Test
------------------

DLS_Cinematic_Test in Test_DLS.cpp initializes behavior when the object is created; sends custom events; creates or destroys objects.

* Source line: ``1434``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Set_Model``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

DLS_Cinematic_Test2
-------------------

DLS_Cinematic_Test2 in Test_DLS.cpp initializes behavior when the object is created; sends custom events; creates or destroys objects.

* Source line: ``1498``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Spawner``
* Summary source: ``heuristic``

DLS_CNC_Sound
-------------

DLS_CNC_Sound in Test_DLS.cpp implements script callbacks.

* Source line: ``1245``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Box_ID:int

DLS_Created_Too_Early
---------------------

DLS_Created_Too_Early in Test_DLS.cpp initializes behavior when the object is created; creates or destroys objects.

* Source line: ``1644``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

DLS_Drop_Unit
-------------

DLS_Drop_Unit in Test_DLS.cpp creates or destroys objects.

* Source line: ``1215``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Box_ID:int

DLS_Filing_Cabinet
------------------

DLS_Filing_Cabinet in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; creates explosions; controls animation playback.

* Source line: ``481``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Get_Health``, ``Get_Max_Health``, ``Start_Timer``, ``Create_Explosion``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Flame_Tank_Test
-------------------

DLS_Flame_Tank_Test in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``874``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

DLS_Goto_Unit
-------------

DLS_Goto_Unit in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1326``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Goto``
* Summary source: ``heuristic``

DLS_Gun_Test
------------

DLS_Gun_Test in Test_DLS.cpp responds to custom events; drives AI action commands.

* Source line: ``292``
* Event hooks: ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Innate_Disable
------------------

DLS_Innate_Disable in Test_DLS.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``1728``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``
* Summary source: ``heuristic``

DLS_Innate_Force_State
----------------------

DLS_Innate_Force_State in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``897``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Position``, ``Action_Reset``, ``Innate_Force_State_Footsteps_Heard``, ``Debug_Message``, ``Innate_Force_State_Bullet_Heard``, ``Innate_Force_State_Gunshots_Heard``, ``Innate_Force_State_Enemy_Seen``
* Summary source: ``heuristic``

DLS_InnateIsStationary_Test
---------------------------

DLS_InnateIsStationary_Test in Test_DLS.cpp initializes behavior when the object is created; handles player poke interaction; drives AI action commands.

* Source line: ``137``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``
* Summary source: ``heuristic``

DLS_Invulnerable_Test
---------------------

DLS_Invulnerable_Test in Test_DLS.cpp initializes behavior when the object is created.

* Source line: ``113``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Apply_Damage``
* Summary source: ``heuristic``

DLS_Math
--------

DLS_Math in Test_DLS.cpp initializes behavior when the object is created.

* Source line: ``1680``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Debug_Message``
* Summary source: ``heuristic``

DLS_No_Innate
-------------

DLS_No_Innate in Test_DLS.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``1369``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``
* Summary source: ``heuristic``

DLS_Playertype
--------------

DLS_Playertype in Test_DLS.cpp initializes behavior when the object is created; handles player poke interaction; changes inventory or weapons.

* Source line: ``1352``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Give_PowerUp``
* Summary source: ``heuristic``

DLS_Rappelling_Activate
-----------------------

DLS_Rappelling_Activate in Test_DLS.cpp creates or destroys objects.

* Source line: ``366``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Spawn_Engineer
------------------

DLS_Spawn_Engineer in Test_DLS.cpp implements script callbacks.

* Source line: ``1258``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Get_Max_Health``, ``Enable_Spawner``
* Summary source: ``heuristic``

DLS_Spawn_Engineer2
-------------------

DLS_Spawn_Engineer2 in Test_DLS.cpp implements script callbacks.

* Source line: ``1272``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Get_Max_Health``, ``Enable_Spawner``
* Summary source: ``heuristic``

DLS_Spawner
-----------

DLS_Spawner in Test_DLS.cpp initializes behavior when the object is created.

* Source line: ``55``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Get_ID``
* Summary source: ``heuristic``

DLS_SpawnTest
-------------

DLS_SpawnTest in Test_DLS.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``27``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Is_A_Star``, ``Trigger_Spawner``
* Summary source: ``heuristic``

DLS_SSM_Test
------------

DLS_SSM_Test in Test_DLS.cpp initializes behavior when the object is created; creates or destroys objects; controls animation playback.

* Source line: ``1475``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object_At_Bone``, ``Set_Model``, ``Attach_To_Object_Bone``, ``Get_ID``, ``Set_Animation``, ``Find_Object``
* Summary source: ``heuristic``

DLS_Star_No_Fall
----------------

DLS_Star_No_Fall in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``3228``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Attach_Script``
* Summary source: ``heuristic``

DLS_Tank_Path_Test
------------------

DLS_Tank_Path_Test in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``391``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Test_Apache
---------------

DLS_Test_Apache in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1294``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

DLS_Test_Conversation
---------------------

DLS_Test_Conversation in Test_DLS.cpp initializes behavior when the object is created; handles player poke interaction; starts conversations.

* Source line: ``1162``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Create_Conversation``, ``Join_Conversation``, ``Get_A_Star``, ``Get_Position``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Test_Evac
-------------

DLS_Test_Evac in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands; sends custom events; controls animation playback.

* Source line: ``1693``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Enable_Hibernation``, ``Action_Goto``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

DLS_Test_Flyovers
-----------------

DLS_Test_Flyovers in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``1572``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

DLS_Test_Hand_Over_Head
-----------------------

DLS_Test_Hand_Over_Head in Test_DLS.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``1620``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Action_Play_Animation``
* Summary source: ``heuristic``

DLS_Test_Homepoint
------------------

DLS_Test_Homepoint in Test_DLS.cpp initializes behavior when the object is created.

* Source line: ``1286``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

DLS_Test_NULL
-------------

DLS_Test_NULL in Test_DLS.cpp initializes behavior when the object is created; handles player poke interaction; starts conversations.

* Source line: ``332``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Test_Pickup
---------------

DLS_Test_Pickup in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects.

* Source line: ``800``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Test_Tank
-------------

DLS_Test_Tank in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1310``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

DLS_Test_Zone_Timer
-------------------

DLS_Test_Zone_Timer in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``1190``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Two_Way
-----------

DLS_Two_Way in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``72``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

DLS_Vehicle_Follow
------------------

DLS_Vehicle_Follow in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``442``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Waypath_Test
----------------

DLS_Waypath_Test in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``586``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

DLS_Where_Am_I
--------------

DLS_Where_Am_I in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``1532``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Preset_Name``, ``Debug_Message``, ``Start_Timer``
* Summary source: ``heuristic``

M00_C130_ParaDrop
-----------------

M00_C130_ParaDrop in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; plays sounds.

* Source line: ``963``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Model``, ``Set_Facing``, ``Set_Animation``, ``Attach_To_Object_Bone``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string

M00_Reinforcement_C130
----------------------

M00_Reinforcement_C130 in Test_DLS.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; plays sounds.

* Source line: ``1140``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``, ``Find_Object``, ``Send_Custom_Event``, ``Stop_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M06_Camera_Behavior
-------------------

M06_Camera_Behavior in Test_DLS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``649``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Get_Position``, ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Debug_Message``, ``Action_Reset``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Angle:float

MX0_Area4_Controller_DLS
------------------------

MX0_Area4_Controller_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; plays sounds; starts conversations.

* Source line: ``1789``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Scale_AI_Awareness``, ``Destroy_Object``, ``Find_Object``, ``Start_Timer``, ``Create_Object``, ``Get_Position``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_Area4_Zone_DLS
------------------

MX0_Area4_Zone_DLS in Test_DLS.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2435``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Area=0:int

MX0_Explosive_Barrels_DLS
-------------------------

MX0_Explosive_Barrels_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; creates explosions.

* Source line: ``3261``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Apply_Damage``, ``Create_Explosion``, ``Get_Position``, ``Create_Logical_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Logical_Sound=0:int, Radius:float

MX0_GDI_Killed_DLS
------------------

MX0_GDI_Killed_DLS in Test_DLS.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; creates or destroys objects.

* Source line: ``2786``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Apply_Damage``, ``Create_Object``, ``Get_Position``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_Facing``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

MX0_GDI_Soldier_DLS
-------------------

MX0_GDI_Soldier_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; changes innate AI behavior; starts conversations.

* Source line: ``2843``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Enable_Engine``, ``Get_Position``, ``Find_Object``, ``Action_Attack``, ``Debug_Message``, ``Get_ID``, ``Get_Random_Int``
* Summary source: ``heuristic``

Parameter Description::

   Attack_Loc0=0:int, Attack_Loc1=0:int, Attack_Loc2=0:int, Attack_Loc3=0:int, Speed=1.0:float

MX0_Gun_Emplacement_DLS
-----------------------

MX0_Gun_Emplacement_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``3032``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Left_Point=0:int, Right_Point=0:int

MX0_Nod_Bunker_DLS
------------------

MX0_Nod_Bunker_DLS in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3176``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Attack``
* Summary source: ``heuristic``

MX0_Nod_RocketSoldier_DLS
-------------------------

MX0_Nod_RocketSoldier_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``3090``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Action_Attack``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

Parameter Description::

   Stationary_Point=0:int

MX0_Obelisk_Weapon_DLS
----------------------

MX0_Obelisk_Weapon_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``2583``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Is_Rendered``, ``Enable_Enemy_Seen``, ``Enable_Hibernation``, ``Innate_Enable``, ``Get_Position``, ``Create_Object``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Max_Range=75.0f:float

MX0_Plant_Ion_Beacon_DLS
------------------------

MX0_Plant_Ion_Beacon_DLS in Test_DLS.cpp initializes behavior when the object is created; drives AI action commands; changes inventory or weapons.

* Source line: ``3205``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``, ``Select_Weapon``, ``Get_Position``, ``Action_Attack``
* Summary source: ``heuristic``

MX0_SAM_DLS
-----------

MX0_SAM_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``3147``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

MX0_Vehicle_DLS
---------------

MX0_Vehicle_DLS in Test_DLS.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; starts conversations.

* Source line: ``2464``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Enable_Engine``, ``Get_Position``, ``Find_Object``, ``Action_Attack``, ``Debug_Message``, ``Get_ID``, ``Create_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Attack_Loc0=0:int, Attack_Loc1=0:int, Attack_Loc2=0:int, Attack_Loc3=0:int, Speed=1.0:float
