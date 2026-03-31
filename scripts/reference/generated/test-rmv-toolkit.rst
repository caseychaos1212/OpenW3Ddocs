Test_RMV_Toolkit.cpp
====================

* Category: ``test-and-prototype``
* Active scripts: ``9``
* Source: ``Code/Scripts/Test_RMV_Toolkit.cpp``

M00_Play_Sound
--------------

M00_Play_Sound in Test_RMV_Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; plays sounds.

* Source line: ``501``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_Random``, ``Start_Timer``, ``Get_Position``, ``Debug_Message``, ``Create_Sound``, ``Create_2D_Sound``, ``Monitor_Sound``
* Summary source: ``heuristic``

Parameter Description::

   Sound_Preset:string, Is_3D=1:int, Offset:vector3, Offset_Randomness:vector3, Frequency_Min=-1:float, 
   Frequency_Max:float

RMV_Building_Engineer_Controller
--------------------------------

DECLARE_SCRIPT(RMV_Engineer_Wander_Terminal, "Animation_Name:string, Custom_Type:int, Custom_Param_1:int, Custom_Param_2:int") {

* Source line: ``291``
* Event hooks: ``Created``, ``Killed``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Debug_Message``, ``Find_Object``, ``Send_Custom_Event``, ``Get_Position``, ``Create_Logical_Sound``
* Summary source: ``source comment``

Parameter Description::

   Killed_Broadcast_Radius:float, 25_Start_ID:int, 25_Number:int, 50_Start_ID:int, 50_Number:int, 
   75_Start_ID:int, 75_Number:int, Building_Number:int

Source Notes::

   DECLARE_SCRIPT(RMV_Engineer_Wander_Terminal, "Animation_Name:string, Custom_Type:int, Custom_Param_1:int, Custom_Param_2:int")
   {
   	enum {ENGINEER_WANDER_TIMER};

   	bool i_am_occupied;
   	Vector3 mypos;
   	int c_type, c_param_1, c_param_2;

   	REGISTER_VARIABLES()
   	{
   		SAVE_VARIABLE(i_am_occupied, 1);
   		SAVE_VARIABLE(mypos, 2);
   		SAVE_VARIABLE(c_type, 3);
   		SAVE_VARIABLE(c_param_1, 4);
   		SAVE_VARIABLE(c_param_2, 5);
   	}

   	void Created(GameObject * obj)
   	{
   	//	Commands->Enable_Hibernation(obj, false);
   		i_am_occupied = false;
   		mypos = Commands->Get_Position(obj);
   		c_type = Get_Int_Parameter("Custom_Type");
   		c_param_1 = Get_Int_Parameter("Custom_Param_1");
   		c_param_2 = Get_Int_Parameter("Custom_Param_2");
   		Commands->Start_Timer(obj, this, 2.0f, ENGINEER_WANDER_TIMER);
   	}

   	void Timer_Expired(GameObject * obj, int timer_id)
   	{
   		if ((timer_id == ENGINEER_WANDER_TIMER) && (!i_am_occupied))
   		{
   			Commands->Create_Logical_Sound(obj, M00_SOUND_ENGINEER_WANDER, mypos, 60.0f);
   			Commands->Start_Timer(obj, this, 2.0f, ENGINEER_WANDER_TIMER);
   		}
   	}

   	void Custom(GameObject * obj, int type, int param, GameObject * sender)
   	{
   		if ((type == c_type) && (param == c_param_1) && (!i_am_occupied))
   		{
   			i_am_occupied = true;
   			const char *anim;
   			anim = Get_Parameter("Animation_Name");
   			Commands->Send_Custom_Event(obj, sender, c_type, (int)anim);
   		}
   		if ((type == c_type) && (param == c_param_2) && (i_am_occupied))
   		{
   			i_am_occupied = false;
   			Commands->Start_Timer(obj, this, 2.0f, ENGINEER_WANDER_TIMER);
   		}
   	}
   };

RMV_Engineer_Wander
-------------------

RMV_Engineer_Wander in Test_RMV_Toolkit.cpp initializes behavior when the object is created; responds to custom events; drives AI action commands; sends custom events.

* Source line: ``103``
* Event hooks: ``Created``, ``Custom``, ``Sound_Heard``, ``Action_Complete``
* Persistence hooks: none detected
* Key engine calls: ``Send_Custom_Event``, ``Action_Reset``, ``Find_Random_Simple_Object``, ``Action_Goto``, ``Get_ID``, ``Find_Object``, ``Get_Facing``, ``Set_Facing``
* Summary source: ``heuristic``

Parameter Description::

   Custom_Type:int, Custom_Param_1:int, Custom_Param_2:int, Building_Number:int, 
   Evac_Object=None:string

RMV_Engineer_Wander_Terminal
----------------------------

RMV_Engineer_Wander_Terminal in Test_RMV_Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``237``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Start_Timer``, ``Create_Logical_Sound``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Animation_Name:string, Custom_Type:int, Custom_Param_1:int, Custom_Param_2:int

RMV_MCT_Switcher
----------------

RMV_MCT_Switcher in Test_RMV_Toolkit.cpp reacts to destruction state; creates or destroys objects.

* Source line: ``488``
* Event hooks: ``Killed``
* Persistence hooks: none detected
* Key engine calls: ``Create_Object``, ``Get_Position``, ``Set_Facing``, ``Get_Facing``
* Summary source: ``heuristic``

RMV_Toggled_Engineer_Target
---------------------------

RMV_Toggled_Engineer_Target in Test_RMV_Toolkit.cpp initializes behavior when the object is created; responds to custom events; continues work on timer callbacks; uses timers; sends custom events.

* Source line: ``421``
* Event hooks: ``Created``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Enable_Hibernation``, ``Get_Position``, ``Create_Logical_Sound``, ``Start_Timer``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Emergency=1:int, Animation_Name:string, Custom_Type:int, Custom_Param_1:int, Custom_Param_2:int

RMV_Trigger_Poked
-----------------

RMV_Trigger_Poked in Test_RMV_Toolkit.cpp handles player poke interaction; sends custom events.

* Source line: ``81``
* Event hooks: ``Poked``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   Target_ID:int, Type:int, Param:int

RMV_Trigger_Zone
----------------

RMV_Trigger_Zone in Test_RMV_Toolkit.cpp watches enter or exit events; sends custom events; creates or destroys objects.

* Source line: ``49``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Find_Object``, ``Send_Custom_Event``, ``Destroy_Object``
* Summary source: ``heuristic``

Parameter Description::

   TargetID:int, Type:int, Param:int

RMV_Trigger_Zone_2
------------------

RMV_Trigger_Zone_2 in Test_RMV_Toolkit.cpp watches enter or exit events; sends custom events.

* Source line: ``66``
* Event hooks: ``Entered``
* Persistence hooks: none detected
* Key engine calls: ``Is_A_Star``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``heuristic``

Parameter Description::

   TargetID:int, Type:int, Param:int
