Toolkit.cpp
===========

* Category: ``toolkit``
* Active scripts: ``26``
* Source: ``Code/Scripts/Toolkit.cpp``

M00_5MetalBarrels_ChainRxn_Controller_JDG
-----------------------------------------

The two following scripts are a controller and a script for a gerneric barrel explosion chain rection. You only need to place the controller in your level and enter the Vector3's and barrel types as editor parameters

* Source line: ``387``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Create_Object``, ``Set_Animation_Frame``, ``Set_Facing``, ``Attach_Script``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Random``
* Summary source: ``source comment``

Parameter Description::

   Barrel01_Location:vector3, Barrel01_Type (1-8):int, Barrel01_Facing = 0:float, 
   Barrel02_Location:vector3, Barrel02_Type (1-8):int, Barrel02_Facing = 0:float, 
   Barrel03_Location:vector3, Barrel03_Type (1-8):int, Barrel03_Facing = 0:float, 
   Barrel04_Location:vector3, Barrel04_Type (1-8):int, Barrel04_Facing = 0:float, 
   Barrel05_Location:vector3, Barrel05_Type (1-8):int, Barrel05_Facing = 0:float

Source Notes::

   The two following scripts are a controller and a script for a gerneric barrel explosion chain rection.
   You only need to place the controller in your level and enter the Vector3's and barrel types as editor parameters
   See Joe G for further details

M00_Advanced_Guard_Tower
------------------------

This script handles the functionality of the Advanced Guard Tower in both single and multiplayer environments. Attach this script to the AGT Building Controller, and center the building

* Source line: ``706``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Get_ID``, ``Start_Timer``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``source comment``

Source Notes::

   M00_Advanced_Guard_Tower

     This script handles the functionality of the Advanced Guard Tower in both single and multiplayer
     environments. Attach this script to the AGT Building Controller, and center the building
     controller directly on the top of the tower roof.

     When created this script:
     - Creates four guard tower machine guns at the corners of the building
     - Attaches another script to the machine guns to allow them enemy_seen capability.
     - Creates a missile object at the top of the building.
     - Attaches another script to the missile object to allow it to respond to the guns.

     - The guns use enemy_seen to spot, and inform the missile when it is time to fire.

M00_Advanced_Guard_Tower_Gun
----------------------------

M00_Advanced_Guard_Tower_Gun in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; changes innate AI behavior.

* Source line: ``947``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Shield_Type``, ``Enable_Hibernation``, ``Innate_Enable``, ``Enable_Enemy_Seen``, ``Find_Object``, ``Get_ID``, ``Send_Custom_Event``, ``Get_Position``
* Summary source: ``heuristic``

M00_Advanced_Guard_Tower_Missile
--------------------------------

M00_Advanced_Guard_Tower_Missile in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``1029``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Is_Rendered``, ``Enable_Hibernation``, ``Find_Object``, ``Get_Position``, ``Get_Distance``, ``Action_Attack``, ``Start_Timer``, ``Action_Reset``
* Summary source: ``heuristic``

M00_ArmorMedal_TextMessage_JDG
------------------------------

M00_ArmorMedal_TextMessage_JDG in Toolkit.cpp responds to custom events.

* Source line: ``1732``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M00_Base_Defense
----------------

M00_Base_Defense in Toolkit.cpp initializes behavior when the object is created; continues work on timer callbacks; watches enter or exit events; drives AI action commands; uses timers; creates or destroys objects; changes innate AI behavior.

* Source line: ``1924``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Debug_Message``, ``Enable_Hibernation``, ``Innate_Enable``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Create_Object``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   MinAttackDistance=0:int, MaxAttackDistance=300:int, AttackTimer=10:int

M00_C130_Explosion
------------------

M00_C130_Explosion in Toolkit.cpp reacts to destruction state.

* Source line: ``320``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion_At_Bone``
* Summary source: ``heuristic``

M00_ChainRxn_Barrel_JDG
-----------------------

M00_ChainRxn_Barrel_JDG in Toolkit.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates explosions; controls animation playback.

* Source line: ``608``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Explosion``, ``Set_Animation``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID :int

M00_Change_L3Mutant_RadarMarker_JDG
-----------------------------------

M00_Change_L3Mutant_RadarMarker_JDG in Toolkit.cpp initializes behavior when the object is created.

* Source line: ``1754``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Obj_Radar_Blip_Color``
* Summary source: ``heuristic``

M00_Damage_Modifier_DME
-----------------------

M00_Damage_Modifier_DME in Toolkit.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``1825``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float, Star_Modifier=1:int, NotStar_Modifier=1:int, Killable_By_Star=1:int, 
   Killable_by_NotStar=1:int

M00_Debug_Text_File_RMV
-----------------------

Writes a text log of object lifecycle, combat, and custom-event activity for debugging attached scripts.

* Source line: ``76``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Enemy_Seen``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``
* Summary source: ``manual``

Parameter Description::

   Description=Object:string, Filename=DebugLog.txt:string

Source Notes::

   Toolkit Script Debuggers

M00_Disable_Physical_Collision_JDG
----------------------------------

M00_Disable_Physical_Collision_JDG in Toolkit.cpp initializes behavior when the object is created.

* Source line: ``304``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Disable_Physical_Collisions``
* Summary source: ``heuristic``

M00_Enable_Physical_Collision_JDG
---------------------------------

M00_Enable_Physical_Collision_JDG in Toolkit.cpp initializes behavior when the object is created.

* Source line: ``312``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Collisions``
* Summary source: ``heuristic``

M00_Generic_Conv_DME
--------------------

M00_Generic_Conv_DME in Toolkit.cpp initializes behavior when the object is created; starts conversations.

* Source line: ``1814``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

Parameter Description::

   ConvName:string

M00_HealthMedal_TextMessage_JDG
-------------------------------

M00_HealthMedal_TextMessage_JDG in Toolkit.cpp responds to custom events.

* Source line: ``1743``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M00_Monitor_Attached_Primary
----------------------------

M00_Monitor_Attached_Primary in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers.

* Source line: ``329``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Start_Timer``, ``Apply_Damage``, ``Find_Object``
* Summary source: ``heuristic``

M00_Nod_Obelisk
---------------

M00_Nod_Obelisk in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1492``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Start_Timer``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Health``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID=0:int

M00_Nod_Obelisk_CNC
-------------------

M00_Nod_Obelisk_CNC in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1241``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Start_Timer``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``, ``Get_Health``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID=0:int

M00_Nod_Turret
--------------

M00_Nod_Turret in Toolkit.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects; changes innate AI behavior.

* Source line: ``1104``
* Event hooks: ``Created``, ``Killed``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Innate_Enable``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Create_Object``, ``Get_ID``, ``Start_Timer``, ``Find_Object``
* Summary source: ``heuristic``

M00_Obelisk_Weapon
------------------

M00_Obelisk_Weapon in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``1560``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Is_Rendered``, ``Enable_Enemy_Seen``, ``Enable_Hibernation``, ``Innate_Enable``, ``Get_Position``, ``Create_Object``, ``Get_ID``
* Summary source: ``heuristic``

M00_Obelisk_Weapon_CNC
----------------------

M00_Obelisk_Weapon_CNC in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior.

* Source line: ``1317``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Player_Type``, ``Set_Is_Rendered``, ``Enable_Enemy_Seen``, ``Enable_Hibernation``, ``Innate_Enable``, ``Get_Position``, ``Create_Object``, ``Get_ID``
* Summary source: ``heuristic``

M00_Purchase_Terminal_GDI
-------------------------

M00_Purchase_Terminal_GDI in Toolkit.cpp handles player poke interaction.

* Source line: ``1078``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Display_GDI_Player_Terminal``
* Summary source: ``heuristic``

M00_Purchase_Terminal_Mutant
----------------------------

M00_Purchase_Terminal_Mutant in Toolkit.cpp handles player poke interaction.

* Source line: ``1095``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Display_Mutant_Player_Terminal``
* Summary source: ``heuristic``

M00_Purchase_Terminal_NOD
-------------------------

M00_Purchase_Terminal_NOD in Toolkit.cpp handles player poke interaction.

* Source line: ``1086``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Display_NOD_Player_Terminal``
* Summary source: ``heuristic``

M00_Select_Empty_Hands
----------------------

M00_Select_Empty_Hands in Toolkit.cpp initializes behavior when the object is created; responds to custom events; changes inventory or weapons.

* Source line: ``1711``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Select_Weapon``
* Summary source: ``heuristic``

Parameter Description::

   On_Created=1:int

M00_SSM_DLS
-----------

M00_SSM_DLS in Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers; creates or destroys objects; controls animation playback.

* Source line: ``1762``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object_At_Bone``, ``Set_Model``, ``Attach_To_Object_Bone``, ``Get_ID``, ``Set_Animation``, ``Find_Object``, ``Start_Timer``, ``Destroy_Object``
* Summary source: ``heuristic``
