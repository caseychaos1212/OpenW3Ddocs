Toolkit_Objectives.cpp
======================

* Category: ``toolkit``
* Active scripts: ``5``
* Source: ``Code/Scripts/Toolkit_Objectives.cpp``

M00_Global_Objective_Controller_RMV
-----------------------------------

M00_Global_Objective_Controller_RMV in Toolkit_Objectives.cpp initializes behavior when the object is created; responds to custom events; updates objectives.

* Source line: ``344``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Change_Objective_Type``, ``Set_Objective_Status``, ``Remove_Objective``
* Summary source: ``heuristic``

Parameter Description::

   Set_Type:int, Set_Status:int, Remove:int

M00_Objective_Controller_For_Locations_RMV
------------------------------------------

M00_Objective_Controller_For_Locations_RMV in Toolkit_Objectives.cpp initializes behavior when the object is created; responds to custom events; updates objectives.

* Source line: ``135``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Set_Objective_Radar_Blip``, ``Set_Objective_Status``
* Summary source: ``heuristic``

Parameter Description::

   Objective_ID:int, Objective_Type=1:int, Objective_Description_ID:int, Radar_Blip=1:int, Hidden=0:int, 
   Location:vector3, Custom_Type:int, Activate_Param=0:int, Unhide_Param=0:int, Success_Param:int, 
   Failure_Param:int

M00_Objective_Controller_For_Objects_Multiple_Triggers_RMV
----------------------------------------------------------

M00_Objective_Controller_For_Objects_Multiple_Triggers_RMV in Toolkit_Objectives.cpp initializes behavior when the object is created; responds to custom events; updates objectives.

* Source line: ``250``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Set_Objective_Status``
* Summary source: ``heuristic``

Parameter Description::

   Objective_ID:int, Objective_Type=1:int, Objective_Description_ID:int, Hidden=0:int, Custom_Type:int, 
   Activate_Param=0:int, Number_Of_Triggers:int, Trigger_Param:int, Unhide_Param=0:int, 
   Failure_Param:int

M00_Objective_Controller_For_Objects_RMV
----------------------------------------

M00_Objective_Controller_For_Objects_RMV in Toolkit_Objectives.cpp initializes behavior when the object is created; responds to custom events; updates objectives.

* Source line: ``40``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Find_Object``, ``Set_Objective_Radar_Blip_Object``, ``Set_Objective_Status``
* Summary source: ``heuristic``

Parameter Description::

   Objective_ID:int, Objective_Type=1:int, Objective_Description_ID:int, Radar_Blip=1:int, Hidden=0:int, 
   Object_ID:int, Custom_Type:int, Activate_Param=0:int, Unhide_Param=0:int, Success_Param:int, 
   Failure_Param:int

M00_Objective_Radar_Blip_On_Object_RMV
--------------------------------------

M00_Objective_Radar_Blip_On_Object_RMV in Toolkit_Objectives.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``232``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Objective_Radar_Blip_Object``
* Summary source: ``heuristic``

Parameter Description::

   Objective_ID:int, Activate_Type=0:int, Activate_Param=0:int
