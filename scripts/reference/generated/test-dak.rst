Test_DAK.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``7``
* Source: ``Code/Scripts/Test_DAK.cpp``

DAK_Electric_Death_DAK
----------------------

DAK_Electric_Death_DAK in Test_DAK.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``146``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Apply_Damage``
* Summary source: ``heuristic``

DAK_Fire_Gas_Elec_Death_DAK
---------------------------

DAK_Fire_Gas_Elec_Death_DAK in Test_DAK.cpp implements script callbacks.

* Source line: ``72``
* Event hooks: ``Damaged``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Get_Max_Health``, ``Action_Play_Animation``, ``Apply_Damage``
* Summary source: ``heuristic``

Parameter Description::

   DeathType:string

DAK_PCT_Pokable_DAK
-------------------

DAK_PCT_Pokable_DAK in Test_DAK.cpp initializes behavior when the object is created.

* Source line: ``180``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Enable_HUD_Pokable_Indicator``, ``Display_Health_Bar``
* Summary source: ``heuristic``

DAK_PlayerSpotted
-----------------

DAK_PlayerSpotted in Test_DAK.cpp drives AI action commands.

* Source line: ``50``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Action_Goto``, ``Action_Attack``
* Summary source: ``heuristic``

DAK_TestScriptOne
-----------------

DAK_TestScriptOne in Test_DAK.cpp drives AI action commands.

* Source line: ``36``
* Event hooks: ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Action_Goto``
* Summary source: ``heuristic``

DAK_Vehicle_Regen_DAK
---------------------

DAK_Vehicle_Regen_DAK in Test_DAK.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``124``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_Health``, ``Get_Max_Health``, ``Apply_Damage``
* Summary source: ``heuristic``

M00_BUILDING_EXPLODE_NO_DAMAGE_DAK
----------------------------------

M00_BUILDING_EXPLODE_NO_DAMAGE_DAK in Test_DAK.cpp reacts to destruction state; creates explosions.

* Source line: ``190``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Shake_Camera``, ``Get_Position``
* Summary source: ``heuristic``
