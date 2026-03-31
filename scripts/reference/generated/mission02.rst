Mission02.cpp
=============

* Category: ``mission``
* Active scripts: ``26``
* Source: ``Code/Scripts/Mission02.cpp``

M02_Approach_Vehicle
--------------------

M02_Approach_Vehicle in Mission02.cpp responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``4966``
* Event hooks: ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Action_Goto``, ``Start_Timer``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

M02_Commando_Start
------------------

M02_Commando_Start in Mission02.cpp initializes behavior when the object is created; changes inventory or weapons.

* Source line: ``5309``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``
* Summary source: ``heuristic``

M02_Dam_MCT
-----------

M02_Dam_MCT in Mission02.cpp initializes behavior when the object is created; sends custom events; controls animation playback.

* Source line: ``4046``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Grant_Key``, ``Set_Animation_Frame``
* Summary source: ``heuristic``

M02_Data_Disk
-------------

M02_Data_Disk in Mission02.cpp responds to custom events.

* Source line: ``5320``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Clear_Map_Region_By_Pos``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

Parameter Description::

   Disk_ID:int

M02_Destroy_Objective
---------------------

M02_Destroy_Objective in Mission02.cpp reacts to destruction state; sends custom events; creates or destroys objects.

* Source line: ``4096``
* Event hooks: ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Objective_ID:int

M02_Destroy_Vehicle
-------------------

M02_Destroy_Vehicle in Mission02.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``5013``
* Event hooks: ``Created``, ``Damaged``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Start_Timer``, ``Action_Goto``, ``Apply_Damage``, ``Action_Attack``
* Summary source: ``heuristic``

M02_Encyclopedia_Reveal
-----------------------

M02_Encyclopedia_Reveal in Mission02.cpp responds to custom events.

* Source line: ``5357``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Vehicle``, ``Reveal_Encyclopedia_Building``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

Parameter Description::

   Disk_ID:int

M02_GDI_Helicopter
------------------

M02_GDI_Helicopter in Mission02.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``5287``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M02_GDI_Soldier
---------------

M02_GDI_Soldier in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``4193``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Disable``, ``Start_Timer``, ``Find_Object``, ``Get_Building_Power``, ``Action_Goto``, ``Get_Position``, ``Get_A_Star``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int, Soldier_Type=0:int

M02_Helipad
-----------

M02_Helipad in Mission02.cpp reacts to destruction state; sends custom events.

* Source line: ``4082``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M02_Mendoza
-----------

M02_Mendoza in Mission02.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects; changes innate AI behavior; starts conversations.

* Source line: ``5059``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Get_Shield_Strength``, ``Innate_Disable``, ``Action_Attack``, ``Start_Timer``, ``Set_Health``, ``Set_Shield_Strength``, ``Action_Goto``
* Summary source: ``heuristic``

M02_Nod_Apache
--------------

M02_Nod_Apache in Mission02.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events.

* Source line: ``4538``
* Event hooks: ``Created``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Start_Timer``, ``Action_Attack``, ``Get_Position``, ``Get_A_Star``, ``Get_Distance``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

M02_Nod_Convoy_Truck
--------------------

M02_Nod_Convoy_Truck in Mission02.cpp reacts to destruction state; sends custom events.

* Source line: ``4166``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``
* Summary source: ``heuristic``

M02_Nod_Jet
-----------

M02_Nod_Jet in Mission02.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``5240``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M02_Nod_Jet_Waypath
-------------------

M02_Nod_Jet_Waypath in Mission02.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``5263``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

M02_Nod_Sakura
--------------

M02_Nod_Sakura in Mission02.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects.

* Source line: ``4872``
* Event hooks: ``Created``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Enable_Engine``, ``Disable_Physical_Collisions``, ``Action_Goto``, ``Start_Timer``, ``Action_Attack``, ``Get_Position``, ``Get_A_Star``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

M02_Nod_Soldier
---------------

M02_Nod_Soldier in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``3373``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Get_Position``, ``Set_Innate_Soldier_Home_Location``, ``Enable_Hibernation``, ``Start_Timer``, ``Grant_Key``, ``Get_A_Star``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Area_Number:int,Area_Officer:int,Pre_Placed:int

M02_Nod_Vehicle
---------------

M02_Nod_Vehicle in Mission02.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events.

* Source line: ``4708``
* Event hooks: ``Created``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Enable_Engine``, ``Action_Attack``, ``Start_Timer``, ``Send_Custom_Event``, ``Get_Position``, ``Get_A_Star``, ``Get_Distance``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

M02_Obelisk
-----------

M02_Obelisk in Mission02.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3884``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Building_Power``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Stop_All_Conversations``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M02_Objective_Controller
------------------------

M02_Objective_Controller in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; changes inventory or weapons; updates objectives; starts conversations.

* Source line: ``45``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Character``, ``Set_Background_Music``, ``Find_Object``, ``Set_Animation_Frame``, ``Enable_Hibernation``, ``Set_HUD_Help_Text``, ``Add_Objective``, ``Set_Objective_HUD_Info_Position``
* Summary source: ``heuristic``

M02_Objective_Zone
------------------

M02_Objective_Zone in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``515``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_ID``, ``Has_Key``, ``Stop_All_Conversations``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M02_Player_Vehicle
------------------

M02_Player_Vehicle in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``4797``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Vehicle_Transitions``, ``Set_Player_Type``, ``Start_Timer``, ``Get_ID``, ``Get_Position``, ``Get_A_Star``, ``Get_Distance``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int

M02_Power_Plant
---------------

M02_Power_Plant in Mission02.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3960``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Max_Health``, ``Set_Health``, ``Stop_All_Conversations``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M02_Reset_Spawn
---------------

M02_Reset_Spawn in Mission02.cpp reacts to destruction state; sends custom events.

* Source line: ``3355``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int,Spawn_Type:int

M02_Respawn_Controller
----------------------

M02_Respawn_Controller in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``2155``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Get_Difficulty_Level``, ``Trigger_Spawner``
* Summary source: ``heuristic``

M02_Stationary_Vehicle
----------------------

M02_Stationary_Vehicle in Mission02.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; changes innate AI behavior; starts conversations.

* Source line: ``4437``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Innate_Disable``, ``Start_Timer``, ``Get_ID``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Area_ID:int
