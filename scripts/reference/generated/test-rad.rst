Test_RAD.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``11``
* Source: ``Code/Scripts/Test_RAD.cpp``

M00_Test_Sound_RAD
------------------

M00_Test_Sound_RAD in Test_RAD.cpp initializes behavior when the object is created; starts conversations.

* Source line: ``3213``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Stop_All_Conversations``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M03_A05_Evac_Zone
-----------------

M03_A05_Evac_Zone in Test_RAD.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; drives AI action commands; creates or destroys objects.

* Source line: ``3136``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Object``, ``Attach_Script``, ``Get_Random``, ``Action_Goto``
* Summary source: ``heuristic``

MX0_A02_ACTOR
-------------

MX0_A02_ACTOR in Test_RAD.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; creates or destroys objects; plays sounds; changes innate AI behavior; starts conversations.

* Source line: ``1268``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Get_Health``, ``Get_Shield_Strength``, ``Innate_Disable``, ``Enable_Enemy_Seen``, ``Send_Custom_Event``, ``Action_Goto``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   ActorID=0:int

MX0_A02_Controller
------------------

MX0_A02_Controller in Test_RAD.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; creates explosions; controls animation playback; plays sounds.

* Source line: ``26``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Attach_Script``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``, ``Destroy_Object``, ``Create_Object``, ``Get_Position``, ``Start_Timer``
* Summary source: ``heuristic``

MX0_A02_DEFAULT_OFF
-------------------

MX0_A02_DEFAULT_OFF in Test_RAD.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``3080``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``, ``Apply_Damage``
* Summary source: ``heuristic``

MX0_A02_GDI_APC
---------------

MX0_A02_GDI_APC in Test_RAD.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; changes innate AI behavior.

* Source line: ``2976``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Get_Max_Health``, ``Action_Attack``, ``Apply_Damage``, ``Innate_Enable``, ``Enable_Enemy_Seen``
* Summary source: ``heuristic``

MX0_A02_GDI_MEDTANK
-------------------

MX0_A02_GDI_MEDTANK in Test_RAD.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``2939``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``, ``Get_Max_Health``, ``Fade_Background_Music``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A02_GDI_VEHICLE
-------------------

MX0_A02_GDI_VEHICLE in Test_RAD.cpp initializes behavior when the object is created.

* Source line: ``2923``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Set_Health``
* Summary source: ``heuristic``

MX0_A02_HELICOPTER
------------------

MX0_A02_HELICOPTER in Test_RAD.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; uses timers; sends custom events.

* Source line: ``3036``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Send_Custom_Event``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   ActorID=0:int

MX0_A02_ZONE_DEFAULT_ON
-----------------------

MX0_A02_ZONE_DEFAULT_ON in Test_RAD.cpp watches enter or exit events; sends custom events.

* Source line: ``3096``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

MX0_A02_ZONE_STARTUP
--------------------

MX0_A02_ZONE_STARTUP in Test_RAD.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``3020``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``
