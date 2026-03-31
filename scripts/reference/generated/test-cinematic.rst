Test_Cinematic.cpp
==================

* Category: ``test-and-prototype``
* Active scripts: ``3``
* Source: ``Code/Scripts/Test_Cinematic.cpp``

M00_Cinematic_Attack_Command_DLS
--------------------------------

M00_Cinematic_Attack_Command_DLS in Test_Cinematic.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``45``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Facing``, ``Get_Position``, ``Action_Attack``, ``Send_Custom_Event``, ``Action_Reset``
* Summary source: ``heuristic``

Parameter Description::

   AttackDuration=1.0:float

Test_Cinematic
--------------

Test_Cinematic in Test_Cinematic.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; controls animation playback; plays sounds; changes innate AI behavior.

* Source line: ``122``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: ``Save_Data``, ``Load_Data``
* Key engine calls: ``Debug_Message``, ``Text_File_Open``, ``Text_File_Get_String``, ``Text_File_Close``, ``Get_Sync_Time``, ``Begin_Chunk``, ``Save_Data``, ``End_Chunk``
* Summary source: ``heuristic``

Parameter Description::

   ControlFilename=:string

Test_Cinematic_Primary_Killed
-----------------------------

Test_Cinematic_Primary_Killed in Test_Cinematic.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events.

* Source line: ``73``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   CallbackID=:int
