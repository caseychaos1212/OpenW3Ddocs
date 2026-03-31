Mission04.cpp
=============

* Category: ``mission``
* Active scripts: ``141``
* Source: ``Code/Scripts/Mission04.cpp``

M04_A01_PatrolGuy_01_JDG
------------------------

M04_A01_PatrolGuy_01_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``1158``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_A01_Sniper_JDG
------------------

M04_A01_Sniper_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``1038``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Reset``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_FirstMateBodyguard_JDG
------------------------------

M04_Aft_FirstMateBodyguard_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``3964``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M04_Aft_LeftBarracks_TalkGuy_JDG
--------------------------------

M04_Aft_LeftBarracks_TalkGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4100``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_LockerRoom_PatrolGuy01_JDG
----------------------------------

M04_Aft_LockerRoom_PatrolGuy01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4124``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_LockerRoom_PatrolGuy02_JDG
----------------------------------

M04_Aft_LockerRoom_PatrolGuy02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4191``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Aft_RightBarracks_PatrolGuy_JDG
-----------------------------------

M04_Aft_RightBarracks_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4033``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_AftDeck_02_Blackhand_PatrolGuy_JDG
--------------------------------------

M04_AftDeck_02_Blackhand_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4379``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Action_Attack``, ``Action_Goto``
* Summary source: ``heuristic``

M04_AftDeck_02_Controller_JDG
-----------------------------

M04_AftDeck_02_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``3577``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Get_ID``, ``Create_Sound``, ``Send_Custom_Event``, ``Trigger_Spawner``, ``Get_Random``, ``Set_Facing``
* Summary source: ``heuristic``

M04_AftDeck_02_Entry_Zone_JDG
-----------------------------

M04_AftDeck_02_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4514``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_PatrolGuy_01_JDG
-------------------------------

M04_AftDeck_02_PatrolGuy_01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4290``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_PatrolGuy_02_JDG
-------------------------------

M04_AftDeck_02_PatrolGuy_02_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4334``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_02_Pointguard_JDG
-----------------------------

M04_AftDeck_02_Pointguard_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``4493``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_AftDeck_InnerSanctum_02_Entry_Zone_JDG
------------------------------------------

M04_AftDeck_InnerSanctum_02_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3564``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_AftDeck_InnerSanctum_Entry_Zone_JDG
---------------------------------------

The following scripts all deal with the aft deck on the way to kill the first mate.

* Source line: ``3546``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts all deal with the aft deck on the way to kill the first mate.

M04_AftDeck_Reinforcement_JDG
-----------------------------

M04_AftDeck_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4258``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Grant_Key``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Announce_Keycard_02_Objective_Zone_JDG
------------------------------------------

M04_Announce_Keycard_02_Objective_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``7859``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Apache_Enter_Zone_JDG
-------------------------

The following are all the temp scripts for the apache hanger

* Source line: ``4564``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following are all the temp scripts for the apache hanger

M04_Apache_GoBackToHangar_EntryZone_JDG
---------------------------------------

M04_Apache_GoBackToHangar_EntryZone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``8645``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_ApacheRoom_Apache_JDG
-------------------------

M04_ApacheRoom_Apache_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``8684``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Action_Goto``, ``Disable_Physical_Collisions``, ``Enable_Collisions``, ``Modify_Action``
* Summary source: ``heuristic``

M04_ApacheRoom_Controller_JDG
-----------------------------

M04_ApacheRoom_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``4597``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Set_Facing``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_BottomFloor_JDG
-----------------------------------------------

M04_ApacheRoom_Second_EntryZone_BottomFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8559``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_MiddleFloor_JDG
-----------------------------------------------

M04_ApacheRoom_Second_EntryZone_MiddleFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8473``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Second_EntryZone_TopFloor_JDG
--------------------------------------------

M04_ApacheRoom_Second_EntryZone_TopFloor_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``8387``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ApacheRoom_Sniper01_JDG
---------------------------

M04_ApacheRoom_Sniper01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4648``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_ApacheRoom_Sniper02_JDG
---------------------------

M04_ApacheRoom_Sniper02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4715``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_BH_MessHall_Guy_JDG
-----------------------

M04_BH_MessHall_Guy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands.

* Source line: ``5314``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Find_Object``, ``Action_Attack``, ``Get_Random``, ``Trigger_Spawner``, ``Attach_Script``
* Summary source: ``heuristic``

M04_BH_MessHall_Trigger_Zone_JDG
--------------------------------

M04_BH_MessHall_Trigger_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5296``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Sound``, ``Get_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_BigSam_EntryZone_JDG
------------------------

M04_BigSam_EntryZone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``10155``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_BigSam_Script_JDG
---------------------

M04_BigSam_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates explosions; controls animation playback; plays sounds.

* Source line: ``10197``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Set_Animation``, ``Send_Custom_Event``, ``Action_Attack``, ``Create_Explosion``, ``Set_Health``, ``Create_2D_Sound``, ``Monitor_Sound``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_JDG
--------------------------

M04_Captains_Bodyguard_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state.

* Source line: ``5172``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Random``, ``Trigger_Spawner``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_Reinforcement02_JDG
------------------------------------------

M04_Captains_Bodyguard_Reinforcement02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5248``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Get_Position``, ``Action_Reset``
* Summary source: ``heuristic``

M04_Captains_Bodyguard_Reinforcement_JDG
----------------------------------------

M04_Captains_Bodyguard_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5200``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Reset``, ``Get_Position``
* Summary source: ``heuristic``

M04_Captains_Bridge_Enter_Zone_JDG
----------------------------------

M04_Captains_Bridge_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5276``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Sound``, ``Get_Position``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_CargoHold_Blackhand_01_JDG
------------------------------

M04_CargoHold_Blackhand_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``1953``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Reset``, ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Create_Conversation``, ``Join_Conversation``
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

* Source line: ``8976``
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

M04_CargoMissileRooms_Dude_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1217``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Catwalk_Enter_Zone_01_JDG
-----------------------------

M04_Catwalk_Enter_Zone_01_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6233``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Catwalk_Enter_Zone_02_JDG
-----------------------------

M04_Catwalk_Enter_Zone_02_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6247``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Cooks_Script_JDG
--------------------

M04_Cooks_Script_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``6658``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``
* Summary source: ``heuristic``

M04_Doorway_Enterer_JDG
-----------------------

M04_Doorway_Enterer_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``6261``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Enable_Hibernation``, ``Grant_Key``, ``Action_Goto``, ``Get_Random_Int``, ``Create_Object``, ``Attach_Script``, ``Action_Play_Animation``
* Summary source: ``heuristic``

Parameter Description::

   first_location:vector3

M04_EngineRoom_BuildingController_JDG
-------------------------------------

M04_EngineRoom_BuildingController_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; plays sounds.

* Source line: ``2181``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Stop_Sound``, ``Debug_Message``, ``Set_Health``, ``Apply_Damage``, ``Create_2D_Sound``, ``Enable_Spawner``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_ChiefEngineer_JDG
--------------------------------

M04_EngineRoom_ChiefEngineer_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

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

* Source line: ``2789``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M04_EngineRoom_Prison_Guard_01_JDG
----------------------------------

M04_EngineRoom_Prison_Guard_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; starts conversations.

* Source line: ``2824``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_EngineRoom_Prison_Guard_02_JDG
----------------------------------

M04_EngineRoom_Prison_Guard_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``2961``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``, ``Action_Reset``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_01_JDG
------------------------------

M04_EngineRoom_Prisoner_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3078``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``, ``Action_Play_Animation``, ``Get_Position``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_02_JDG
------------------------------

M04_EngineRoom_Prisoner_02_JDG in Mission04.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``3262``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Loiters_Allowed``, ``Action_Play_Animation``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_02_JDG
------------------------------

M04_EngineRoom_Prisoner_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; creates or destroys objects.

* Source line: ``3297``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``, ``Action_Play_Animation``, ``Get_Position``, ``Action_Reset``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Prisoner_03_JDG
------------------------------

DECLARE_SCRIPT(M04_EngineRoom_Prisoner_02_JDG, "")//this guys ID number is M04_PRISON_PRISONER_02_JDG 101196 {

* Source line: ``3365``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Action_Play_Animation``, ``Get_Max_Health``, ``Set_Health``, ``Create_Sound``, ``Get_Position``, ``Action_Reset``, ``Action_Attack``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(M04_EngineRoom_Prisoner_02_JDG, "")//this guys ID number is M04_PRISON_PRISONER_02_JDG 101196
   {
   	bool firstTimeDamaged;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE(firstTimeDamaged, 1);
   	}

   	void Created( GameObject * obj ) override
   	{
   		Commands->Set_Innate_Is_Stationary ( obj, true);
   		firstTimeDamaged = true;
   	}

   	void Damaged( GameObject * obj, GameObject * damager, float amount ) override
   	{
   		if (obj && damager == STAR)
   		{
   			int myMaxHealth = Commands->Get_Max_Health ( obj );
   			Commands->Set_Health ( obj, myMaxHealth );

   			if (firstTimeDamaged == true)
   			{
   				Commands->Create_Sound ( "00-N066E", Vector3 (0,0,0), obj );//you are firing on a friendly unit
   				firstTimeDamaged = false;
   				ActionParamsStruct params;
   				params.Set_Basic( this, 100, M01_DOING_ANIMATION_02_JDG );
   				params.Set_Animation( "H_A_J21C", false );
   				Commands->Action_Play_Animation (  obj, params );
   				Vector3 myPosition = Commands->Get_Position ( obj );
   				Commands->Create_Sound ( "M04 PanicGuy 01 Twiddler", myPosition, obj );
   			}
   		}
   	}

   	void Custom (GameObject* obj, int type, uintptr_t param, GameObject* sender) override
   	{
   		ActionParamsStruct params;

   		if (param == M01_MODIFY_YOUR_ACTION_JDG)//you've been freed--cheer you ungrateful bastard
   		{
   			const char* animationName = M01_Choose_Cheer_Animation ( );
   			Commands->Action_Reset (  obj, 100 );
   			params.Set_Basic( this, 100, M01_DOING_ANIMATION_01_JDG );
   			params.Set_Animation( animationName, false );

   			Commands->Action_Play_Animation (  obj, params );

   			Vector3 myPosition = Commands->Get_Position ( obj );
   			Commands->Create_Sound ( "M01_GDI_Thanks_Twiddler", myPosition, obj );
   		}
   	}

   	void Action_Complete (GameObject *obj, int action_id, ActionCompleteReason complete_reason) override
   	{
   		if (action_id == M01_DOING_ANIMATION_01_JDG && complete_reason == ACTION_COMPLETE_NORMAL)
   		{
   			Commands->Destroy_Object ( obj );
   		}

   		else if (action_id == M01_DOING_ANIMATION_02_JDG && complete_reason == ACTION_COMPLETE_NORMAL)
   		{
   			firstTimeDamaged = true;
   		}
   	}
   };

M04_EngineRoom_PrisonLift_EnterZone_JDG
---------------------------------------

M04_EngineRoom_PrisonLift_EnterZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``2758``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_SniperScript_JDG
-------------------------------

M04_EngineRoom_SniperScript_JDG in Mission04.cpp initializes behavior when the object is created; creates or destroys objects.

* Source line: ``7896``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Difficulty_Level``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Start_Guard_Conversation_Zone_JDG
------------------------------------------------

M04_EngineRoom_Start_Guard_Conversation_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``2800``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Stationary_Tech_JDG
----------------------------------

M04_EngineRoom_Stationary_Tech_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``6063``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Loiters_Allowed``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``, ``Get_Random``, ``Debug_Message``
* Summary source: ``heuristic``

Parameter Description::

   Console_ID :int

M04_EngineRoom_TalkToPrisoners_Zone_JDG
---------------------------------------

M04_EngineRoom_TalkToPrisoners_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3051``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target01_JDG
---------------------------

M04_EngineRoom_Target01_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8275``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target02_JDG
---------------------------

M04_EngineRoom_Target02_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8303``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target03_JDG
---------------------------

M04_EngineRoom_Target03_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8331``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EngineRoom_Target04_JDG
---------------------------

M04_EngineRoom_Target04_JDG in Mission04.cpp reacts to destruction state; sends custom events; creates explosions.

* Source line: ``8359``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_EnterCargoBay_BottomRight_Zone_JDG
--------------------------------------

M04_EnterCargoBay_BottomRight_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5875``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_EnterCargoBay_TopLeft_Zone_JDG
----------------------------------

M04_EnterCargoBay_TopLeft_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5900``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Firefight_Controller_JDG
----------------------------

M04_Firefight_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``9098``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Send_Custom_Event``, ``Mission_Complete``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Firefight_NodGuys
---------------------

M04_Firefight_NodGuys in Mission04.cpp reacts to destruction state; sends custom events.

* Source line: ``5516``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Firefight_Prisoner
----------------------

M04_Firefight_Prisoner in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; starts conversations.

* Source line: ``8984``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Get_Health``, ``Get_Max_Health``, ``Set_HUD_Help_Text``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Firefight_RallyZone
-----------------------

M04_Firefight_RallyZone in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``9395``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_Difficulty_Level``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_Firefight_Start_Battle_Music_JDG
------------------------------------

The following are the scripts and controller for the end fire fight.

* Source line: ``5485``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   The following are the scripts and controller for the end fire fight.

M04_ForeDeck_ClosetSurprise_Guy_JDG
-----------------------------------

M04_ForeDeck_ClosetSurprise_Guy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``5376``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Goto``, ``Get_Position``
* Summary source: ``heuristic``

M04_ForeDeck_ClosetSurprise_Trigger_Zone_JDG
--------------------------------------------

M04_ForeDeck_ClosetSurprise_Trigger_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5415``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ForeDeck_Controller_JDG
---------------------------

The following scripts are for the foredeck. They include both the messhalls and the captain's encounter.

* Source line: ``4971``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Get_ID``, ``Trigger_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts are for the foredeck.  They include both the messhalls and the captain's encounter.

M04_ForeDeck_Initial_Enter_Zone_JDG
-----------------------------------

M04_ForeDeck_Initial_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4802``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_ForeDeck_MapRoom_Guard01_JDG
--------------------------------

M04_ForeDeck_MapRoom_Guard01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``4879``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_ForeDeck_MapRoom_Guard02_JDG
--------------------------------

M04_ForeDeck_MapRoom_Guard02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4893``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_ForeDeck_Reinforcement_JDG
------------------------------

M04_ForeDeck_Reinforcement_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``4849``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Action_Goto``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_ForeDeck_RocketGuy_JDG
--------------------------

The following are the initial scripts for the fore deck

* Source line: ``4786``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``source comment``

Source Notes::

   The following are the initial scripts for the fore deck

M04_ForeDeck_TorpedoRoom_Guard_JDG
----------------------------------

M04_ForeDeck_TorpedoRoom_Guard_JDG in Mission04.cpp initializes behavior when the object is created.

* Source line: ``4960``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M04_Front_ofThe_Boat_Population_JDG
-----------------------------------

play eva warning conversation here***** {

* Source line: ``6649``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``source comment``

Source Notes::

   play eva warning conversation here*****
   				{
   					int conv = Commands->Create_Conversation( "M04_Eva_WarnsAboutHunters_Conversation", 100, 50, false);
   					Commands->Join_Conversation( NULL, conv, false, false, false );
   					Commands->Start_Conversation( conv,  conv );
   				}

   				else
   				{
   					Commands->Send_Custom_Event( obj, obj, 0, M01_MODIFY_YOUR_ACTION_02_JDG, 5 );
   				}
   			}
   		}
   	}

   	void Destroyed( GameObject * obj )
   	{
   		GameObject * myController = Commands->Find_Object ( M04_ENGINEROOM_HUNTING_CONTROLLER_JDG );
   		if (myController != NULL)
   		{
   			Commands->Send_Custom_Event( obj, myController, 0, M01_START_ACTING_JDG, 1 );
   		}
   	}

   	void Damaged( GameObject * obj, GameObject * damager, float amount ) override
   	{
   		if (obj && damager == STAR)
   		{
   			Commands->Send_Custom_Event( obj, obj, 0, M01_MODIFY_YOUR_ACTION_JDG, 0 );
   		}
   	}

   	void Enemy_Seen( GameObject * obj, GameObject * enemy )
   	{
   		if (enemy == STAR)
   		{
   			Commands->Send_Custom_Event( obj, obj, 0, M01_MODIFY_YOUR_ACTION_JDG, 0 );
   		}
   	}

   	void Timer_Expired( GameObject * obj, int timer_id )
   	{
   		if (timer_id == M01_GOTO_IDLE_JDG)
   		{
   			//Commands->Enable_Hibernation( obj, true );
   			Vector3 myPosition = Commands->Get_Position ( obj );
   			Vector3 playerPosition = Commands->Get_Position ( STAR );
   			float distanceFromStar = Commands->Get_Distance ( myPosition, playerPosition );

   			if (distanceFromStar >= 150)
   			{
   				bool visible = Commands->Is_Object_Visible( obj, STAR );

   				if (visible != true)
   				{
   					Commands->Apply_Damage( obj, 100000, "BlamoKiller", NULL );
   				}

   				else
   				{
   					Commands->Start_Timer ( obj, this, 20, M01_GOTO_IDLE_JDG );
   				}
   			}

   			else
   			{
   				Commands->Start_Timer ( obj, this, 20, M01_GOTO_IDLE_JDG );
   			}
   		}
   	}
   };

M04_GruntMessHall_Entry_Zone_JDG
--------------------------------

M04_GruntMessHall_Entry_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5458``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_GruntMessHall_Exit_Zone_JDG
-------------------------------

M04_GruntMessHall_Exit_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5441``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Hunter_Controller_JDG
-------------------------

M04_Hunter_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; starts conversations.

* Source line: ``6356``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Object``, ``Get_ID``, ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Hunter_JDG
--------------

M04_Hunter_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``6433``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Enable_Hibernation``, ``Send_Custom_Event``, ``Action_Goto``, ``Get_Position``, ``Get_Distance``, ``Find_Object``
* Summary source: ``heuristic``

M04_Hunter_JDG
--------------

M04_Hunter_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``6507``
* Event hooks: ``Created``, ``Destroyed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Grant_Key``, ``Enable_Hibernation``, ``Action_Attack``, ``Start_Timer``, ``Modify_Action``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   MyLeaders_ID :int

M04_Keycard_01_Script_JDG
-------------------------

M04_Keycard_01_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``7523``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Keycard_02_Script_JDG
-------------------------

M04_Keycard_02_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7539``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Keycard_03_Script_JDG
-------------------------

M04_Keycard_03_Script_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7581``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``
* Summary source: ``heuristic``

M04_MedLab_Enter_Zone_JDG
-------------------------

M04_MedLab_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4825``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_MedLab_Tech_JDG
-------------------

M04_MedLab_Tech_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``7731``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Find_Object``, ``Action_Attack``, ``Action_Reset``, ``Action_Goto``, ``Get_Position``, ``Action_Face_Location``
* Summary source: ``heuristic``

M04_MissileRoom_EnterZone_Left_JDG
----------------------------------

The following scripts all deal with the first time through the cargo and missile rooms.

* Source line: ``1169``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   The following scripts all deal with the first time through the cargo and missile rooms.

M04_MissileRoom_EnterZone_Right_JDG
-----------------------------------

M04_MissileRoom_EnterZone_Right_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``1193``
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

* Source line: ``7834``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_MissileRoom_Target01_JDG
----------------------------

M04_MissileRoom_Target01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``7911``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target02_JDG
----------------------------

M04_MissileRoom_Target02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``8002``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target03_JDG
----------------------------

M04_MissileRoom_Target03_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``8093``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_Target04_JDG
----------------------------

M04_MissileRoom_Target04_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``8184``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Monitor_Sound``, ``Set_Obj_Radar_Blip_Shape``, ``Set_Obj_Radar_Blip_Color``, ``Set_Animation``
* Summary source: ``heuristic``

M04_MissileRoom_UpperGuard_01_JDG
---------------------------------

M04_MissileRoom_UpperGuard_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``1390``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Actions``, ``Action_Goto``, ``Attach_Script``
* Summary source: ``heuristic``

M04_MissileRoom_UpperGuard_02_JDG
---------------------------------

M04_MissileRoom_UpperGuard_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``1430``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Actions``, ``Action_Goto``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Mutant_UpdateDisc_JDG
-------------------------

M04_Mutant_UpdateDisc_JDG in Mission04.cpp responds to custom events.

* Source line: ``9533``
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
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Add_Objective``, ``Add_Radar_Marker``, ``Get_Position``, ``Find_Object``, ``Set_Objective_HUD_Info_Position``, ``Create_Sound``
* Summary source: ``heuristic``

M04_Objective_Reminder_Controller_JDG
-------------------------------------

M04_Objective_Reminder_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``10299``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_Player_Is_Leaving_Aft_Deck_JDG
----------------------------------

M04_Player_Is_Leaving_Aft_Deck_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4010``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_PlaySound_OnZoneEntry_OneTime_JDG
-------------------------------------

M04_PlaySound_OnZoneEntry_OneTime_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``10265``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Random``, ``Create_Sound``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   SoundName:string

M04_Pog_Controller_JDG
----------------------

M04_Pog_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``9676``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Set_Objective_HUD_Info_Position``, ``Set_Objective_HUD_Info``
* Summary source: ``heuristic``

M04_PointGuard_JDG
------------------

The following are the scripts for the dudes in the sub bay when the mission first starts.

* Source line: ``1022``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``source comment``

Source Notes::

   The following are the scripts for the dudes in the sub bay when the mission first starts.

M04_PostFirstMate_FrontDeck_PatrolGuy01_JDG
-------------------------------------------

M04_PostFirstMate_FrontDeck_PatrolGuy01_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5764``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_FrontDeck_PatrolGuy02_JDG
-------------------------------------------

M04_PostFirstMate_FrontDeck_PatrolGuy02_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5819``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_MissileRoom_PatrolGuy_JDG
-------------------------------------------

M04_PostFirstMate_MissileRoom_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5618``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_OfficerQuarters_PatrolGuy_JDG
-----------------------------------------------

M04_PostFirstMate_OfficerQuarters_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5709``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_PostFirstMate_SamRoom_PatrolGuy_JDG
---------------------------------------

M04_PostFirstMate_SamRoom_PatrolGuy_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``5527``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Play_Animation``
* Summary source: ``heuristic``

M04_Prison_CellDoor_Zone_JDG
----------------------------

M04_Prison_CellDoor_Zone_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3475``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Has_Key``, ``Find_Object``, ``Destroy_Object``, ``Set_Position``, ``Set_Facing``, ``Control_Enable``, ``Set_Is_Rendered``
* Summary source: ``heuristic``

M04_Prison_Keycard_CheckZone_JDG
--------------------------------

M04_Prison_Keycard_CheckZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects.

* Source line: ``6667``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Prison_Warden_JDG
---------------------

M04_Prison_Warden_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; creates or destroys objects; starts conversations.

* Source line: ``7682``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Find_Object``, ``Action_Attack``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M04_Prisoners_Rescued_Controller_JDG
------------------------------------

The Following are all the scripts associated with the objectives...including controller

* Source line: ``7812``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Set_Position``, ``Set_Facing``, ``Control_Enable``, ``Set_Is_Rendered``
* Summary source: ``source comment``

Source Notes::

   The Following are all the scripts associated with the objectives...including controller

M04_RocketEmplacement_01_JDG
----------------------------

M04_RocketEmplacement_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``5923``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_RocketEmplacement_02_JDG
----------------------------

M04_RocketEmplacement_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6020``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_SecondaryApache01_JDG
-------------------------

M04_SecondaryApache01_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``5966``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_SecondaryApache02_JDG
-------------------------

M04_SecondaryApache02_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``5993``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_SecondaryBridge_Enter_Zone_JDG
----------------------------------

M04_SecondaryBridge_Enter_Zone_JDG in Mission04.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3985``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Ships_Captain_JDG
---------------------

M04_Ships_Captain_JDG in Mission04.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; creates or destroys objects.

* Source line: ``7621``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M04_Ships_FirstMate_JDG
-----------------------

M04_Ships_FirstMate_JDG in Mission04.cpp initializes behavior when the object is created; reacts to destruction state; creates or destroys objects.

* Source line: ``7647``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Get_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M04_Start_TorpedoObjective_Zone_JDG
-----------------------------------

M04_Start_TorpedoObjective_Zone_JDG in Mission04.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``10074``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Surprise_Apache_JDG
-----------------------

M04_Surprise_Apache_JDG in Mission04.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``4537``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TiberiumHold_EntryZone_and_Controller_JDG
---------------------------------------------

M04_TiberiumHold_EntryZone_and_Controller_JDG in Mission04.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``6691``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M04_TibHold_Mutant_NoThreat_JDG
-------------------------------

M04_TibHold_Mutant_NoThreat_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects; controls animation playback.

* Source line: ``7285``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Max_Health``, ``Set_Animation_Frame``, ``Set_Health``, ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TibHold_MutantChamber_JDG
-----------------------------

M04_TibHold_MutantChamber_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions; controls animation playback.

* Source line: ``6744``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Get_Health``, ``Set_Health``, ``Send_Custom_Event``, ``Set_Animation``, ``Get_Position``, ``Create_Explosion``, ``Create_Object``
* Summary source: ``heuristic``

M04_TibHold_MutantChamber_NoThreat_JDG
--------------------------------------

M04_TibHold_MutantChamber_NoThreat_JDG in Mission04.cpp initializes behavior when the object is created; sends custom events; creates explosions; controls animation playback.

* Source line: ``7236``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Get_Health``, ``Set_Health``, ``Set_Animation``, ``Get_Position``, ``Create_Explosion``, ``Find_Object``, ``Debug_Message``
* Summary source: ``heuristic``

M04_TibHold_MutantChambers_Controller_JDG
-----------------------------------------

M04_TibHold_MutantChambers_Controller_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``7105``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Get_ID``, ``Debug_Message``, ``Find_Object``, ``Get_Position``, ``Get_Facing``
* Summary source: ``heuristic``

M04_TibHold_RealMutant_JDG
--------------------------

DECLARE_SCRIPT(M11_MutantCrypt_Spawner03_Guy_JDG, "") {

* Source line: ``7028``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Random_Int``, ``Action_Play_Animation``, ``Action_Goto``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Sound``, ``Apply_Damage``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(M11_MutantCrypt_Spawner03_Guy_JDG, "")
   {
   	typedef enum {
   		IDLE,
   		ATTACKING,
   		DEAD,
   	} M11_Mutant_State;

   	M11_Mutant_State myState;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE(myState, 1);
   	}

   	void Created( GameObject * obj ) override
   	{
   		myState = IDLE;
   		float delayTimer = Commands->Get_Random ( 10, 20 );
   		Commands->Send_Custom_Event ( obj, obj, 0, M01_START_ACTING_JDG, delayTimer );
   		Commands->Send_Custom_Event ( obj, obj, 0, M01_PICK_A_NEW_LOCATION_JDG, 0 );
   	}

   	void Killed( GameObject * obj, GameObject * killer ) override
   	{
   		myState = DEAD;

   		GameObject * mutantController = Commands->Find_Object ( M11_MUTANT_CRYPT_SPAWNER_CONTROLLER_JDG );
   		if (mutantController != NULL)
   		{
   			Commands->Send_Custom_Event ( obj, mutantController, 0, M01_SPAWNER_IS_DEAD_JDG, 0 );
   		}
   	}

   	void Enemy_Seen( GameObject * obj, GameObject * enemy )
   	{
   		if (obj && enemy == STAR && myState == IDLE)//
   		{
   			myState = ATTACKING;
   			char *soundName = M11_Choose_Mutant_Alerted_Sound ( );
   			Vector3 myPosition = Commands->Get_Position ( obj );
   			Commands->Create_Sound ( soundName, myPosition, obj );

   			Commands->Send_Custom_Event( obj, obj, 0, M01_HUNT_THE_PLAYER_JDG, 1 );

   			Commands->Create_Logical_Sound (obj, M11_MUTANT_IS_NEARBY_JDG, myPosition, 50 );
   		}
   	}

   	void Sound_Heard( GameObject * obj, const CombatSound & sound )
   	{
   		if ( sound.Type == M11_MUTANT_IS_NEARBY_JDG )
   		{
   			Commands->Send_Custom_Event( obj, obj, 0, M01_HUNT_THE_PLAYER_JDG, 1 );
   		}
   	}

   	void Custom( GameObject * obj, int type, uintptr_t param, GameObject * sender ) override
   	{
   		if (param == M01_START_ACTING_JDG)
   		{
   			if (obj && myState == IDLE)
   			{
   				char *soundName = M11_Choose_Mutant_Idle_Sound ( );
   				Vector3 myPosition = Commands->Get_Position ( obj );
   				Commands->Create_Sound ( soundName, myPosition, obj );

   				float delayTimer = Commands->Get_Random ( 10, 20 );
   				Commands->Send_Custom_Event ( obj, obj, 0, M01_START_ACTING_JDG, delayTimer );
   			}

   			else if (obj && myState != DEAD)
   			{
   				char *soundName = M11_Choose_Mutant_Attack_Sound ( );
   				Vector3 myPosition = Commands->Get_Position ( obj );
   				Commands->Create_Sound ( soundName, myPosition, obj );

   				float delayTimer = Commands->Get_Random ( 0, 10 );
   				Commands->Send_Custom_Event ( obj, obj, 0, M01_START_ACTING_JDG, delayTimer );
   			}
   		}

   		else if (obj && param == M01_PICK_A_NEW_LOCATION_JDG)
   		{
   			ActionParamsStruct params;
   			params.Set_Basic(this, 80, M01_PICK_A_NEW_LOCATION_JDG);
   			params.Set_Movement( Vector3(-15.128f, 17.965f, -63.748f), .1f, 1 );

   			Commands->Action_Goto( obj, params );
   		}

   		else if (obj && param == M01_HUNT_THE_PLAYER_JDG)
   		{
   			if (STAR)
   			{
   				ActionParamsStruct params;
   				params.Set_Basic(this, 100, M01_HUNT_THE_PLAYER_JDG);
   				params.Set_Movement(STAR, 2, 1);

   				Commands->Action_Goto ( obj, params );
   			}

   			else
   			{
   				Commands->Send_Custom_Event( obj, obj, 0, M01_HUNT_THE_PLAYER_JDG, 1 );
   			}
   		}
   	}

   	void Action_Complete( GameObject * obj, int action_id, ActionCompleteReason complete_reason ) override
   	{
   		ActionParamsStruct params;

   		if (complete_reason == ACTION_COMPLETE_NORMAL)
   		{
   			if (obj && action_id == M01_PICK_A_NEW_LOCATION_JDG)
   			{
   				ActionParamsStruct params;
   				params.Set_Basic(this, 80, M01_WALKING_WAYPATH_01_JDG);
   				params.Set_Movement( Vector3(0,0,0), .1f, 1 );

   				int random = Commands->Get_Random_Int(0, 4);

   				if (random == 0)
   				{
   					params.WaypathID = 100076;
   					params.WaypointStartID = 100077;
   					params.WaypointEndID = 100085;
   				}

   				else if (random == 1)
   				{
   					params.WaypathID = 100087;
   					params.WaypointStartID = 100088;
   					params.WaypointEndID = 100096;
   				}

   				else if (random == 3)
   				{
   					params.WaypathID = 100076;
   					params.WaypointStartID = 100085;
   					params.WaypointEndID = 100077;
   				}

   				else
   				{
   					params.WaypathID = 100087;
   					params.WaypointStartID = 100096;
   					params.WaypointEndID = 100088;
   				}

   				Commands->Action_Goto( obj, params );


   			}

   			else if (obj && action_id == M01_WALKING_WAYPATH_01_JDG)
   			{
   				const char* animationName = M01_Choose_Idle_Animation ( );

   				params.Set_Basic( this, 60, M01_DOING_ANIMATION_01_JDG );
   				params.Set_Animation (animationName, false);
   				Commands->Action_Play_Animation (obj, params);
   			}

   			else if (obj && action_id == M01_DOING_ANIMATION_01_JDG)
   			{
   				ActionParamsStruct params;
   				params.Set_Basic(this, 80, M01_PICK_A_NEW_LOCATION_JDG);
   				params.Set_Movement( Vector3(-15.128f, 17.965f, -63.748f), .1f, 1 );

   				Commands->Action_Goto( obj, params );
   			}

   			else if (obj && action_id == M01_HUNT_THE_PLAYER_JDG)
   			{
   				if (STAR)
   				{
   					char *soundName = M11_Choose_Mutant_Attack_Sound ( );
   					Vector3 myPosition = Commands->Get_Position ( obj );
   					Commands->Create_Sound ( soundName, myPosition, obj );

   					const char* animationName = M11_Choose_Mutant_Attack_Animation ( );

   					params.Set_Basic( this, 100, M01_DOING_ANIMATION_01_JDG );
   					params.Set_Animation (animationName, false);
   					Commands->Action_Play_Animation (obj, params);

   					Commands->Apply_Damage( STAR, 5, "TiberiumRaw", obj );
   					Commands->Send_Custom_Event( obj, obj, 0, M01_HUNT_THE_PLAYER_JDG, 1 );
   				}
   			}
   		}
   	}
   };

M04_TibHold_SimpleMutant_JDG
----------------------------

M04_TibHold_SimpleMutant_JDG in Mission04.cpp initializes behavior when the object is created; controls animation playback.

* Source line: ``6824``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``
* Summary source: ``heuristic``

M04_TorpedoRoom_EnterZone_JDG
-----------------------------

M04_TorpedoRoom_EnterZone_JDG in Mission04.cpp watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``10136``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_TorpedoRoom_Target01_JDG
----------------------------

M04_TorpedoRoom_Target01_JDG in Mission04.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``9545``
* Event hooks: ``Created``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Set_Animation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_TorpedoRoom_Target02_JDG
----------------------------

M04_TorpedoRoom_Target02_JDG in Mission04.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; controls animation playback.

* Source line: ``9611``
* Event hooks: ``Created``, ``Animation_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Get_Position``, ``Set_Animation_Frame``, ``Create_Sound``, ``Set_Animation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M04_Visceroid_Dude_01_JDG
-------------------------

M04_Visceroid_Dude_01_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``7383``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M04_Visceroid_Dude_02_JDG
-------------------------

M04_Visceroid_Dude_02_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``7447``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Action_Play_Animation``, ``Get_Position``, ``Create_Explosion``, ``Create_Object``, ``Attach_Script``, ``Destroy_Object``
* Summary source: ``heuristic``

M04_Visceroid_JDG
-----------------

M04_Visceroid_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; starts conversations.

* Source line: ``7328``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Get_Position``, ``Find_Closest_Soldier``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M11_MutantCrypt_Spawner03_Guy_JDG
---------------------------------

M11_MutantCrypt_Spawner03_Guy_JDG in Mission04.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``6832``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Create_Sound``, ``Create_Logical_Sound``, ``Action_Goto``, ``Get_Random_Int``
* Summary source: ``heuristic``
