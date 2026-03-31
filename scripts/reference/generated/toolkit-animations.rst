Toolkit_Animations.cpp
======================

* Category: ``toolkit``
* Active scripts: ``3``
* Source: ``Code/Scripts/Toolkit_Animations.cpp``

M00_Animation_Play_Drop_Object_Attach_Script_RMV
------------------------------------------------

M00_Animation_Drop_Object_Attach_Script_RMV This script plays an animation when the object it is attached to receives a custom, drops

* Source line: ``214``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Reset``, ``Create_Object_At_Bone``, ``Attach_Script``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Action_Priority:int, Action_ID:int, Animation:string, Drop_Frame:int, Drop_Object:string, 
   Drop_Bone:string, Script_Name:string, Script_Params:string, Debug_Mode=0:int

Source Notes::

   M00_Animation_Drop_Object_Attach_Script_RMV

     This script plays an animation when the object it is attached to receives a custom, drops
     a new object at a specified frame of the animation, and then attaches a script to the
     new object.

     Parameters:

     Animation		= The animation to play.
     Drop_Frame	= The frame at which to drop the object.
     Drop_Object	= The object to drop.
     Drop_Bone		= The bone from which the object is dropped.
     Script_Name	= The name of the script to attach.
     Script_Params	= The parameters for the attached script.

M00_Animation_Play_Drop_Object_RMV
----------------------------------

This script plays an animation when the object it is attached to receives a custom.

* Source line: ``145``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Reset``, ``Create_Object_At_Bone``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=1:int, 
   Action_Priority:int, Action_ID:int, Animation:string, Drop_Frame:int, Drop_Object:string, 
   Drop_Bone:string, Debug_Mode=0:int

Source Notes::

   M00_Animation_Play_Drop_Object_RMV

     This script plays an animation when the object it is attached to receives a custom.

     Parameters:

     Animation		= The animation to play.
     Drop_Frame	= The frame at which an object should drop.
     Drop_Object	= The object to drop.
     Drop_Bone		= The bone from which to drop the object.

M00_Animation_Play_RMV
----------------------

M00_Animation_Play_On_Activation_RMV This script plays an animation when the object it is attached to receives a custom.

* Source line: ``88``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Action_Reset``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Action_Priority:int, Action_ID:int, Animation:string, Loop=0:int, Debug_Mode=0:int

Source Notes::

   M00_Animation_Play_On_Activation_RMV

     This script plays an animation when the object it is attached to receives a custom.

     Parameters:

     Animation	= The animation to play.
     Loop		= Whether the animation should loop or not. 1 for looping. 0 for not.
