MissionX0.cpp
=============

* Category: ``mission``
* Active scripts: ``32``
* Source: ``Code/Scripts/MissionX0.cpp``

DAK_MX0_Sec_3_Humvee
--------------------

DAK_MX0_Sec_3_Humvee in MissionX0.cpp watches enter or exit events; drives AI action commands.

* Source line: ``1370``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Debug_Message``
* Summary source: ``heuristic``

Havoc_Script
------------

Havoc_Script in MissionX0.cpp reacts to destruction state.

* Source line: ``462``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Mission_Complete``
* Summary source: ``heuristic``

MX0_A03_CONTROLLER_DAK
----------------------

MX0_A03_CONTROLLER_DAK in MissionX0.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1777``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Get_Position``, ``Attach_Script``, ``Set_Facing``, ``Action_Reset``, ``Action_Goto``
* Summary source: ``heuristic``

MX0_A03_END_ZONE
----------------

MX0_A03_END_ZONE in MissionX0.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``2625``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A03_FIRST_PLAYER_ZONE
-------------------------

MX0_A03_FIRST_PLAYER_ZONE in MissionX0.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; drives AI action commands; sends custom events; creates or destroys objects.

* Source line: ``2544``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Action_Reset``, ``Create_Object``, ``Get_Position``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_A03_GDI_INFANTRY
--------------------

MX0_A03_GDI_INFANTRY in MissionX0.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior.

* Source line: ``1613``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Attach_Script``, ``Action_Reset``, ``Find_Object``, ``Action_Goto``, ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   troop_num:int

MX0_A03_GDI_TANK_DROP_ZONE_DAK
------------------------------

MX0_A03_GDI_TANK_DROP_ZONE_DAK in MissionX0.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``1747``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_A03_GDI_TROOP_DROP_ZONE_DAK
-------------------------------

MX0_A03_GDI_TROOP_DROP_ZONE_DAK in MissionX0.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``1718``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_A03_GDI_TROOPER_ONE
-----------------------

MX0_A03_GDI_TROOPER_ONE in MissionX0.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``2422``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Innate_Enable``, ``Action_Reset``, ``Action_Goto``, ``Debug_Message``, ``Create_Conversation``
* Summary source: ``heuristic``

MX0_A03_HAVOC_TANK
------------------

MX0_A03_HAVOC_TANK in MissionX0.cpp responds to custom events; sends custom events.

* Source line: ``2517``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A03_HUMVEE
--------------

MX0_A03_HUMVEE in MissionX0.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``2090``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Action_Goto``, ``Debug_Message``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

MX0_A03_NOD_BUGGIE
------------------

MX0_A03_NOD_BUGGIE in MissionX0.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``2269``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Get_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_A03_NOD_HARVESTER
---------------------

MX0_A03_NOD_HARVESTER in MissionX0.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events; controls animation playback.

* Source line: ``2333``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Set_Health``, ``Action_Goto``, ``Set_Animation``, ``Send_Custom_Event``, ``Debug_Message``, ``Get_Health``, ``Apply_Damage``
* Summary source: ``heuristic``

MX0_A03_NOD_PLACED_MINIGUNNER
-----------------------------

MX0_A03_NOD_PLACED_MINIGUNNER in MissionX0.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``1389``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Innate_Enable``
* Summary source: ``heuristic``

MX0_A03_NOD_TROOPER_TIB_DEATH
-----------------------------

MX0_A03_NOD_TROOPER_TIB_DEATH in MissionX0.cpp responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``2310``
* Event hooks: ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A03_NOD_TURRET
------------------

MX0_A03_NOD_TURRET in MissionX0.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``2603``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A03_TANK
------------

MX0_A03_TANK in MissionX0.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``2210``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

MX0_A03_TROOPER_ONE_TEST
------------------------

MX0_A03_TROOPER_ONE_TEST in MissionX0.cpp initializes behavior when the object is created.

* Source line: ``2595``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``
* Summary source: ``heuristic``

MX0_AmbientBattle
-----------------

MX0_AmbientBattle in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``1189``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Get_Position``, ``Monitor_Sound``, ``Start_Timer``
* Summary source: ``heuristic``

MX0_Engineer1
-------------

MX0_Engineer1 in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``470``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``, ``Get_Position``, ``Action_Goto``, ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float

MX0_Engineer2
-------------

MX0_Engineer2 in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; controls animation playback; starts conversations.

* Source line: ``701``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Get_ID``, ``Get_Position``, ``Action_Goto``, ``Get_Action_ID``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float

MX0_Engineer_Goto
-----------------

MX0_Engineer_Goto in MissionX0.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``984``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   GotoDest1:int, GotoDest2:int, Count:int

MX0_Engineer_Goto2
------------------

MX0_Engineer_Goto2 in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events.

* Source line: ``1029``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Set_HUD_Help_Text``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   GotoDest1:int, GotoDest2:int, Count:int

MX0_Engineer_Return
-------------------

MX0_Engineer_Return in MissionX0.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``958``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

MX0_GDI_ORCA
------------

MX0_GDI_ORCA in MissionX0.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1410``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Fade_Background_Music``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

MX0_Kill_Sniper
---------------

MX0_Kill_Sniper in MissionX0.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``1099``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_KillNotify
--------------

MX0_KillNotify in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; starts conversations.

* Source line: ``1282``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Get_Random_Int``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

MX0_MissionStart_DME
--------------------

MX0_MissionStart_DME in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; changes inventory or weapons; changes innate AI behavior; starts conversations.

* Source line: ``42``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Select_Weapon``, ``Get_Position``, ``Find_Object``, ``Get_Facing``, ``Fade_Background_Music``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

MX0_NOD_INFANTRY
----------------

MX0_NOD_INFANTRY in MissionX0.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``1522``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Attach_Script``, ``Set_Innate_Is_Stationary``, ``Action_Attack``, ``Action_Reset``, ``Debug_Message``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   troop_num:int

MX0_NOD_TroopDrop
-----------------

MX0_NOD_TroopDrop in MissionX0.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1128``
* Event hooks: ``Created``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Start_Timer``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_SniperAction
----------------

MX0_SniperAction in MissionX0.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; changes innate AI behavior.

* Source line: ``1221``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Innate_Disable``, ``Start_Timer``, ``Apply_Damage``, ``Reveal_Encyclopedia_Character``, ``Display_Encyclopedia_Event_UI``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   FaceObj:int

MX0_Triggered_Conv
------------------

MX0_Triggered_Conv in MissionX0.cpp initializes behavior when the object is created.

* Source line: ``2680``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: none detected
* Summary source: ``heuristic``
