Mission06.cpp
=============

* Category: ``mission``
* Active scripts: ``85``
* Source: ``Code/Scripts/Mission06.cpp``

M06_Activate_Flyovers
---------------------

M06_Activate_Flyovers in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``5011``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Active=0:int

M06_Activate_Midtro
-------------------

M06_Activate_Midtro in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``638``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Frame``, ``Is_A_Star``, ``Static_Anim_Phys_Goto_Last_Frame``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Set_Position``, ``Create_Object``
* Summary source: ``heuristic``

M06_Activate_MidtroC
--------------------

M06_Activate_MidtroC in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``5557``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Set_Facing``, ``Get_Position``, ``Set_Position``, ``Attach_Script``
* Summary source: ``heuristic``

M06_Activate_Secret_Door
------------------------

M06_Activate_Secret_Door in Mission06.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; starts conversations.

* Source line: ``927``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Static_Anim_Phys_Goto_Last_Frame``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Secret_Door_ID=0:int

M06_Alarm_Behavior
------------------

M06_Alarm_Behavior in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``1499``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Footsteps_Heard``, ``Get_Difficulty_Level``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Get_Distance``, ``Action_Face_Location``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Alarm_Enemy_Seen=0.0:float, Alarm_Damaged=0.0:float

M06_Alarm_Controller
--------------------

M06_Alarm_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; controls animation playback; starts conversations.

* Source line: ``1374``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Animation_Frame``, ``Get_Position``, ``Debug_Message``, ``Get_ID``, ``Send_Custom_Event``, ``Start_Timer``, ``Create_Sound``
* Summary source: ``heuristic``

M06_Alarm_Engineer
------------------

M06_Alarm_Engineer in Mission06.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3166``
* Event hooks: ``Created``, ``Sound_Heard``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Find_Object``, ``Action_Face_Location``, ``Get_Health``, ``Get_Max_Health``, ``Action_Attack``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

M06_Alarm_Switch
----------------

M06_Alarm_Switch in Mission06.cpp initializes behavior when the object is created; responds to custom events; sends custom events; controls animation playback.

* Source line: ``1788``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Debug_Message``, ``Get_ID``, ``Set_Animation_Frame``, ``Send_Custom_Event``, ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

M06_Alarm_Terminal_DLS
----------------------

M06_Alarm_Terminal_DLS in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; handles player poke interaction; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``1845``
* Event hooks: ``Created``, ``Killed``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation_Frame``, ``Enable_HUD_Pokable_Indicator``, ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Position``, ``Get_Facing``, ``Create_Object``
* Summary source: ``heuristic``

M06_Apply_Damage
----------------

M06_Apply_Damage in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``2856``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Apply_Damage``
* Summary source: ``heuristic``

M06_Assistance_Farmer_DLS
-------------------------

M06_Assistance_Farmer_DLS in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; sends custom events; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``3533``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``, ``Action_Goto``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Barracks_Controller
-----------------------

M06_Barracks_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``2614``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Start_Timer``, ``Create_Logical_Sound``, ``Send_Custom_Event``, ``Enable_Spawner``
* Summary source: ``heuristic``

M06_Barracks_Eagle
------------------

M06_Barracks_Eagle in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``3328``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Barracks_Mess_Unit
----------------------

M06_Barracks_Mess_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4605``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Barracks_Patrol
-------------------

M06_Barracks_Patrol in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects; starts conversations.

* Source line: ``2339``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Find_Object``, ``Action_Goto``, ``Start_Timer``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

M06_Bathroom_Unit
-----------------

M06_Bathroom_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4644``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Civ_Prisoner
----------------

M06_Civ_Prisoner in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; handles player poke interaction; drives AI action commands; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``974``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Innate_Is_Stationary``, ``Enable_HUD_Pokable_Indicator``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Get_Position``
* Summary source: ``heuristic``

M06_Clear_For_Mendoza
---------------------

M06_Clear_For_Mendoza in Mission06.cpp initializes behavior when the object is created; creates or destroys objects.

* Source line: ``5626``
* Event hooks: ``Created``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Destroy_Object``
* Summary source: ``heuristic``

M06_Collapse_Zone
-----------------

M06_Collapse_Zone in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects; controls animation playback.

* Source line: ``5311``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Set_Model``, ``Set_Animation``
* Summary source: ``heuristic``

Parameter Description::

   Zone_ID=0:int

M06_Courtyard_Apache
--------------------

M06_Courtyard_Apache in Mission06.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4853``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

M06_Courtyard_Controller
------------------------

M06_Courtyard_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``2525``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Enable_Spawner``, ``Create_Logical_Sound``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M06_Courtyard_Eagle
-------------------

M06_Courtyard_Eagle in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; sends custom events.

* Source line: ``3243``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Action_Goto``, ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Courtyard_Patrol
--------------------

M06_Courtyard_Patrol in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; starts conversations.

* Source line: ``1997``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID=0:int, Waypath_Loc:Vector3

M06_Courtyard_Unit
------------------

M06_Courtyard_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4413``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_DataDisc_01_DLS
-------------------

M06_DataDisc_01_DLS in Mission06.cpp responds to custom events.

* Source line: ``5646``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Character``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

M06_Destruction_Stub
--------------------

M06_Destruction_Stub in Mission06.cpp responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; creates explosions.

* Source line: ``685``
* Event hooks: ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Set_Facing``, ``Get_Random``, ``Start_Timer``, ``Get_Position``, ``Get_Facing``
* Summary source: ``heuristic``

M06_Drop_Thunder_Squad
----------------------

M06_Drop_Thunder_Squad in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; creates or destroys objects; starts conversations.

* Source line: ``5057``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M06_Enable_Alarm_Objective
--------------------------

M06_Enable_Alarm_Objective in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``5662``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Barracks
-------------------

M06_Enable_Barracks in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``2970``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Barracks_Mess
------------------------

M06_Enable_Barracks_Mess in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4554``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Bathroom
-------------------

M06_Enable_Bathroom in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4506``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Courtyard
--------------------

M06_Enable_Courtyard in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4454``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Exterior_Courtyard
-----------------------------

M06_Enable_Exterior_Courtyard in Mission06.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``2876``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Create_Logical_Sound``
* Summary source: ``heuristic``

M06_Enable_Floor1_Bedroom
-------------------------

M06_Enable_Floor1_Bedroom in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3804``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Floor1_Library
-------------------------

M06_Enable_Floor1_Library in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3726``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Floor2_Bedroom
-------------------------

M06_Enable_Floor2_Bedroom in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3844``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Floor2_Conference
----------------------------

M06_Enable_Floor2_Conference in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4034``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Floor2_Library
-------------------------

M06_Enable_Floor2_Library in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``3956``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Greenhouse
---------------------

M06_Enable_Greenhouse in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3075``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Guard_Tower
----------------------

M06_Enable_Guard_Tower in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``1091``
* Event hooks: ``Created``, ``Action_Complete``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Hedgemaze
--------------------

M06_Enable_Hedgemaze in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``2922``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Interior
-------------------

M06_Enable_Interior in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``3018``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Lab
--------------

M06_Enable_Lab in Mission06.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``3125``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Enable_Spawner``
* Summary source: ``heuristic``

M06_Enable_North_Barracks
-------------------------

M06_Enable_North_Barracks in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4774``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_Officers_Mess
------------------------

M06_Enable_Officers_Mess in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4318``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_South_Barracks
-------------------------

M06_Enable_South_Barracks in Mission06.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``4683``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Enable_WarRoom
------------------

M06_Enable_WarRoom in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``4225``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object_At_Bone``, ``Attach_To_Object_Bone``, ``Disable_All_Collisions``, ``Set_Facing``, ``Get_Facing``
* Summary source: ``heuristic``

M06_Enable_Warroom_DoorGuard
----------------------------

M06_Enable_Warroom_DoorGuard in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``4157``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Escort_Tank
---------------

M06_Escort_Tank in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers.

* Source line: ``1289``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Enable_Enemy_Seen``, ``Enable_Hibernation``, ``Action_Goto``, ``Debug_Message``, ``Enable_Engine``, ``Attach_Script``
* Summary source: ``heuristic``

M06_Floor1_Bedroom_Unit
-----------------------

M06_Floor1_Bedroom_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``3772``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``
* Summary source: ``heuristic``

M06_Floor1_Library_Unit
-----------------------

M06_Floor1_Library_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``3684``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Disable``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Floor2_Bedroom_Unit
-----------------------

M06_Floor2_Bedroom_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``3884``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``
* Summary source: ``heuristic``

M06_Floor2_Conference_Unit
--------------------------

M06_Floor2_Conference_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``3993``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Floor2_Library_Unit
-----------------------

M06_Floor2_Library_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``3914``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Flyover
-----------

M06_Flyover in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``5040``
* Event hooks: ``Created``, ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Flyover_ID=0:int

M06_Flyover_Controller
----------------------

M06_Flyover_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``4914``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M06_Gate_Guards
---------------

M06_Gate_Guards in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``1143``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``, ``Debug_Message``, ``Action_Goto``, ``Create_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Soldier_ID=0:int

M06_GDI_Prisoner
----------------

M06_GDI_Prisoner in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; sends custom events; changes inventory or weapons; starts conversations.

* Source line: ``839``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Player_Type``, ``Enable_HUD_Pokable_Indicator``, ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M06_Greenhouse_Shaft_Unit
-------------------------

M06_Greenhouse_Shaft_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``3643``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Havoc_DLS
-------------

M06_Havoc_DLS in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; changes inventory or weapons.

* Source line: ``3353``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Give_PowerUp``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Debug_Message``, ``Create_Logical_Sound``, ``Set_Position``
* Summary source: ``heuristic``

M06_Hedgemaze_Controller
------------------------

M06_Hedgemaze_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``2572``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Enable_Spawner``, ``Create_Logical_Sound``
* Summary source: ``heuristic``

M06_Hedgemaze_Eagle
-------------------

M06_Hedgemaze_Eagle in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``3304``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_Hedgemaze_Patrol
--------------------

M06_Hedgemaze_Patrol in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; starts conversations.

* Source line: ``2102``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID=0:int, Waypath_Loc:Vector3

M06_Interior_Controller
-----------------------

M06_Interior_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; starts conversations.

* Source line: ``2690``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Enable_Spawner``
* Summary source: ``heuristic``

M06_Interior_Patrol
-------------------

M06_Interior_Patrol in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``2206``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID=0:int, Waypath_Loc:Vector3

M06_KaneHead
------------

M06_KaneHead in Mission06.cpp initializes behavior when the object is created; creates or destroys objects; starts conversations.

* Source line: ``4271``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Find_Object``, ``Start_Conversation``, ``Monitor_Conversation``, ``Destroy_Object``
* Summary source: ``heuristic``

M06_Lab_Guard
-------------

M06_Lab_Guard in Mission06.cpp initializes behavior when the object is created.

* Source line: ``2484``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``
* Summary source: ``heuristic``

M06_Lab_Patrol
--------------

M06_Lab_Patrol in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``2275``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID=0:int, Waypath_Loc:Vector3

M06_Mendoza
-----------

M06_Mendoza in Mission06.cpp reacts to destruction state; sends custom events.

* Source line: ``828``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M06_MidtroB_Explosion_Controller
--------------------------------

M06_MidtroB_Explosion_Controller in Mission06.cpp responds to custom events; creates explosions.

* Source line: ``620``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Get_Position``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Loc0_ID=0:int, Loc1_ID=0:int, Loc2_ID=0:int, Loc3_ID=0:int, Loc4_ID=0:int

M06_Move_Sydney
---------------

M06_Move_Sydney in Mission06.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``5283``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Move_Loc=0:int

M06_Nod_Tower
-------------

M06_Nod_Tower in Mission06.cpp initializes behavior when the object is created; reacts to destruction state.

* Source line: ``2499``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Enable_Spawner``
* Summary source: ``heuristic``

M06_North_Barracks_Unit
-----------------------

M06_North_Barracks_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``4821``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``
* Summary source: ``heuristic``

M06_Objective_Controller
------------------------

M06_Objective_Controller in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``48``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Background_Music``, ``Scale_AI_Awareness``, ``Start_Timer``, ``Enable_Hibernation``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M06_Officers_Mess_Unit
----------------------

M06_Officers_Mess_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4373``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Resistance_Raider_DLS
-------------------------

M06_Resistance_Raider_DLS in Mission06.cpp initializes behavior when the object is created; handles player poke interaction; creates or destroys objects; controls animation playback; starts conversations.

* Source line: ``3473``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Set_Animation``, ``Apply_Damage``, ``Enable_HUD_Pokable_Indicator``, ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Servant_Behavior
--------------------

M06_Servant_Behavior in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; starts conversations.

* Source line: ``5132``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Get_Position``, ``Action_Face_Location``, ``Action_Play_Animation``, ``Create_Logical_Sound``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Loc1_ID=0:int, Loc2_ID=0:int, Loc3_ID=0:int, Animation=S_A_HUMAN.H_A_A0F0:string

M06_South_Barracks_Unit
-----------------------

M06_South_Barracks_Unit in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4732``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Innate_Enable``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M06_Sydney_Mobius
-----------------

M06_Sydney_Mobius in Mission06.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``381``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Is_Stationary``, ``Grant_Key``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

M06_Thunder_Unit
----------------

M06_Thunder_Unit in Mission06.cpp initializes behavior when the object is created; reacts to destruction state; drives AI action commands; creates or destroys objects.

* Source line: ``5098``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Set_Innate_Soldier_Home_Location``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M06_Tower_Patrol
----------------

M06_Tower_Patrol in Mission06.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; starts conversations.

* Source line: ``1891``
* Event hooks: ``Created``, ``Killed``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Start_Timer``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID=0:int, Waypath_Loc:Vector3

M06_WarRoom_Bodyguard_DLS
-------------------------

M06_WarRoom_Bodyguard_DLS in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``4122``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Innate_Enable``
* Summary source: ``heuristic``

M06_WarRoom_Computer
--------------------

M06_WarRoom_Computer in Mission06.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``309``
* Event hooks: ``Created``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Create_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M06_WarRoom_DoorGuard
---------------------

M06_WarRoom_DoorGuard in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior.

* Source line: ``4191``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Innate_Enable``
* Summary source: ``heuristic``

M06_WarRoom_Officer_DLS
-----------------------

M06_WarRoom_Officer_DLS in Mission06.cpp initializes behavior when the object is created; responds to custom events; changes innate AI behavior; starts conversations.

* Source line: ``4073``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Set_Innate_Is_Stationary``, ``Innate_Enable``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``
