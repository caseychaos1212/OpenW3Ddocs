Toolkit_Powerup.cpp
===================

* Category: ``toolkit``
* Active scripts: ``12``
* Source: ``Code/Scripts/Toolkit_Powerup.cpp``

M00_CNC_Crate
-------------

M00_CNC_Crate in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``403``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Give_Money``
* Summary source: ``heuristic``

M00_Death_Powerup
-----------------

M00_Death_Powerup in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``415``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Apply_Damage``
* Summary source: ``heuristic``

M00_GrantMoney_Powerup
----------------------

M00_GrantMoney_Powerup in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``347``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Give_Money``
* Summary source: ``heuristic``

Parameter Description::

   ScoreAmount:float,Entire_Team=0:int,Randomizer=1:int

M00_GrantScore_Powerup
----------------------

M00_GrantScore_Powerup in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``316``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random_Int``, ``Give_Points``
* Summary source: ``heuristic``

Parameter Description::

   ScoreAmount:float,Entire_Team=0:int,Randomizer=1:int

M00_Powerup_Destroy
-------------------

M00_Powerup_Destroy in Toolkit_Powerup.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``207``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Difficulty_Level``, ``Start_Timer``, ``Expire_Powerup``
* Summary source: ``heuristic``

M00_Reveal_Enc_Building_DAY
---------------------------

M00_Reveal_Enc_Building_DAY in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``234``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Building``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

Parameter Description::

   BuildingEncyclopediaID:int

M00_Reveal_Enc_Character_DAY
----------------------------

M00_Reveal_Enc_Character_DAY in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``252``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Character``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

Parameter Description::

   CharacterEncyclopediaID:int

M00_Reveal_Enc_Vehicle_DAY
--------------------------

M00_Reveal_Enc_Vehicle_DAY in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``270``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Vehicle``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

Parameter Description::

   VehicleEncyclopediaID:int

M00_Reveal_Enc_Weapon_DAY
-------------------------

M00_Reveal_Enc_Weapon_DAY in Toolkit_Powerup.cpp responds to custom events.

* Source line: ``289``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Reveal_Encyclopedia_Weapon``, ``Display_Encyclopedia_Event_UI``
* Summary source: ``heuristic``

Parameter Description::

   WeaponEncyclopediaID:int

M00_Soldier_Powerup_Disable
---------------------------

M00_Soldier_Powerup_Disable in Toolkit_Powerup.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``189``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M00_Soldier_Powerup_Grant
-------------------------

M00_Soldier_Powerup_Grant in Toolkit_Powerup.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; creates or destroys objects.

* Source line: ``72``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Is_A_Star``, ``Get_Random_Int``, ``Get_Difficulty_Level``, ``Get_Preset_Name``, ``Get_Health``, ``Get_Max_Health``, ``Get_Shield_Strength``
* Summary source: ``heuristic``

M00_Tiberium_Refinery
---------------------

M00_Tiberium_Refinery in Toolkit_Powerup.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers.

* Source line: ``381``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Health``, ``Give_Money``
* Summary source: ``heuristic``

Parameter Description::

   MoneyAmount:int,TimerLength:int
