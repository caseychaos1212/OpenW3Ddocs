MissionDemo.cpp
===============

* Category: ``mission``
* Active scripts: ``10``
* Source: ``Code/Scripts/MissionDemo.cpp``

MDD_Commando
------------

MDD_Commando in MissionDemo.cpp initializes behavior when the object is created.

* Source line: ``1788``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Control_Enable``, ``Set_Shield_Type``
* Summary source: ``heuristic``

MDD_Flying_Vehicle
------------------

MDD_Flying_Vehicle in MissionDemo.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events.

* Source line: ``1691``
* Event hooks: ``Created``, ``Destroyed``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Enable_Enemy_Seen``, ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Start_Timer``, ``Action_Attack``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Unit_ID:int

MDD_GDI_Soldier
---------------

MDD_GDI_Soldier in MissionDemo.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects; changes innate AI behavior.

* Source line: ``1215``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Innate_Disable``, ``Start_Timer``, ``Apply_Damage``, ``Get_A_Star``, ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int, Soldier_Type=0:int

MDD_Havoc_Unit
--------------

MDD_Havoc_Unit in MissionDemo.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1798``
* Event hooks: ``Created``, ``Custom``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Shield_Type``, ``Set_Shield_Strength``, ``Start_Timer``, ``Action_Goto``
* Summary source: ``heuristic``

MDD_Nod_Apache
--------------

MDD_Nod_Apache in MissionDemo.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events.

* Source line: ``1448``
* Event hooks: ``Created``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Start_Timer``, ``Action_Attack``, ``Get_Position``, ``Find_Object``, ``Get_A_Star``, ``Get_Distance``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

MDD_Nod_Soldier
---------------

MDD_Nod_Soldier in MissionDemo.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes innate AI behavior.

* Source line: ``711``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Enable_Hibernation``, ``Start_Timer``, ``Grant_Key``, ``Get_A_Star``, ``Find_Object``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Area_Number:int,Area_Officer:int,Pre_Placed:int

MDD_Nod_Stealth
---------------

MDD_Nod_Stealth in MissionDemo.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``1623``
* Event hooks: ``Created``, ``Destroyed``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Enable_Enemy_Seen``, ``Action_Goto``, ``Start_Timer``, ``Action_Attack``, ``Get_Position``, ``Create_Logical_Sound``, ``Create_Object``
* Summary source: ``heuristic``

MDD_Objective_Controller
------------------------

MDD_Objective_Controller in MissionDemo.cpp initializes behavior when the object is created; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``48``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD``, ``Create_Object``, ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Enable_Hibernation``, ``Add_Objective``
* Summary source: ``heuristic``

MDD_Respawn_Controller
----------------------

MDD_Respawn_Controller in MissionDemo.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``97``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Create_Object``, ``Attach_Script``, ``Start_Timer``, ``Set_Facing``, ``Debug_Message``, ``Get_Difficulty_Level``
* Summary source: ``heuristic``

MDD_Stationary_Vehicle
----------------------

MDD_Stationary_Vehicle in MissionDemo.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events.

* Source line: ``1375``
* Event hooks: ``Created``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Enemy_Seen``, ``Start_Timer``, ``Action_Attack``, ``Get_Player_Type``, ``Send_Custom_Event``, ``Apply_Damage``, ``Action_Reset``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int
