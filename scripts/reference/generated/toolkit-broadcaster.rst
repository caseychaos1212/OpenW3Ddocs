Toolkit_Broadcaster.cpp
=======================

* Category: ``toolkit``
* Active scripts: ``3``
* Source: ``Code/Scripts/Toolkit_Broadcaster.cpp``

M00_Broadcaster_Activator_RAD
-----------------------------

This script is an easy way to activate terminals through the Level Editor.

* Source line: ``502``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``source comment``

Parameter Description::

   Terminal_ID:int, Prompt_Value=0:int, Debug_Mode=0:int

Source Notes::

   M00_Broadcaster_Activator_RAD

     This script is an easy way to activate terminals through the Level Editor.

     Parameters:

     Terminal_ID	= The ID of the terminal you wish to register with.
     Prompt_Value	= The prompt value you wish to send to the terminal before the custom.

     0	= Object is sending a custom that should be sent to everyone with one parameter.
     1	= Object is sending a custom that should be sent to random objects with one parameter.
     2	= Object is sending a custom that should be sent to everyone with random parameter.
     3	= Object is sending a custom that should be sent to random objects with random parameter.

     Script activates upon receipt of a custom. Defaults to constant send, 0.

M00_Broadcaster_Register_RAD
----------------------------

This script registers an object with a terminal.

* Source line: ``59``
* Event hooks: ``Created``, ``Destroyed``, ``Custom``, ``Timer_Expired``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Start_Timer``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``source comment``

Parameter Description::

   Terminal_ID:int, Send_Attempts=3:int, Send_Delay=1:int, Debug_Mode=0:int

Source Notes::

   M00_Broadcaster_Register_RAD

     This script registers an object with a terminal.

     Parameters:

     Terminal_ID	= The ID of the terminal you wish to register with.
     Send_Attempts	= The number of attempts to send to the terminal this will make before failing.
     Send_Delay	= The delay between attempts to send.
     Debug_Mode	= Turn this on if debug information is needed.

     Custom:

     M00_CUSTOM_BROADCASTER_REGISTRATION

     Script activates upon creation.

M00_Broadcaster_Terminal_RAD
----------------------------

This script is a terminal, which transfers customs to other objects. It can store up to 100 objects before returning an error.

* Source line: ``168``
* Event hooks: ``Created``, ``Custom``
* Persistence hooks: none detected
* Key engine calls: ``Get_ID``, ``Get_Random``, ``Find_Object``, ``Send_Custom_Event``
* Summary source: ``source comment``

Parameter Description::

   Random_Percentage=100.0:float, Random_Param_Min=0:int, Random_Param_Max=0:int, Debug_Mode=0:int

Source Notes::

   M00_Broadcaster_Terminal_RAD

     This script is a terminal, which transfers customs to other objects. It can store
     up to 100 objects before returning an error.

     Values:

     object_specific_record	= Storage of each registry item one at a time.
     object_random_record		= Storage of any registry item as many times as desired.
     object_prompts			= Storage of any sent prompts from objects.
   	0 = Object ID that is prompting.
   	1 = custom type to send with next regular custom.

     Parameters:

     Random_Percentage	= Number from 1 to 99 to determine chance of sending the custom.
     Random_Param_Min	= Minimum random parameter for random sends.
     Random_Param_Max	= Maximum random parameter for random sends.

     M00_CUSTOM_BROADCASTER_REGISTRATION
     M00_CUSTOM_BROADCASTER_PROMPTER

     Prompt Parameters:

     0	= Object is sending a custom that should be sent to everyone with one parameter.
     1	= Object is sending a custom that should be sent to random objects with one parameter.
     2	= Object is sending a custom that should be sent to everyone with random parameter.
     3	= Object is sending a custom that should be sent to random objects with random parameter.

     Script activates upon receipt of a custom.
