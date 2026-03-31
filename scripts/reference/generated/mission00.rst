Mission00.cpp
=============

* Category: ``mission``
* Active scripts: ``22``
* Source: ``Code/Scripts/Mission00.cpp``

MSK_Controller
--------------

MSK_Controller in Mission00.cpp initializes behavior when the object is created; responds to custom events; starts conversations.

* Source line: ``3869``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``, ``Add_Radar_Marker``, ``Trigger_Spawner``
* Summary source: ``heuristic``

MSK_Info_Zone
-------------

MSK_Info_Zone in Mission00.cpp initializes behavior when the object is created; watches enter or exit events; starts conversations.

* Source line: ``4155``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Clear_Radar_Marker``, ``Force_Camera_Look``, ``Set_HUD_Help_Text``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

MSK_Soldier
-----------

MSK_Soldier in Mission00.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``3926``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Enable_Innate_Conversations``, ``Enable_Hibernation``, ``Action_Goto``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Player_Type``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Spawner_ID:int

MTU_Building_Controller
-----------------------

MTU_Building_Controller in Mission00.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``3728``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Get_Max_Health``, ``Set_Health``, ``Set_Building_Power``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Building_ID:int

MTU_Commando
------------

MTU_Commando in Mission00.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; changes inventory or weapons.

* Source line: ``3346``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Weapon``, ``Select_Weapon``, ``Control_Enable``, ``Action_Follow_Input``, ``Force_Camera_Look``, ``Start_Timer``, ``Get_Health``, ``Get_Max_Health``
* Summary source: ``heuristic``

MTU_Commando_Startup
--------------------

MTU_Commando_Startup in Mission00.cpp initializes behavior when the object is created.

* Source line: ``3456``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``
* Summary source: ``heuristic``

MTU_Flyover
-----------

MTU_Flyover in Mission00.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``3837``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Vehicle_ID:int

MTU_GDI_Soldier
---------------

MTU_GDI_Soldier in Mission00.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; controls animation playback; changes inventory or weapons; changes innate AI behavior; starts conversations.

* Source line: ``3228``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Loiters_Allowed``, ``Enable_Enemy_Seen``, ``Innate_Disable``, ``Get_ID``, ``Start_Timer``, ``Get_Position``, ``Get_Distance``
* Summary source: ``heuristic``

MTU_GDI_Vehicle
---------------

MTU_GDI_Vehicle in Mission00.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``3641``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Find_Object``, ``Send_Custom_Event``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

Parameter Description::

   Vehicle_ID:int

MTU_Nod_Apache
--------------

MTU_Nod_Apache in Mission00.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects.

* Source line: ``3507``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``, ``Action_Goto``, ``Start_Timer``, ``Destroy_Object``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Apache_ID:int

MTU_Nod_Soldier
---------------

MTU_Nod_Soldier in Mission00.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes innate AI behavior.

* Source line: ``3773``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Innate_Disable``, ``Action_Goto``, ``Start_Timer``, ``Set_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Soldier_ID:int

MTU_PowerUp_Armor
-----------------

MTU_PowerUp_Armor in Mission00.cpp responds to custom events; sends custom events.

* Source line: ``3486``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MTU_PowerUp_Health
------------------

MTU_PowerUp_Health in Mission00.cpp responds to custom events; sends custom events.

* Source line: ``3465``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MTU_Range_Powerup
-----------------

MTU_Range_Powerup in Mission00.cpp responds to custom events; sends custom events.

* Source line: ``3624``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Powerup_ID:int

MTU_Range_Target
----------------

MTU_Range_Target in Mission00.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; changes innate AI behavior.

* Source line: ``3544``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Innate_Disable``, ``Get_Position``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Target_ID:int

MTU_Range_Target_Miss_Commando
------------------------------

MTU_Range_Target_Miss_Commando in Mission00.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3604``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Action_Attack``
* Summary source: ``heuristic``

MTU_Range_Target_Path_Left
--------------------------

MTU_Range_Target_Path_Left in Mission00.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3591``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

MTU_Range_Target_Path_Mid
-------------------------

MTU_Range_Target_Path_Mid in Mission00.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3565``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

MTU_Range_Target_Path_Right
---------------------------

MTU_Range_Target_Path_Right in Mission00.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``3578``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

MTU_Trigger_Zone
----------------

MTU_Trigger_Zone in Mission00.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``2758``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Set_HUD_Help_Text``, ``Find_Object``, ``Send_Custom_Event``, ``Has_Key``, ``Clear_Radar_Marker``, ``Destroy_Object``, ``Get_Max_Health``
* Summary source: ``heuristic``

MTU_Tutorial_Controller
-----------------------

MTU_Tutorial_Controller in Mission00.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; controls animation playback; updates objectives; changes innate AI behavior.

* Source line: ``45``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Map``, ``Add_Radar_Marker``, ``Add_Objective``, ``Start_Timer``, ``Find_Object``, ``Set_Animation_Frame``, ``Send_Custom_Event``, ``Create_Object``
* Summary source: ``heuristic``

MTU_Tutorial_Instructor
-----------------------

MTU_Tutorial_Instructor in Mission00.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects; controls animation playback; changes inventory or weapons; updates objectives; changes innate AI behavior; starts conversations.

* Source line: ``1218``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Loiters_Allowed``, ``Innate_Disable``, ``Set_Shield_Type``, ``Enable_Hibernation``, ``Send_Custom_Event``, ``Start_Timer``, ``Action_Reset``, ``Find_Object``
* Summary source: ``heuristic``
