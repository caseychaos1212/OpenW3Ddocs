Mission09.cpp
=============

* Category: ``mission``
* Active scripts: ``96``
* Source: ``Code/Scripts/Mission09.cpp``

M09_Ambient_Clutter
-------------------

M09_Ambient_Clutter in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates explosions.

* Source line: ``4203``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Get_Random_Int``, ``Get_Position``, ``Create_Sound``, ``Start_Timer``, ``Create_Explosion``, ``Find_Object``
* Summary source: ``heuristic``

M09_Animating_Mutant
--------------------

M09_Animating_Mutant in Mission09.cpp responds to custom events; drives AI action commands.

* Source line: ``696``
* Event hooks: ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Find_Object``, ``Get_Position``, ``Action_Goto``, ``Action_Reset``, ``Set_Facing``, ``Action_Play_Animation``
* Summary source: ``heuristic``

Parameter Description::

   Animation=0:int

M09_Attack_Blocked_False
------------------------

M09_Attack_Blocked_False in Mission09.cpp drives AI action commands.

* Source line: ``4667``
* Event hooks: ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M09_Block_Off
-------------

M09_Block_Off in Mission09.cpp watches enter or exit events; sends custom events.

* Source line: ``3522``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Camera_Activate
-------------------

M09_Camera_Activate in Mission09.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``4575``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Camera0=0:int, Camera1=0:int, Camera2=0:int, Camera3=0:int, Camera4=0:int

M09_CheckpointA_Controller
--------------------------

M09_CheckpointA_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``2257``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_CheckpointA_Counter
-----------------------

M09_CheckpointA_Counter in Mission09.cpp reacts to destruction state; sends custom events.

* Source line: ``2286``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Chinook_ParaDrop
--------------------

M09_Chinook_ParaDrop in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; plays sounds.

* Source line: ``2294``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Model``, ``Set_Facing``, ``Set_Animation``, ``Attach_To_Object_Bone``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string

M09_Containment_Key_1
---------------------

M09_Containment_Key_1 in Mission09.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``2939``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M09_Containment_Key_2
---------------------

M09_Containment_Key_2 in Mission09.cpp responds to custom events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``2959``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M09_Cryo_Mutant_Zone_01
-----------------------

M09_Cryo_Mutant_Zone_01 in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers.

* Source line: ``2830``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Start_Timer``, ``Enable_Spawner``
* Summary source: ``heuristic``

M09_Custom_Attack
-----------------

M09_Custom_Attack in Mission09.cpp responds to custom events; drives AI action commands.

* Source line: ``2779``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M09_Damage_Modifier
-------------------

M09_Damage_Modifier in Mission09.cpp initializes behavior when the object is created.

* Source line: ``3707``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float

M09_Destroy_Self_Zone
---------------------

M09_Destroy_Self_Zone in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``4302``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M09_Destroy_Zone
----------------

M09_Destroy_Zone in Mission09.cpp continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects.

* Source line: ``4626``
* Event hooks: ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Destroy_Object``
* Summary source: ``heuristic``

M09_Elevator_All_Controller
---------------------------

M09_Elevator_All_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``3328``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Static_Anim_Phys_Goto_Last_Frame``, ``Destroy_Object``, ``Send_Custom_Event``, ``Get_ID``, ``Start_Timer``, ``Create_Object``, ``Set_Is_Rendered``
* Summary source: ``heuristic``

Parameter Description::

   Waypoint_num:int, Elev_obj_num:int, Anim_num:int, Direction = 0:int, Mobius_exit_goto:int

M09_Elevator_All_Zone
---------------------

M09_Elevator_All_Zone in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``3288``
* Event hooks: ``Created``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Controller_num:int

M09_Elevator_Exit
-----------------

M09_Elevator_Exit in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4642``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Mobius_exit_goto:int

M09_Elevator_Movement_Zone
--------------------------

M09_Elevator_Movement_Zone in Mission09.cpp watches enter or exit events.

* Source line: ``3255``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Static_Anim_Phys_Goto_Last_Frame``
* Summary source: ``heuristic``

Parameter Description::

   Direction:int, Anim_num:int, Elev_obj_num:int

M09_Entrance_Zone
-----------------

M09_Entrance_Zone in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; drives AI action commands.

* Source line: ``2194``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Attach_Script``, ``Find_Object``, ``Set_Innate_Is_Stationary``, ``Action_Goto``
* Summary source: ``heuristic``

M09_Evac_Bone
-------------

M09_Evac_Bone in Mission09.cpp controls animation playback.

* Source line: ``3951``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``
* Summary source: ``heuristic``

M09_Evac_Helicopter
-------------------

M09_Evac_Helicopter in Mission09.cpp continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; controls animation playback.

* Source line: ``3963``
* Event hooks: ``Killed``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Animation``, ``Mission_Complete``, ``Enable_Collisions``
* Summary source: ``heuristic``

Parameter Description::

   Gunner:int

M09_Evac_Point_Objective
------------------------

M09_Evac_Point_Objective in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; drives AI action commands; uses timers; sends custom events; creates or destroys objects.

* Source line: ``516``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Attach_Script``, ``Start_Timer``, ``Send_Custom_Event``, ``Get_Distance``, ``Get_Position``, ``Get_Facing``, ``Create_Object``
* Summary source: ``heuristic``

M09_Evac_Transport
------------------

M09_Evac_Transport in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects; controls animation playback.

* Source line: ``3895``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Find_Object``, ``Get_Position``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Set_Model``, ``Set_Animation``
* Summary source: ``heuristic``

M09_Excavation_Tunnel_3
-----------------------

M09_Excavation_Tunnel_3 in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2157``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Attach_Script``, ``Find_Object``, ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M09_Excavation_Tunnel_Controller
--------------------------------

M09_Excavation_Tunnel_Controller in Mission09.cpp responds to custom events.

* Source line: ``1943``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

M09_Excavation_Tunnel_Encounter_Off
-----------------------------------

M09_Excavation_Tunnel_Encounter_Off in Mission09.cpp watches enter or exit events; sends custom events.

* Source line: ``1932``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Excavation_Tunnel_Encounter_On
----------------------------------

M09_Excavation_Tunnel_Encounter_On in Mission09.cpp watches enter or exit events; sends custom events.

* Source line: ``1921``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Explosion_Zone_Lab01
------------------------

M09_Explosion_Zone_Lab01 in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects; creates explosions.

* Source line: ``2580``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Start_Timer``, ``Create_Object``
* Summary source: ``heuristic``

M09_Explosion_Zone_Lab02
------------------------

M09_Explosion_Zone_Lab02 in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects; creates explosions.

* Source line: ``2620``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

M09_Explosion_Zone_Tunnel01
---------------------------

M09_Explosion_Zone_Tunnel01 in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``2652``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Explosion``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

M09_First_Mutant_Encounter
--------------------------

M09_First_Mutant_Encounter in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``2530``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M09_First_Mutant_Encounter_Zone
-------------------------------

M09_First_Mutant_Encounter_Zone in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers.

* Source line: ``2483``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Attach_Script``, ``Start_Timer``
* Summary source: ``heuristic``

M09_Flamer_Attack_Zone
----------------------

M09_Flamer_Attack_Zone in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2797``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``
* Summary source: ``heuristic``

M09_Flyover_Controller
----------------------

M09_Flyover_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``3822``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M09_Flyover_Recycle
-------------------

M09_Flyover_Recycle in Mission09.cpp reacts to destruction state; sends custom events.

* Source line: ``3865``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Gunner
----------

M09_Gunner in Mission09.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``3993``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Attach_To_Object_Bone``, ``Enable_Collisions``, ``Find_Object``, ``Action_Goto``, ``Set_Innate_Aggressiveness``, ``Modify_Action``, ``Set_Health``
* Summary source: ``heuristic``

M09_Havoc_Script
----------------

M09_Havoc_Script in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; changes inventory or weapons.

* Source line: ``319``
* Event hooks: ``Created``, ``Destroyed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``, ``Start_Timer``, ``Grant_Key``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Home_Location_10
--------------------

M09_Home_Location_10 in Mission09.cpp initializes behavior when the object is created.

* Source line: ``1467``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

M09_Immobile
------------

M09_Immobile in Mission09.cpp initializes behavior when the object is created; drives AI action commands; changes innate AI behavior.

* Source line: ``2552``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Attack``
* Summary source: ``heuristic``

M09_Innate_Activate
-------------------

M09_Innate_Activate in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4522``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Target0=0:int, Target1=0:int, Target2=0:int, Target3=0:int, Target4=0:int, Target5=0:int, 
   Target6=0:int, Target7=0:int, Target8=0:int, Target9=0:int

M09_Innate_Disable
------------------

M09_Innate_Disable in Mission09.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``4051``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Find_Object``, ``Get_Health``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Innate_Force_State_Gunshots_Heard``, ``Get_Position``, ``Set_Health``
* Summary source: ``heuristic``

M09_Innate_Enable_Zone
----------------------

M09_Innate_Enable_Zone in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers.

* Source line: ``4119``
* Event hooks: ``Created``, ``Sound_Heard``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Create_Logical_Sound``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   SoundProjector:int, Radius=7.0:float, Total_Enemies:int

M09_Invincible_MrShuman
-----------------------

M09_Invincible_MrShuman in Mission09.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``3227``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``
* Summary source: ``heuristic``

M09_Key_Box
-----------

M09_Key_Box in Mission09.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; starts conversations.

* Source line: ``3028``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M09_Key_Controller_Zones
------------------------

M09_Key_Controller_Zones in Mission09.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``2991``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Key_Grant
-------------

M09_Key_Grant in Mission09.cpp handles player poke interaction; creates or destroys objects.

* Source line: ``2895``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M09_KeyCard_Zone
----------------

M09_KeyCard_Zone in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; starts conversations.

* Source line: ``4340``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Start_Timer``, ``Get_Distance``, ``Get_Position``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M09_Lab_Key_Controller
----------------------

M09_Lab_Key_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``2908``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``heuristic``

M09_Lab_Powerup
---------------

M09_Lab_Powerup in Mission09.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``4187``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``, ``Action_Reset``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Target:int

M09_LabRoom_Controller
----------------------

M09_LabRoom_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; starts conversations.

* Source line: ``755``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M09_LabRoom_Zones
-----------------

M09_LabRoom_Zones in Mission09.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; drives AI action commands; sends custom events.

* Source line: ``650``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Reset``, ``Grant_Key``
* Summary source: ``heuristic``

Parameter Description::

   Mutant_Num:int, Mutant_Goto:int

M09_Level10Key
--------------

M09_Level10Key in Mission09.cpp watches enter or exit events.

* Source line: ``4618``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``
* Summary source: ``heuristic``

M09_Mobius_Follow
-----------------

M09_Mobius_Follow in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``911``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Action_Goto``, ``Action_Attack``, ``Send_Custom_Event``, ``Mission_Complete``, ``Get_ID``, ``Action_Reset``
* Summary source: ``heuristic``

M09_Mobius_Goto
---------------

M09_Mobius_Goto in Mission09.cpp watches enter or exit events; sends custom events.

* Source line: ``4041``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   GotoObject:int

M09_Mobius_Initial_Conversation
-------------------------------

M09_Mobius_Initial_Conversation in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes inventory or weapons; changes innate AI behavior; starts conversations.

* Source line: ``799``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Disable``, ``Get_Health``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M09_Mobius_OnFollow
-------------------

M09_Mobius_OnFollow in Mission09.cpp watches enter or exit events; sends custom events.

* Source line: ``4680``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Mobius_Suit_Objective
-------------------------

M09_Mobius_Suit_Objective in Mission09.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; drives AI action commands; sends custom events; creates or destroys objects; controls animation playback; changes inventory or weapons; starts conversations.

* Source line: ``358``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Set_Position``, ``Destroy_Object``, ``Action_Reset``, ``Send_Custom_Event``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

M09_MrShuman_Zone
-----------------

M09_MrShuman_Zone in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3104``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_Distance``, ``Get_Position``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M09_Mutant
----------

M09_Mutant in Mission09.cpp initializes behavior when the object is created.

* Source line: ``2572``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``
* Summary source: ``heuristic``

M09_Mutant_Ambush_Zone_01
-------------------------

M09_Mutant_Ambush_Zone_01 in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``1475``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Attach_Script``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M09_Mutant_Attack
-----------------

M09_Mutant_Attack in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3531``
* Event hooks: ``Created``, ``Sound_Heard``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Get_Facing``, ``Set_Facing``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Target_num:int

M09_Mutant_Damage_Mod_10
------------------------

M09_Mutant_Damage_Mod_10 in Mission09.cpp initializes behavior when the object is created.

* Source line: ``1530``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

M09_Mutant_Damage_Mod_50
------------------------

M09_Mutant_Damage_Mod_50 in Mission09.cpp initializes behavior when the object is created.

* Source line: ``1564``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

M09_Mutant_Encounter_Controller
-------------------------------

M09_Mutant_Encounter_Controller in Mission09.cpp responds to custom events; sends custom events.

* Source line: ``3671``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``heuristic``

M09_Mutant_Excavation_Zone_01
-----------------------------

M09_Mutant_Excavation_Zone_01 in Mission09.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2730``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M09_Mutant_Path_01
------------------

M09_Mutant_Path_01 in Mission09.cpp drives AI action commands.

* Source line: ``2867``
* Event hooks: ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M09_Mutant_Path_02
------------------

M09_Mutant_Path_02 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2881``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M09_No_Obj_Damage
-----------------

M09_No_Obj_Damage in Mission09.cpp initializes behavior when the object is created.

* Source line: ``3802``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

M09_Nod_Damage_Mod_10
---------------------

M09_Nod_Damage_Mod_10 in Mission09.cpp initializes behavior when the object is created.

* Source line: ``1598``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

M09_Objective_Controller
------------------------

M09_Objective_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; updates objectives.

* Source line: ``47``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Num_Tertiary_Objectives``, ``Start_Timer``, ``Enable_Hibernation``, ``Set_Objective_HUD_Info``, ``Add_Objective``, ``Find_Object``, ``Set_Objective_Radar_Blip_Object``, ``Set_Objective_HUD_Info_Position``
* Summary source: ``heuristic``

M09_PSuitAnim
-------------

M09_PSuitAnim in Mission09.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``4688``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``, ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M09_Sam_Controller
------------------

M09_Sam_Controller in Mission09.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``2694``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Sam_Counter
---------------

M09_Sam_Counter in Mission09.cpp reacts to destruction state; sends custom events.

* Source line: ``2686``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Sam_Engineer_1
------------------

M09_Sam_Engineer_1 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1876``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M09_Sam_Engineer_2
------------------

M09_Sam_Engineer_2 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1898``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M09_Scientist_Cower
-------------------

M09_Scientist_Cower in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``4282``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M09_Stationary
--------------

M09_Stationary in Mission09.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; creates or destroys objects.

* Source line: ``1355``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Random_Int``, ``Set_Health``, ``Get_Position``, ``Create_Object``, ``Set_Player_Type``
* Summary source: ``heuristic``

Parameter Description::

   Reward_override=0:int

M09_Stationary_Nod
------------------

M09_Stationary_Nod in Mission09.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; creates or destroys objects.

* Source line: ``1414``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Get_Random_Int``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M09_Stationary_StealthTank
--------------------------

M09_Stationary_StealthTank in Mission09.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``1666``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Destroy_Object``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M09_Stealth_Tank_Pilot
----------------------

M09_Stealth_Tank_Pilot in Mission09.cpp initializes behavior when the object is created; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``1632``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Facing``, ``Innate_Disable``, ``Get_Position``, ``Find_Object``, ``Action_Goto``, ``Destroy_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M09_Surface_Objective
---------------------

M09_Surface_Objective in Mission09.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``472``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M09_Tunnel_Spawner_354
----------------------

M09_Tunnel_Spawner_354 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2066``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M09_Tunnel_Spawner_356
----------------------

M09_Tunnel_Spawner_356 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2086``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M09_Tunnel_Spawner_357
----------------------

M09_Tunnel_Spawner_357 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2045``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Enable_Enemy_Seen``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M09_Tunnel_Spawner_383_381
--------------------------

M09_Tunnel_Spawner_383_381 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2131``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Action_Goto``, ``Debug_Message``, ``Action_Reset``, ``Enable_Enemy_Seen``
* Summary source: ``heuristic``

M09_Tunnel_Spawner_384_382
--------------------------

M09_Tunnel_Spawner_384_382 in Mission09.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2106``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Action_Goto``, ``Debug_Message``, ``Action_Reset``, ``Enable_Enemy_Seen``
* Summary source: ``heuristic``

M09_Unteamed
------------

M09_Unteamed in Mission09.cpp initializes behavior when the object is created.

* Source line: ``2722``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``
* Summary source: ``heuristic``

M09_Vehicle_Attack_01
---------------------

M09_Vehicle_Attack_01 in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1692``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``, ``Get_Position``, ``Get_Distance``, ``Modify_Action``, ``Start_Timer``, ``Action_Reset``
* Summary source: ``heuristic``

M09_Vehicle_Attack_02
---------------------

M09_Vehicle_Attack_02 in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1808``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Get_Distance``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``

M09_Vehicle_Attack_03
---------------------

M09_Vehicle_Attack_03 in Mission09.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1977``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Get_Distance``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``

M09_Waypath_Run
---------------

M09_Waypath_Run in Mission09.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes innate AI behavior.

* Source line: ``3580``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Action_Goto``, ``Action_Reset``, ``Action_Play_Animation``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_num:int, Attacker_num:int, Controller_num:int

M09_Weather_Off
---------------

M09_Weather_Off in Mission09.cpp watches enter or exit events.

* Source line: ``3884``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Fog_Enable``, ``Set_Fog_Range``, ``Set_Lightning``, ``Set_Rain``
* Summary source: ``heuristic``

M09_Weather_On
--------------

M09_Weather_On in Mission09.cpp watches enter or exit events.

* Source line: ``3873``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Fog_Enable``, ``Set_Fog_Range``, ``Set_Lightning``, ``Set_Rain``
* Summary source: ``heuristic``

M09_Zone_Destroy
----------------

M09_Zone_Destroy in Mission09.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``4179``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M09_Zone_Enabled_Mobius
-----------------------

M09_Zone_Enabled_Mobius in Mission09.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3757``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_id:int, Condition=0:int
