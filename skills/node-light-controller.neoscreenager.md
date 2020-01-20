---
description: 
---
This skills allows to turn on/off, the Red/Green LEDs attached with NodeMCU microcontroller.
It is using Thinger.io (https://thinger.io/) server installed on local machine to control the
LEDs through REST API calls. Thinger.io server provides an interface to manage all the IoT resources
and automatically creates REST APIs with secure authentication mechanism to control the resources.
This skill at present only providing voice control for turning Red/Green led ON of OFF.
But it could be extended or new skills can be created using same tools to give Mycroft more capabilities to
control IoT devices via voice. As an example, room temperature sensor could be added to the NodeMCU board ( L35 analog temperature sensor is used here, check this article for
tutorial on how to connect it with NodeMCU : http://www.instructables.com/id/Interface-LM35-With-NodeMCU/ ) and with few code addition, this skill allows Mycroft to fetch room temperature reading using voice command.
This skill has not yet been submitted to Mycroft skill set, as some code modifications ( like reading the authentication headers from config files) need to be done.
The sketch is also provided with this code (NodeMCUThinger.ino) which can be flashed into a NodeMCU unit.
Also, this repository contains a PDF file with overview of components required for creating and using this skill.
Demo videos on YouTube:
1. https://youtu.be/2W1dCUOKwTw    Demo to turn LEDs ON/OFF
2. https://youtu.be/Tw6L6K-t1TA    Demo to query room temperature
3. https://youtu.be/Zdkx1vZKKfw    Screencast walkthrough under the hood.

**Github:** (https://github.com/neoscreenager/node-light-controller)

**Owner:** [@neoscreenager](https://github.com/neoscreenager) ![avatart](https://avatars2.githubusercontent.com/u/5783434?v=4)

