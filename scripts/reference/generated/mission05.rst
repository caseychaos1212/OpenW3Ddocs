Mission05.cpp
=============

* Category: ``mission``
* Active scripts: ``111``
* Source: ``Code/Scripts/Mission05.cpp``

M00_InnateIsStationary
----------------------

M00_InnateIsStationary in Mission05.cpp initializes behavior when the object is created.

* Source line: ``6736``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M05_Activate_ApacheStrike
-------------------------

M05_Activate_ApacheStrike in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects.

* Source line: ``7145``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Find_Object``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Strike_Loc_ID=0:int

M05_Activate_Artillery
----------------------

M05_Activate_Artillery in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; creates explosions.

* Source line: ``7031``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Get_Random_Int``, ``Start_Timer``, ``Get_Position``, ``Find_Object``, ``Create_Sound``, ``Monitor_Sound``, ``Get_Random``
* Summary source: ``heuristic``

Parameter Description::

   Artillery_ID1=0:int, Artillery_ID2=0:int, Artillery_ID3=0:int

M05_Activate_Babushka_Encounter
-------------------------------

M05_Activate_Babushka_Encounter in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2594``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Deadeye
--------------------

M05_Activate_Deadeye in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``2509``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Entrapment_Civ
---------------------------

M05_Activate_Entrapment_Civ in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5853``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Spawner``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Activate_Execution
----------------------

M05_Activate_Execution in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``7277``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Nod_Apc
--------------------

M05_Activate_Nod_Apc in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``678``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Nuke_Encounter
---------------------------

M05_Activate_Nuke_Encounter in Mission05.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``3598``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``
* Summary source: ``heuristic``

M05_Activate_Objective_501
--------------------------

M05_Activate_Objective_501 in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``407``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Objective_502
--------------------------

M05_Activate_Objective_502 in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``456``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Get_A_Star``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Objective_504
--------------------------

M05_Activate_Objective_504 in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``513``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Objective_507
--------------------------

M05_Activate_Objective_507 in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``570``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Objective_508
--------------------------

M05_Activate_Objective_508 in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``628``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Activate_Objective_509
--------------------------

M05_Activate_Objective_509 in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``710``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Enable_Spawner``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

M05_Activate_Objective_510
--------------------------

M05_Activate_Objective_510 in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``775``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Get_A_Star``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Activate_Roadblock_Tank
---------------------------

M05_Activate_Roadblock_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects; creates explosions.

* Source line: ``6577``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Start_Timer``, ``Create_Explosion``, ``Get_Position``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_Activate_Surprise
---------------------

M05_Activate_Surprise in Mission05.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``6943``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Spawner_ID1=0:int, Spawner_ID2=0:int, Spawner_ID3=0:int

M05_Activate_Surprise_Tank
--------------------------

M05_Activate_Surprise_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects; creates explosions.

* Source line: ``5666``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Start_Timer``, ``Create_Explosion``, ``Get_Position``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_Activate_Triangle_Tank_Drop
-------------------------------

M05_Activate_Triangle_Tank_Drop in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects.

* Source line: ``7220``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Get_Position``, ``Find_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Activate_Truck_Spill
------------------------

M05_Activate_Truck_Spill in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects.

* Source line: ``7185``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Aggressiveness_Take_Cover
-----------------------------

M05_Aggressiveness_Take_Cover in Mission05.cpp initializes behavior when the object is created.

* Source line: ``7255``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

Parameter Description::

   Aggessiveness=0.0:float, Take_Cover=0.0:float

M05_Alley_Sprint
----------------

M05_Alley_Sprint in Mission05.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5360``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M05_APC_Deploy
--------------

M05_APC_Deploy in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects; controls animation playback.

* Source line: ``7499``
* Event hooks: ``Created``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Set_Animation``, ``Start_Timer``, ``Action_Attack``, ``Get_ID``, ``Create_Object_At_Bone``, ``Attach_To_Object_Bone``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string, Soldier_Qty=0:int, Fire_Gun=1:int

M05_APC_Deploy_Soldier
----------------------

M05_APC_Deploy_Soldier in Mission05.cpp initializes behavior when the object is created; drives AI action commands; controls animation playback.

* Source line: ``7595``
* Event hooks: ``Created``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Enable_Hibernation``, ``Find_Object``, ``Attach_To_Object_Bone``, ``Get_Position``, ``Get_Facing``, ``Get_Random``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   APC_ID=0:int

M05_Apc_Drop_DME
----------------

M05_Apc_Drop_DME in Mission05.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``5569``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M05_Apc_Drop_Zone_DME
---------------------

M05_Apc_Drop_Zone_DME in Mission05.cpp watches enter or exit events; sends custom events.

* Source line: ``5652``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Babushka
------------

M05_Babushka in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; changes inventory or weapons; starts conversations.

* Source line: ``2625``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Set_Player_Type``, ``Set_Innate_Is_Stationary``, ``Action_Play_Animation``, ``Select_Weapon``, ``Is_A_Star``, ``Action_Reset``, ``Give_PowerUp``
* Summary source: ``heuristic``

M05_Babushka_Guard
------------------

M05_Babushka_Guard in Mission05.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; starts conversations.

* Source line: ``2762``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Is_A_Star``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Barrel_Explosion
--------------------

M05_Barrel_Explosion in Mission05.cpp reacts to destruction state; creates explosions.

* Source line: ``7475``
* Event hooks: ``Destroyed``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``
* Summary source: ``heuristic``

M05_Bridge_Tank
---------------

M05_Bridge_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1836``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Action_Attack``, ``Get_Player_Type``
* Summary source: ``heuristic``

M05_Building_Collapse
---------------------

M05_Building_Collapse in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``1637``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Get_ID``, ``Is_A_Star``, ``Debug_Message``, ``Set_Model``, ``Attach_Script``, ``Destroy_Object``, ``Find_Object``
* Summary source: ``heuristic``

M05_Building_Debris
-------------------

M05_Building_Debris in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; creates or destroys objects; creates explosions.

* Source line: ``6623``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Set_Shield_Type``, ``Get_Player_Type``, ``Set_Health``, ``Get_Health``, ``Create_Explosion``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M05_Cache_Assault
-----------------

M05_Cache_Assault in Mission05.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2195``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

M05_Cache_Controller
--------------------

M05_Cache_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``4868``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Get_Distance``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Cache_Escort
----------------

M05_Cache_Escort in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1968``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Send_Custom_Event``, ``Find_Object``, ``Is_A_Star``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Cache_Surprise
------------------

M05_Cache_Surprise in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects.

* Source line: ``6358``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Cache_Unit
--------------

M05_Cache_Unit in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``4967``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

M05_Cathedral_Apache
--------------------

M05_Cathedral_Apache in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``6119``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Action_Attack``, ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Modify_Action``
* Summary source: ``heuristic``

Parameter Description::

   Apache_ID=0:int

M05_Cathedral_Artillery
-----------------------

M05_Cathedral_Artillery in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``7381``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Fire_Loc1=0:int, Fire_Loc2=0:int

M05_Cathedral_Controller
------------------------

M05_Cathedral_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``5987``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Set_Facing``, ``Create_Logical_Sound``, ``Get_Position``
* Summary source: ``heuristic``

M05_Cathedral_Para_Unit
-----------------------

M05_Cathedral_Para_Unit in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``6281``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Get_Distance``, ``Get_Position``, ``Start_Timer``, ``Apply_Damage``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Soldier_ID=0:int

M05_Chateau_Escapee
-------------------

M05_Chateau_Escapee in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``2282``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Animation``, ``Set_Player_Type``, ``Get_Position``, ``Create_Object``, ``Start_Timer``, ``Apply_Damage``
* Summary source: ``heuristic``

M05_Chinook_Supply_Cache
------------------------

M05_Chinook_Supply_Cache in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``2229``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Civ_Lead
------------

M05_Civ_Lead in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; changes innate AI behavior; starts conversations.

* Source line: ``3938``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_HUD_Pokable_Indicator``, ``Innate_Enable``, ``Action_Goto``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M05_Civ_Warn
------------

M05_Civ_Warn in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; changes inventory or weapons; starts conversations.

* Source line: ``3868``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Enable_Hibernation``, ``Give_PowerUp``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Select_Weapon``
* Summary source: ``heuristic``

M05_DataDisc_01_DLS
-------------------

M05_DataDisc_01_DLS in Mission05.cpp responds to custom events.

* Source line: ``7845``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Character``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

M05_Deactivate_Alley_Sprint
---------------------------

M05_Deactivate_Alley_Sprint in Mission05.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``5384``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``
* Summary source: ``heuristic``

M05_DEAD6_Engineer
------------------

M05_DEAD6_Engineer in Mission05.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``832``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Set_Player_Type``, ``Set_Obj_Radar_Blip_Color``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``, ``Find_Object``, ``Is_A_Star``
* Summary source: ``heuristic``

M05_DEAD6_Engineer2
-------------------

M05_DEAD6_Engineer2 in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``921``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``, ``Find_Object``, ``Mission_Complete``, ``Start_Timer``, ``Get_Distance``
* Summary source: ``heuristic``

M05_DEAD6_Grenadier
-------------------

M05_DEAD6_Grenadier in Mission05.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``1419``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Enable_HUD_Pokable_Indicator``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``, ``Find_Object``, ``Mission_Complete``, ``Is_A_Star``
* Summary source: ``heuristic``

M05_Dead6_Help
--------------

M05_Dead6_Help in Mission05.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``6745``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Message_ID=0:int

M05_DEAD6_MiniGunner
--------------------

M05_DEAD6_MiniGunner in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``1205``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Start_Timer``, ``Find_Object``, ``Action_Goto``, ``Send_Custom_Event``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

M05_DEAD6_Rocket_Soldier
------------------------

M05_DEAD6_Rocket_Soldier in Mission05.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1073``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Debug_Message``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``, ``Find_Object``, ``Is_A_Star``, ``Create_Conversation``
* Summary source: ``heuristic``

M05_DEAD6_Rocket_Soldier2
-------------------------

M05_DEAD6_Rocket_Soldier2 in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``995``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Get_Health``, ``Set_Health``, ``Get_Max_Health``, ``Apply_Damage``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Dump_Captives
-----------------

M05_Dump_Captives in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes inventory or weapons.

* Source line: ``5041``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Give_PowerUp``, ``Start_Timer``, ``Get_Random``, ``Get_Position``, ``Select_Weapon``
* Summary source: ``heuristic``

M05_Dump_Controller
-------------------

M05_Dump_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``5157``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Dump_Unit
-------------

M05_Dump_Unit in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``5131``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

M05_Enable_Overlook
-------------------

M05_Enable_Overlook in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1907``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``
* Summary source: ``heuristic``

M05_Entrapment_Mendoza
----------------------

M05_Entrapment_Mendoza in Mission05.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects; starts conversations.

* Source line: ``5901``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Set_Innate_Is_Stationary``, ``Set_Facing``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_Entrapment_Technician
-------------------------

M05_Entrapment_Technician in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; uses timers; starts conversations.

* Source line: ``3643``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Start_Timer``, ``Enable_HUD_Pokable_Indicator``, ``Is_A_Star``
* Summary source: ``heuristic``

M05_Escapee_Brother
-------------------

M05_Escapee_Brother in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; handles player poke interaction; sends custom events; creates or destroys objects; changes inventory or weapons; starts conversations.

* Source line: ``2329``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Give_PowerUp``, ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M05_Escapee_Invaders
--------------------

M05_Escapee_Invaders in Mission05.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2433``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M05_Escapee_Windows
-------------------

M05_Escapee_Windows in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects; creates explosions.

* Source line: ``2454``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Is_Rendered``, ``Find_Object``, ``Action_Attack``, ``Create_Explosion``, ``Get_Position``, ``Start_Timer``, ``Modify_Action``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_Execution_Civilian
----------------------

M05_Execution_Civilian in Mission05.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``5744``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``, ``Set_Player_Type``, ``Innate_Disable``, ``Is_A_Star``, ``Innate_Enable``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M05_Execution_Nod
-----------------

M05_Execution_Nod in Mission05.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``5819``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M05_Explode_Debris
------------------

M05_Explode_Debris in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback.

* Source line: ``6664``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``, ``Set_Animation``, ``Start_Timer``, ``Create_Sound``, ``Get_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_FleeEngineer
----------------

M05_FleeEngineer in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3420``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Find_Object``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_Flyover_Controller
----------------------

M05_Flyover_Controller in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``6699``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Free_Dump_Captives
----------------------

M05_Free_Dump_Captives in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``5006``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Spawner``
* Summary source: ``heuristic``

M05_Free_Overlook_Captives
--------------------------

M05_Free_Overlook_Captives in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4687``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Havoc_DLS
-------------

M05_Havoc_DLS in Mission05.cpp initializes behavior when the object is created; changes inventory or weapons.

* Source line: ``387``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``
* Summary source: ``heuristic``

M05_Heal_Dead6
--------------

M05_Heal_Dead6 in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers.

* Source line: ``2542``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Start_Timer``, ``Apply_Damage``, ``Find_Object``
* Summary source: ``heuristic``

M05_Hotwire_Conversation
------------------------

M05_Hotwire_Conversation in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; starts conversations.

* Source line: ``6907``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M05_Inn_APC
-----------

M05_Inn_APC in Mission05.cpp responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``7644``
* Event hooks: ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Inn_Controller
------------------

M05_Inn_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``5504``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Inn_Tank
------------

M05_Inn_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``5416``
* Event hooks: ``Created``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Action_Attack``, ``Get_Player_Type``
* Summary source: ``heuristic``

M05_Mendoza
-----------

M05_Mendoza in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1531``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Start_Timer``, ``Get_Max_Health``, ``Action_Play_Animation``, ``Destroy_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Find_Object``
* Summary source: ``heuristic``

M05_Mendoza3
------------

M05_Mendoza3 in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects; changes inventory or weapons; starts conversations.

* Source line: ``3504``
* Event hooks: ``Created``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Max_Health``, ``Give_PowerUp``, ``Select_Weapon``, ``Destroy_Object``, ``Get_Health``, ``Set_Health``, ``Create_Conversation``
* Summary source: ``heuristic``

M05_Mendoza4
------------

M05_Mendoza4 in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects; changes inventory or weapons; starts conversations.

* Source line: ``3753``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Action_Attack``, ``Start_Timer``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Nod_APC
-----------

M05_Nod_APC in Mission05.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``4837``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M05_Nod_Bridge_Gun_Emplacement
------------------------------

M05_Nod_Bridge_Gun_Emplacement in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``4534``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``, ``Start_Timer``, ``Enable_Enemy_Seen``, ``Get_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Nod_Gun_Emplacement
-----------------------

M05_Nod_Gun_Emplacement in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``4465``
* Event hooks: ``Created``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Get_Player_Type``
* Summary source: ``heuristic``

M05_Objective_Controller
------------------------

M05_Objective_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``45``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Background_Music``, ``Enable_Hibernation``, ``Start_Timer``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Add_Objective``, ``Find_Object``
* Summary source: ``heuristic``

M05_Overlook_Captives
---------------------

M05_Overlook_Captives in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes inventory or weapons.

* Source line: ``4622``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Goto``, ``Give_PowerUp``, ``Start_Timer``, ``Select_Weapon``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Overlook_Civ
----------------

M05_Overlook_Civ in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands.

* Source line: ``4811``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

M05_Overlook_Controller
-----------------------

M05_Overlook_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``4718``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Overlook_Nod
----------------

M05_Overlook_Nod in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4785``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_Park_Activate
-----------------

M05_Park_Activate in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``2823``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Park_Apache
---------------

M05_Park_Apache in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``3031``
* Event hooks: ``Created``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``, ``Enable_Enemy_Seen``, ``Innate_Force_State_Enemy_Seen``, ``Modify_Action``, ``Start_Timer``
* Summary source: ``heuristic``

M05_Park_Buggy
--------------

M05_Park_Buggy in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``3168``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Innate_Force_State_Enemy_Seen``, ``Get_Player_Type``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Park_Controller
-------------------

M05_Park_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``2869``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Start_Timer``, ``Create_Explosion``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_ParkEngineer
----------------

M05_ParkEngineer in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3261``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Action_Face_Location``, ``Start_Timer``, ``Action_Play_Animation``, ``Get_Random_Int``, ``Destroy_Object``
* Summary source: ``heuristic``

M05_ParkSniper
--------------

M05_ParkSniper in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``3107``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Is_A_Star``, ``Create_Logical_Sound``, ``Get_Position``, ``Innate_Force_State_Enemy_Seen``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_Resistance_Poke_Conversation
--------------------------------

M05_Resistance_Poke_Conversation in Mission05.cpp initializes behavior when the object is created; handles player poke interaction; starts conversations.

* Source line: ``7746``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Get_Preset_Name``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M05_Roadblock_Controller
------------------------

M05_Roadblock_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``6449``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Roadblock_Unit
------------------

M05_Roadblock_Unit in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``6525``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

M05_SniperAlley_Sniper
----------------------

M05_SniperAlley_Sniper in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands.

* Source line: ``5242``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Set_Innate_Is_Stationary``, ``Innate_Force_State_Enemy_Seen``
* Summary source: ``heuristic``

Parameter Description::

   Sniper_ID=0:int

M05_Surprise_Tank
-----------------

M05_Surprise_Tank in Mission05.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5719``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``
* Summary source: ``heuristic``

M05_Surprise_Unit
-----------------

M05_Surprise_Unit in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``6991``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Apply_Damage``, ``Get_Position``, ``Create_Sound``
* Summary source: ``heuristic``

M05_Swap_Artillery
------------------

M05_Swap_Artillery in Mission05.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects.

* Source line: ``7316``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Attach_Script``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Artillery_ID=0:int

M05_TownSquare_Controller
-------------------------

M05_TownSquare_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``4314``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Enable_Spawner``, ``Debug_Message``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M05_TownSquare_FlameTank
------------------------

M05_TownSquare_FlameTank in Mission05.cpp reacts to destruction state; sends custom events.

* Source line: ``4456``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

M05_TownSquare_Sniper
---------------------

M05_TownSquare_Sniper in Mission05.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands.

* Source line: ``4285``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``, ``Enable_Spawner``
* Summary source: ``heuristic``

M05_TownSquare_Tank
-------------------

M05_TownSquare_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``1771``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M05_TownSquare_Unit
-------------------

M05_TownSquare_Unit in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``4407``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Find_Object``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

M05_Triangle_Controller
-----------------------

M05_Triangle_Controller in Mission05.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``4180``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Triangle_Tank
-----------------

M05_Triangle_Tank in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1693``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Get_Random_Int``, ``Find_Object``, ``Action_Attack``, ``Get_Player_Type``
* Summary source: ``heuristic``

M05_Triangle_Unit
-----------------

M05_Triangle_Unit in Mission05.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``4108``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Health``, ``Find_Object``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID=0:int

M05_Vehicle_Dec
---------------

M05_Vehicle_Dec in Mission05.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``6396``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``, ``Start_Timer``, ``Modify_Action``
* Summary source: ``heuristic``

M05_X5N_MIDTRO_B
----------------

M05_X5N_MIDTRO_B in Mission05.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7437``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Set_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``
