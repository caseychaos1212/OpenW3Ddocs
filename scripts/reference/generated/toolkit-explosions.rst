Toolkit_Explosions.cpp
======================

* Category: ``toolkit``
* Active scripts: ``4``
* Source: ``Code/Scripts/Toolkit_Explosions.cpp``

M00_Create_Random_Explosion_DLS
-------------------------------

M00_Create_Random_Explosion_DLS in Toolkit_Explosions.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates explosions.

* Source line: ``135``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Get_Random_Int``, ``Create_Explosion``, ``Get_Position``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Explosion_Name:string, Delay_Min=0.0f:float, Delay_Max=4.0f:float, Loc_ID0=0:int, Loc_ID1=0:int, 
   Loc_ID2=0:int, Loc_ID3=0:int, Loc_ID4=0:int, Loc_ID5=0:int, Loc_ID6=0:int, Loc_ID7=0:int, 
   Loc_ID8=0:int, Loc_ID9=0:int

M00_Explosion_Create_At_Bone_RMV
--------------------------------

This creates an explosion on a specific bone of an object.

* Source line: ``101``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Explosion_At_Bone``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On:int, Explosion_Name:string, Object_ID:int, 
   Bone_Name:string, Debug_Mode=0:int

Source Notes::

   M00_Explosion_Create_At_Bone_RMV

     This creates an explosion on a specific bone of an object.

     Parameters:

     Explosion_Name	= The name of the explosion to create.
     Object_ID			= The ID of the object to create the explosion on.
     Bone_Name			= The bone name to create the explosion on.

M00_Explosion_Create_RMV
------------------------

This creates an explosion at a location.

* Source line: ``51``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Explosion``
* Summary source: ``source comment``

Parameter Description::

   Start_Now=0:int, Create_At_Obj=0:int, Receive_Type:int, Receive_Param_On=1:int, 
   Explosion_Name:string, Origin:vector3, Debug_Mode=0:int

Source Notes::

   M00_Explosion_Create_RMV

     This creates an explosion at a location.

     Parameters:

     Explosion_Name	= The name of the explosion type to make.
     Origin			= The Vector3 location of the explosion.

M00_NukeStrike_Anim
-------------------

M00_NukeStrike_Anim in Toolkit_Explosions.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; plays sounds.

* Source line: ``207``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Object``, ``Get_Position``, ``Set_Model``, ``Attach_Script``, ``Create_3D_Sound_At_Bone``, ``Shake_Camera``
* Summary source: ``heuristic``
