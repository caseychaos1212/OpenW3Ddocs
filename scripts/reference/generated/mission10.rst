Mission10.cpp
=============

* Category: ``mission``
* Active scripts: ``79``
* Source: ``Code/Scripts/Mission10.cpp``

DME_Cinematic_Zone
------------------

DME_Cinematic_Zone in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects.

* Source line: ``2886``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Find_Object``, ``Get_Position``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Start_Timer``, ``Get_Random_Int``
* Summary source: ``heuristic``

M10_Airstrip
------------

M10_Airstrip in Mission10.cpp reacts to destruction state; sends custom events; starts conversations.

* Source line: ``961``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Apache
----------

M10_Apache in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``1342``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Vehicle_Transitions``, ``Enable_Hibernation``, ``Get_Position``, ``Action_Goto``, ``Find_Object``, ``Apply_Damage``, ``Get_Facing``, ``Get_Safe_Flight_Height``
* Summary source: ``heuristic``

Parameter Description::

   Area:int

M10_Apache_Controller
---------------------

M10_Apache_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1182``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Create_Object``, ``Find_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Start_Timer``, ``Enable_Engine``
* Summary source: ``heuristic``

M10_Cargo_Plane_Dropoff
-----------------------

M10_Cargo_Plane_Dropoff in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1888``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Find_Object``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_ID``, ``Start_Timer``
* Summary source: ``heuristic``

M10_Chinook_ParaDrop
--------------------

M10_Chinook_ParaDrop in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; plays sounds.

* Source line: ``1683``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Model``, ``Set_Facing``, ``Set_Animation``, ``Attach_To_Object_Bone``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string

M10_ComCenter_Spawn_Zones
-------------------------

M10_ComCenter_Spawn_Zones in Mission10.cpp watches enter or exit events.

* Source line: ``2277``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Zone_Number:int

M10_Comm_Center
---------------

M10_Comm_Center in Mission10.cpp reacts to destruction state; sends custom events; creates or destroys objects; changes inventory or weapons; starts conversations.

* Source line: ``889``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Enable_Radar``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Con_Yard
------------

M10_Con_Yard in Mission10.cpp reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``753``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Con_Yard_Repair
-------------------

M10_Con_Yard_Repair in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``4208``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Health``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   RepairSpeed=1:float

M10_Conversation_Zone
---------------------

M10_Conversation_Zone in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; starts conversations.

* Source line: ``3462``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Start_Timer``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Get_Health``
* Summary source: ``heuristic``

Parameter Description::

   Conv_Num:int

M10_ConYard_Key_Grant
---------------------

M10_ConYard_Key_Grant in Mission10.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``2744``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M10_Destroy_Self
----------------

M10_Destroy_Self in Mission10.cpp responds to custom events; creates or destroys objects.

* Source line: ``1174``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M10_Destroyed_Turret
--------------------

M10_Destroyed_Turret in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; plays sounds.

* Source line: ``1161``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_2D_Sound``
* Summary source: ``heuristic``

M10_Flyover_Controller
----------------------

M10_Flyover_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3371``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_Random``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M10_Gate_Check
--------------

M10_Gate_Check in Mission10.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; starts conversations.

* Source line: ``2637``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Has_Key``, ``Static_Anim_Phys_Goto_Last_Frame``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Objective:int, Gate1:int, Gate2:int

M10_Gate_Test
-------------

M10_Gate_Test in Mission10.cpp handles player poke interaction.

* Source line: ``2333``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Last_Frame``
* Summary source: ``heuristic``

M10_GDI_Reinforcement
---------------------

M10_GDI_Reinforcement in Mission10.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``2546``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Find_Object``, ``Get_Facing``, ``Get_Position``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M10_GDI_Reinforcement_Waypath
-----------------------------

M10_GDI_Reinforcement_Waypath in Mission10.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``2526``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Hand_Of_Nod
---------------

M10_Hand_Of_Nod in Mission10.cpp reacts to destruction state; sends custom events; starts conversations.

* Source line: ``917``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Havoc_Script
----------------

M10_Havoc_Script in Mission10.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; changes inventory or weapons.

* Source line: ``614``
* Event hooks: ``Created``, ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Helipad_Destroyed
---------------------

M10_Helipad_Destroyed in Mission10.cpp reacts to destruction state; sends custom events; starts conversations.

* Source line: ``3991``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   PadNumber:int

M10_Helipad_Killed
------------------

M10_Helipad_Killed in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``2842``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Holograph_EntryZone2_DME
----------------------------

M10_Holograph_EntryZone2_DME in Mission10.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4646``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M10_Holograph_EntryZone_DME
---------------------------

M10_Holograph_EntryZone_DME in Mission10.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4599``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object_At_Bone``, ``Attach_To_Object_Bone``, ``Disable_All_Collisions``, ``Set_Facing``, ``Get_Facing``
* Summary source: ``heuristic``

M10_Home_Point
--------------

M10_Home_Point in Mission10.cpp initializes behavior when the object is created.

* Source line: ``2134``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Radius=5.0:float

M10_Hon_Killed
--------------

M10_Hon_Killed in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``2830``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_HON_KillPrevention
----------------------

M10_HON_KillPrevention in Mission10.cpp reacts to destruction state.

* Source line: ``4377``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``
* Summary source: ``heuristic``

M10_HON_Spawn_Zones
-------------------

M10_HON_Spawn_Zones in Mission10.cpp watches enter or exit events.

* Source line: ``2142``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Zone_Number:int

M10_Humm_SAMIgnore
------------------

M10_Humm_SAMIgnore in Mission10.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``4164``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``
* Summary source: ``heuristic``

M10_Ion_Cannon
--------------

M10_Ion_Cannon in Mission10.cpp responds to custom events; sends custom events.

* Source line: ``602``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M10_Ion_Cannon_Detector
-----------------------

M10_Ion_Cannon_Detector in Mission10.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``2016``
* Event hooks: ``Created``, ``Damaged``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Set_Is_Rendered``, ``Enable_Hibernation``, ``Disable_All_Collisions``, ``Set_Health``, ``Get_Max_Health``, ``Find_Object``, ``Get_Position``, ``Get_Distance``
* Summary source: ``heuristic``

M10_KaneHead2_DME
-----------------

M10_KaneHead2_DME in Mission10.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``4741``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation_Facing``, ``Get_ID``, ``Start_Conversation``, ``Monitor_Conversation``, ``Debug_Message``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M10_KaneHead_DME
----------------

M10_KaneHead_DME in Mission10.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``4692``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation_Facing``, ``Get_ID``, ``Start_Conversation``, ``Monitor_Conversation``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M10_Light_Tank
--------------

M10_Light_Tank in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1972``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Attack``, ``Modify_Action``
* Summary source: ``heuristic``

M10_Lv2_KeyCarrier
------------------

M10_Lv2_KeyCarrier in Mission10.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``4589``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M10_Mammoth_Activate_Zone
-------------------------

M10_Mammoth_Activate_Zone in Mission10.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2448``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Mammoth_Attack
------------------

M10_Mammoth_Attack in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``2341``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Start_Timer``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M10_Mammoth_Grant_Controller
----------------------------

M10_Mammoth_Grant_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``2766``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Attach_Script``, ``Set_Health``
* Summary source: ``heuristic``

M10_Mammoth_Target_Destruction
------------------------------

M10_Mammoth_Target_Destruction in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``2439``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Target_Number:int

M10_Mrls_Grant
--------------

M10_Mrls_Grant in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; uses timers; creates or destroys objects.

* Source line: ``4052``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Create_Logical_Sound``, ``Get_Position``, ``Find_Object``, ``Start_Timer``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M10_Mrls_Waypath
----------------

M10_Mrls_Waypath in Mission10.cpp initializes behavior when the object is created; drives AI action commands; sends custom events.

* Source line: ``4145``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``, ``Action_Goto``
* Summary source: ``heuristic``

M10_NBase_Attacked
------------------

M10_NBase_Attacked in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; starts conversations.

* Source line: ``4486``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Start_Timer``
* Summary source: ``heuristic``

M10_NBase_Damage_Modifier
-------------------------

M10_NBase_Damage_Modifier in Mission10.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``4524``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float

M10_No_More_Parachute
---------------------

M10_No_More_Parachute in Mission10.cpp reacts to destruction state; plays sounds.

* Source line: ``1854``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``
* Summary source: ``heuristic``

M10_Nod_Obelisk
---------------

M10_Nod_Obelisk in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``3235``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Disable_All_Collisions``, ``Set_Player_Type``, ``Set_Is_Rendered``, ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Destroy_Object``
* Summary source: ``heuristic``

M10_Obelisk
-----------

M10_Obelisk in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``1042``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Set_Health``, ``Start_Timer``, ``Set_Building_Power``
* Summary source: ``heuristic``

M10_Obelisk_MCT
---------------

M10_Obelisk_MCT in Mission10.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events.

* Source line: ``3315``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Is_Rendered``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Objective_Controller
------------------------

M10_Objective_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``42``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Num_Tertiary_Objectives``, ``Start_Timer``, ``Add_Objective``, ``Set_Objective_HUD_Info``, ``Find_Object``, ``Set_Objective_Radar_Blip_Object``, ``Set_Objective_HUD_Info_Position``, ``Get_Position``
* Summary source: ``heuristic``

M10_Occupied
------------

M10_Occupied in Mission10.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``4177``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``
* Summary source: ``heuristic``

M10_Playertype_Nod
------------------

M10_Playertype_Nod in Mission10.cpp initializes behavior when the object is created.

* Source line: ``3363``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``
* Summary source: ``heuristic``

M10_Pokeable_Item_OnePoke
-------------------------

M10_Pokeable_Item_OnePoke in Mission10.cpp initializes behavior when the object is created; handles player poke interaction.

* Source line: ``4301``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``
* Summary source: ``heuristic``

M10_Power_Plant
---------------

M10_Power_Plant in Mission10.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``680``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Find_Object``, ``Set_Building_Power``, ``Send_Custom_Event``, ``Enable_Radar``, ``Destroy_Object``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M10_PowerPlant_Spawn_Zones
--------------------------

M10_PowerPlant_Spawn_Zones in Mission10.cpp watches enter or exit events.

* Source line: ``2241``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Zone_Number:int

M10_Radar_Scramble
------------------

M10_Radar_Scramble in Mission10.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``4327``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Enable_Radar``
* Summary source: ``heuristic``

M10_Radar_UnScramble
--------------------

M10_Radar_UnScramble in Mission10.cpp watches enter or exit events.

* Source line: ``4369``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Radar``
* Summary source: ``heuristic``

M10_Refinery
------------

M10_Refinery in Mission10.cpp reacts to destruction state; sends custom events; starts conversations.

* Source line: ``939``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Refinery_Key_Grant
----------------------

M10_Refinery_Key_Grant in Mission10.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``2623``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Set_Objective_Radar_Blip_Object``
* Summary source: ``heuristic``

M10_Refinery_Keycard
--------------------

M10_Refinery_Keycard in Mission10.cpp responds to custom events; sends custom events.

* Source line: ``3347``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M10_Refinery_Spawn_Zones
------------------------

M10_Refinery_Spawn_Zones in Mission10.cpp watches enter or exit events.

* Source line: ``2191``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Zone_Number:int

M10_Reinforcement_Chinook
-------------------------

M10_Reinforcement_Chinook in Mission10.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; plays sounds.

* Source line: ``1862``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``, ``Find_Object``, ``Send_Custom_Event``, ``Stop_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M10_Reinforcement_Controller
----------------------------

M10_Reinforcement_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``1563``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M10_Sam_Killed
--------------

M10_Sam_Killed in Mission10.cpp reacts to destruction state; sends custom events; updates objectives.

* Source line: ``3938``
* Event hooks: ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Set_Objective_Status``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   SamNumber:int

M10_SAM_Reinforce
-----------------

M10_SAM_Reinforce in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``2615``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Silo
--------

M10_Silo in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``984``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M10_Silo_Controller
-------------------

M10_Silo_Controller in Mission10.cpp initializes behavior when the object is created; responds to custom events; sends custom events; updates objectives; starts conversations.

* Source line: ``996``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Set_Objective_Status``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_SoldierPoke
---------------

M10_SoldierPoke in Mission10.cpp initializes behavior when the object is created; handles player poke interaction; starts conversations.

* Source line: ``4388``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M10_Spacecraft_Check
--------------------

M10_Spacecraft_Check in Mission10.cpp handles player poke interaction.

* Source line: ``2755``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Static_Anim_Phys_Goto_Last_Frame``
* Summary source: ``heuristic``

M10_Ssm_Trigger
---------------

M10_Ssm_Trigger in Mission10.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4276``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M10_Stationary
--------------

M10_Stationary in Mission10.cpp initializes behavior when the object is created.

* Source line: ``2477``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M10_Stealth
-----------

M10_Stealth in Mission10.cpp initializes behavior when the object is created.

* Source line: ``2126``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Stealth``
* Summary source: ``heuristic``

M10_Stealth_Attack_01
---------------------

M10_Stealth_Attack_01 in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``2977``
* Event hooks: ``Created``, ``Killed``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Start_Timer``, ``Debug_Message``, ``Get_Position``, ``Find_Object``, ``Modify_Action``, ``Send_Custom_Event``, ``Get_Distance``
* Summary source: ``heuristic``

M10_Stealth_Attack_02
---------------------

M10_Stealth_Attack_02 in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``3104``
* Event hooks: ``Created``, ``Killed``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Enable_Stealth``, ``Start_Timer``, ``Action_Attack``, ``Send_Custom_Event``, ``Find_Object``, ``Debug_Message``, ``Get_Position``
* Summary source: ``heuristic``

M10_Stealth_Drop
----------------

M10_Stealth_Drop in Mission10.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; creates or destroys objects.

* Source line: ``2850``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Stealth``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Destroy_Object``
* Summary source: ``heuristic``

M10_TestStealth
---------------

M10_TestStealth in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; changes innate AI behavior.

* Source line: ``2486``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Random``, ``Start_Timer``, ``Enable_Stealth``, ``Debug_Message``
* Summary source: ``heuristic``

M10_Turret
----------

M10_Turret in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``1129``
* Event hooks: ``Created``, ``Killed``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M10_Turret_Killed
-----------------

M10_Turret_Killed in Mission10.cpp reacts to destruction state; sends custom events.

* Source line: ``4041``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M10_Turret_Tank
---------------

M10_Turret_Tank in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``644``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``
* Summary source: ``heuristic``

Parameter Description::

   CheckBlocked=1:int

M10_Vehicle_Attack_02
---------------------

M10_Vehicle_Attack_02 in Mission10.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``2060``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Get_Distance``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``
