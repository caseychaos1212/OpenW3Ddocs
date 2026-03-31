Mission01.cpp
=============

* Category: ``mission``
* Active scripts: ``294``
* Source: ``Code/Scripts/Mission01.cpp``

M01_AccessDenied_Zone_JDG
-------------------------

M01_AccessDenied_Zone_JDG in Mission01.cpp watches enter or exit events; starts conversations.

* Source line: ``17438``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Airstrike_Controller_JDG
----------------------------

M01_Airstrike_Controller_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``17089``
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

M01_Announce_Barn_Objective_Zone in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4409``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Announce_First_ObjectiveZone_JDG
------------------------------------

M01_Announce_First_ObjectiveZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``17301``
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

* Source line: ``19704``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BackPath_EntranceZone_JDG
-----------------------------

M01_BackPath_EntranceZone_JDG in Mission01.cpp responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``21539``
* Event hooks: ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BackPath_NodGuy_JDG
-----------------------

M01_BackPath_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``10358``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Barn_Babushkas_Conversation_Zone_JDG
----------------------------------------

M01_Barn_Babushkas_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7777``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Barn_Door_Guard_JDG
-----------------------

M01_Barn_Door_Guard_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7941``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_EntryZone_JDG
----------------------

M01_Barn_EntryZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15355``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Barn_Point_Guard_01_JDG
---------------------------

M01_Barn_Point_Guard_01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7844``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Point_Guard_02_JDG
---------------------------

M01_Barn_Point_Guard_02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``7874``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Get_Health``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Prisoner_01_JDG
------------------------

M01_Barn_Prisoner_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12771``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Action_Play_Animation``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Hibernation``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Barn_Prisoner_02_JDG
------------------------

M01_Barn_Prisoner_02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12945``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Action_Play_Animation``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Hibernation``, ``Action_Reset``, ``Get_Position``
* Summary source: ``heuristic``

M01_Barn_Prisoner_03_JDG
------------------------

M01_Barn_Prisoner_03_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``13091``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Action_Play_Animation``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``, ``Enable_Hibernation``
* Summary source: ``heuristic``

M01_Barn_Talk_Guard_01_JDG
--------------------------

M01_Barn_Talk_Guard_01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``7960``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Barn_Truck_JDG
------------------

M01_Barn_Truck_JDG in Mission01.cpp reacts to destruction state; creates explosions.

* Source line: ``10106``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``
* Summary source: ``heuristic``

M01_BarnArea_AI_ExitZone_JDG
----------------------------

M01_BarnArea_AI_ExitZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``7979``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Chopper_JDG
---------------------------------

M01_BarnArea_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12642``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Rope_JDG
------------------------------

M01_BarnArea_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12573``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_BarnArea_Air_Evac_Waypath_JDG
---------------------------------

M01_BarnArea_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``12608``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_BarnArea_EvacMonitor_JDG
----------------------------

M01_BarnArea_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``15429``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Monitor_Conversation``, ``Create_Object``, ``Attach_Script``, ``Get_ID``
* Summary source: ``heuristic``

M01_BarnArea_NOD_Commander_JDG
------------------------------

M01_BarnArea_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``6871``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Distance``, ``Action_Play_Animation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M01_BarnArea_NOD_Commander_Trigger_Zone02_JDG
---------------------------------------------

M01_BarnArea_NOD_Commander_Trigger_Zone02_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``18146``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BarnArea_NOD_Commander_Trigger_Zone_JDG
-------------------------------------------

M01_BarnArea_NOD_Commander_Trigger_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``14660``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_BasalBuilding_Population_JDG
--------------------------------

M01_BasalBuilding_Population_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``7632``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Random``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_Base_GDI_Fodder_JDG
-----------------------

M01_Base_GDI_Fodder_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``18012``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Get_Random``, ``Send_Custom_Event``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Base_GDI_Grenadier_JDG
--------------------------

M01_Base_GDI_Grenadier_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``18853``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Health``, ``Destroy_Object``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Base_GDI_Minigunner_JDG
---------------------------

M01_Base_GDI_Minigunner_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``21580``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Create_Object``, ``Attach_Script``, ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Send_Custom_Event``, ``Destroy_Object``, ``Find_Object``
* Summary source: ``heuristic``

M01_Base_Nod_Minigunner_JDG
---------------------------

M01_Base_Nod_Minigunner_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``17707``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_Base_POW01_JDG
------------------

M01_Base_POW01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``19295``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Health``, ``Set_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Base_POW02_JDG
------------------

M01_Base_POW02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``19434``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Health``, ``Set_Health``, ``Destroy_Object``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Base_StartZone_JDG
----------------------

M01_Base_StartZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``18043``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Beach_Datadisc_JDG
----------------------

M01_Beach_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21113``
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

* Source line: ``8906``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_BuggyScript_New_JDG
-----------------------

M01_BuggyScript_New_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``8965``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Enemy_Seen``, ``Action_Attack``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Get_Max_Shield_Strength``, ``Set_Shield_Strength``, ``Create_Sound``
* Summary source: ``heuristic``

M01_C130_Dropoff_Dude_JDG
-------------------------

M01_C130_Dropoff_Dude_JDG in Mission01.cpp creates or destroys objects.

* Source line: ``17990``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_C4_Tutorial_Zone_JDG
------------------------

M01_C4_Tutorial_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``18077``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_C4_TutorialScript_JDG
-------------------------

M01_C4_TutorialScript_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``17408``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_CantBring_MediumTank_ThroughHereZone_JDG
--------------------------------------------

M01_CantBring_MediumTank_ThroughHereZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``20782``
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

* Source line: ``9345``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Goto``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Action_Attack``
* Summary source: ``heuristic``

M01_CHURCH_Chinook_Spawned_Soldier02_GDI
----------------------------------------

M01_CHURCH_Chinook_Spawned_Soldier02_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events.

* Source line: ``9634``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``, ``Action_Reset``, ``Get_Random``, ``Set_Innate_Soldier_Home_Location``, ``Action_Goto``, ``Get_Position``
* Summary source: ``heuristic``

M01_Church_EvacController_JDG
-----------------------------

M01_Church_EvacController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``11788``
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

* Source line: ``9200``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Attack``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Church_Interior_Nun_JDG
---------------------------

M01_Church_Interior_Nun_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior.

* Source line: ``12299``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Position``, ``Create_Sound``, ``Stop_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``, ``Start_Sound``
* Summary source: ``heuristic``

M01_Church_Loveshack_InterrogationConv_Zone_JDG
-----------------------------------------------

M01_Church_Loveshack_InterrogationConv_Zone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``9235``
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

* Source line: ``12446``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Create_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``, ``Action_Goto``, ``Enable_Hibernation``, ``Get_Position``
* Summary source: ``heuristic``

M01_Church_Priest_JDG
---------------------

M01_Church_Priest_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``12095``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Position``, ``Create_Sound``, ``Stop_Sound``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``, ``Start_Sound``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Chopper_JDG
-----------------------------------

M01_ChurchArea_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11989``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Rope_JDG
--------------------------------

M01_ChurchArea_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11920``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_ChurchArea_Air_Evac_Waypath_JDG
-----------------------------------

M01_ChurchArea_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``11955``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_ChurchArea_EvacMonitor_JDG
------------------------------

M01_ChurchArea_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``10153``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ChurchArea_NOD_Commander_JDG
--------------------------------

M01_ChurchArea_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``7149``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Get_Distance``, ``Action_Play_Animation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M01_ChurchArea_Spawner_Controller_JDG
-------------------------------------

M01_ChurchArea_Spawner_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6690``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Trigger_Spawner``, ``Get_Random``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ChurchArea_Spawner_Guy_JDG
------------------------------

M01_ChurchArea_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6835``
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

M01_Comm_Base_Scapegoat_JDG
---------------------------

M01_Comm_Base_Scapegoat_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``5958``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_Comm_Ceiling_Camera_JDG
---------------------------

M01_Comm_Ceiling_Camera_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``5967``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Comm_Center_Building_Script_JDG
-----------------------------------

M01_Comm_Center_Building_Script_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``10451``
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

* Source line: ``15619``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_Comm_Center_Player_Terminal_Zone
------------------------------------

M01_Comm_Center_Player_Terminal_Zone in Mission01.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events.

* Source line: ``11493``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Display_Health_Bar``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``
* Summary source: ``heuristic``

M01_COMM_Chinook_Spawned_Soldier_GDI
------------------------------------

M01_COMM_Chinook_Spawned_Soldier_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events.

* Source line: ``9901``
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

* Source line: ``11451``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_HUD_Info_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Mainframe_PogZone_02_JDG
---------------------------------

M01_Comm_Mainframe_PogZone_02_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``11465``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_HUD_Info_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Comm_Mainframe_PogZone_03_JDG
---------------------------------

M01_Comm_Mainframe_PogZone_03_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``11479``
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

* Source line: ``10376``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_Hibernation``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``, ``Find_Object``, ``Get_Max_Health``, ``Get_Max_Shield_Strength``
* Summary source: ``heuristic``

M01_Comm_Stationary_Tech_JDG
----------------------------

DECLARE_SCRIPT(M01_Comm_Base_Scapegoat_JDG, "")//this guys ID is M01_COMMCENTER_BASE_SCAPEGOAT_JDG 101938 {

* Source line: ``5998``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(M01_Comm_Base_Scapegoat_JDG, "")//this guys ID is M01_COMMCENTER_BASE_SCAPEGOAT_JDG 101938
   {
   	void Created( GameObject * obj ) override
   	{
   		Vector3 myPosition = Commands->Get_Position ( obj );
   		Commands->Set_Innate_Soldier_Home_Location ( obj, myPosition, 5 );
   	}
   };

   DECLARE_SCRIPT(M01_Comm_Ceiling_Camera_JDG, "")//this guys ID is M01_COMMCENTER_CEILING_CAMERA_JDG 101937
   {
   	void Created( GameObject * obj ) override
   	{
   		ActionParamsStruct params;

   		params.Set_Basic(this, 100, M01_START_ATTACKING_01_JDG);
   		params.Set_Attack( Commands->Find_Object (M01_COMMCENTER_BASE_SCAPEGOAT_JDG), 0, 0, true );
   		Commands->Action_Attack( obj, params );
   	}

   	void Custom( GameObject * obj, int type, uintptr_t param, GameObject * sender ) override
   	{
   		ActionParamsStruct params;

   		switch (param)
   		{
   			case M01_START_ATTACKING_01_JDG: //kane has told you to kill the scapegoat
   				{
   					if (Commands->Find_Object (M01_COMMCENTER_BASE_SCAPEGOAT_JDG))
   					{
   						params.Set_Basic(this, 100, M01_START_ATTACKING_01_JDG);
   						params.Set_Attack( Commands->Find_Object (M01_COMMCENTER_BASE_SCAPEGOAT_JDG), 100, 0, true );
   						Commands->Action_Attack( obj, params );
   					}
   				}
   				break;
   		}
   	}
   };

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

* Source line: ``15687``
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

* Source line: ``15660``
* Event hooks: ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M01_ConDropZone_JDG
-------------------

M01_ConDropZone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17964``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_ConYard_Dropoff_Dude_JDG
----------------------------

M01_ConYard_Dropoff_Dude_JDG in Mission01.cpp creates or destroys objects.

* Source line: ``17979``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_DataDisc_TextController_JDG
-------------------------------

M01_DataDisc_TextController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``21374``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Deco_LightTanks_JDG
-----------------------

M01_Deco_LightTanks_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``17053``
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

* Source line: ``13934``
* Event hooks: ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionCiv_Air_Evac_Chopper_JDG
-------------------------------------

M01_DetentionCiv_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``8337``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Set_Animation``, ``Find_Object``
* Summary source: ``heuristic``

M01_DetentionCiv_Air_Evac_Waypath_JDG
-------------------------------------

M01_DetentionCiv_Air_Evac_Waypath_JDG in Mission01.cpp responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``8309``
* Event hooks: ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_DetentionGDI_Air_Evac_Chopper_JDG
-------------------------------------

M01_DetentionGDI_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``8504``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Set_Animation``, ``Find_Object``
* Summary source: ``heuristic``

M01_DetentionGDI_Air_Evac_Waypath_JDG
-------------------------------------

M01_DetentionGDI_Air_Evac_Waypath_JDG in Mission01.cpp responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``8476``
* Event hooks: ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_DetentionPen_CivDeathMonitor
--------------------------------

M01_DetentionPen_CivDeathMonitor in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``8148``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Mission_Complete``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_DetentionPen_Evac_Controller01_JDG
--------------------------------------

M01_DetentionPen_Evac_Controller01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``8244``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Mission_Complete``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionPen_Evac_Controller02_JDG
--------------------------------------

M01_DetentionPen_Evac_Controller02_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``8428``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_DetentionPen_GDIDeathMonitor
--------------------------------

M01_DetentionPen_GDIDeathMonitor in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``8196``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Mission_Complete``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Goto``
* Summary source: ``heuristic``

M01_Duncan_Assailer_JDG
-----------------------

M01_Duncan_Assailer_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``21472``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Duncan_InHere_ConvController_JDG
------------------------------------

M01_Duncan_InHere_ConvController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``21486``
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

* Source line: ``13349``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M01_First_AutoRifle_JDG
-----------------------

M01_First_AutoRifle_JDG in Mission01.cpp responds to custom events; starts conversations.

* Source line: ``17283``
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

M01_FodderHovercraft_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates explosions.

* Source line: ``21035``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Random``, ``Apply_Damage``, ``Get_Position``, ``Create_Explosion``
* Summary source: ``heuristic``

M01_FP_BaseToBase_NorthSouth_Contoller_JDG
------------------------------------------

M01_FP_BaseToBase_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16395``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_BaseToBase_SouthNorth_Contoller_JDG
------------------------------------------

M01_FP_BaseToBase_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16460``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Start_Timer``, ``Get_Random_Int``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_GDIOcean_NorthSouth_Contoller_JDG
----------------------------------------

M01_FP_GDIOcean_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16924``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_GDIOcean_SouthNorth_Contoller_JDG
----------------------------------------

M01_FP_GDIOcean_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16989``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_Dogfight_Contoller_JDG
-------------------------------------

M01_FP_NodBase_Dogfight_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16325``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_EastWest_Contoller_JDG
-------------------------------------

M01_FP_NodBase_EastWest_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16561``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_NorthSouth_Contoller_JDG
---------------------------------------

M01_FP_NodBase_NorthSouth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16756``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_SouthNorth_Contoller_JDG
---------------------------------------

M01_FP_NodBase_SouthNorth_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16840``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_FP_NodBase_WestEast_Contoller_JDG
-------------------------------------

M01_FP_NodBase_WestEast_Contoller_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``16671``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Get_Random``
* Summary source: ``heuristic``

M01_GateSwitch_Tutorial_Zone_JDG
--------------------------------

M01_GateSwitch_Tutorial_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``18109``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_Base_Artillery_Controller_JDG
-------------------------------------

M01_GDI_Base_Artillery_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``7309``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_Random``, ``Create_Sound``, ``Monitor_Sound``, ``Find_Object``, ``Destroy_Object``, ``Create_Explosion``
* Summary source: ``heuristic``

M01_GDI_Base_Spawner_Controller_JDG
-----------------------------------

M01_GDI_Base_Spawner_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6399``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Enable_Hibernation``, ``Get_Difficulty_Level``, ``Trigger_Spawner``, ``Get_Random``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_Base_Spawner_Guy_JDG
----------------------------

M01_GDI_Base_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6521``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDI_BaseCommander_Backside_EntryZone_JDG
--------------------------------------------

M01_GDI_BaseCommander_Backside_EntryZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15373``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_BeachGuy01_JDG
----------------------

M01_GDI_BeachGuy01_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands; changes innate AI behavior.

* Source line: ``19669``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_Hibernation``, ``Action_Goto``, ``Get_Health``, ``Set_Health``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_GDI_Escort_Conversation_Controller_GDI
------------------------------------------

M01_GDI_Escort_Conversation_Controller_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; starts conversations.

* Source line: ``9274``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_GDI_GuardTower02_SniperRifle_JDG
------------------------------------

M01_GDI_GuardTower02_SniperRifle_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``19752``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_GDI_GuardTower_02_Enter_Zone_JDG
------------------------------------

M01_GDI_GuardTower_02_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``19732``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDI_GuardTower_NOD_Commander_JDG
------------------------------------

M01_GDI_GuardTower_NOD_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``14691``
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

M01_GDIBase_AI_ExitZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; updates objectives.

* Source line: ``15058``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Set_Objective_Status``
* Summary source: ``heuristic``

M01_GDIBase_BackPath_NodGuy_JDG
-------------------------------

M01_GDIBase_BackPath_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``15240``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBase_BaseCommander_JDG
-----------------------------

M01_GDIBase_BaseCommander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``18584``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Set_Objective_Status``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``, ``Create_Object``
* Summary source: ``heuristic``

M01_GDIBase_EvacMonitor_JDG
---------------------------

M01_GDIBase_EvacMonitor_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``10115``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinook_Script_JDG
-----------------------------------

M01_GDIBase_FirstChinook_Script_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``11770``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinookFlamethrowerGuy_JDG
-------------------------------------------

M01_GDIBase_FirstChinookFlamethrowerGuy_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``13541``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_FirstChinookMinigunnerGuy_JDG
-----------------------------------------

M01_GDIBase_FirstChinookMinigunnerGuy_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``17453``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_GDIBase_LightTank_JDG
-------------------------

M01_GDIBase_LightTank_JDG in Mission01.cpp responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``15122``
* Event hooks: ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Object``, ``Attach_Script``, ``Get_Position``, ``Get_Difficulty_Level``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBase_LightTank_PastTunnelZone_JDG
----------------------------------------

M01_GDIBase_LightTank_PastTunnelZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``15020``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_GDIBase_POW_Conversation_Controller_JDG
-------------------------------------------

M01_GDIBase_POW_Conversation_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``19570``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GDIBase_POWEncounter02_Controller_JDG
-----------------------------------------

M01_GDIBase_POWEncounter02_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; updates objectives; changes innate AI behavior.

* Source line: ``17736``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Set_Objective_Status``, ``Get_ID``, ``Debug_Message``, ``Get_Position``, ``Create_Object``, ``Set_Model``, ``Attach_Script``
* Summary source: ``heuristic``

M01_GDIBase_RealLightTank_JDG
-----------------------------

M01_GDIBase_RealLightTank_JDG in Mission01.cpp responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; starts conversations.

* Source line: ``17188``
* Event hooks: ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``, ``Action_Attack``
* Summary source: ``heuristic``

M01_GDIBase_SecondChinookFlamethrowerGuy_JDG
--------------------------------------------

M01_GDIBase_SecondChinookFlamethrowerGuy_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``13562``
* Event hooks: ``Created``, ``Killed``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_GDIBase_SecondChinookMinigunnerGuy_JDG
------------------------------------------

M01_GDIBase_SecondChinookMinigunnerGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``13597``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Chopper_JDG
-----------------------------------------

M01_GDIBaseCommander_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``17474``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Rope_JDG
--------------------------------------

M01_GDIBaseCommander_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13396``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBaseCommander_Air_Evac_Waypath_JDG
-----------------------------------------

M01_GDIBaseCommander_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13362``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBaseCommander_EvacController_JDG
---------------------------------------

M01_GDIBaseCommander_EvacController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``17577``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Debug_Message``, ``Get_ID``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Chopper_JDG
-----------------------------------

M01_GDIBasePOW_Air_Evac_Chopper_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``17869``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Debug_Message``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Rope_JDG
--------------------------------

M01_GDIBasePOW_Air_Evac_Rope_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13271``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GDIBasePOW_Air_Evac_Waypath_JDG
-----------------------------------

M01_GDIBasePOW_Air_Evac_Waypath_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``13308``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Debug_Message``, ``Set_Animation``
* Summary source: ``heuristic``

M01_GiveMCTSpeech_Zone_JDG
--------------------------

M01_GiveMCTSpeech_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``20516``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``, ``Get_ID``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M01_GuardTower02_NewSniperTarget_JDG
------------------------------------

M01_GuardTower02_NewSniperTarget_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``19958``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Action_Attack``, ``Send_Custom_Event``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_Target01_JDG
------------------------------------

M01_GuardTower02_Sniper_Target01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``19772``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_ID``, ``Action_Goto``, ``Find_Object``, ``Action_Reset``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_Target02_JDG
------------------------------------

M01_GuardTower02_Sniper_Target02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``20020``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Reset``
* Summary source: ``heuristic``

M01_GuardTower02_Sniper_TowerZone_JDG
-------------------------------------

M01_GuardTower02_Sniper_TowerZone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``19897``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_GuardTower_Sniper_Target_JDG
--------------------------------

M01_GuardTower_Sniper_Target_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``7500``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Action_Goto``, ``Get_Position``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Action_Play_Animation``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   wave_location:vector3,  delete_location:vector3

M01_Gunboat_Spawn_Hovercraft_Zone_JDG
-------------------------------------

M01_Gunboat_Spawn_Hovercraft_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``7598``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_GunboatAction_Controller_JDG
--------------------------------

M01_GunboatAction_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``18312``
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

* Source line: ``7642``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Action_Goto``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Create_Sound``, ``Create_Object``
* Summary source: ``heuristic``

M01_Havoc_In_WarroomZone_JDG
----------------------------

M01_Havoc_In_WarroomZone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``20641``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Havoc_Out_WarroomZone_JDG
-----------------------------

M01_Havoc_Out_WarroomZone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``20656``
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

* Source line: ``20160``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_02_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_02_GDI_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``20369``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_03_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_03_GDI_JDG in Mission01.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``8802``
* Event hooks: ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``
* Summary source: ``heuristic``

M01_HON_Chinook_Spawned_Soldier_04_GDI_JDG
------------------------------------------

M01_HON_Chinook_Spawned_Soldier_04_GDI_JDG in Mission01.cpp responds to custom events; drives AI action commands; sends custom events.

* Source line: ``8854``
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

* Source line: ``11148``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_ID``, ``Create_Sound``, ``Action_Play_Animation``, ``Action_Goto``, ``Action_Reset``, ``Get_Position``, ``Get_Random``
* Summary source: ``heuristic``

M01_HON_Dojo_Trainer_JDG
------------------------

M01_HON_Dojo_Trainer_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``10983``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Get_Random``, ``Send_Custom_Event``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
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
* Key engine calls: ``Innate_Disable``, ``Set_Facing``, ``Send_Custom_Event``, ``Find_Object``, ``Innate_Enable``, ``Action_Play_Animation``, ``Enable_Hibernation``, ``Get_Random``
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

* Source line: ``8727``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_Hibernation``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``, ``Find_Object``, ``Get_Max_Health``, ``Get_Max_Shield_Strength``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Commander_JDG
-----------------------------------------

M01_HON_Escorts_Warroom_MCT_Commander_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``8673``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Protector01_JDG
-------------------------------------------

M01_HON_Escorts_Warroom_MCT_Protector01_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``8709``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_Protector02_JDG
-------------------------------------------

M01_HON_Escorts_Warroom_MCT_Protector02_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``8717``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_HON_Escorts_Warroom_MCT_ZoneController_JDG
----------------------------------------------

M01_HON_Escorts_Warroom_MCT_ZoneController_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``20132``
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

* Source line: ``2524``
* Event hooks: ``Created``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Enable_Hibernation``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_HON_Paintball_Team_01_JDG
-----------------------------

M01_HON_Paintball_Team_01_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``10695``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Set_Player_Type``, ``Set_Obj_Radar_Blip_Color``, ``Get_Position``, ``Get_Random``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_HON_Paintball_Team_02_JDG
-----------------------------

M01_HON_Paintball_Team_02_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``10836``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Get_Position``, ``Get_Random``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``, ``Set_Innate_Soldier_Home_Location``, ``Start_Timer``, ``Find_Object``
* Summary source: ``heuristic``

M01_HON_RedKey_Zone_JDG
-----------------------

M01_HON_RedKey_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``15600``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_HON_WarroomController_JDG
-----------------------------

M01_HON_WarroomController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``20671``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Find_Object``, ``Apply_Damage``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Hovercraft_Explosion_Controller_JDG
---------------------------------------

M01_Hovercraft_Explosion_Controller_JDG in Mission01.cpp responds to custom events; creates or destroys objects.

* Source line: ``21002``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Destroy_Object``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Hunt_The_Player_JDG
-----------------------

M01_Hunt_The_Player_JDG in Mission01.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``8616``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Start_Timer``, ``Action_Goto``, ``Get_Position``, ``Get_Distance``, ``Is_Object_Visible``, ``Apply_Damage``
* Summary source: ``heuristic``

M01_Initial_Gunboat_Script_JDG
------------------------------

M01_Initial_Gunboat_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``18384``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Action_Attack``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M01_Interior_Nun_Conversation_Zone_JDG
--------------------------------------

M01_Interior_Nun_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``9165``
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

* Source line: ``15043``
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

* Source line: ``9128``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Mainframe_Tutorial_Zone_JDG
-------------------------------

M01_Mainframe_Tutorial_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``18096``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Medium_Tank01_JDG
---------------------

M01_Medium_Tank01_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``20770``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Medium_Tank_JDG
-------------------

M01_Medium_Tank_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``20836``
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

* Source line: ``19182``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``, ``Find_Object``, ``Monitor_Conversation``, ``Start_Timer``, ``Get_ID``
* Summary source: ``heuristic``

M01_Medlab_Datadisc_JDG
-----------------------

M01_Medlab_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21356``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Reveal_Map``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_MiniGunner_Point_Guard_JDG
------------------------------

M01_MiniGunner_Point_Guard_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``4672``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Difficulty_Level``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M01_Mission_Controller_JDG
--------------------------

M01_Mission_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; plays sounds; updates objectives; starts conversations.

* Source line: ``53``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Clouds``, ``Set_Wind``, ``Set_Rain``, ``Set_Lightning``, ``Reveal_Encyclopedia_Character``, ``Reveal_Encyclopedia_Weapon``, ``Reveal_Encyclopedia_Vehicle``
* Summary source: ``heuristic``

M01_MovieProjector_JDG
----------------------

M01_MovieProjector_JDG in Mission01.cpp initializes behavior when the object is created; sends custom events; creates explosions; controls animation playback.

* Source line: ``10189``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Explosion``, ``Set_Health``
* Summary source: ``heuristic``

M01_Nod_Chinook_Reinforcement_Guy_JDG
-------------------------------------

M01_Nod_Chinook_Reinforcement_Guy_JDG in Mission01.cpp drives AI action commands; sends custom events.

* Source line: ``8595``
* Event hooks: ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Nod_Commander_Conversation_Controller_GDI
---------------------------------------------

M01_Nod_Commander_Conversation_Controller_GDI in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``14938``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Get_Random_Int``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Nod_GuardTower_01_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_01_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7437``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_02_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_02_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7457``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_03_Enter_Zone_JDG
------------------------------------

M01_Nod_GuardTower_03_Enter_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``7477``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Nod_GuardTower_Tailgun_JDG
------------------------------

M01_Nod_GuardTower_Tailgun_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``11440``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Attack``
* Summary source: ``heuristic``

M01_Nod_Truck_JDG
-----------------

M01_Nod_Truck_JDG in Mission01.cpp initializes behavior when the object is created.

* Source line: ``18067``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Obj_Radar_Blip_Color``
* Summary source: ``heuristic``

M01_Obelisk_UpdateDisc_JDG
--------------------------

M01_Obelisk_UpdateDisc_JDG in Mission01.cpp responds to custom events.

* Source line: ``15417``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Building``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Objective_Pog_Controller_JDG
--------------------------------

M01_Objective_Pog_Controller_JDG in Mission01.cpp responds to custom events; sends custom events; updates objectives; starts conversations.

* Source line: ``11554``
* Event hooks: ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Set_Objective_Radar_Blip``, ``Set_Objective_HUD_Info_Position``, ``Set_HUD_Help_Text``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M01_PaintballRoom_ChatterController_JDG
---------------------------------------

M01_PaintballRoom_ChatterController_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``10481``
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

* Source line: ``15310``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_PlayerLeaving_BarnArea_Zone_JDG
-----------------------------------

M01_PlayerLeaving_BarnArea_Zone_JDG in Mission01.cpp watches enter or exit events; sends custom events.

* Source line: ``15331``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_POW_Nod_Minigunner01_JDG
----------------------------

M01_POW_Nod_Minigunner01_JDG in Mission01.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``17715``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M01_Priest_Conversation_Zone_JDG
--------------------------------

M01_Priest_Conversation_Zone_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``9091``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_Priest_Datadisc_JDG
-----------------------

M01_Priest_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21309``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_PrisonPen_Civilian_JDG
--------------------------

M01_PrisonPen_Civilian_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``14283``
* Event hooks: ``Created``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Get_ID``, ``Start_Timer``, ``Get_Random``, ``Action_Goto``, ``Find_Object``
* Summary source: ``heuristic``

M01_PrisonPen_POW_JDG
---------------------

M01_PrisonPen_POW_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``14021``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``, ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Innate_Disable``, ``Action_Attack``, ``Get_Random``
* Summary source: ``heuristic``

M01_Propaganda_Sounds_Controller_JDG
------------------------------------

M01_Propaganda_Sounds_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``10224``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``, ``Send_Custom_Event``, ``Get_Random_Int``, ``Create_Object``, ``Get_ID``, ``Create_Sound``, ``Monitor_Sound``
* Summary source: ``heuristic``

M01_QuickSave_Zone_JDG
----------------------

M01_QuickSave_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17462``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_RealLightTank_TriggerZone_JDG
---------------------------------

M01_RealLightTank_TriggerZone_JDG in Mission01.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; plays sounds.

* Source line: ``17251``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_2D_Sound``
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

* Source line: ``21214``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_Sinking_Gunboat_JDG
-----------------------

M01_Sinking_Gunboat_JDG in Mission01.cpp initializes behavior when the object is created; creates or destroys objects; controls animation playback.

* Source line: ``15293``
* Event hooks: ``Created``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_SniperRifle_01_JDG
----------------------

M01_SniperRifle_01_JDG in Mission01.cpp responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``17330``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M01_SniperRifle_01_Target_JDG
-----------------------------

M01_SniperRifle_01_Target_JDG in Mission01.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``17348``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Enable_Hibernation``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M01_SniperRifle_02_AirdropZone_JDG
----------------------------------

M01_SniperRifle_02_AirdropZone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``17392``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_SniperRifle_02_JDG
----------------------

M01_SniperRifle_02_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``17377``
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

* Source line: ``6533``
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

DECLARE_SCRIPT(M01_BarnArea_NOD_Commander_JDG, "")//M01_BARNAREA_NOD_COMMANDER_02_JDG 102476 {

* Source line: ``6989``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Get_Distance``, ``Action_Play_Animation``, ``Send_Custom_Event``, ``Get_Difficulty_Level``, ``Find_Object``, ``Get_Random``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(M01_BarnArea_NOD_Commander_JDG, "")//M01_BARNAREA_NOD_COMMANDER_02_JDG 102476
   {
   	bool deadYet;
   	bool firstTimeDamaged;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE(deadYet, 1);
   		SAVE_VARIABLE(firstTimeDamaged, 2);
   	}

   	void Created( GameObject * obj ) override
   	{
   		deadYet = false;
   		firstTimeDamaged = true;

   		Vector3 myPosition = Commands->Get_Position ( obj );
   		Commands->Set_Innate_Soldier_Home_Location ( obj, myPosition, 10 );
   	}

   	void Damaged( GameObject * obj, GameObject * damager, float amount ) override
   	{
   		if (obj)
   		{
   			if (damager == STAR && deadYet == false && firstTimeDamaged == true)
   			{
   				Vector3 myPosition = Commands->Get_Position ( obj );
   				Vector3 playerPosition = Commands->Get_Position ( STAR );
   				float playerDistance = Commands->Get_Distance ( myPosition, playerPosition );

   				if (playerDistance >= 15)
   				{
   					firstTimeDamaged = false;
   					ActionParamsStruct params;
   					params.Set_Basic( this, 100, M01_DOING_ANIMATION_02_JDG );
   					params.Set_Animation( "H_A_J21C", false );
   					Commands->Action_Play_Animation (  obj, params );
   				}
   			}
   		}
   	}

   	void Killed( GameObject * obj, GameObject * killer ) override
   	{
   		deadYet = true;
   	}

   	void Custom( GameObject * obj, int type, uintptr_t param, GameObject * sender ) override
   	{
   		if (type == 0)
   		{
   			switch (param)
   			{
   				case M01_START_ACTING_JDG: //set timer--then call in next reinforcements
   					{
   						Commands->Send_Custom_Event( obj, obj, 0, M01_MODIFY_YOUR_ACTION_JDG, 0 );
   						Commands->Send_Custom_Event( obj, obj, 0, M01_CALL_IN_REINFORCEMENTS_JDG, 0 );
   					}
   					break;

   				case M01_MODIFY_YOUR_ACTION_JDG://here comes player start calling in reinforcements
   					{
   						if (obj)
   						{
   							int currentDifficulty = Commands->Get_Difficulty_Level( );
   							int medium = 1;
   							int hard = 2;
   							float delayTimer;

   							if (currentDifficulty == hard)
   							{
   								delayTimer = 60;
   							}

   							else if (currentDifficulty == medium)
   							{
   								delayTimer = 90;
   							}

   							else
   							{
   								delayTimer = 120;
   							}

   							Commands->Send_Custom_Event( obj, obj, 0, M01_SEND_BARN_CHINOOK_JDG, delayTimer );
   							Commands->Send_Custom_Event( obj, obj, 0, M01_MODIFY_YOUR_ACTION_JDG, delayTimer );
   						}
   					}
   					break;

   				case M01_SEND_BARN_CHINOOK_JDG: //here comes player start calling in reinforcements
   					{
   						if (obj)
   						{
   							Commands->Send_Custom_Event( obj, Commands->Find_Object ( M01_MISSION_CONTROLLER_JDG ), 0, M01_SEND_BARN_CHINOOK_JDG, 0 );
   						}
   					}
   					break;

   				case M01_CALL_IN_REINFORCEMENTS_JDG: //here comes player start calling in reinforcements
   					{
   						if (obj && deadYet == false)
   						{
   							GameObject * nodCommanderDialogController = Commands->Find_Object ( 103398 );
   							if (nodCommanderDialogController != NULL)
   							{
   								Commands->Send_Custom_Event( obj, nodCommanderDialogController, 0, M01_MODIFY_YOUR_ACTION_JDG, 0 );
   							}
   							float delayTimer = Commands->Get_Random ( 15, 30 );
   							Commands->Send_Custom_Event( obj, obj, 0, M01_CALL_IN_REINFORCEMENTS_JDG, delayTimer );
   						}
   					}
   					break;
   			}
   		}
   	}
   };

M01_TailgunRun_Spawner_Guy_JDG
------------------------------

M01_TailgunRun_Spawner_Guy_JDG in Mission01.cpp reacts to destruction state; sends custom events.

* Source line: ``6678``
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
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Set_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TibCave01_Datadisc_JDG
--------------------------

M01_TibCave01_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21165``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_TibCave02_Datadisc_JDG
--------------------------

M01_TibCave02_Datadisc_JDG in Mission01.cpp responds to custom events; sends custom events.

* Source line: ``21257``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

M01_TibCave_StartZone_JDG
-------------------------

M01_TibCave_StartZone_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``13663``
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

* Source line: ``13870``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TiberiumCave_UpThere_NodGuy_JDG
-----------------------------------

M01_TiberiumCave_UpThere_NodGuy_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``13896``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Attack``, ``Send_Custom_Event``, ``Create_Sound``
* Summary source: ``heuristic``

M01_TibField_Guard01_New_JDG
----------------------------

M01_TibField_Guard01_New_JDG in Mission01.cpp responds to custom events; starts conversations.

* Source line: ``7748``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M01_TriggerZone_GDIBase_BaseCommander_JDG
-----------------------------------------

M01_TriggerZone_GDIBase_BaseCommander_JDG in Mission01.cpp watches enter or exit events; sends custom events; creates or destroys objects; updates objectives.

* Source line: ``13439``
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

* Source line: ``6847``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TurnOff_TankReminder_Zone_JDG
---------------------------------

M01_TurnOff_TankReminder_Zone_JDG in Mission01.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``20116``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M01_TurretBeach_Chinook_Spawned_Soldier_NOD
-------------------------------------------

M01_TurretBeach_Chinook_Spawned_Soldier_NOD in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``16053``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Action_Goto``, ``Innate_Enable``, ``Action_Reset``, ``Debug_Message``, ``Enable_Hibernation``, ``Get_Health``
* Summary source: ``heuristic``

M01_TurretBeach_Engineer_JDG
----------------------------

M01_TurretBeach_Engineer_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``15771``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Get_Max_Health``, ``Action_Reset``, ``Innate_Enable``, ``Innate_Force_State_Enemy_Seen``, ``Get_ID``, ``Debug_Message``, ``Find_Object``
* Summary source: ``heuristic``

M01_TurretBeach_FodderHovercraft_Controller_JDG
-----------------------------------------------

M01_TurretBeach_FodderHovercraft_Controller_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``20936``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Get_ID``
* Summary source: ``heuristic``

M01_TurretBeach_GDI_Guy_01_JDG
------------------------------

M01_TurretBeach_GDI_Guy_01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``8011``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Reset``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M01_TurretBeach_GDI_Guy_02_JDG
------------------------------

M01_TurretBeach_GDI_Guy_02_JDG in Mission01.cpp drives AI action commands.

* Source line: ``8101``
* Event hooks: ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M01_TurretBeach_Turret_01_Script_JDG
------------------------------------

M01_TurretBeach_Turret_01_Script_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``18181``
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

* Source line: ``17423``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M01_Visceroid01_JDG
-------------------

M01_Visceroid01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13706``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid02_JDG
-------------------

M01_Visceroid02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13739``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid03_JDG
-------------------

M01_Visceroid03_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13772``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid_NodGuy01_JDG
--------------------------

M01_Visceroid_NodGuy01_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13801``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Create_Sound``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M01_Visceroid_NodGuy02_JDG
--------------------------

M01_Visceroid_NodGuy02_JDG in Mission01.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``13835``
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
* Key engine calls: ``Innate_Disable``, ``Get_Max_Health``, ``Action_Goto``, ``Innate_Enable``, ``Action_Play_Animation``, ``Action_Reset``, ``Grant_Key``, ``Action_Attack``
* Summary source: ``heuristic``
