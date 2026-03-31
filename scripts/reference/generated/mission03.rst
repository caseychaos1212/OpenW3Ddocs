Mission03.cpp
=============

* Category: ``mission``
* Active scripts: ``92``
* Source: ``Code/Scripts/Mission03.cpp``

DLS_Volcano_Active
------------------

DECLARE_SCRIPT(M03_Dock_Evacuator, "Building:int") {

* Source line: ``5371``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Set_Clouds``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``source comment``

Parameter Description::

   Receive_Type=0:int, Receive_Param=0:int, Volcano_Timer_Id=0:int, Volcano_Delay=0.0:float, 
   Explosion_Delay_Min=0.0:float, Explosion_Delay_Max=0.0:float, Rumble_Delay_Min=0.0:float, 
   Rumble_Delay_Max=0.0:float, Debug_Mode=0:int

Source Notes::

   DECLARE_SCRIPT(M03_Dock_Evacuator, "Building:int")
   {
   	void Created(GameObject * obj) override
   	{

   		Commands->Grant_Key(obj, 6, true);
   		Commands->Grant_Key(obj, 2, true);

   		ActionParamsStruct params;
   		params.Set_Basic(this, 99, 0);
   		params.Set_Movement(Vector3(0,0,0), RUN, 1.0f);
   		params.WaypathID = Get_Waypath(Get_Int_Parameter("Building"));
   		params.WaypathSplined = true;
   		Commands->Action_Goto(obj, params);
   	}

   	int Get_Waypath(int building)
   	{
   		int waypaths[3] = {1144983, 1145002, 1145011};
   		return waypaths[building];
   	}

   	void Action_Complete(GameObject * obj, int action_id, ActionCompleteReason reason) override
   	{
   		if (reason != ACTION_COMPLETE_NORMAL)
   		{
   			return;
   		}
   		if (action_id == 0)
   		{
   			ActionParamsStruct params;
   			params.Set_Basic(this, 99, 1);
   			params.Set_Movement(Vector3(0,0,0), RUN, 1.0f);
   			params.WaypathID = 1145021;
   			params.WaypathSplined = true;
   			Commands->Action_Goto(obj, params);
   		}
   		if (action_id == 1)
   		{
   			Commands->Destroy_Object(obj);
   		}
   	}
   };

DLS_Volcano_Stumble
-------------------

DLS_Volcano_Stumble in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``5542``
* Event hooks: ``Created``, ``Sound_Heard``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Take_Cover_Probability``, ``Set_Innate_Aggressiveness``, ``Action_Reset``, ``Get_Random``, ``Get_Position``, ``Action_Play_Animation``, ``Start_Timer``, ``Get_Random_Int``
* Summary source: ``heuristic``

Parameter Description::

   Debug_Mode=0:int

M03_AggAndCover
---------------

M03_AggAndCover in Mission03.cpp initializes behavior when the object is created.

* Source line: ``6973``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Set_Innate_Take_Cover_Probability``
* Summary source: ``heuristic``

M03_Alternate_Sam_Site
----------------------

M03_Alternate_Sam_Site in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; creates or destroys objects; starts conversations.

* Source line: ``3821``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Object``, ``Get_ID``, ``Attach_Script``, ``Attach_To_Object_Bone``, ``Action_Attack``, ``Start_Timer``, ``Get_Position``
* Summary source: ``heuristic``

Parameter Description::

   Chinook_Controller_ID:int

M03_Ambient_Birdcall_Controller_JDG
-----------------------------------

DECLARE_SCRIPT(M03_Refinery_Crusher_Controller_JDG, "") {

* Source line: ``1679``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Get_A_Star``, ``Get_Position``, ``Get_Random``, ``Create_Sound``, ``Is_A_Star``, ``Destroy_Object``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(M03_Refinery_Crusher_Controller_JDG, "")
   {
   	int start_sounds;
   	int stop_sounds;
   	int play_sounds;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE( start_sounds, 1 );
   		SAVE_VARIABLE( stop_sounds, 2 );
   		SAVE_VARIABLE( play_sounds, 3 );
   	}

   	void Created( GameObject * obj ) override
   	{
   		start_sounds		=	100;
   		stop_sounds		=	101;
   		play_sounds		=	102;
   		if (obj) {
   			Commands->Send_Custom_Event( obj, obj, 0, start_sounds, 0 , 0.0f);
   		}
   	}

   	void Custom( GameObject * obj, int type, uintptr_t param, GameObject * sender ) override
   	{
   		if (param == stop_sounds)
   		{
   		}

   		if (param == start_sounds)
   		{
   			if (obj) {
   				Commands->Send_Custom_Event( obj, obj, 0, play_sounds, 0 , 0.0f);
   			}
   		}

   		if (param == play_sounds)
   		{
   			char *soundName = "Refinery Crusher Twiddler";
   			Vector3 soundPosition (-179.60f, -2.03f, 3.42f);

   			Commands->Create_Sound ( soundName, soundPosition, obj );

   			float delayTimer = Commands->Get_Random ( 0, 5 );
   			if (obj) {
   				Commands->Send_Custom_Event( obj, obj, 0, play_sounds, delayTimer , 0.0f);
   			}

   		}
   	}
   };

M03_Announce_CommCenter_Controller_JDG
--------------------------------------

01-I022E "Proper Identification must be worn at all times." 01-I028E "All coded messages must be sent on designated security channel alpha."

* Source line: ``2687``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Sound``, ``Get_Random``, ``Destroy_Object``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   01-I022E	"Proper Identification must be worn at all times."
   01-I028E	"All coded messages must be sent on designated security channel alpha."
   01-I030E	"In accordance with Brotherhood directive AC-MBM, all messages are monitored."
   01-I032E	"A visceroid has been spotted in Tiberium Field iota. Containment team en route."
   01-I034E	"Tiberium value is increasing Worldwide."
   01-I036E	"Project 'Ezekiel's Cape' has passed initial tests.  Prototypes are now in production."
   01-I038E	"Colonel Shepard's personal aide has been located in Washington D.C.  Aquisition team en route."
   01-I040E	"Anamolous EVA signal detected.  Reconnaissance force is being dispatched."
   01-I042E	"World wide public opinion of the Brotherhood is on the rise."
   01-I044E	"Refinery technicians have failed to report in.  Investigation team en route."
   01-I046E	"Possible EVA intrusion in message squirt Alpha. Switching to Beta channels."
   01-I048E	"Incoming transmission for Captain Jones.  Captain Jones please report to a secured terminal."
   01-I050E	"Do you know someone who would make a positive addition to the Brotherhood? Now they can enlist online at 'WWW dot BrotherhoodRecruitment dot Nod' "
   01-I062E	"Immediately report the presence of visceroids to your supervisor."
   01-I066E	"Workers found loitering in this area will be terminated."

M03_Announce_PowerPlant_Controller_JDG
--------------------------------------

01-I000E "Core temperture fluctuating." 01-I002E "Extended exposure to core environment is hazardous."

* Source line: ``1777``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Sound``, ``Get_Random``
* Summary source: ``source comment``

Source Notes::

   01-I000E	"Core temperture fluctuating."
   01-I002E	"Extended exposure to core environment is hazardous."
   01-I004E	"Power output exceeding optimal levels."
   01-I006E	"Radiation levels fluctuating."
   01-I008E	"Radiation hazard. Proper safety equipment is required."
   01-I010E	"If the decontamination shower does not function, contact a technician immediately."
   01-I012E	"Tertiary coolant system malfunctioning.  Dispatch technician immediately."
   01-I014E	"Comm Center power demands have fallen.  Diverting power to secondary grid."
   01-I016E	"Power production levels wavering."
   01-I018E	"Critical failure potential increasing. Reallocate available engineers."
   01-I020E	"Tertiary grid demands increasing; diverting surplus power."
   01-I022E	"Proper Identification must be worn at all times."
   01-I024E	"Secondary power grid has been taken offline. Tertiary grid surplus being redirected."
   01-I026E	"Power core radiation levels vacillating."
   01-I050E	"Do you know someone who would make a positive addition to the Brotherhood? Now they can enlist online at 'WWW dot BrotherhoodRecruitment dot Nod' "
   01-I062E	"Immediately report the presence of visceroids to your supervisor."
   01-I066E	"Workers found loitering in this area will be terminated."
   01-I076E	"Hazmat suits are required for your safety."
   01-I078E	"Please do not inhale decontamination agents."

M03_Announce_Refinery_Controller_JDG
------------------------------------

The following is a list of all level 3 refinery related dialogs Line # Dialog

* Source line: ``2171``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Sound``, ``Get_Random``, ``Destroy_Object``, ``Find_Object``
* Summary source: ``source comment``

Source Notes::

   The following is a list of all level 3 refinery related dialogs
   Line #		Dialog
   01-i010E	"If the decontamination shower does not function, contact a technician immediately."
   01-i022E	"Proper Identification must be worn at all times."
   01-i032E	"A visceroid has been spotted in Tiberium Field iota. Containment team en route."
   01-i034E	"Tiberium value is increasing Worldwide."
   01-i052E	"The yellow zone is for harvester unloading only. There is no parking in the yellow zone."
   01-i054E	"Harvester approaching. Please clear docking bay at once."  Only plays when harvester is approaching.
   01-i056E	"Harvester now unloading"
   01-i058E	"Smoking is not permitted within the refinery."
   01-i060E	"Leaking barrels are a health hazard. Report any faulty containment vessels to your supervisor immediately."
   01-i062E	"Immediately report the presence of visceroids to your supervisor."
   01-i064E	"Do not discharge weapons near containment barrels."
   01-i066E	"Workers found loitering in this area will be terminated."
   01-i068E	"For your safety, avoid all moving parts."
   01-i070E	"Supply trucks have the right of way."
   01-i072E	"Tiberium field omega has decreased in size. Changing harvester target to facilitate growth."
   01-i074E	"Additional tests are required for current Tiberium batch. Highest priority."
   01-i076E	"Hazmat suits are required for your safety."
   01-i078E	"Please do not inhale decontamination agents."
   01-i080E	"Quarternary gas vacuum has malfunctioned. Backup compressors are now on line."
   01-i082E	"Blockage in left ventricle of secondary crushing unit."
   01-i084E	"Refinery reagents are a biohazard. Report all leaks immediately."
   01-i086E	"Hydroxyl levels at supersaturation.  Venting protocols initiated."
   01-i088E	"Uranium fuel levels nominal."
   01-i090E	"Smelting furnace fully operational."
   01-i092E	"SPF 128 required while working under the Ultra Violet lights."
   01-i094E	"Polarized safety goggles are mandatory while working under the Ultra Violet lights."
   01-i096E	"Distiller fumes are toxic. Avoid inhaling any gasses in this area."
   01-i098E	"Tiberium only to be distilled in this area."

M03_Area_Troop_Counter
----------------------

M03_Area_Troop_Counter in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``5829``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``heuristic``

M03_Base_Harvester
------------------

M03_Base_Harvester in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; drives AI action commands; uses timers; controls animation playback.

* Source line: ``4229``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Animation_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Action_Goto``, ``Set_Animation``, ``Action_Dock``, ``Start_Timer``, ``Get_Position``, ``Get_Random``
* Summary source: ``heuristic``

Parameter Description::

   Tiberium_Loc:vector3, Dock_Location:vector3, Dock_Entrance:vector3, Sakura_Dest:vector3

M03_Base_Patrol
---------------

M03_Base_Patrol in Mission03.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4206``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Innate_Soldier_Enable_Footsteps_Heard``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   WaypathID:int

M03_Beach_Radio
---------------

M03_Beach_Radio in Mission03.cpp initializes behavior when the object is created; reacts to destruction state; handles player poke interaction; starts conversations.

* Source line: ``5701``
* Event hooks: ``Created``, ``Killed``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Stop_Conversation``
* Summary source: ``heuristic``

M03_Beach_Reinforce
-------------------

M03_Beach_Reinforce in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``6464``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Trigger_Spawner``, ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M03_Beach_Scenario_Controller
-----------------------------

M03_Beach_Scenario_Controller in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events; starts conversations.

* Source line: ``5143``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Grant_Key``
* Summary source: ``heuristic``

M03_Beach_Soldier_GDI
---------------------

M03_Beach_Soldier_GDI in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``3271``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Start_Timer``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Number:int

M03_Beach_Turret
----------------

M03_Beach_Turret in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``4957``
* Event hooks: ``Created``, ``Killed``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Action_Attack``, ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

M03_Big_Gun_Explosion
---------------------

M03_Big_Gun_Explosion in Mission03.cpp initializes behavior when the object is created; plays sounds.

* Source line: ``4137``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``
* Summary source: ``heuristic``

M03_Chinook_Drop_Soldiers_GDI
-----------------------------

M03_Chinook_Drop_Soldiers_GDI in Mission03.cpp initializes behavior when the object is created; responds to custom events.

* Source line: ``3182``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M03_Chinook_Fodder_Creator
--------------------------

M03_Chinook_Fodder_Creator in Mission03.cpp responds to custom events; continues work on timer callbacks; uses timers; sends custom events; starts conversations.

* Source line: ``3986``
* Event hooks: ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Attach_Script``, ``Start_Timer``, ``Create_Sound``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M03_Chinook_ParaDrop
--------------------

M03_Chinook_ParaDrop in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects; controls animation playback; plays sounds.

* Source line: ``4657``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``, ``Set_Model``, ``Set_Facing``, ``Set_Animation``, ``Attach_To_Object_Bone``, ``Get_ID``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string

M03_Chinook_Reinforcements
--------------------------

M03_Chinook_Reinforcements in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects.

* Source line: ``3307``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Create_Sound``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Beach_Preset:string, Inlet_Preset:string, Base_Preset:string, Trigger_Count:int

M03_Chinook_Spawned_Soldier_GDI
-------------------------------

M03_Chinook_Spawned_Soldier_GDI in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; handles player poke interaction; drives AI action commands; uses timers; sends custom events; starts conversations.

* Source line: ``3433``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Aggressiveness``, ``Start_Timer``, ``Action_Goto``, ``Get_Random``, ``Get_Position``, ``Get_Facing``, ``Find_Closest_Soldier``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Area:int, Send_Type_When_Killed:int, Target_ID:int

M03_Cine_Explosion
------------------

M03_Cine_Explosion in Mission03.cpp responds to custom events; creates explosions.

* Source line: ``7090``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion``, ``Get_Position``
* Summary source: ``heuristic``

M03_Comm_Killed
---------------

M03_Comm_Killed in Mission03.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``6133``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``, ``Send_Custom_Event``, ``Find_Object``, ``Enable_Radar``
* Summary source: ``heuristic``

M03_Commando_Script
-------------------

M03_Commando_Script in Mission03.cpp initializes behavior when the object is created; responds to custom events; reacts to destruction state; sends custom events.

* Source line: ``3060``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``, ``Custom``, ``Sound_Heard``
* Persistence hooks: none detected
* Key engine calls: ``Shake_Camera``, ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M03_CommCenter_Arrow
--------------------

M03_CommCenter_Arrow in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``6037``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Mission_Complete``, ``Send_Custom_Event``, ``Find_Object``, ``Set_HUD_Help_Text``, ``Start_Timer``
* Summary source: ``heuristic``

M03_CommCenter_SateliteDish_Controller_JDG
------------------------------------------

M03_CommCenter_SateliteDish_Controller_JDG in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``1575``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Sound``, ``Get_Random``
* Summary source: ``heuristic``

M03_CommCenter_Warning
----------------------

M03_CommCenter_Warning in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``5961``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M03_Conversation_Zone
---------------------

M03_Conversation_Zone in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; starts conversations.

* Source line: ``6172``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Start_Timer``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Has_Key``
* Summary source: ``heuristic``

Parameter Description::

   Conv_Num:int

M03_ConYardSeen
---------------

M03_ConYardSeen in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``7101``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M03_Damage_Modifier_All
-----------------------

M03_Damage_Modifier_All in Mission03.cpp initializes behavior when the object is created.

* Source line: ``7046``
* Event hooks: ``Created``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``
* Summary source: ``heuristic``

Parameter Description::

   Damage_multiplier:float

M03_DataDiscMessage
-------------------

M03_DataDiscMessage in Mission03.cpp responds to custom events.

* Source line: ``7133``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M03_Destroyed_Chinook
---------------------

M03_Destroyed_Chinook in Mission03.cpp reacts to destruction state; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``3960``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Find_Object``, ``Destroy_Object``, ``Create_Explosion_At_Bone``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int, Simple_ID:int

M03_Destroyed_SAM_Site
----------------------

M03_Destroyed_SAM_Site in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; plays sounds.

* Source line: ``5090``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_2D_Sound``
* Summary source: ``heuristic``

M03_Destroyed_Turret
--------------------

M03_Destroyed_Turret in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; uses timers; plays sounds; starts conversations.

* Source line: ``5103``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_2D_Sound``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

M03_Dock_Evacuation_Controller
------------------------------

M03_Dock_Evacuation_Controller in Mission03.cpp responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``5288``
* Event hooks: ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M03_Dock_Evacuator
------------------

M03_Dock_Evacuator in Mission03.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``5327``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Building:int

M03_Engineer_Repair
-------------------

M03_Engineer_Repair in Mission03.cpp initializes behavior when the object is created; drives AI action commands; sends custom events.

* Source line: ``6732``
* Event hooks: ``Created``, ``Sound_Heard``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Get_Player_Type``, ``Get_ID``, ``Send_Custom_Event``, ``Get_Position``, ``Action_Goto``, ``Action_Reset``, ``Find_Object``, ``Action_Attack``
* Summary source: ``heuristic``

Parameter Description::

   Repair_Priority=96:int

M03_Engineer_Target
-------------------

M03_Engineer_Target in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; uses timers.

* Source line: ``6676``
* Event hooks: ``Created``, ``Destroyed``, ``Damaged``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Create_Logical_Sound``, ``Get_Position``, ``Start_Timer``
* Summary source: ``heuristic``

M03_Evacuation_Controller
-------------------------

M03_Evacuation_Controller in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``5182``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

Parameter Description::

   Preset:string

M03_Evacuator
-------------

M03_Evacuator in Mission03.cpp initializes behavior when the object is created; drives AI action commands; creates or destroys objects.

* Source line: ``5242``
* Event hooks: ``Created``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Grant_Key``, ``Action_Goto``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Building:int

M03_Flyover_Controller
----------------------

M03_Flyover_Controller in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``3891``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_Random``, ``Create_Object``, ``Attach_Script``
* Summary source: ``heuristic``

M03_Goto_Star
-------------

M03_Goto_Star in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``5939``
* Event hooks: ``Created``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Action_Attack``
* Summary source: ``heuristic``

M03_Gunboat_Controller_RMV
--------------------------

M03_Gunboat_Controller_RMV in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; creates or destroys objects; plays sounds; starts conversations.

* Source line: ``825``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Disable_Physical_Collisions``, ``Disable_All_Collisions``, ``Enable_Engine``, ``Get_Max_Health``, ``Get_Random``, ``Action_Attack``, ``Start_Timer``
* Summary source: ``heuristic``

Parameter Description::

   Receive_Type:int, Receive_Param_For_Village:int, Receive_Param_For_Cannon:int, 
   Beach_Destination:vector3, Village_Start:vector3, Village_Destination:vector3, Cannon_Start:vector3, 
   Cannon_Destination:Vector3, Receive_Param_Destroy:int

M03_Holograph_EntryZone_JDG
---------------------------

M03_Holograph_EntryZone_JDG in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``6363``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Object_At_Bone``, ``Attach_To_Object_Bone``, ``Disable_All_Collisions``, ``Set_Facing``, ``Get_Facing``
* Summary source: ``heuristic``

M03_Initial_Powerups
--------------------

M03_Initial_Powerups in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; changes inventory or weapons.

* Source line: ``3016``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_A_Star``, ``Get_Position``, ``Give_PowerUp``, ``Grant_Key``, ``Get_ID``, ``Attach_Script``
* Summary source: ``heuristic``

M03_Inlet_Nod_Reinforcements
----------------------------

M03_Inlet_Nod_Reinforcements in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``4145``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Start_Timer``
* Summary source: ``heuristic``

M03_Inlet_Soldier_GDI
---------------------

M03_Inlet_Soldier_GDI in Mission03.cpp initializes behavior when the object is created; continues work on timer callbacks; drives AI action commands; uses timers.

* Source line: ``3237``
* Event hooks: ``Created``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Start_Timer``, ``Action_Goto``
* Summary source: ``heuristic``

Parameter Description::

   Number:int

M03_Intro_Substitute
--------------------

M03_Intro_Substitute in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; starts conversations.

* Source line: ``3730``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M03_KaneHead_JDG
----------------

M03_KaneHead_JDG in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``6408``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Debug_Message``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

M03_Key_Card
------------

M03_Key_Card in Mission03.cpp responds to custom events; sends custom events.

* Source line: ``4644``
* Event hooks: ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

M03_Killed_Disabled_Spawner
---------------------------

M03_Killed_Disabled_Spawner in Mission03.cpp reacts to destruction state.

* Source line: ``5928``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Spawner_num:int

M03_Killed_Sound
----------------

M03_Killed_Sound in Mission03.cpp reacts to destruction state; sends custom events.

* Source line: ``6455``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Officer=0:int, Location=0:int

M03_Mct_Poke
------------

M03_Mct_Poke in Mission03.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events.

* Source line: ``6109``
* Event hooks: ``Created``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M03_Mission_Complete_Zone
-------------------------

M03_Mission_Complete_Zone in Mission03.cpp initializes behavior when the object is created; watches enter or exit events.

* Source line: ``5882``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Mission_Complete``
* Summary source: ``heuristic``

M03_Move_Commando_To_Start
--------------------------

M03_Move_Commando_To_Start in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``3151``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Get_A_Star``, ``Get_Position``, ``Set_Position``
* Summary source: ``heuristic``

M03_No_More_Parachute
---------------------

M03_No_More_Parachute in Mission03.cpp reacts to destruction state; plays sounds.

* Source line: ``4846``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``
* Summary source: ``heuristic``

M03_Objective_Controller
------------------------

M03_Objective_Controller in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; updates objectives; starts conversations.

* Source line: ``52``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Set_Num_Tertiary_Objectives``, ``Set_Wind``, ``Start_Timer``, ``Get_Random``, ``Add_Objective``, ``Create_Sound``, ``Find_Object``, ``Set_Objective_Radar_Blip_Object``
* Summary source: ``heuristic``

M03_Objective_Tracker
---------------------

M03_Objective_Tracker in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``3698``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``
* Summary source: ``heuristic``

M03_Officer_With_Key_Card
-------------------------

M03_Officer_With_Key_Card in Mission03.cpp reacts to destruction state; creates or destroys objects; starts conversations.

* Source line: ``4613``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Get_Position``, ``Create_Object``, ``Attach_Script``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``
* Summary source: ``heuristic``

M03_Officer_With_Key_Card2
--------------------------

M03_Officer_With_Key_Card2 in Mission03.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``4632``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Has_Key``, ``Get_Position``, ``Create_Object``
* Summary source: ``heuristic``

M03_Outro_Cinematic
-------------------

M03_Outro_Cinematic in Mission03.cpp responds to custom events; continues work on timer callbacks; watches enter or exit events; uses timers; sends custom events; creates or destroys objects.

* Source line: ``1278``
* Event hooks: ``Custom``, ``Timer_Expired``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Find_Object``, ``Send_Custom_Event``, ``Set_Position``, ``Create_Object``, ``Start_Timer``
* Summary source: ``heuristic``

M03_Paratrooper_Run
-------------------

M03_Paratrooper_Run in Mission03.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands.

* Source line: ``6993``
* Event hooks: ``Created``, ``Damaged``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Set_Health``, ``Get_Random``, ``Get_Position``, ``Get_Facing``, ``Action_Goto``
* Summary source: ``heuristic``

M03_Past_Pillbox
----------------

M03_Past_Pillbox in Mission03.cpp watches enter or exit events; sends custom events.

* Source line: ``6668``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M03_Power_Plant
---------------

M03_Power_Plant in Mission03.cpp reacts to destruction state; sends custom events.

* Source line: ``5804``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Set_Building_Power``, ``Send_Custom_Event``, ``Enable_Radar``
* Summary source: ``heuristic``

M03_PowerPlant_Warning
----------------------

M03_PowerPlant_Warning in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events.

* Source line: ``5999``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``, ``Set_HUD_Help_Text``
* Summary source: ``heuristic``

M03_Protect_The_MCT
-------------------

M03_Protect_The_MCT in Mission03.cpp initializes behavior when the object is created; starts conversations.

* Source line: ``5760``
* Event hooks: ``Created``, ``Enemy_Seen``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Set_Innate_Soldier_Home_Location``
* Summary source: ``heuristic``

Parameter Description::

   Building:int

M03_Radar_Scramble
------------------

M03_Radar_Scramble in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; sends custom events; starts conversations.

* Source line: ``6798``
* Event hooks: ``Created``, ``Custom``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Get_Health``, ``Find_Object``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Enable_Radar``
* Summary source: ``heuristic``

M03_Radar_UnScramble
--------------------

M03_Radar_UnScramble in Mission03.cpp watches enter or exit events.

* Source line: ``6840``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Radar``
* Summary source: ``heuristic``

M03_Refinery
------------

M03_Refinery in Mission03.cpp reacts to destruction state; sends custom events.

* Source line: ``5820``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

M03_Refinery_Crusher_Controller_JDG
-----------------------------------

M03_Refinery_Crusher_Controller_JDG in Mission03.cpp initializes behavior when the object is created; responds to custom events; sends custom events.

* Source line: ``1626``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Create_Sound``, ``Get_Random``
* Summary source: ``heuristic``

M03_Reinforce_Area
------------------

M03_Reinforce_Area in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``4383``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Start_Timer``, ``Create_Object``, ``Set_Facing``, ``Attach_Script``, ``Send_Custom_Event``, ``Create_Conversation``, ``Join_Conversation``
* Summary source: ``heuristic``

M03_Reinforcement_Chinook
-------------------------

M03_Reinforcement_Chinook in Mission03.cpp initializes behavior when the object is created; reacts to destruction state; sends custom events; plays sounds.

* Source line: ``4854``
* Event hooks: ``Created``, ``Destroyed``, ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_3D_Sound_At_Bone``, ``Find_Object``, ``Send_Custom_Event``, ``Stop_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M03_Sakura_Explosion
--------------------

M03_Sakura_Explosion in Mission03.cpp reacts to destruction state.

* Source line: ``5530``
* Event hooks: ``Destroyed``
* Persistence hooks: none detected
* Key engine calls: ``Create_Explosion_At_Bone``
* Summary source: ``heuristic``

M03_SAM_Site_Logic
------------------

M03_SAM_Site_Logic in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; creates or destroys objects.

* Source line: ``4983``
* Event hooks: ``Created``, ``Killed``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Enemy_Seen``, ``Start_Timer``, ``Get_Random``, ``Is_A_Star``, ``Get_ID``, ``Get_Position``, ``Action_Attack``, ``Action_Reset``
* Summary source: ``heuristic``

M03_Staged_Conversation_1
-------------------------

M03_Staged_Conversation_1 in Mission03.cpp responds to custom events; sends custom events; starts conversations.

* Source line: ``4880``
* Event hooks: ``Custom``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Soldier_1_ID:int, Soldier_2_ID:int

M03_Staged_Conversation_Soldier
-------------------------------

M03_Staged_Conversation_Soldier in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``4917``
* Event hooks: ``Created``, ``Damaged``, ``Custom``, ``Enemy_Seen``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Set_Innate_Is_Stationary``, ``Innate_Soldier_Enable_Footsteps_Heard``, ``Innate_Soldier_Enable_Gunshot_Heard``, ``Innate_Soldier_Enable_Bullet_Heard``
* Summary source: ``heuristic``

M03_Structure_Powerup_Drop
--------------------------

M03_Structure_Powerup_Drop in Mission03.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``5127``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Get_Position``, ``Get_Facing``, ``Create_Object``
* Summary source: ``heuristic``

Parameter Description::

   Powerup:string

M03_Tailgun
-----------

M03_Tailgun in Mission03.cpp reacts to destruction state; sends custom events.

* Source line: ``4034``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int

M03_Tailgun_Fodder
------------------

M03_Tailgun_Fodder in Mission03.cpp initializes behavior when the object is created; drives AI action commands.

* Source line: ``4112``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Reset``, ``Get_A_Star``, ``Get_Position``, ``Action_Attack``
* Summary source: ``heuristic``

M03_Tailgun_Fodder_Zone
-----------------------

M03_Tailgun_Fodder_Zone in Mission03.cpp initializes behavior when the object is created; responds to custom events; watches enter or exit events; creates or destroys objects.

* Source line: ``4045``
* Event hooks: ``Created``, ``Custom``, ``Entered``, ``Exited``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Spawner``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   Spawner_ID_1:int, Spawner_ID_2:int, Spawner_ID_3:int

M03_Technician_Work
-------------------

M03_Technician_Work in Mission03.cpp initializes behavior when the object is created.

* Source line: ``6982``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Action_Play_Animation``
* Summary source: ``heuristic``

M03_Tiberium_Cave_Stay_Put
--------------------------

M03_Tiberium_Cave_Stay_Put in Mission03.cpp initializes behavior when the object is created.

* Source line: ``4129``
* Event hooks: ``Created``
* Persistence hooks: none detected
* Key engine calls: ``Set_Innate_Soldier_Home_Location``, ``Get_Position``
* Summary source: ``heuristic``

M03_Wheres_The_Star
-------------------

M03_Wheres_The_Star in Mission03.cpp watches enter or exit events; sends custom events.

* Source line: ``4374``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Controller_ID:int, Type:int, Param:int

M03_Zone_Enabled_Spawner
------------------------

M03_Zone_Enabled_Spawner in Mission03.cpp watches enter or exit events.

* Source line: ``5911``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Enable_Spawner``
* Summary source: ``heuristic``

Parameter Description::

   Spawner_num:int, Control_num:int

M10_Elevator_All_Controller
---------------------------

M10_Elevator_All_Controller in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; creates or destroys objects.

* Source line: ``6873``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Static_Anim_Phys_Goto_Last_Frame``, ``Destroy_Object``, ``Find_Object``, ``Start_Timer``, ``Create_Object``, ``Get_ID``, ``Set_Facing``, ``Set_Is_Rendered``
* Summary source: ``heuristic``

M10_Elevator_All_Zone
---------------------

M10_Elevator_All_Zone in Mission03.cpp initializes behavior when the object is created; watches enter or exit events; sends custom events.

* Source line: ``6848``
* Event hooks: ``Created``, ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Find_Object``
* Summary source: ``heuristic``

Parameter Description::

   Controller_num:int

RMV_M03_Comm_Center_Terminal
----------------------------

RMV_M03_Comm_Center_Terminal in Mission03.cpp initializes behavior when the object is created; handles player poke interaction; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1324``
* Event hooks: ``Created``, ``Damaged``, ``Action_Complete``, ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Grant_Key``
* Summary source: ``heuristic``

RMV_Temp_EVA_Dialogue
---------------------

RMV_Temp_EVA_Dialogue in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers.

* Source line: ``1170``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Start_Timer``, ``Create_Sound``, ``Get_Random``
* Summary source: ``heuristic``

RMV_Test_Big_Gun_Turning
------------------------

RMV_Test_Big_Gun_Turning in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; reacts to destruction state; drives AI action commands; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``684``
* Event hooks: ``Created``, ``Killed``, ``Damaged``, ``Custom``, ``Sound_Heard``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Create_Sound``, ``Create_Object``, ``Attach_Script``, ``Send_Custom_Event``, ``Find_Object``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``
* Summary source: ``heuristic``

RMV_Volcano_And_Lava_Ball_Creator
---------------------------------

RMV_Volcano_And_Lava_Ball_Creator in Mission03.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events; creates or destroys objects; starts conversations.

* Source line: ``1386``
* Event hooks: ``Created``, ``Custom``, ``Action_Complete``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Cinematic_Freeze``, ``Reveal_Encyclopedia_Character``, ``Reveal_Encyclopedia_Vehicle``, ``Create_Conversation``, ``Join_Conversation``, ``Start_Conversation``, ``Monitor_Conversation``, ``Set_Ash``
* Summary source: ``heuristic``

Sakura_Killed
-------------

DECLARE_SCRIPT(RMV_Temp_EVA_Dialogue, "") {

* Source line: ``1240``
* Event hooks: ``Created``, ``Killed``, ``Damaged``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``, ``Get_Health``, ``Set_Health``, ``Create_Object``, ``Grant_Key``
* Summary source: ``source comment``

Source Notes::

   DECLARE_SCRIPT(RMV_Temp_EVA_Dialogue, "")
   {
   	int last;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE( last, 1 );
   	}

   	void Created(GameObject * obj) override
   	{
   		last = 0;
   	}

   	void Custom(GameObject * obj, int type, uintptr_t param, GameObject * sender) override
   	{
   		char *list[11];

   		list[0] = "00-N184E";	//Locate Comm Center
   		list[1] = "00-N186E";	//Secure Beachhead
   		list[2] = NULL;//"00-N188E";	//Destroy SAM #1
   		list[3] = "00-N188E";	//Destroy SAM #2
   		list[4] = NULL;//"00-N188E";	//Destroy SAM #3
   		list[5] = "00-N188E";	//Destroy SAM #4
   		list[6] = "00-N154E";	//Destroy Big Gun
   		list[7] = "00-N200E";	//Acquire Keycard
   		list[8] = "00-N210E";	//Access Comm Center Terminal
   		list[9] = "00-N204E";	//Destroy Power Plant Terminal
   		list[10] = "00-N150E";	//Escape via the sub

   		if (param == 1)
   		{
   			Commands->Start_Timer(obj, this, 2.0f, 0);
   		}

   		if (type == last) return;
   		if ((param == 3) || (param == 4))
   		{
   			int num = type - 300;
   			if (num <= 10)
   			{
   				if (list[num] != NULL)
   				{
   				//	Commands->Create_Sound(list[num], Vector3(0,0,0), obj);
   				}
   			}
   		}
   		last = type;
   	}

   	void Timer_Expired(GameObject * obj, int timer_id) override
   	{
   		char *taunts[4];

   		taunts[0] = "laugh1";
   		taunts[1] = "lefty1";
   		taunts[2] = "bombit1";
   		taunts[3] = "keepem1";

   		float random = Commands->Get_Random(0, 11);
   		if (random < 8.0f)
   		{
   			random /= 2.0f;
   			random = WWMath::Clamp(random, 0, 3);
   			int d_random = (int)random;
   			Commands->Create_Sound(taunts[d_random], Vector3(0,0,0), obj);
   		}
   	}
   };
