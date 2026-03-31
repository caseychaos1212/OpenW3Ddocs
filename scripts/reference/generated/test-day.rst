Test_DAY.cpp
============

* Category: ``test-and-prototype``
* Active scripts: ``13``
* Source: ``Code/Scripts/Test_DAY.cpp``

DAY_TestScriptOne
-----------------

DAY_TestScriptOne in Test_DAY.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``69``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Find_Object``, ``Action_Attack``, ``Send_Custom_Event``
* Summary source: ``heuristic``

DAY_TestScriptThree
-------------------

DAY_TestScriptThree in Test_DAY.cpp initializes behavior when the object is created; creates explosions.

* Source line: ``128``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Get_Position``
* Summary source: ``heuristic``

DAY_TestScriptTwo
-----------------

DAY_TestScriptTwo in Test_DAY.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``119``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Disable``
* Summary source: ``heuristic``

DAY_VTOL_CircleAttack
---------------------

DAY_VTOL_CircleAttack in Test_DAY.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``137``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Get_Position``, ``Get_Safe_Flight_Height``, ``Get_ID``, ``Send_Custom_Event``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

M00_Cinematic_Kill_Object_DAY
-----------------------------

M00_Cinematic_Kill_Object_DAY in Test_DAY.cpp initializes behavior when the object is created.

* Source line: ``319``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Apply_Damage``
* Summary source: ``heuristic``

M00_DestroyedStateObject_DAY
----------------------------

M00_DestroyedStateObject_DAY in Test_DAY.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``226``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Create_Object``, ``Set_Facing``
* Summary source: ``heuristic``

Parameter Description::

   OriginalModelFacing:float,DestroyedModelPreset:string

M00_Disable_Loiter_DAY
----------------------

M00_Disable_Loiter_DAY in Test_DAY.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``301``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_Loiters_Allowed``
* Summary source: ``heuristic``

M00_GrantPowerup_Created
------------------------

M00_GrantPowerup_Created in Test_DAY.cpp initializes behavior when the object is created; changes inventory or weapons.

* Source line: ``196``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Give_PowerUp``
* Summary source: ``heuristic``

Parameter Description::

   WeaponDef:string

M00_Play_Sound_Object_Bone_DAY
------------------------------

M00_Play_Sound_Object_Bone_DAY in Test_DAY.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; plays sounds.

* Source line: ``241``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Get_Position``, ``Debug_Message``, ``Create_3D_Sound_At_Bone``, ``Monitor_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Sound_Preset:string, Frequency_Min=-1.0:float, Frequency_Max:float

M00_PlayAnimation_DestroyObject_DAY
-----------------------------------

M00_PlayAnimation_DestroyObject_DAY in Test_DAY.cpp initializes behavior when the object is created; creates or destroys objects; controls animation playback.

* Source line: ``284``
* Event hooks: ``Created``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Animation``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   AnimationName:string

M00_Screenshot_Poser_DAY
------------------------

M00_Screenshot_Poser_DAY in Test_DAY.cpp initializes behavior when the object is created; changes innate AI behavior.

* Source line: ``37``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Set_Loiters_Allowed``, ``Innate_Disable``, ``Innate_Soldier_Enable_Enemy_Seen``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``, ``Innate_Soldier_Enable_Actions``, ``Action_Play_Animation``
* Summary source: ``heuristic``

Parameter Description::

   Anim_Name:string

M00_Set_Background_Music_DAY
----------------------------

M00_Set_Background_Music_DAY in Test_DAY.cpp initializes behavior when the object is created.

* Source line: ``329``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Background_Music``
* Summary source: ``heuristic``

Parameter Description::

   MusicFile:string

M00_VisceroidInnate_DAY
-----------------------

M00_VisceroidInnate_DAY in Test_DAY.cpp initializes behavior when the object is created; reacts to destruction state; controls animation playback.

* Source line: ``208``
* Event hooks: ``Created``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Set_Loiters_Allowed``, ``Set_Animation``
* Summary source: ``heuristic``
