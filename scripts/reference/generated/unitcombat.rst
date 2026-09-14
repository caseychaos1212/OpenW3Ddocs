unitcombat.cpp
==============

* Category: ``misc``
* Indexed registrations: ``1``
* Source: ``Code/Scripts/unitcombat.cpp``

Unit_Combat
-----------

Unit_Combat in unitcombat.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; controls animation playback.

* Source line: ``59``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Random``, ``Get_ID``, ``Get_Position``, ``Start_Timer``, ``Enable_Enemy_Seen``, ``Get_Health``
* Summary source: ``heuristic``

Parameter Description::

   Scoreboard_ID=0:int,Controller_ID=0:int,Script_Override=0:int,Soldier_Type=0:int
