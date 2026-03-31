Toolkit_Objects.cpp
===================

* Category: ``toolkit``
* Active scripts: ``13``
* Source: ``Code/Scripts/Toolkit_Objects.cpp``

M00_Create_Anim_Effect_DAY
--------------------------

One Time Special Effect Player Used with M00_PowerUp_Create_When_Killed_JDG

* Source line: ``334``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``, ``Destroy_Object``
* Summary source: ``source comment``

Parameter Description::

   Effect_Model:string

Source Notes::

   One Time Special Effect Player
   Used with M00_PowerUp_Create_When_Killed_JDG

   - Attach this script to an object that is created through script to play a W3d animation
   - (Effect_Model:string) is the name of the animation of the object.

M00_Disable_Transition
----------------------

M00_Disable_Transition in Toolkit_Objects.cpp initializes behavior when the object is created.

* Source line: ``445``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Vehicle_Transitions``
* Summary source: ``heuristic``

M00_Fire_Gas_Elec_Death_DAK
---------------------------

Death Script for Fire, Gas and Electric troops. - new script for default Fire, Gas and Electric troop deaths.

* Source line: ``463``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Get_Max_Health``, ``Action_Play_Animation``, ``Apply_Damage``
* Summary source: ``source comment``

Parameter Description::

   DeathType=1:int,HealthThreshhold=0.25:float

Source Notes::

   Death Script for Fire, Gas and Electric troops.

   - new script for default Fire, Gas and Electric troop deaths.
   - Takes preset DeathType:string ("Fire", "Gas", "Electric") and plays appropriate animation
   	and weapon FX. (1 = flailing and smoke. 2 = Elec Twiching and smoke? 3 = choking and green smoke. )

M00_No_Falling_Damage_DME
-------------------------

One Time Damage Modifier - Attach this script to an object that you do not want to recieve falling damage.

* Source line: ``364``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``source comment``

Source Notes::

   One Time Damage Modifier

   - Attach this script to an object that you do not want to recieve falling damage.
     Such as from a paradrop.

M00_Object_Create_Attach_Script_RMV
-----------------------------------

M00_Object_Create_Attach_Script_RMV in Toolkit_Objects.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``136``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Object_To_Create:string, Location:vector3, 
   Facing=0.00:float, Debug_Mode=0:int, Script_To_Attach:string, Script_Params:string

M00_Object_Create_RMV
---------------------

Creates a configured object immediately or after receiving a matching custom event.

* Source line: ``51``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``
* Summary source: ``manual``

Parameter Description::

   Start_Now=0:int, Receive_Type:int, Receive_Param_On=1:int, Object_To_Create:string, Location:vector3, 
   Facing=0.00:float, Debug_Mode=0:int

Source Notes::

   M00_Object_Create_RMV

     This script creates an object upon activation.

     Parameters:

     Object_To_Create	= The object to create.
     Location			= Where to create the object.
     Facing			= What facing to place the object at.

M00_Object_Destroy_RMV
----------------------

M00_Object_Destroy_RMV in Toolkit_Objects.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``99``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Receive_Type_Activate:int, Debug_Mode=0:int

M00_Object_Destroy_Self_RMV
---------------------------

M00_Object_Destroy_Self_RMV in Toolkit_Objects.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``207``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Get_ID``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Start_Now=1:int, Receive_Type=3:int, Receive_Param_On=1:int, Receive_Param_Off=0:int, 
   Receive_Param_Activate:int, Debug_Mode=0:int

M00_PCT_Pokable_DAK
-------------------

M00_PCT_Pokable_DAK in Toolkit_Objects.cpp initializes behavior when the object is created.

* Source line: ``569``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Display_Health_Bar``
* Summary source: ``heuristic``

M00_Permanent_No_Falling_Damage_IML
-----------------------------------

Permanent Damage Modifier - Attach this script to an object that you do not want to recieve falling damage.

* Source line: ``412``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``source comment``

Source Notes::

   Permanent Damage Modifier

   - Attach this script to an object that you do not want to recieve falling damage.

M00_PowerUp_Create_When_Killed_JDG
----------------------------------

PowerUp Creation - Includes ability to create any preset in the asset database by preset name

* Source line: ``272``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Get_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``source comment``

Parameter Description::

   rcentage=100:float,Create_At_Death_Pos=1:int,Position:vector3,Z_Offset=0.75:float,Spawn_Effect=0:int

Source Notes::

   PowerUp Creation

   - Includes ability to create any preset in the asset database by preset name
   - Includes ability to check a random to drop item (Drop_Percentage)
   - Arbitrary Create Position (Create_At_Death_Pos) & (Position)
   - Provision to Play a "Spawning" Special Effect with Create_Anim_Effect_DAY Script

M00_Send_Object_ID
------------------

M00_Send_Object_ID in Toolkit_Objects.cpp initializes behavior when the object is created; sends custom events.

* Source line: ``578``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Debug_Message``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Receiver_ID:int, Param=0:int, Delay=1.0f:int

M00_Vehicle_Regen_DAK
---------------------

Vehicle Health Regeneration Script for GDI Mammoth Tanks and Tiberium Harvesters. - continually checks vehicle's health to see if it needs to be regenerated.

* Source line: ``547``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_Health``, ``Get_Max_Health``, ``Apply_Damage``
* Summary source: ``source comment``

Source Notes::

   Vehicle Health Regeneration Script for GDI Mammoth Tanks and Tiberium Harvesters.

   - continually checks vehicle's health to see if it needs to be regenerated.
   - regenerates vehicle to 50% max health
