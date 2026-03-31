unitcombat.cpp
==============

* Category: ``misc``
* Active scripts: ``1``
* Source: ``Code/Scripts/unitcombat.cpp``

Unit_Combat
-----------

Unit_Combat in unitcombat.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; creates or destroys objects; controls animation playback.

* Source line: ``59``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: ``Save_Data``, ``Load_Data``
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Random``, ``Get_ID``, ``Get_Position``, ``Start_Timer``, ``Enable_Enemy_Seen``, ``Enable_Sound_Heard``
* Summary source: ``heuristic``

Parameter Description::

   Scoreboard_ID=0:int,Controller_ID=0:int,Script_Override=0:int,Soldier_Type=0:int
