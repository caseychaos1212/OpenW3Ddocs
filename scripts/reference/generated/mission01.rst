Mission01.cpp
=============

* Category: ``mission``
* Indexed registrations: ``289``
* Source: ``Code/Scripts/Mission01.cpp``

M01_AccessDenied_Zone_JDG
-------------------------

M01_AccessDenied_Zone_JDG in Mission01.cpp watches enter or exit events; starts conversations.

* Source line: ``17439``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_Airstrike_Controller_JDG
----------------------------

M01_Airstrike_Controller_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``17090``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Get_ID``
* Summary source: ``heuristic``

M01_Ambient_Sound_Controller_JDG
--------------------------------

M01_Ambient_Sound_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``2638``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Stop_Sound``, ``Debug_Message``, ``Create_Sound``, ``Get_Random``, ``Get_A_Star``, ``Get_Position``
* Summary source: ``heuristic``

M01_Announce_Barn_Objective_Zone
--------------------------------

M01_Announce_Barn_Objective_Zone in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``4409``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_Announce_First_ObjectiveZone_JDG
------------------------------------

M01_Announce_First_ObjectiveZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``17302``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``, ``Create_Object``, ``Attach_Script``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Announce_Hand_of_Nod_Zone
-----------------------------

M01_Announce_Hand_of_Nod_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4387``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Announce_Prisoner_Objective_Zone
------------------------------------

M01_Announce_Prisoner_Objective_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3149``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Announce_TankAirstrikeZone_JDG
----------------------------------

M01_Announce_TankAirstrikeZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``19703``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BackPath_EntranceZone_JDG
-----------------------------

M01_BackPath_EntranceZone_JDG in Mission01.cpp responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``21525``
* Event hooks: ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BackPath_NodGuy_JDG
-----------------------

M01_BackPath_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``10360``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Barn_Babushkas_Conversation_Zone_JDG
----------------------------------------

M01_Barn_Babushkas_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7781``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Barn_Door_Guard_JDG
-----------------------

M01_Barn_Door_Guard_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7945``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_EntryZone_JDG
----------------------

M01_Barn_EntryZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15356``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Barn_Point_Guard_01_JDG
---------------------------

M01_Barn_Point_Guard_01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7848``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Point_Guard_02_JDG
---------------------------

M01_Barn_Point_Guard_02_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7878``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Health``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Prisoner_01_JDG
------------------------

M01_Barn_Prisoner_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12777``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Action_Play_Animation``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Hibernation``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Barn_Prisoner_02_JDG
------------------------

M01_Barn_Prisoner_02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12950``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Action_Play_Animation``, ``Create_Sound``, ``Find_Object``, ``Send_Custom_Event``, ``Enable_Hibernation``, ``Action_Reset``, ``Get_Position``
* Summary source: ``heuristic``

M01_Barn_Prisoner_03_JDG
------------------------

M01_Barn_Prisoner_03_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``13095``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Play_Animation``, ``Create_Sound``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Enable_Hibernation``, ``Action_Reset``
* Summary source: ``heuristic``

M01_Barn_Talk_Guard_01_JDG
--------------------------

M01_Barn_Talk_Guard_01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7964``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Truck_JDG
------------------

M01_Barn_Truck_JDG in Mission01.cpp reacts to destruction state; creates explosions.

* Source line: ``10108``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``
* Summary source: ``heuristic``

M01_BarnArea_AI_ExitZone_JDG
----------------------------

M01_BarnArea_AI_ExitZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``7983``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Chopper_JDG
---------------------------------

M01_BarnArea_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12648``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Rope_JDG
------------------------------

M01_BarnArea_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12579``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Waypath_JDG
---------------------------------

M01_BarnArea_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12614``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_BarnArea_EvacMonitor_JDG
----------------------------

M01_BarnArea_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``15430``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Monitor_Conversation``, ``Create_Object``, ``Attach_Script``, ``Get_ID``
* Summary source: ``heuristic``

M01_BarnArea_NOD_Commander_Trigger_Zone02_JDG
---------------------------------------------

M01_BarnArea_NOD_Commander_Trigger_Zone02_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``18147``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BarnArea_NOD_Commander_Trigger_Zone_JDG
-------------------------------------------

M01_BarnArea_NOD_Commander_Trigger_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``14661``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BasalBuilding_Population_JDG
--------------------------------

M01_BasalBuilding_Population_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``7636``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Random``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_Base_GDI_Fodder_JDG
-----------------------

M01_Base_GDI_Fodder_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``18013``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Get_Random``, ``Send_Custom_Event``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Base_GDI_Grenadier_JDG
--------------------------

M01_Base_GDI_Grenadier_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``18852``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Health``, ``Destroy_Object``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Base_GDI_Minigunner_JDG
---------------------------

M01_Base_GDI_Minigunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``21566``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Create_Object``, ``Attach_Script``, ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Send_Custom_Event``, ``Destroy_Object``, ``Find_Object``
* Summary source: ``heuristic``

M01_Base_Nod_Minigunner_JDG
---------------------------

M01_Base_Nod_Minigunner_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``17708``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_Base_POW01_JDG
------------------

M01_Base_POW01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``19294``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Health``, ``Set_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Base_POW02_JDG
------------------

M01_Base_POW02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``19433``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Health``, ``Set_Health``, ``Destroy_Object``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Base_StartZone_JDG
----------------------

M01_Base_StartZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``18044``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Beach_Datadisc_JDG
----------------------

M01_Beach_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21099``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_Billys_Conversation_Zone_JDG
--------------------------------

M01_Billys_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5481``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BuggyNew_Controller_JDG
---------------------------

M01_BuggyNew_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``8910``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BuggyScript_New_JDG
-----------------------

M01_BuggyScript_New_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``8969``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Enemy_Seen``, ``Action_Attack``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Get_Max_Shield_Strength``, ``Set_Shield_Strength``, ``Create_Sound``
* Summary source: ``heuristic``

M01_C130_Dropoff_Dude_JDG
-------------------------

M01_C130_Dropoff_Dude_JDG in Mission01.cpp creates or destroys objects.

* Source line: ``17991``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_C4_Tutorial_Zone_JDG
------------------------

M01_C4_Tutorial_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``18078``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_C4_TutorialScript_JDG
-------------------------

M01_C4_TutorialScript_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``17409``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_CantBring_MediumTank_ThroughHereZone_JDG
--------------------------------------------

M01_CantBring_MediumTank_ThroughHereZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``20779``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Church_Balcony_MiniGunner_JDG
---------------------------------

M01_Church_Balcony_MiniGunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``4279``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_CHURCH_Chinook_Spawned_Soldier01_GDI
----------------------------------------

M01_CHURCH_Chinook_Spawned_Soldier01_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; starts conversations.

* Source line: ``9347``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Goto``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Action_Attack``
* Summary source: ``heuristic``

M01_CHURCH_Chinook_Spawned_Soldier02_GDI
----------------------------------------

M01_CHURCH_Chinook_Spawned_Soldier02_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events.

* Source line: ``9636``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``, ``Action_Reset``, ``Get_Random``, ``Set_Innate_Soldier_Home_Location``, ``Action_Goto``, ``Get_Position``
* Summary source: ``heuristic``

M01_Church_EvacController_JDG
-----------------------------

M01_Church_EvacController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``11796``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Find_Object``, ``Send_Custom_Event``, ``Get_ID``, ``Debug_Message``
* Summary source: ``heuristic``

M01_Church_Exterior_MiniGunner_JDG
----------------------------------

M01_Church_Exterior_MiniGunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``4154``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Goto``, ``Action_Attack``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_Church_Guard_MiniGunner_JDG
-------------------------------

M01_Church_Guard_MiniGunner_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``9202``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Attack``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Church_Interior_Nun_JDG
---------------------------

M01_Church_Interior_Nun_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12307``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Position``, ``Create_Sound``, ``Stop_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``, ``Start_Sound``
* Summary source: ``heuristic``

M01_Church_Loveshack_InterrogationConv_Zone_JDG
-----------------------------------------------

M01_Church_Loveshack_InterrogationConv_Zone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``9237``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Church_LoveShack_MiniGunner_JDG
-----------------------------------

M01_Church_LoveShack_MiniGunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``4101``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Attack``, ``Find_Object``, ``Destroy_Object``, ``Send_Custom_Event``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Church_LoveShack_Nun_JDG
----------------------------

M01_Church_LoveShack_Nun_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12453``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``, ``Action_Goto``, ``Enable_Hibernation``, ``Get_Position``
* Summary source: ``heuristic``

M01_Church_Priest_JDG
---------------------

M01_Church_Priest_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``12103``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Position``, ``Create_Sound``, ``Stop_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``, ``Start_Sound``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Chopper_JDG
-----------------------------------

M01_ChurchArea_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11997``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Rope_JDG
--------------------------------

M01_ChurchArea_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11928``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Waypath_JDG
-----------------------------------

M01_ChurchArea_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11963``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_ChurchArea_EvacMonitor_JDG
------------------------------

M01_ChurchArea_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``10155``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ChurchArea_NOD_Commander_JDG
--------------------------------

M01_ChurchArea_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``7151``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Get_Distance``, ``Action_Play_Animation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M01_ChurchArea_Spawner_Controller_JDG
-------------------------------------

M01_ChurchArea_Spawner_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6692``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Trigger_Spawner``, ``Get_Random``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ChurchArea_Spawner_Guy_JDG
------------------------------

M01_ChurchArea_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6837``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Civ_To_Minigunner_Guy_JDG
-----------------------------

M01_Civ_To_Minigunner_Guy_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5879``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Comm_Base_Commander_Conv_Start_Zone_JDG
-------------------------------------------

M01_Comm_Base_Commander_Conv_Start_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``6193``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Base_Commander_JDG
---------------------------

M01_Comm_Base_Commander_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``5897``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Reset``, ``Innate_Force_State_Enemy_Seen``, ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``
* Summary source: ``heuristic``

M01_Comm_Center_Building_Script_JDG
-----------------------------------

M01_Comm_Center_Building_Script_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``10453``
* Event hooks: ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Center_Exterior_Zone
-----------------------------

M01_Comm_Center_Exterior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3005``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Center_Interior_Zone
-----------------------------

M01_Comm_Center_Interior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``2994``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Center_Pen_Gate
------------------------

M01_Comm_Center_Pen_Gate in Mission01.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events.

* Source line: ``15620``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Center_Player_Terminal_Zone
------------------------------------

M01_Comm_Center_Player_Terminal_Zone in Mission01.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events.

* Source line: ``11499``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Display_Health_Bar``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``
* Summary source: ``heuristic``

M01_COMM_Chinook_Spawned_Soldier_GDI
------------------------------------

M01_COMM_Chinook_Spawned_Soldier_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events.

* Source line: ``9903``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``, ``Action_Reset``, ``Get_Random``, ``Set_Innate_Soldier_Home_Location``, ``Action_Goto``, ``Get_Position``
* Summary source: ``heuristic``

M01_COMM_Commander_Guy
----------------------

M01_COMM_Commander_Guy in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``3191``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_ComputerRoom_Tech_JDG
------------------------------

M01_Comm_ComputerRoom_Tech_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``6058``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_Comm_Kane_n_Havoc_Conv_Start_Zone_JDG
-----------------------------------------

M01_Comm_Kane_n_Havoc_Conv_Start_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``6215``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Mainframe_PogZone_01_JDG
---------------------------------

M01_Comm_Mainframe_PogZone_01_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``11457``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_HUD_Info_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Mainframe_PogZone_02_JDG
---------------------------------

M01_Comm_Mainframe_PogZone_02_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``11471``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_HUD_Info_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Mainframe_PogZone_03_JDG
---------------------------------

M01_Comm_Mainframe_PogZone_03_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``11485``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_HUD_Info_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_MCT_Placeholder_JDG
----------------------------

M01_Comm_MCT_Placeholder_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6235``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Repair_Engineer_JDG
----------------------------

M01_Comm_Repair_Engineer_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``10378``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_Hibernation``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``, ``Find_Object``, ``Get_Max_Health``, ``Get_Max_Shield_Strength``
* Summary source: ``heuristic``

M01_Comm_Stationary_Tech_JDG
----------------------------

M01_Comm_Stationary_Tech_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``5998``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_Comm_Upstairs_Guard_JDG
---------------------------

M01_Comm_Upstairs_Guard_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; changes innate AI behavior.

* Source line: ``6114``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Get_Random``, ``Start_Timer``
* Summary source: ``heuristic``

M01_Commander_Shack_Zone_JDG
----------------------------

M01_Commander_Shack_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``15688``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_CommCenter_Evacuator_JDG
----------------------------

M01_CommCenter_Evacuator_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; sends custom events.

* Source line: ``3239``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Random``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_CommCenter_SAMSite_Script
-----------------------------

M01_CommCenter_SAMSite_Script in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``15661``
* Event hooks: ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_ConDropZone_JDG
-------------------

M01_ConDropZone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17965``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ConYard_Dropoff_Dude_JDG
----------------------------

M01_ConYard_Dropoff_Dude_JDG in Mission01.cpp creates or destroys objects.

* Source line: ``17980``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_DataDisc_TextController_JDG
-------------------------------

M01_DataDisc_TextController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``21360``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Deco_LightTanks_JDG
-----------------------

M01_Deco_LightTanks_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``17054``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Destroyed_SAMSITE_JDG
-------------------------

M01_Destroyed_SAMSITE_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3222``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Detention_GuardTower_Enter_Zone_JDG
---------------------------------------

M01_Detention_GuardTower_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``13935``
* Event hooks: ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionCiv_Air_Evac_Chopper_JDG
-------------------------------------

M01_DetentionCiv_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``8341``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Set_Animation``, ``Find_Object``
* Summary source: ``heuristic``

M01_DetentionCiv_Air_Evac_Waypath_JDG
-------------------------------------

M01_DetentionCiv_Air_Evac_Waypath_JDG in Mission01.cpp responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``8313``
* Event hooks: ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_DetentionGDI_Air_Evac_Chopper_JDG
-------------------------------------

M01_DetentionGDI_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``8508``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Set_Animation``, ``Find_Object``
* Summary source: ``heuristic``

M01_DetentionGDI_Air_Evac_Waypath_JDG
-------------------------------------

M01_DetentionGDI_Air_Evac_Waypath_JDG in Mission01.cpp responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``8480``
* Event hooks: ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_DetentionPen_CivDeathMonitor
--------------------------------

M01_DetentionPen_CivDeathMonitor in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``8152``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Mission_Complete``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_DetentionPen_Evac_Controller01_JDG
--------------------------------------

M01_DetentionPen_Evac_Controller01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``8248``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Mission_Complete``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionPen_Evac_Controller02_JDG
--------------------------------------

M01_DetentionPen_Evac_Controller02_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``8432``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionPen_GDIDeathMonitor
--------------------------------

M01_DetentionPen_GDIDeathMonitor in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``8200``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Mission_Complete``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Duncan_Assailer_JDG
-----------------------

M01_Duncan_Assailer_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``21458``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Duncan_InHere_ConvController_JDG
------------------------------------

M01_Duncan_InHere_ConvController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``21472``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_Entering_Church_Area_Zone
-----------------------------

M01_Entering_Church_Area_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``2946``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Evac_TroopBone_JDG
----------------------

M01_Evac_TroopBone_JDG in Mission01.cpp creates or destroys objects.

* Source line: ``13350``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_First_AutoRifle_JDG
-----------------------

M01_First_AutoRifle_JDG in Mission01.cpp responds to custom events; starts conversations.

* Source line: ``17284``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Flamethrower_Point_Guard_JDG
--------------------------------

M01_Flamethrower_Point_Guard_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``4599``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Set_Innate_Soldier_Home_Location``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Get_Random``, ``Send_Custom_Event``, ``Action_Face_Location``
* Summary source: ``heuristic``

M01_Flyover_Generic_Script_JDG
------------------------------

M01_Flyover_Generic_Script_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``2615``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Enable_Hibernation``, ``Enable_Cinematic_Freeze``, ``Get_Max_Health``, ``Get_Random``, ``Get_Max_Shield_Strength``, ``Set_Health``, ``Set_Shield_Strength``
* Summary source: ``heuristic``

M01_FodderHovercraft_Script_JDG
-------------------------------

M01_FodderHovercraft_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``21032``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Random``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_FP_BaseToBase_NorthSouth_Contoller_JDG
------------------------------------------

M01_FP_BaseToBase_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16396``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_BaseToBase_SouthNorth_Contoller_JDG
------------------------------------------

M01_FP_BaseToBase_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16461``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Start_Timer``, ``Get_Random_Int``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_GDIOcean_NorthSouth_Contoller_JDG
----------------------------------------

M01_FP_GDIOcean_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16925``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_GDIOcean_SouthNorth_Contoller_JDG
----------------------------------------

M01_FP_GDIOcean_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16990``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_Dogfight_Contoller_JDG
-------------------------------------

M01_FP_NodBase_Dogfight_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16326``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_EastWest_Contoller_JDG
-------------------------------------

M01_FP_NodBase_EastWest_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16562``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_NorthSouth_Contoller_JDG
---------------------------------------

M01_FP_NodBase_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16757``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_SouthNorth_Contoller_JDG
---------------------------------------

M01_FP_NodBase_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16841``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_WestEast_Contoller_JDG
-------------------------------------

M01_FP_NodBase_WestEast_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16672``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_GateSwitch_Tutorial_Zone_JDG
--------------------------------

M01_GateSwitch_Tutorial_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``18110``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_Base_Artillery_Controller_JDG
-------------------------------------

M01_GDI_Base_Artillery_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``7311``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_Random``, ``Create_Sound``, ``Monitor_Sound``, ``Find_Object``, ``Destroy_Object``, ``Create_Explosion``
* Summary source: ``heuristic``

M01_GDI_Base_Spawner_Controller_JDG
-----------------------------------

M01_GDI_Base_Spawner_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6401``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Enable_Hibernation``, ``Get_Difficulty_Level``, ``Trigger_Spawner``, ``Get_Random``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_Base_Spawner_Guy_JDG
----------------------------

M01_GDI_Base_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6523``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDI_BaseCommander_Backside_EntryZone_JDG
--------------------------------------------

M01_GDI_BaseCommander_Backside_EntryZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15374``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_BeachGuy01_JDG
----------------------

M01_GDI_BeachGuy01_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; changes innate AI behavior.

* Source line: ``19668``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_Hibernation``, ``Action_Goto``, ``Get_Health``, ``Set_Health``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_GDI_Escort_Conversation_Controller_GDI
------------------------------------------

M01_GDI_Escort_Conversation_Controller_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; starts conversations.

* Source line: ``9276``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_GDI_GuardTower02_SniperRifle_JDG
------------------------------------

M01_GDI_GuardTower02_SniperRifle_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``19751``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_GDI_GuardTower_02_Enter_Zone_JDG
------------------------------------

M01_GDI_GuardTower_02_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``19731``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_GuardTower_NOD_Commander_JDG
------------------------------------

M01_GDI_GuardTower_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``14692``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Get_Distance``, ``Action_Play_Animation``, ``Stop_Conversation``, ``Find_Object``, ``Destroy_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDI_Toolshed_PatrolGuy_JDG
------------------------------

M01_GDI_Toolshed_PatrolGuy_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``6243``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_GDIBase_AI_ExitZone_JDG
---------------------------

M01_GDIBase_AI_ExitZone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``15059``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_BackPath_NodGuy_JDG
-------------------------------

M01_GDIBase_BackPath_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``15241``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBase_BaseCommander_JDG
-----------------------------

M01_GDIBase_BaseCommander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``18583``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Set_Objective_Status``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``, ``Create_Object``
* Summary source: ``heuristic``

M01_GDIBase_EvacMonitor_JDG
---------------------------

M01_GDIBase_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``10117``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinook_Script_JDG
-----------------------------------

M01_GDIBase_FirstChinook_Script_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``11778``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinookFlamethrowerGuy_JDG
-------------------------------------------

M01_GDIBase_FirstChinookFlamethrowerGuy_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``13542``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinookMinigunnerGuy_JDG
-----------------------------------------

M01_GDIBase_FirstChinookMinigunnerGuy_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``17454``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_GDIBase_LightTank_JDG
-------------------------

M01_GDIBase_LightTank_JDG in Mission01.cpp responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``15123``
* Event hooks: ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Get_Position``, ``Get_Difficulty_Level``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBase_LightTank_PastTunnelZone_JDG
----------------------------------------

M01_GDIBase_LightTank_PastTunnelZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15021``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDIBase_POW_Conversation_Controller_JDG
-------------------------------------------

M01_GDIBase_POW_Conversation_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``19569``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_POWEncounter02_Controller_JDG
-----------------------------------------

M01_GDIBase_POWEncounter02_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; updates objectives; changes innate AI behavior.

* Source line: ``17737``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Set_Objective_Status``, ``Get_ID``, ``Get_Position``, ``Create_Object``, ``Set_Model``, ``Attach_Script``, ``Innate_Disable``
* Summary source: ``heuristic``

M01_GDIBase_RealLightTank_JDG
-----------------------------

M01_GDIBase_RealLightTank_JDG in Mission01.cpp responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``17189``
* Event hooks: ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Chopper_JDG
-----------------------------------------

M01_GDIBaseCommander_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``17475``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Rope_JDG
--------------------------------------

M01_GDIBaseCommander_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13397``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Waypath_JDG
-----------------------------------------

M01_GDIBaseCommander_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13363``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBaseCommander_EvacController_JDG
---------------------------------------

M01_GDIBaseCommander_EvacController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``17578``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Debug_Message``, ``Get_ID``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Chopper_JDG
-----------------------------------

M01_GDIBasePOW_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``17870``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Rope_JDG
--------------------------------

M01_GDIBasePOW_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13272``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Waypath_JDG
-----------------------------------

M01_GDIBasePOW_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13309``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GiveMCTSpeech_Zone_JDG
--------------------------

M01_GiveMCTSpeech_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``20513``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Get_ID``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M01_GuardTower02_NewSniperTarget_JDG
------------------------------------

M01_GuardTower02_NewSniperTarget_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``19955``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Action_Attack``, ``Send_Custom_Event``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_Target01_JDG
------------------------------------

M01_GuardTower02_Sniper_Target01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``19771``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_ID``, ``Action_Goto``, ``Find_Object``, ``Action_Reset``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_Target02_JDG
------------------------------------

M01_GuardTower02_Sniper_Target02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``20017``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Reset``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_TowerZone_JDG
-------------------------------------

M01_GuardTower02_Sniper_TowerZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``19894``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_GuardTower_Sniper_Target_JDG
--------------------------------

M01_GuardTower_Sniper_Target_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``7502``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Get_Position``, ``Get_Random_Int``, ``Create_Object``, ``Action_Play_Animation``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   wave_location:vector3,  delete_location:vector3

M01_Gunboat_Spawn_Hovercraft_Zone_JDG
-------------------------------------

M01_Gunboat_Spawn_Hovercraft_Zone_JDG in Mission01.cpp has no extracted behavior summary yet.

* Source line: ``7602``
* Event hooks: none detected
* Persistence hooks: none detected
* Key engine calls: none detected
* Summary source: ``heuristic``

M01_GunboatAction_Controller_JDG
--------------------------------

M01_GunboatAction_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``18311``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_ID``
* Summary source: ``heuristic``

M01_Hand_of_Nod_Building_Script_JDG
-----------------------------------

M01_Hand_of_Nod_Building_Script_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; creates or destroys objects.

* Source line: ``2564``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Stop_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Get_Max_Health``, ``Get_Max_Shield_Strength``, ``Set_Health``
* Summary source: ``heuristic``

M01_Hand_Of_Nod_Dojo_Zone
-------------------------

M01_Hand_Of_Nod_Dojo_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``4090``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Hand_Of_Nod_Exterior_Zone
-----------------------------

M01_Hand_Of_Nod_Exterior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``2983``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Hand_Of_Nod_Grunt_Zone
--------------------------

M01_Hand_Of_Nod_Grunt_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``4079``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Hand_Of_Nod_Interior_Zone
-----------------------------

M01_Hand_Of_Nod_Interior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``2972``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_HandOfNod_SAMSite_Script
----------------------------

M01_HandOfNod_SAMSite_Script in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``3201``
* Event hooks: ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_HarvesterScript_New_JDG
---------------------------

M01_HarvesterScript_New_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; controls animation playback; starts conversations.

* Source line: ``7646``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Action_Goto``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Sound``, ``Create_Object``
* Summary source: ``heuristic``

M01_Havoc_In_WarroomZone_JDG
----------------------------

M01_Havoc_In_WarroomZone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``20638``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Havoc_Out_WarroomZone_JDG
-----------------------------

M01_Havoc_Out_WarroomZone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``20653``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_HON_BackDoor_Evacuator_JDG
------------------------------

M01_HON_BackDoor_Evacuator_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; sends custom events.

* Source line: ``3355``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Random``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_HON_Cafeteria_Eating_Guy_JDG
--------------------------------

M01_HON_Cafeteria_Eating_Guy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3851``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Cafeteria_Walking_Guy_JDG
---------------------------------

M01_HON_Cafeteria_Walking_Guy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3947``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Goto``, ``Enable_Hibernation``, ``Get_Random``, ``Action_Face_Location``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_01_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_01_GDI_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``20157``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_02_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_02_GDI_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``20366``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_03_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_03_GDI_JDG in Mission01.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``8806``
* Event hooks: ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_04_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_04_GDI_JDG in Mission01.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``8858``
* Event hooks: ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_HON_Commander_Guy
---------------------

M01_HON_Commander_Guy in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``3183``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_HON_Dojo_Civ_01_JDG
-----------------------

M01_HON_Dojo_Civ_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``11152``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_ID``, ``Create_Sound``, ``Action_Play_Animation``, ``Action_Goto``, ``Action_Reset``, ``Get_Position``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Dojo_Trainer_JDG
------------------------

M01_HON_Dojo_Trainer_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``10985``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Find_Object``, ``Get_Random``, ``Send_Custom_Event``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Footsteps_Heard``
* Summary source: ``heuristic``

M01_HON_Dorm_ChemGuy_JDG
------------------------

M01_HON_Dorm_ChemGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3588``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Dorm_Crapper_JDG
------------------------

M01_HON_Dorm_Crapper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3396``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Enable_Hibernation``, ``Get_Random``, ``Action_Goto``
* Summary source: ``heuristic``

M01_HON_Dorm_FlameGuy_JDG
-------------------------

M01_HON_Dorm_FlameGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3499``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Dorm_MiniGunner_JDG
---------------------------

M01_HON_Dorm_MiniGunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3764``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Dorm_RocketGuy_JDG
--------------------------

M01_HON_Dorm_RocketGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``3677``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Easy_Spawned_Guy_01_JDG
-------------------------------

M01_HON_Easy_Spawned_Guy_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4717``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Reset``, ``Innate_Force_State_Enemy_Seen``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M01_HON_Easy_Spawned_Guy_02_JDG
-------------------------------

M01_HON_Easy_Spawned_Guy_02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4833``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Reset``, ``Innate_Force_State_Enemy_Seen``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M01_HON_Easy_Spawned_Guy_03_JDG
-------------------------------

M01_HON_Easy_Spawned_Guy_03_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4948``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Reset``, ``Innate_Force_State_Enemy_Seen``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M01_HON_Engineer02_JDG
----------------------

M01_HON_Engineer02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``8731``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_Hibernation``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``, ``Find_Object``, ``Get_Max_Health``, ``Get_Max_Shield_Strength``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Commander_JDG
-----------------------------------------

M01_HON_Escorts_Warroom_MCT_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``8677``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Protector01_JDG
-------------------------------------------

M01_HON_Escorts_Warroom_MCT_Protector01_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``8713``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Protector02_JDG
-------------------------------------------

M01_HON_Escorts_Warroom_MCT_Protector02_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``8721``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_ZoneController_JDG
----------------------------------------------

M01_HON_Escorts_Warroom_MCT_ZoneController_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``20129``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_HON_FrontDoor_Evacuator_JDG
-------------------------------

M01_HON_FrontDoor_Evacuator_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; sends custom events.

* Source line: ``3290``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_MCT_Placeholder_JDG
---------------------------

M01_HON_MCT_Placeholder_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6227``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_HON_Medlab_DropOff_Guy_JDG
------------------------------

M01_HON_Medlab_DropOff_Guy_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects; changes innate AI behavior.

* Source line: ``2526``
* Event hooks: ``Created``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_Hibernation``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_HON_Paintball_Team_01_JDG
-----------------------------

M01_HON_Paintball_Team_01_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``10697``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Set_Player_Type``, ``Set_Obj_Radar_Blip_Color``, ``Get_Position``, ``Get_Random``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_HON_Paintball_Team_02_JDG
-----------------------------

M01_HON_Paintball_Team_02_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``10838``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Get_Position``, ``Get_Random``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Set_Innate_Soldier_Home_Location``, ``Start_Timer``, ``Find_Object``
* Summary source: ``heuristic``

M01_HON_RedKey_Zone_JDG
-----------------------

M01_HON_RedKey_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``15601``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_HON_WarroomController_JDG
-----------------------------

M01_HON_WarroomController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``20668``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Find_Object``, ``Apply_Damage``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Hovercraft_Explosion_Controller_JDG
---------------------------------------

M01_Hovercraft_Explosion_Controller_JDG in Mission01.cpp responds to custom events.

* Source line: ``20999``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Hunt_The_Player_JDG
-----------------------

M01_Hunt_The_Player_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``8620``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Start_Timer``, ``Action_Goto``, ``Get_Position``, ``Get_Distance``, ``Is_Object_Visible``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Initial_Gunboat_Script_JDG
------------------------------

M01_Initial_Gunboat_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``18383``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Action_Attack``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M01_Interior_Nun_Conversation_Zone_JDG
--------------------------------------

M01_Interior_Nun_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``9167``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Interrogation_Room_L03_Keycard_JDG
--------------------------------------

M01_Interrogation_Room_L03_Keycard_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``5329``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Shape``
* Summary source: ``heuristic``

M01_Interrogation_Room_Surprise_Guy_JDG
---------------------------------------

M01_Interrogation_Room_Surprise_Guy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``5337``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Create_Sound``, ``Get_Position``, ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_KeyCard01_Script_JDG
------------------------

M01_KeyCard01_Script_JDG in Mission01.cpp responds to custom events; starts conversations.

* Source line: ``15044``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_Left_Interrogation_Room_Enter_Zone_JDG
------------------------------------------

M01_Left_Interrogation_Room_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5281``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Lose_Any_Church_Escorts_Zone
--------------------------------

M01_Lose_Any_Church_Escorts_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3105``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Lose_Any_Church_Escorts_Zone_02
-----------------------------------

M01_Lose_Any_Church_Escorts_Zone_02 in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3116``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Lose_Any_HON_Escorts_Zone
-----------------------------

M01_Lose_Any_HON_Escorts_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3127``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Lose_Any_HON_Escorts_Zone_02
--------------------------------

M01_Lose_Any_HON_Escorts_Zone_02 in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3138``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Loveshack_Nun_Conversation_Zone_JDG
---------------------------------------

M01_Loveshack_Nun_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``9130``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Mainframe_Tutorial_Zone_JDG
-------------------------------

M01_Mainframe_Tutorial_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``18097``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Medium_Tank01_JDG
---------------------

M01_Medium_Tank01_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``20767``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Medium_Tank_JDG
-------------------

M01_Medium_Tank_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``20833``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Create_Object``, ``Attach_Script``, ``Action_Reset``
* Summary source: ``heuristic``

M01_Medium_Tank_Tunnel_Squish_Guy_JDG
-------------------------------------

M01_Medium_Tank_Tunnel_Squish_Guy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; plays sounds.

* Source line: ``5455``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Create_3D_Sound_At_Bone``
* Summary source: ``heuristic``

M01_MediumTank_ReminderZone_JDG
-------------------------------

M01_MediumTank_ReminderZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; creates or destroys objects; starts conversations.

* Source line: ``19181``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``, ``Find_Object``, ``Monitor_Conversation``, ``Start_Timer``, ``Get_ID``
* Summary source: ``heuristic``

M01_Medlab_Datadisc_JDG
-----------------------

M01_Medlab_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21342``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Reveal_Map``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_MiniGunner_Point_Guard_JDG
------------------------------

M01_MiniGunner_Point_Guard_JDG in Mission01.cpp has no extracted behavior summary yet.

* Source line: ``4672``
* Event hooks: none detected
* Persistence hooks: none detected
* Key engine calls: none detected
* Summary source: ``heuristic``

M01_Mission_Controller_JDG
--------------------------

M01_Mission_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; plays sounds; updates objectives; starts conversations.

* Source line: ``53``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Wind``, ``Set_Rain``, ``Set_Lightning``, ``Reveal_Encyclopedia_Character``, ``Reveal_Encyclopedia_Weapon``, ``Reveal_Encyclopedia_Vehicle``, ``Reveal_Encyclopedia_Building``
* Summary source: ``heuristic``

M01_MovieProjector_JDG
----------------------

M01_MovieProjector_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events; creates explosions; controls animation playback.

* Source line: ``10191``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Explosion``, ``Set_Health``
* Summary source: ``heuristic``

M01_Nod_Chinook_Reinforcement_Guy_JDG
-------------------------------------

M01_Nod_Chinook_Reinforcement_Guy_JDG in Mission01.cpp drives AI action commands; sends custom events.

* Source line: ``8599``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Nod_Commander_Conversation_Controller_GDI
---------------------------------------------

M01_Nod_Commander_Conversation_Controller_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``14939``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Get_Random_Int``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Nod_GuardTower_01_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_01_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7439``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_02_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_02_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7459``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_03_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_03_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7479``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_Tailgun_JDG
------------------------------

M01_Nod_GuardTower_Tailgun_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``11446``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M01_Nod_Truck_JDG
-----------------

M01_Nod_Truck_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``18068``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Obj_Radar_Blip_Color``
* Summary source: ``heuristic``

M01_Obelisk_UpdateDisc_JDG
--------------------------

M01_Obelisk_UpdateDisc_JDG in Mission01.cpp responds to custom events.

* Source line: ``15418``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Building``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Objective_Pog_Controller_JDG
--------------------------------

M01_Objective_Pog_Controller_JDG in Mission01.cpp responds to custom events; sends custom events; updates objectives; starts conversations.

* Source line: ``11560``
* Event hooks: ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Set_Objective_Radar_Blip``, ``Set_Objective_HUD_Info_Position``, ``Set_HUD_Help_Text``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M01_PaintballRoom_ChatterController_JDG
---------------------------------------

M01_PaintballRoom_ChatterController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``10483``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_Player_Is_Crossing_Bridge_Via_Cave_Zone
-------------------------------------------

M01_Player_Is_Crossing_Bridge_Via_Cave_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4527``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Player_Is_Crossing_Bridge_Via_Church_Zone
---------------------------------------------

M01_Player_Is_Crossing_Bridge_Via_Church_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4563``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Player_Is_Crossing_Bridge_Zone
----------------------------------

M01_Player_Is_Crossing_Bridge_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4490``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Player_is_Entering_GDI_Base_Zone
------------------------------------

M01_Player_is_Entering_GDI_Base_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3094``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Player_Is_Entering_Tailgun_Alley_Backway_JDG
------------------------------------------------

M01_Player_Is_Entering_Tailgun_Alley_Backway_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5657``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Player_Is_Entering_Tailgun_Alley_JDG
----------------------------------------

M01_Player_Is_Entering_Tailgun_Alley_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``5603``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Player_is_Leaving_GDI_Base_Zone
-----------------------------------

M01_Player_is_Leaving_GDI_Base_Zone in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``3060``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_PlayerEntering_BarnArea_Zone_JDG
------------------------------------

M01_PlayerEntering_BarnArea_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``15311``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_PlayerLeaving_BarnArea_Zone_JDG
-----------------------------------

M01_PlayerLeaving_BarnArea_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``15332``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_POW_Nod_Minigunner01_JDG
----------------------------

M01_POW_Nod_Minigunner01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``17716``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Priest_Conversation_Zone_JDG
--------------------------------

M01_Priest_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``9093``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Priest_Datadisc_JDG
-----------------------

M01_Priest_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21295``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_PrisonPen_Civilian_JDG
--------------------------

M01_PrisonPen_Civilian_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``14284``
* Event hooks: ``Created``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Get_ID``, ``Start_Timer``, ``Get_Random``, ``Action_Goto``, ``Find_Object``
* Summary source: ``heuristic``

M01_PrisonPen_POW_JDG
---------------------

M01_PrisonPen_POW_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``14022``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Innate_Disable``, ``Action_Attack``, ``Get_Random``
* Summary source: ``heuristic``

M01_Propaganda_Sounds_Controller_JDG
------------------------------------

M01_Propaganda_Sounds_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``10226``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Get_ID``, ``Create_Sound``, ``Stop_Sound``
* Summary source: ``heuristic``

M01_QuickSave_Zone_JDG
----------------------

M01_QuickSave_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17463``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_RealLightTank_TriggerZone_JDG
---------------------------------

M01_RealLightTank_TriggerZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``17252``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Right_Interrogation_Room_Enter_Zone_JDG
-------------------------------------------

M01_Right_Interrogation_Room_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5305``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Scramble_Radar_Zone
-----------------------

M01_Scramble_Radar_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3161``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Shed_Datadisc_JDG
---------------------

M01_Shed_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21200``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_Sinking_Gunboat_JDG
-----------------------

M01_Sinking_Gunboat_JDG in Mission01.cpp initializes behavior when the object is created; creates or destroys objects; controls animation playback.

* Source line: ``15294``
* Event hooks: ``Created``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_SniperRifle_01_JDG
----------------------

M01_SniperRifle_01_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``17331``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_SniperRifle_01_Target_JDG
-----------------------------

M01_SniperRifle_01_Target_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``17349``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Enable_Hibernation``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_SniperRifle_02_AirdropZone_JDG
----------------------------------

M01_SniperRifle_02_AirdropZone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17393``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_SniperRifle_02_JDG
----------------------

M01_SniperRifle_02_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``17378``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_TailGun_01_JDG
------------------

M01_TailGun_01_JDG in Mission01.cpp responds to custom events; drives AI action commands.

* Source line: ``5814``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M01_TailGun_02_JDG
------------------

M01_TailGun_02_JDG in Mission01.cpp responds to custom events; drives AI action commands.

* Source line: ``5831``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M01_Tailgun_02_SpawnApache_Zone_JDG
-----------------------------------

M01_Tailgun_02_SpawnApache_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``5865``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TailGun_03_JDG
------------------

M01_TailGun_03_JDG in Mission01.cpp responds to custom events; drives AI action commands.

* Source line: ``5848``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M01_Tailgun_Run_Spawner_Controller_JDG
--------------------------------------

M01_Tailgun_Run_Spawner_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6535``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Trigger_Spawner``, ``Get_Random``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TailGunner_01_JDG
---------------------

M01_TailGunner_01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``5703``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Find_Object``, ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``, ``Action_Enter_Exit``
* Summary source: ``heuristic``

M01_TailGunner_02_JDG
---------------------

M01_TailGunner_02_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``5740``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Find_Object``, ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``, ``Action_Enter_Exit``
* Summary source: ``heuristic``

M01_TailGunner_03_JDG
---------------------

M01_TailGunner_03_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``5777``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Find_Object``, ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``, ``Action_Enter_Exit``
* Summary source: ``heuristic``

M01_TailgunRun_NOD_Commander_JDG
--------------------------------

M01_TailgunRun_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``6991``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Get_Distance``, ``Action_Play_Animation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M01_TailgunRun_Spawner_Guy_JDG
------------------------------

M01_TailgunRun_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6680``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Tank_Entering_Tunnel_Zone_JDG
---------------------------------

M01_Tank_Entering_Tunnel_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5549``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TibCave01_Datadisc_JDG
--------------------------

M01_TibCave01_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21151``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_TibCave02_Datadisc_JDG
--------------------------

M01_TibCave02_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21243``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_TibCave_StartZone_JDG
-------------------------

M01_TibCave_StartZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``13664``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Tiberium_Cave_Helicopter_JDG
--------------------------------

M01_Tiberium_Cave_Helicopter_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``4423``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Action_Attack``, ``Get_Random``, ``Send_Custom_Event``, ``Modify_Action``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Tiberium_Cave_Spawn_Helicopter_Zone_JDG
-------------------------------------------

M01_Tiberium_Cave_Spawn_Helicopter_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``13871``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TiberiumCave_UpThere_NodGuy_JDG
-----------------------------------

M01_TiberiumCave_UpThere_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``13897``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Attack``, ``Send_Custom_Event``, ``Create_Sound``
* Summary source: ``heuristic``

M01_TibField_Guard01_New_JDG
----------------------------

M01_TibField_Guard01_New_JDG in Mission01.cpp responds to custom events; starts conversations.

* Source line: ``7752``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_TriggerZone_GDIBase_BaseCommander_JDG
-----------------------------------------

M01_TriggerZone_GDIBase_BaseCommander_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; updates objectives.

* Source line: ``13440``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Objective_Status``
* Summary source: ``heuristic``

M01_Tunnel_Exterior_Zone
------------------------

M01_Tunnel_Exterior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3027``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Tunnel_Interior_Zone
------------------------

M01_Tunnel_Interior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3016``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Turn_on_the_Hand_of_Nod_Zone_JDG
------------------------------------

M01_Turn_on_the_Hand_of_Nod_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``6849``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TurnOff_TankReminder_Zone_JDG
---------------------------------

M01_TurnOff_TankReminder_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``20113``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TurretBeach_Chinook_Spawned_Soldier_NOD
-------------------------------------------

M01_TurretBeach_Chinook_Spawned_Soldier_NOD in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``16054``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Action_Goto``, ``Innate_Enable``, ``Action_Reset``, ``Debug_Message``, ``Enable_Hibernation``, ``Get_Health``
* Summary source: ``heuristic``

M01_TurretBeach_Engineer_JDG
----------------------------

M01_TurretBeach_Engineer_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``15772``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Max_Health``, ``Action_Reset``, ``Innate_Enable``, ``Innate_Force_State_Enemy_Seen``, ``Get_ID``, ``Debug_Message``, ``Find_Object``
* Summary source: ``heuristic``

M01_TurretBeach_FodderHovercraft_Controller_JDG
-----------------------------------------------

M01_TurretBeach_FodderHovercraft_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``20933``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_ID``
* Summary source: ``heuristic``

M01_TurretBeach_GDI_Guy_01_JDG
------------------------------

M01_TurretBeach_GDI_Guy_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``8015``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Reset``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M01_TurretBeach_GDI_Guy_02_JDG
------------------------------

M01_TurretBeach_GDI_Guy_02_JDG in Mission01.cpp drives AI action commands.

* Source line: ``8105``
* Event hooks: ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_TurretBeach_Turret_01_Script_JDG
------------------------------------

M01_TurretBeach_Turret_01_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``18182``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``, ``Get_Max_Health``, ``Set_Health``
* Summary source: ``heuristic``

M01_UnScramble_Radar_Zone
-------------------------

M01_UnScramble_Radar_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3172``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Use_Ladder_Zone_JDG
-----------------------

M01_Use_Ladder_Zone_JDG in Mission01.cpp watches enter or exit events; starts conversations.

* Source line: ``17424``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Visceroid01_JDG
-------------------

M01_Visceroid01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13707``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid02_JDG
-------------------

M01_Visceroid02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13740``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid03_JDG
-------------------

M01_Visceroid03_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13773``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid_NodGuy01_JDG
--------------------------

M01_Visceroid_NodGuy01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13802``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Create_Sound``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid_NodGuy02_JDG
--------------------------

M01_Visceroid_NodGuy02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13836``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Create_Sound``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Waterfall_Exterior_Zone
---------------------------

M01_Waterfall_Exterior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3049``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Waterfall_Interior_Zone
---------------------------

M01_Waterfall_Interior_Zone in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``3038``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Whack_A_Mole_Enter_Zone_JDG
-------------------------------

M01_Whack_A_Mole_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5069``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Whack_A_Mole_Exit_Zone_JDG
------------------------------

M01_Whack_A_Mole_Exit_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5082``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Whack_A_Mole_Minigunner_JDG
-------------------------------

M01_Whack_A_Mole_Minigunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``5113``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Action_Goto``, ``Innate_Enable``, ``Action_Play_Animation``, ``Action_Reset``, ``Grant_Key``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``
