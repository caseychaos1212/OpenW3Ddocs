Toolkit_Actions.cpp
===================

* Category: ``toolkit``
* Active scripts: ``4``
* Source: ``Code/Scripts/Toolkit_Actions.cpp``

M00_Action
----------

Configurable movement and attack controller that can start immediately or in response to a custom event.

* Source line: ``75``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Attack``, ``Action_Goto``, ``Action_Reset``
* Summary source: ``manual``

Parameter Description::

   Start_Now=0:int, Receive_Type=14:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Action_Priority=99:int, Action_ID=0:int, _Move_Target_ID=0:int, _Move_Following=0:int, 
   _Move_Destination:vector3, _Move_Waypath_ID=0:int, _Move_Waypath_Start_ID=0:int, 
   _Move_Waypath_End_ID:int, _Move_Waypath_Splined=0:int, _Move_Arrive_Distance=1.0:float, 
   _Move_Speed=1.0:float, _Move_Crouch=0:int, _Move_Backwards=0:int, _Move_Pathfind=1:int, 
   _Attack_Target_ID=0:int, _Attack_Location:vector3, _Attack_Range=100.0:float, 
   _Attack_Deviation=0.0:float, _Attack_Primary=1:int, _Attack_Crouched=0:int, Debug_Mode=0:int

Source Notes::

   M00_Action

     Animations are not handled with this script - they are handled separately.

     Parameters:

     _Move_Target_ID			= The Target ID to move towards.
     _Move_Following			= Whether this unit should follow the Target ID or not.
     _Move_Destination			= The Vector3 location of the movement destination.

     _Move_Waypath_ID			= The ID of a waypath to follow.
     _Move_Waypath_Start_ID	= The starting point to use on the waypath.
     _Move_Waypath_End_ID		= The ending point to use on the waypath.
     _Move_Waypath_Splined		= Whether to use splined movement or not on waypaths.
     _Move_Waypath_Looping		= If the unit should circle on the waypath.

     _Move_Patrol_Radius		= A radius to use if patrolling an area.
     _Move_Patrol_Loiter_Time	= How long to wait at each point until patrolling again.

     _Move_Arrive_Distance		= The distance to close to with the destination.
     _Move_Speed				= The speed at which the unit moves.
     _Move_Crouch				= Whether to move crouched or not.
     _Move_Backwards			= Whether to move backwards or not.
     _Move_Pathfind			= Whether to use pathfinding data for movement or not.

     _Attack_Target_ID			= The attack target's ID.
     _Attack_Location			= The location of the attack (if no target).

     _Attack_Range				= The maximum effective range of the attack.
     _Attack_Deviation			= The deviation of the attack.
     _Attack_Primary			= Whether to use the primary weapon or not.
     _Attack_Crouched			= Whether to crouch when firing or not.

M00_Action_Innate_Follow_Player
-------------------------------

M00_Action_Innate_Follow_Player in Toolkit_Actions.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``375``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Position``, ``Get_A_Star``, ``Action_Goto``
* Summary source: ``heuristic``

M00_Action_Innate_Follow_Waypath
--------------------------------

M00_Action_Innate_Follow_Waypath in Toolkit_Actions.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``341``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Waypath_ID:int

M00_Action_Set_Home_Location
----------------------------

M00_Action_Set_Home_Location in Toolkit_Actions.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``314``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=1:int, Receive_Type:int, Receive_Param_On:int, Home_Location:vector3, 
   Wander_Distance=99999.0:float
