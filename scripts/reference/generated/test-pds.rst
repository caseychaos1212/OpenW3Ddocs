Test_PDS.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``15``
* Source: ``Code/Scripts/Test_PDS.cpp``

PDS_Generic_Test
----------------

PDS_Generic_Test in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``42``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_The_Star``, ``Get_Position``, ``Get_Safe_Flight_Height``, ``Set_Position``
* Summary source: ``heuristic``

PDS_Get_In_Vehicle_Do_Waypath
-----------------------------

PDS_Get_In_Vehicle_Do_Waypath in Test_PDS.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``299``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Position``, ``Action_Movement_Goto_Location``, ``Action_Goto``, ``Action_Movement_Follow_Waypath``
* Summary source: ``heuristic``

Parameter Description::

   VehicleID=:int,WaypathID=:int,V3Test=1.3 44.543 0:vector3

PDS_Test_Bubba
--------------

PDS_Test_Bubba in Test_PDS.cpp initializes behavior when the object is created.

* Source line: ``796``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Clear_Map_Cell_By_Pos``, ``Get_Position``, ``Clear_Map_Cell``
* Summary source: ``heuristic``

PDS_Test_Controller
-------------------

PDS_Test_Controller in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``835``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_The_Star``, ``Attach_Script``
* Summary source: ``heuristic``

PDS_Test_Conversation
---------------------

PDS_Test_Conversation in Test_PDS.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; controls animation playback; starts conversations.

* Source line: ``188``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Set_Animation``, ``Create_Conversation``, ``Join_Conversation``, ``Get_The_Star``, ``Find_Object``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   Conversation Name=:string,Soldier1_ID=0:int,Soldier2_ID=0:int,Soldier3_ID=0:int

PDS_Test_Dock
-------------

PDS_Test_Dock in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``138``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Enable_Engine``, ``Get_Position``, ``Action_Dock``
* Summary source: ``heuristic``

Parameter Description::

   DockDestObjID=:int,DockEntranceObjID=:int

PDS_Test_Follow_Player
----------------------

PDS_Test_Follow_Player in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; changes innate AI behavior.

* Source line: ``440``
* Event hooks: ``Created``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Grant_Key``, ``Innate_Disable``, ``Action_Movement_Follow_Object``, ``Get_The_Star``, ``Action_Attack``, ``Action_Goto``
* Summary source: ``heuristic``

PDS_Test_Follow_Waypath
-----------------------

PDS_Test_Follow_Waypath in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``484``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Enable_Engine``, ``Get_The_Star``, ``Action_Attack``, ``Action_Movement_Follow_Waypath``, ``Modify_Action``, ``Action_Goto``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   WaypathID=:int,WaypointStartID=:int,WaypointEndID=:int

PDS_Test_Goto_Loc
-----------------

PDS_Test_Goto_Loc in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``395``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Get_Position``, ``Action_Movement_Goto_Location``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   ObjDestID=:int

PDS_Test_Goto_Player
--------------------

PDS_Test_Goto_Player in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``356``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_The_Star``, ``Action_Goto``
* Summary source: ``heuristic``

PDS_Test_Gunboat
----------------

PDS_Test_Gunboat in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``864``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Engine``, ``Disable_All_Collisions``, ``Start_Timer``, ``Get_Random``, ``Action_Goto``, ``Get_The_Star``, ``Get_Position``, ``Action_Attack``
* Summary source: ``heuristic``

PDS_Test_Harvester
------------------

PDS_Test_Harvester in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``557``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``, ``Find_Object``, ``Get_Position``, ``Action_Movement_Goto_Location``, ``Action_Goto``, ``Action_Movement_Backup_Goto_Location``
* Summary source: ``heuristic``

Parameter Description::

   TiberiumID=:int,DriveToID=:int,EntranceID=:int,DockID=:int

PDS_Test_Inventory
------------------

PDS_Test_Inventory in Test_PDS.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``727``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: none detected
* Summary source: ``heuristic``

PDS_Test_Modify_Attack
----------------------

PDS_Test_Modify_Attack in Test_PDS.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``69``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Enable_Engine``, ``Action_Attack``, ``Get_The_Star``, ``Action_Goto``, ``Modify_Action``
* Summary source: ``heuristic``

Parameter Description::

   WaypathID=:int

PDS_Test_Sound
--------------

PDS_Test_Sound in Test_PDS.cpp initializes behavior when the object is created; responds to custom events; handles player poke interaction.

* Source line: ``977``
* Event hooks: ``Created``, ``Custom``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Stop_Sound``, ``Start_Sound``
* Summary source: ``heuristic``
