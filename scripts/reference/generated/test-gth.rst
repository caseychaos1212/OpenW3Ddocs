Test_GTH.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``12``
* Source: ``Code/Scripts/Test_GTH.cpp``

GTH_Create_Object_On_Enter
--------------------------

GTH_Create_Object_On_Enter (verified) This script will create an object when a script zone is entered by a game object. Use it

* Source line: ``184``
* Event hooks: ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Get_Random_Int``, ``Start_Timer``, ``Create_Object``
* Summary source: ``source comment``

Parameter Description::

   =:string,Position:vector3,Min_Delay=10:int,Max_Creations=1:int,Probability=100:int,Player_Type=2:int

Source Notes::

   GTH_Create_Object_On_Enter (verified)
   This script will create an object when a script zone is entered by a game object.  Use it
   to fire off cinematics for example...

   Params:
   Create_Object - name of the preset to create an instance of
   Position - world space position to create the object at
   Min_Delay - amount of time to wait before re-enabling the script once it has fired
   Max_Creations - maximum number of times the script should create an object
   Probability - integer between 1 and 100, chance on any given "Enter" that the object will be created
   Player_Type - type of player that can trigger integer, 0 = Nod, 1 = GDI, 2 = any

GTH_Create_Objective
--------------------

Adds an objective to the mission when the specified action (create, enter, poke, or kill) happens to the object with this script on it.

* Source line: ``470``
* Event hooks: ``Created``, ``Killed``, ``Poked``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Add_Objective``, ``Set_Objective_Radar_Blip``, ``Set_Objective_HUD_Info_Position``
* Summary source: ``source comment``

Parameter Description::

   e=0:int,Short_Desc_ID=0:int,Long_Desc_ID=0:int,Priority=90:float,Position:vector3,Pog_Texture:string

Source Notes::

   GTH_Create_Objective
   Adds an objective to the mission when the specified action (create, enter, poke, or kill)
   happens to the object with this script on it.

   params:
   Creation_Type - 0=Create, 1=Entered, 2=Poked, 3=Killed
   Objective_ID - id of the objective, match this with the "GTH_Objective_Complete" script
   Objective_Type - 0=PRIMARY, 1=SECONDARY
   Short_Desc_ID - string id for short description
   Long_Desc_ID - string id for long description
   Priority - priority of this objective
   Position - 3d position of the objective
   Pog_Texture - tga file for the objective pog
   Pog_Text_ID - string id for the pog text (usually something like IDS_POG_DESTROY)

GTH_Credit_Trickle
------------------

This script will give an amount money to its team at a regular interval. You can use it to create silos that give money as long as they're alive.

* Source line: ``770``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Give_Money``
* Summary source: ``source comment``

Parameter Description::

   Credits=1:int,Delay=2.0:float

Source Notes::

   GTH_Credit_Trickle
   This script will give an amount money to its team at a regular interval.  You can use it to
   create silos that give money as long as they're alive.
   NOTE: this won't work on buildings, only things like turrets, characters, or vehicles so make your
   "silos" as a weaponless vehcile set up like the nod-turret for example.

   Params:
   Credits - number of credits to give
   Delay - time between credit grants

GTH_CTF_Object2
---------------

GTH_CTF_Object This script will make the object it is attached to behave kind of like a CTF "flag" by

* Source line: ``871``
* Event hooks: ``Created``, ``Damaged``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Start_Timer``, ``Get_Player_Type``, ``Set_Position``, ``Find_Object``, ``Send_Custom_Event``, ``Get_ID``, ``Attach_To_Object_Bone``
* Summary source: ``source comment``

Parameter Description::

   _Object_To_Kill1=0:int,Win_Object_To_Kill2=0:int,Win_Object_To_Kill3=0:int,Win_Object_To_Kill4=0:int

Source Notes::

   GTH_CTF_Object
   This script will make the object it is attached to behave kind of like a CTF "flag" by
   attaching to the opposing player who pokes it.  If its position gets within a
   certain distance of the "enemy home" an internal counter is incremented.  Once the counter
   reaches a desired number, an object in the level is destroyed.  This object should be the
   only building owned by the flag's team so that they immediately lose.

   You should use this script on an object that has "projectile" collision only.  Make a model
   of your "flag", give it projectile collision and make a preset for it similar to the "Marker_Flag"
   in LevelEdit (you can find "Marker_Flag" under Object->Simple).

   CTF Rules as implemented:
   - this script controls how many flag captures cause a win
   - enemy entering the pickup radius of the flag attaches it to him
   - enemy teammates can take the flag from each other
   - friend poking the flag sends it back to its initial position (only if its not carried by an enemy)
   - enemy getting the flag to his home position increments an internal counter
   - when win count is reached, all of the "Win_Object_To_Kill" objects are destroyed (make sure
     this destroys all of the enemy team's buildings

   Params:
   Update_Delay - how many times per second to update (this will *always* be laggy though...)
   Enemy_Player_Type - type of player that wants to grab this flag (0=Nod,1=GDI)
   Enemy_Home_Position - when flag gets here, capture count increments!
   Pickup_Radius - how close to flag we need to pickup flag
   Home_Radius - how close to enemy home position we need to get to count
   Capture_Respawn_Timer - When flag is dropped respawn back at home position after x seconds.
         x < 0 means flag MUST be poked for it to be returned.
   Captures_Needed_To_Win - after this many captures, we destroy the token "building" for the win
   Flag_Stolen_Event_ID - custom event id to send when the flag is stolen
   Flag_Stolen_Object_ID - Object that receives the event
   Flag_Lost_Event_ID - custom event id to send when enemy team gets flag back to Enemy_Home_Position :-(
   Flag_Lost_Object_ID - Object that receives the event
   Flag_Saved_Event_ID - custom event id to send when flag carrier is killed
   Flag_Saved_Object_ID - Object that receives the event
   Flag_Returned_Event_ID - custom event id to send when flag has been returned to home position.
   Flag_Returned_Object_ID - Object that receives the event
   Captures_Exceeded_Event_ID - custom event id to send when flag has been captured "Captures_Needed_To_Win" times.
   Captures_Exceeded_Object_ID - Object that receives the event
   Win_Object_To_Kill0 - object that we destroy when the capture count is reached
   Win_Object_To_Kill1 - object that we destroy when the capture count is reached
   Win_Object_To_Kill2 - object that we destroy when the capture count is reached
   Win_Object_To_Kill3 - object that we destroy when the capture count is reached
   Win_Object_To_Kill4 - object that we destroy when the capture count is reached

GTH_Drop_Object_On_Death
------------------------

GTH_Drop_Object_On_Death (verified) This script will create an object at the position of the object when it dies.

* Source line: ``44``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Get_Position``, ``Create_Object``
* Summary source: ``source comment``

Parameter Description::

   Drop_Object=:string,Drop_Height=0.25:float,Probability=100:int

Source Notes::

   GTH_Drop_Object_On_Death  (verified)
   This script will create an object at the position of the object when it dies.

   Params:
   Drop_Object - name of the preset to create an instance of
   Drop_Height - float meters to add to the Z coord of the original object when creating the drop obj
   Probability - int between 1 and 100, chance that the object will be created

GTH_Drop_Object_On_Death_Zone
-----------------------------

GTH_Drop_Object_On_Death_Zone (verified) This script is just like the other drop object on death except that it must also

* Source line: ``80``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Get_Position``, ``Create_Object``
* Summary source: ``source comment``

Parameter Description::

   Custom_Message=20000:int,Drop_Object=:string,Drop_Height=0.25:float,Probability=100:int

Source Notes::

   GTH_Drop_Object_On_Death_Zone (verified)
   This script is just like the other drop object on death except that it must also
   be activated by a custom message from another script.  Use the GTH_Zone_Send_Custom
   to enable and disable this script.

   Params:
   Custom_Message - message id that turns this script on or off, use message ID's greater than 10000!
   Drop_Object - name of the preset to create an instance of
   Drop_Height - float meters to add to the Z coord of the original object when creating the drop obj
   Probability - int between 1 and 100, chance that the object will be created

GTH_Enable_Spawner_On_Enter
---------------------------

This script will enable or disable a spawner when its zone is entered Params:

* Source line: ``800``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Enable_Spawner``
* Summary source: ``source comment``

Parameter Description::

   SpawnerID=0:int,Player_Type=2:int,Enable=1:int

Source Notes::

   GTH_Enable_Spawner_On_Enter
   This script will enable or disable a spawner when its zone is entered

   Params:
   SpawnerID - id of the spawner
   Player_Type - type of player that can trigger integer, 0 = Nod, 1 = GDI, 2 = any
   Enable - enable or disable the spawner (1=enable, 0=disable)

GTH_Objective_Complete_Enter_Kill_Poke
--------------------------------------

GTH_Objective_Complete Ends an objective with either success or failure. All of the following things

* Source line: ``528``
* Event hooks: ``Created``, ``Killed``, ``Poked``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Set_Objective_Status``
* Summary source: ``source comment``

Parameter Description::

   Objective_ID=0:int, Success=1:int, Player_Type=2:int

Source Notes::

   GTH_Objective_Complete
   Ends an objective with either success or failure.  All of the following things
   cause the objective to complete: "Entered", "Killed", or "Poked"

   param
   Objective_ID - id of the objective
   Success - 0 or 1, success or failure
   Player_Type - player type allowed to trigger this.  0=nod, 1=gdi, 2=any

GTH_On_Enter_Mission_Complete
-----------------------------

GTH_On_Enter_Mission_Complete (verified) When you enter a zone with this script on it, the mission is complete. NOTE, this only

* Source line: ``380``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Mission_Complete``
* Summary source: ``source comment``

Parameter Description::

   Success=1:int, Player_Type=2:int

Source Notes::

   GTH_On_Enter_Mission_Complete (verified)
   When you enter a zone with this script on it, the mission is complete. NOTE, this only
   works in single player levels

   Parameters:
   Success - 0 = mission failed, 1 = missuion succeeded
   Player_Type - type of player allowed to trigger, 0=nod, 1=gdi, 2=any

GTH_On_Killed_Mission_Complete
------------------------------

GTH_On_Death_Mission_Complete (verified) When you kill something this script on it, the mission is complete. NOTE this

* Source line: ``421``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Mission_Complete``
* Summary source: ``source comment``

Parameter Description::

   Success=1:int, Player_Type=2:int

Source Notes::

   GTH_On_Death_Mission_Complete (verified)
   When you kill something this script on it, the mission is complete.  NOTE this
   only works in single-player levels.

   Parameters:
   Success - 0 = mission failed, 1 = missuion succeeded
   Player_Type - type of player allowed to trigger, 0=nod, 1=gdi, 2=any

GTH_User_Controllable_Base_Defense
----------------------------------

GTH_User_Controllable_Base_Defense (verified) Just like M00_Base_Defense except that if a player enters, he can control the object

* Source line: ``583``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Debug_Message``, ``Enable_Hibernation``, ``Innate_Enable``, ``Enable_Enemy_Seen``, ``Get_Position``, ``Create_Object``, ``Get_ID``
* Summary source: ``source comment``

Parameter Description::

   MinAttackDistance=0:int, MaxAttackDistance=300:int, AttackTimer=10:int

Source Notes::

   GTH_User_Controllable_Base_Defense (verified)
   Just like M00_Base_Defense except that if a player enters, he can control the object

   params:
   MinAttackDistance - min range for auto attack
   MaxAttackDistance - max range for auto attack
   AttackTimer - amount of time to continue tracking after last "enemy seen"

GTH_Zone_Send_Custom
--------------------

GTH_Zone_Send_Custom (verified) This script lets you send a custom message to an object on enter and exit of a zone. To talk

* Source line: ``150``
* Event hooks: ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``source comment``

Parameter Description::

   Enter_Message=20000:int,Enter_Param=1:int,Exit_Message=20000:int,Exit_Param=0:int

Source Notes::

   GTH_Zone_Send_Custom (verified)
   This script lets you send a custom message to an object on enter and exit of a zone.  To talk
   to the "drop in death zone" script, send the same custom message with 1 for Enter_Param and
   0 for Exit_Param...

   Params:
   Enter_Message = message id to send when an object enters this zone
   Enter_Param = message parameter to send when an object enters
   Exit_Message = message id to send when an object exits
   Exit_Param = message id to send when and object exits
