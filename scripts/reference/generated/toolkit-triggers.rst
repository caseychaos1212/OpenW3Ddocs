Toolkit_Triggers.cpp
====================

* Category: ``toolkit``
* Active scripts: ``12``
* Source: ``Code/Scripts/Toolkit_Triggers.cpp``

M00_Trigger_State_Sequence_RAD
------------------------------

Custom Parameter Settings:

* Source line: ``1323``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Get_Random``, ``Send_Custom_Event``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Num_States=2:int, Loop_States=0:int, Send_Type:int, Target_ID:int, 
   Min_Delay=0.0:float, Max_Delay=0.0:float, Debug_Mode=0:int

Source Notes::

   Custom Parameter Settings:

     0 = Turn this state sequence off.
     -1 = Advance to the next state.
     1+ = Adjust to this particular numbered state.

M00_Trigger_Timer_Expired_RAD
-----------------------------

M00_Trigger_Timer_Expired_RAD in Toolkit_Triggers.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``1188``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=0:int, Receive_Type=15:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Timer_Min=0.0:float, Timer_Max=1.0:float, Trigger_Count=0:int, Target_ID:int, Send_Type:int, 
   Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Debug_Mode=0:int

M00_Trigger_When_Action_Complete_RMV
------------------------------------

This script triggers when the unit completes any action. It is designed to respond to a particular Action ID.

* Source line: ``1008``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=8:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Action_ID:int, 
   Trigger_Count=0:int, Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Action_Complete_RMV

     This script triggers when the unit completes any action. It is designed to respond to
     a particular Action ID.

     Parameters:

     Trigger_Count	= How many times this will trigger.

M00_Trigger_When_Animation_Complete_RMV
---------------------------------------

This script triggers when the unit completes an animation.

* Source line: ``1103``
* Event hooks: ``Created``, ``Custom``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=9:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Animation_Name:string, Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, 
   Trigger_Count=0:int, Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Animation_Complete_RMV

     This script triggers when the unit completes an animation.

     Parameters:

     Animation_Name	= The name of the animation that is completing.
     Trigger_Count		= How many times this will trigger.

M00_Trigger_When_Created_RMV
----------------------------

This script triggers when the object it is attached to is created. NOTE that this script has no ability to be enabled/disabled.

* Source line: ``262``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Target_ID:int, Send_Type:int, Send_Parameter:int, Min_Delay=0.0:float, Max_Delay=0.0:float, 
   Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Created_RMV

     This script triggers when the object it is attached to is created.

     NOTE that this script has no ability to be enabled/disabled.

M00_Trigger_When_Damaged_RMV
----------------------------

This script triggers when the unit is damaged.

* Source line: ``914``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=7:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Trigger_Count=0:int, 
   Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Damaged_RMV

     This script triggers when the unit is damaged.

     Parameters:

     Trigger_Count	= How many times this will trigger.

M00_Trigger_When_Destroyed_RMV
------------------------------

This script triggers when the object it is attached to is destroyed.

* Source line: ``181``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=2:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Destroyed_RMV

     This script triggers when the object it is attached to is destroyed.

M00_Trigger_When_Enemy_Seen_RMV
-------------------------------

This script triggers when an enemy is seen.

* Source line: ``823``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=6:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Parameter:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Trigger_Count=0:int, 
   Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Enemy_Seen_RMV

     This script triggers when an enemy is seen.

     Parameters:

     Trigger_Count		= How many times this trigger will fire. Enter 0 for infinite.

M00_Trigger_When_Killed_RMV
---------------------------

Sends a custom event when the host object is enabled and a kill condition is reached.

* Source line: ``100``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``manual``

Parameter Description::

   Start_Now=1:int, Receive_Type=1:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Debug_Mode=0:int

Source Notes::

   M00_Trigger_When_Killed_RMV

     This script triggers when the object it is attached to is killed.

M00_Trigger_Zone_Entered_Or_Exited_RMV
--------------------------------------

This script triggers when the zone it is attached to is entered or exited.

* Source line: ``615``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=5:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Trigger_Count=0:int, 
   Triggerer=0:int, Debug_Mode=0:int

Source Notes::

   M00_Trigger_Zone_Entered_Or_Exited_RMV

     This script triggers when the zone it is attached to is entered or exited.

     Parameters:

     Trigger_Count		= How many times this trigger will fire.
     Triggerer         = Who can activate this trigger.

     Special Information:

     Values for Triggerer: 0 = Anyone, 1 = Commando Only, 2 = Non-Commando only
     Values for Trigger_Count: Enter 0 for infinite triggering.

M00_Trigger_Zone_Entered_RMV
----------------------------

This script triggers when the zone it is attached to is entered.

* Source line: ``314``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=3:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Trigger_Count=0:int, 
   Triggerer=0:int, Debug_Mode=0:int

Source Notes::

   M00_Trigger_Zone_Entered_RMV

     This script triggers when the zone it is attached to is entered.

     Parameters:

     Trigger_Count		= How many times this trigger will fire.
     Triggerer         = Who can activate this trigger.

     Special Information:

     Values for Triggerer: 0 = Anyone, 1 = Commando Only, 2 = Non-Commando only
     Values for Trigger_Count: Enter 0 for infinite triggering.

M00_Trigger_Zone_Exited_RMV
---------------------------

This script triggers when the zone it is attached to is exited.

* Source line: ``465``
* Event hooks: ``Created``, ``Custom``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_A_Star``, ``Find_Object``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=1:int, Receive_Type=4:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, Target_ID:int, 
   Send_Type:int, Send_Param:int, Min_Delay=0.0:float, Max_Delay=0.0:float, Trigger_Count=0:int, 
   Triggerer=0:int, Debug_Mode=0:int

Source Notes::

   M00_Trigger_Zone_Exited_RMV

     This script triggers when the zone it is attached to is exited.

     Parameters:

     Trigger_Count		= How many times this trigger will fire.
     Triggerer         = Who can activate this trigger.

     Special Information:

     Values for Triggerer: 0 = Anyone, 1 = Commando Only, 2 = Non-Commando only
     Values for Trigger_Count: Enter 0 for infinite triggering.
