Mission04.cpp
=============

* Category: ``mission``
* Indexed registrations: ``138``
* Source: ``Code/Scripts/Mission04.cpp``

M04_A01_PatrolGuy_01_JDG
------------------------

M04_A01_PatrolGuy_01_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``1160``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_A01_Sniper_JDG
------------------

M04_A01_Sniper_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1040``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Reset``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_FirstMateBodyguard_JDG
------------------------------

M04_Aft_FirstMateBodyguard_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``3951``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M04_Aft_LeftBarracks_TalkGuy_JDG
--------------------------------

M04_Aft_LeftBarracks_TalkGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4087``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_LockerRoom_PatrolGuy01_JDG
----------------------------------

M04_Aft_LockerRoom_PatrolGuy01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4111``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_LockerRoom_PatrolGuy02_JDG
----------------------------------

M04_Aft_LockerRoom_PatrolGuy02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4178``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_RightBarracks_PatrolGuy_JDG
-----------------------------------

M04_Aft_RightBarracks_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4020``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_AftDeck_02_Blackhand_PatrolGuy_JDG
--------------------------------------

M04_AftDeck_02_Blackhand_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4366``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Attack``, ``Action_Goto``
* Summary source: ``heuristic``

M04_AftDeck_02_Controller_JDG
-----------------------------

M04_AftDeck_02_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``3564``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Get_ID``, ``Send_Custom_Event``, ``Trigger_Spawner``, ``Get_Random``, ``Set_Facing``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_Entry_Zone_JDG
-----------------------------

M04_AftDeck_02_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4501``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_PatrolGuy_01_JDG
-------------------------------

M04_AftDeck_02_PatrolGuy_01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4277``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_PatrolGuy_02_JDG
-------------------------------

M04_AftDeck_02_PatrolGuy_02_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4321``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_Pointguard_JDG
-----------------------------

M04_AftDeck_02_Pointguard_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``4480``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_InnerSanctum_02_Entry_Zone_JDG
------------------------------------------

M04_AftDeck_InnerSanctum_02_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3551``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_AftDeck_InnerSanctum_Entry_Zone_JDG
---------------------------------------

The following scripts all deal with the aft deck on the way to kill the first mate.

* Source line: ``3533``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts all deal with the aft deck on the way to kill the first mate.

M04_AftDeck_Reinforcement_JDG
-----------------------------

M04_AftDeck_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4245``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Grant_Key``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Announce_Keycard_02_Objective_Zone_JDG
------------------------------------------

M04_Announce_Keycard_02_Objective_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7846``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Apache_Enter_Zone_JDG
-------------------------

The following are all the temp scripts for the apache hanger

* Source line: ``4551``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following are all the temp scripts for the apache hanger

M04_Apache_GoBackToHangar_EntryZone_JDG
---------------------------------------

M04_Apache_GoBackToHangar_EntryZone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``8632``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_ApacheRoom_Apache_JDG
-------------------------

M04_ApacheRoom_Apache_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``8671``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Action_Goto``, ``Disable_Physical_Collisions``, ``Enable_Collisions``, ``Modify_Action``
* Summary source: ``heuristic``

M04_ApacheRoom_Controller_JDG
-----------------------------

M04_ApacheRoom_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``4584``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Set_Facing``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_BottomFloor_JDG
-----------------------------------------------

M04_ApacheRoom_Second_EntryZone_BottomFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8546``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_MiddleFloor_JDG
-----------------------------------------------

M04_ApacheRoom_Second_EntryZone_MiddleFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8460``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_TopFloor_JDG
--------------------------------------------

M04_ApacheRoom_Second_EntryZone_TopFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8374``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Sniper01_JDG
---------------------------

M04_ApacheRoom_Sniper01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4635``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_ApacheRoom_Sniper02_JDG
---------------------------

M04_ApacheRoom_Sniper02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4702``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_BH_MessHall_Guy_JDG
-----------------------

M04_BH_MessHall_Guy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands.

* Source line: ``5301``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Find_Object``, ``Action_Attack``, ``Get_Random``, ``Trigger_Spawner``, ``Attach_Script``
* Summary source: ``heuristic``

M04_BH_MessHall_Trigger_Zone_JDG
--------------------------------

M04_BH_MessHall_Trigger_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5283``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Sound``, ``Get_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_BigSam_EntryZone_JDG
------------------------

M04_BigSam_EntryZone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``10146``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_BigSam_Script_JDG
---------------------

M04_BigSam_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates explosions; controls animation playback; plays sounds.

* Source line: ``10188``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Set_Animation``, ``Send_Custom_Event``, ``Action_Attack``, ``Create_Explosion``, ``Set_Health``, ``Create_2D_Sound``, ``Monitor_Sound``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_JDG
--------------------------

M04_Captains_Bodyguard_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state.

* Source line: ``5159``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Random``, ``Trigger_Spawner``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_Reinforcement02_JDG
------------------------------------------

M04_Captains_Bodyguard_Reinforcement02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5235``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Get_Position``, ``Action_Reset``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_Reinforcement_JDG
----------------------------------------

M04_Captains_Bodyguard_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5187``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Reset``, ``Get_Position``
* Summary source: ``heuristic``

M04_Captains_Bridge_Enter_Zone_JDG
----------------------------------

M04_Captains_Bridge_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5263``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Sound``, ``Get_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_CargoHold_Blackhand_01_JDG
------------------------------

M04_CargoHold_Blackhand_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``1953``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Reset``, ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Random``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_CargoHold_Blackhand_02_JDG
------------------------------

M04_CargoHold_Blackhand_02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2068``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_CargoHold_Stationary_Officer_JDG
------------------------------------

M04_CargoHold_Stationary_Officer_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``8963``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M04_CargoHold_TalkGuy01_JDG
---------------------------

M04_CargoHold_TalkGuy01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1470``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``, ``Get_Random``, ``Action_Play_Animation``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_CargoHold_TalkGuy02_JDG
---------------------------

M04_CargoHold_TalkGuy02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1553``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``, ``Get_Random``, ``Action_Play_Animation``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_CargoHold_TalkGuy03_JDG
---------------------------

M04_CargoHold_TalkGuy03_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1636``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``, ``Get_Random``, ``Action_Play_Animation``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_CargoMissileRooms_Dude_Controller_JDG
-----------------------------------------

M04_CargoMissileRooms_Dude_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``1219``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Set_Facing``, ``Get_ID``, ``Send_Custom_Event``, ``Get_Random``
* Summary source: ``heuristic``

M04_Catwalk_Enter_Zone_01_JDG
-----------------------------

M04_Catwalk_Enter_Zone_01_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6219``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Catwalk_Enter_Zone_02_JDG
-----------------------------

M04_Catwalk_Enter_Zone_02_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6233``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Cooks_Script_JDG
--------------------

M04_Cooks_Script_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``6645``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``
* Summary source: ``heuristic``

M04_Doorway_Enterer_JDG
-----------------------

M04_Doorway_Enterer_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``6247``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Enable_Hibernation``, ``Grant_Key``, ``Action_Goto``, ``Get_Random_Int``, ``Create_Object``, ``Action_Play_Animation``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

Parameter Description::

   first_location:vector3

M04_EngineRoom_BuildingController_JDG
-------------------------------------

M04_EngineRoom_BuildingController_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; plays sounds.

* Source line: ``2181``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Stop_Sound``, ``Debug_Message``, ``Apply_Damage``, ``Create_2D_Sound``, ``Enable_Spawner``, ``Find_Object``, ``Get_Random``
* Summary source: ``heuristic``

M04_EngineRoom_ChiefEngineer_JDG
--------------------------------

M04_EngineRoom_ChiefEngineer_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``2342``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Footsteps_Heard``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``, ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Create_Sound``
* Summary source: ``heuristic``

M04_EngineRoom_EnterZone_JDG
----------------------------

The following scripts deal with the engine room--first time through

* Source line: ``2157``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts deal with the engine room--first time through

M04_EngineRoom_LiftEngineer_JDG
-------------------------------

M04_EngineRoom_LiftEngineer_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``2779``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M04_EngineRoom_Prison_Guard_01_JDG
----------------------------------

M04_EngineRoom_Prison_Guard_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; starts conversations.

* Source line: ``2814``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_EngineRoom_Prison_Guard_02_JDG
----------------------------------

M04_EngineRoom_Prison_Guard_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``2953``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``, ``Action_Reset``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_01_JDG
------------------------------

M04_EngineRoom_Prisoner_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3068``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``, ``Action_Play_Animation``, ``Find_Object``, ``Send_Custom_Event``, ``Action_Attack``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_02_JDG
------------------------------

M04_EngineRoom_Prisoner_02_JDG in Mission04.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``3250``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_03_JDG
------------------------------

M04_EngineRoom_Prisoner_03_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3353``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Play_Animation``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``, ``Action_Reset``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_EngineRoom_PrisonLift_EnterZone_JDG
---------------------------------------

M04_EngineRoom_PrisonLift_EnterZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``2748``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_SniperScript_JDG
-------------------------------

M04_EngineRoom_SniperScript_JDG in Mission04.cpp initializes behavior when the object is created; creates or destroys objects.

* Source line: ``7883``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Difficulty_Level``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Start_Guard_Conversation_Zone_JDG
------------------------------------------------

M04_EngineRoom_Start_Guard_Conversation_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``2790``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Stationary_Tech_JDG
----------------------------------

M04_EngineRoom_Stationary_Tech_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``6050``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Loiters_Allowed``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``, ``Get_Random``, ``Debug_Message``
* Summary source: ``heuristic``

Parameter Description::

   Console_ID :int

M04_EngineRoom_TalkToPrisoners_Zone_JDG
---------------------------------------

M04_EngineRoom_TalkToPrisoners_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3041``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target01_JDG
---------------------------

M04_EngineRoom_Target01_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8262``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target02_JDG
---------------------------

M04_EngineRoom_Target02_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8290``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target03_JDG
---------------------------

M04_EngineRoom_Target03_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8318``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target04_JDG
---------------------------

M04_EngineRoom_Target04_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8346``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EnterCargoBay_BottomRight_Zone_JDG
--------------------------------------

M04_EnterCargoBay_BottomRight_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5862``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EnterCargoBay_TopLeft_Zone_JDG
----------------------------------

M04_EnterCargoBay_TopLeft_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5887``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Firefight_Controller_JDG
----------------------------

M04_Firefight_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``9085``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Mission_Complete``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Firefight_NodGuys
---------------------

M04_Firefight_NodGuys in Mission04.cpp reacts to destruction state; sends custom events.

* Source line: ``5503``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Firefight_Prisoner
----------------------

M04_Firefight_Prisoner in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; starts conversations.

* Source line: ``8971``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Health``, ``Get_Max_Health``, ``Set_HUD_Help_Text``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Firefight_RallyZone
-----------------------

M04_Firefight_RallyZone in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``9384``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_Difficulty_Level``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_Firefight_Start_Battle_Music_JDG
------------------------------------

The following are the scripts and controller for the end fire fight.

* Source line: ``5472``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   The following are the scripts and controller for the end fire fight.

M04_ForeDeck_ClosetSurprise_Guy_JDG
-----------------------------------

M04_ForeDeck_ClosetSurprise_Guy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``5363``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Goto``, ``Get_Position``
* Summary source: ``heuristic``

M04_ForeDeck_ClosetSurprise_Trigger_Zone_JDG
--------------------------------------------

M04_ForeDeck_ClosetSurprise_Trigger_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5402``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ForeDeck_Controller_JDG
---------------------------

The following scripts are for the foredeck. They include both the messhalls and the captain's encounter.

* Source line: ``4958``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Get_ID``, ``Trigger_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts are for the foredeck.  They include both the messhalls and the captain's encounter.

M04_ForeDeck_Initial_Enter_Zone_JDG
-----------------------------------

M04_ForeDeck_Initial_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4789``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ForeDeck_MapRoom_Guard01_JDG
--------------------------------

M04_ForeDeck_MapRoom_Guard01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``4866``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_ForeDeck_MapRoom_Guard02_JDG
--------------------------------

M04_ForeDeck_MapRoom_Guard02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4880``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_ForeDeck_Reinforcement_JDG
------------------------------

M04_ForeDeck_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4836``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_ForeDeck_RocketGuy_JDG
--------------------------

The following are the initial scripts for the fore deck

* Source line: ``4773``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``source comment``

Source Notes::

   The following are the initial scripts for the fore deck

M04_ForeDeck_TorpedoRoom_Guard_JDG
----------------------------------

M04_ForeDeck_TorpedoRoom_Guard_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``4947``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_Front_ofThe_Boat_Population_JDG
-----------------------------------

M04_Front_ofThe_Boat_Population_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``6636``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_GruntMessHall_Entry_Zone_JDG
--------------------------------

M04_GruntMessHall_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5445``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_GruntMessHall_Exit_Zone_JDG
-------------------------------

M04_GruntMessHall_Exit_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5428``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Hunter_Controller_JDG
-------------------------

M04_Hunter_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``6343``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Object``, ``Get_ID``, ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Hunter_JDG
--------------

M04_Hunter_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``6420``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Enable_Hibernation``, ``Send_Custom_Event``, ``Action_Goto``, ``Get_Position``, ``Get_Distance``, ``Find_Object``
* Summary source: ``heuristic``

M04_Keycard_01_Script_JDG
-------------------------

M04_Keycard_01_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``7510``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Keycard_02_Script_JDG
-------------------------

M04_Keycard_02_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7526``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Keycard_03_Script_JDG
-------------------------

M04_Keycard_03_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7568``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``
* Summary source: ``heuristic``

M04_MedLab_Enter_Zone_JDG
-------------------------

M04_MedLab_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4812``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_MedLab_Tech_JDG
-------------------

M04_MedLab_Tech_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``7718``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Find_Object``, ``Action_Attack``, ``Action_Goto``, ``Action_Reset``, ``Get_Position``, ``Action_Face_Location``
* Summary source: ``heuristic``

M04_MissileRoom_EnterZone_Left_JDG
----------------------------------

The following scripts all deal with the first time through the cargo and missile rooms.

* Source line: ``1171``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts all deal with the first time through the cargo and missile rooms.

M04_MissileRoom_EnterZone_Right_JDG
-----------------------------------

M04_MissileRoom_EnterZone_Right_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``1195``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_MissileRoom_Guard_01_JDG
----------------------------

M04_MissileRoom_Guard_01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1729``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Guard_02_JDG
----------------------------

M04_MissileRoom_Guard_02_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1841``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_ObjectiveZone_JDG
---------------------------------

M04_MissileRoom_ObjectiveZone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7821``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_MissileRoom_Target01_JDG
----------------------------

M04_MissileRoom_Target01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``7898``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target02_JDG
----------------------------

M04_MissileRoom_Target02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``7989``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target03_JDG
----------------------------

M04_MissileRoom_Target03_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``8080``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target04_JDG
----------------------------

M04_MissileRoom_Target04_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``8171``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_UpperGuard_01_JDG
---------------------------------

M04_MissileRoom_UpperGuard_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``1392``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Attach_Script``
* Summary source: ``heuristic``

M04_MissileRoom_UpperGuard_02_JDG
---------------------------------

M04_MissileRoom_UpperGuard_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``1431``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Goto``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Mutant_UpdateDisc_JDG
-------------------------

M04_Mutant_UpdateDisc_JDG in Mission04.cpp responds to custom events.

* Source line: ``9522``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Character``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M04_Objective_Controller_JDG
----------------------------

M04_Objective_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``44``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Add_Objective``, ``Add_Radar_Marker``, ``Get_Position``, ``Find_Object``, ``Set_Objective_HUD_Info_Position``, ``Set_Obj_Radar_Blip_Shape``
* Summary source: ``heuristic``

M04_Objective_Reminder_Controller_JDG
-------------------------------------

M04_Objective_Reminder_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``10290``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Player_Is_Leaving_Aft_Deck_JDG
----------------------------------

M04_Player_Is_Leaving_Aft_Deck_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3997``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_PlaySound_OnZoneEntry_OneTime_JDG
-------------------------------------

M04_PlaySound_OnZoneEntry_OneTime_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``10256``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Random``, ``Create_Sound``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   SoundName:string

M04_Pog_Controller_JDG
----------------------

M04_Pog_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``9665``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Set_Objective_HUD_Info_Position``, ``Set_Objective_HUD_Info``
* Summary source: ``heuristic``

M04_PointGuard_JDG
------------------

The following are the scripts for the dudes in the sub bay when the mission first starts.

* Source line: ``1024``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``source comment``

Source Notes::

   The following are the scripts for the dudes in the sub bay when the mission first starts.

M04_PostFirstMate_FrontDeck_PatrolGuy01_JDG
-------------------------------------------

M04_PostFirstMate_FrontDeck_PatrolGuy01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5751``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_FrontDeck_PatrolGuy02_JDG
-------------------------------------------

M04_PostFirstMate_FrontDeck_PatrolGuy02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5806``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_MissileRoom_PatrolGuy_JDG
-------------------------------------------

M04_PostFirstMate_MissileRoom_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5605``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_OfficerQuarters_PatrolGuy_JDG
-----------------------------------------------

M04_PostFirstMate_OfficerQuarters_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5696``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_SamRoom_PatrolGuy_JDG
---------------------------------------

M04_PostFirstMate_SamRoom_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5514``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Prison_CellDoor_Zone_JDG
----------------------------

M04_Prison_CellDoor_Zone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3462``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Has_Key``, ``Find_Object``, ``Destroy_Object``, ``Set_Position``, ``Set_Facing``, ``Control_Enable``, ``Set_Is_Rendered``
* Summary source: ``heuristic``

M04_Prison_Keycard_CheckZone_JDG
--------------------------------

M04_Prison_Keycard_CheckZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6654``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Prison_Warden_JDG
---------------------

M04_Prison_Warden_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; creates or destroys objects; starts conversations.

* Source line: ``7669``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M04_Prisoners_Rescued_Controller_JDG
------------------------------------

The Following are all the scripts associated with the objectives...including controller

* Source line: ``7799``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Set_Position``, ``Set_Facing``, ``Control_Enable``, ``Set_Is_Rendered``
* Summary source: ``source comment``

Source Notes::

   The Following are all the scripts associated with the objectives...including controller

M04_RocketEmplacement_01_JDG
----------------------------

M04_RocketEmplacement_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``5910``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_RocketEmplacement_02_JDG
----------------------------

M04_RocketEmplacement_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6007``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_SecondaryApache01_JDG
-------------------------

M04_SecondaryApache01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``5953``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_SecondaryApache02_JDG
-------------------------

M04_SecondaryApache02_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``5980``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_SecondaryBridge_Enter_Zone_JDG
----------------------------------

M04_SecondaryBridge_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3972``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Ships_Captain_JDG
---------------------

M04_Ships_Captain_JDG in Mission04.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; creates or destroys objects.

* Source line: ``7608``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M04_Ships_FirstMate_JDG
-----------------------

M04_Ships_FirstMate_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; creates or destroys objects.

* Source line: ``7634``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Start_TorpedoObjective_Zone_JDG
-----------------------------------

M04_Start_TorpedoObjective_Zone_JDG in Mission04.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``10063``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Surprise_Apache_JDG
-----------------------

M04_Surprise_Apache_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``4524``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TiberiumHold_EntryZone_and_Controller_JDG
---------------------------------------------

M04_TiberiumHold_EntryZone_and_Controller_JDG in Mission04.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``6678``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_TibHold_Mutant_NoThreat_JDG
-------------------------------

M04_TibHold_Mutant_NoThreat_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``7272``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Set_Animation_Frame``, ``Set_Health``, ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TibHold_MutantChamber_JDG
-----------------------------

M04_TibHold_MutantChamber_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions; controls animation playback.

* Source line: ``6731``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Get_Health``, ``Set_Health``, ``Send_Custom_Event``, ``Set_Animation``, ``Get_Position``, ``Create_Explosion``, ``Create_Object``
* Summary source: ``heuristic``

M04_TibHold_MutantChamber_NoThreat_JDG
--------------------------------------

M04_TibHold_MutantChamber_NoThreat_JDG in Mission04.cpp initializes behavior when the object is created; sends custom events; creates explosions; controls animation playback.

* Source line: ``7223``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Get_Health``, ``Set_Health``, ``Set_Animation``, ``Get_Position``, ``Create_Explosion``, ``Find_Object``, ``Debug_Message``
* Summary source: ``heuristic``

M04_TibHold_MutantChambers_Controller_JDG
-----------------------------------------

M04_TibHold_MutantChambers_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7092``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Get_ID``, ``Debug_Message``, ``Find_Object``, ``Get_Position``, ``Get_Facing``
* Summary source: ``heuristic``

M04_TibHold_RealMutant_JDG
--------------------------

M04_TibHold_RealMutant_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``7015``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Random_Int``, ``Action_Play_Animation``, ``Action_Goto``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Sound``, ``Apply_Damage``
* Summary source: ``heuristic``

M04_TibHold_SimpleMutant_JDG
----------------------------

M04_TibHold_SimpleMutant_JDG in Mission04.cpp initializes behavior when the object is created; controls animation playback.

* Source line: ``6811``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``
* Summary source: ``heuristic``

M04_TorpedoRoom_EnterZone_JDG
-----------------------------

M04_TorpedoRoom_EnterZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``10127``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TorpedoRoom_Target01_JDG
----------------------------

M04_TorpedoRoom_Target01_JDG in Mission04.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``9534``
* Event hooks: ``Created``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Set_Animation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_TorpedoRoom_Target02_JDG
----------------------------

M04_TorpedoRoom_Target02_JDG in Mission04.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``9600``
* Event hooks: ``Created``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Set_Animation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Visceroid_Dude_01_JDG
-------------------------

M04_Visceroid_Dude_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``7370``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_Visceroid_Dude_02_JDG
-------------------------

M04_Visceroid_Dude_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``7434``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Action_Play_Animation``, ``Get_Position``, ``Create_Explosion``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Visceroid_JDG
-----------------

M04_Visceroid_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``7315``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Get_Position``, ``Find_Closest_Soldier``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``
