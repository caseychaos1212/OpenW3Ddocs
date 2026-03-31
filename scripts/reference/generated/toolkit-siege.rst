Toolkit_Siege.cpp
=================

* Category: ``toolkit``
* Active scripts: ``2``
* Source: ``Code/Scripts/Toolkit_Siege.cpp``

M00_Siege_Actor_RAD
-------------------

M00_Siege_Actor_RAD in Toolkit_Siege.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``169``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_ID``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=1:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   My_Group_ID=0:int, Debug_Mode=0:int

M00_Siege_Zone_RAD
------------------

M00_Siege_Zone_RAD in Toolkit_Siege.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``41``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Get_Position``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Logical_Sound``, ``Get_ID``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=1:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Wander_Distance=3.0:float, My_Group_ID=0:int, Attraction_Radius=20.0:float, Debug_Mode=0:int
