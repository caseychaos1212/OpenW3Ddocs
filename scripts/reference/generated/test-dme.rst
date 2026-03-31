Test_DME.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``12``
* Source: ``Code/Scripts/Test_DME.cpp``

DME_Cinematic_Test
------------------

DME_Cinematic_Test in Test_DME.cpp initializes behavior when the object is created; sends custom events; creates or destroys objects.

* Source line: ``1015``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Set_Player_Type``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Set_Model``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

DME_Destroy_Item
----------------

DME_Destroy_Item in Test_DME.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``199``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   timer_length: float

DME_Test_Ejected_Soldier
------------------------

DME_Test_Ejected_Soldier in Test_DME.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``234``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

DME_Test_Paradrop
-----------------

DME_Test_Paradrop in Test_DME.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; plays sounds.

* Source line: ``252``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object_At_Bone``, ``Attach_To_Object_Bone``, ``Set_Model``, ``Set_Animation``, ``Create_3D_Sound_At_Bone``, ``Start_Timer``, ``Get_Facing``
* Summary source: ``heuristic``

DME_Test_Powerup
----------------

DME_Test_Powerup in Test_DME.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``38``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Trigger_Spawner``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Debug_Message``
* Summary source: ``heuristic``

DME_Test_Work_Area
------------------

DME_Test_Work_Area in Test_DME.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``672``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Send_Custom_Event``
* Summary source: ``heuristic``

DME_Test_Worker_Wander
----------------------

DME_Test_Worker_Wander in Test_DME.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; handles player poke interaction; drives AI action commands; uses timers; sends custom events; creates or destroys objects; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``305``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Get_ID``, ``Find_Object``, ``Get_Position``, ``Get_Facing``, ``Action_Goto``, ``Get_Distance``
* Summary source: ``heuristic``

Parameter Description::

   Work_Area=3:int

DME_Waypath_test
----------------

DME_Waypath_test in Test_DME.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``217``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``
* Summary source: ``heuristic``

M05_Tank_Attack_DME
-------------------

M05_Tank_Attack_DME in Test_DME.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``744``
* Event hooks: ``Created``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Get_Position``, ``Get_Distance``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``

M05_Tank_Drop_01_DME
--------------------

M05_Tank_Drop_01_DME in Test_DME.cpp initializes behavior when the object is created; responds to custom events; creates or destroys objects.

* Source line: ``713``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M05_Tech_Wander_DME
-------------------

M05_Tech_Wander_DME in Test_DME.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; sends custom events; controls animation playback; changes innate AI behavior; starts conversations.

* Source line: ``814``
* Event hooks: ``Created``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Debug_Message``, ``Get_ID``, ``Find_Object``, ``Get_Position``, ``Get_Facing``, ``Action_Goto``, ``Get_Distance``
* Summary source: ``heuristic``

Parameter Description::

   Work_Area=1:int

test_Ssm_Trigger
----------------

test_Ssm_Trigger in Test_DME.cpp sends custom events.

* Source line: ``1004``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``heuristic``
