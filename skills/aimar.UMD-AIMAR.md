---
description: Controls the aimar robot
---

### _aimar.UMD-AIMAR_  
## Description:  
Controls the aimar robot with commands for movement, navigation, image recognition, and more.
The AIMAR skill runs alongside Mycroft. Mycroft uses Python 3 and runs on the TurtleBot.
The skill executes arm movements using the uArm-Python-SDK. __init__.py (skill file) should not directly call SDK functions.
Instead, __init__.py imports aimar_arm.py and the SDK is imported in aimar_arm.py.
To send ROS messages (if we are using a library that uses ROS subscribers), we have to write ROS publishser/subscriber code.
This has to be written in the robot-server application, since ROS Kinetic uses Python 2.
We can then make a call to robot-server by using a web request.
For functions like database access and skin image classification, we send a web request to desk-server.  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
  
###Tags: \#Robot \#Medical   
## Examples:  
> Turn left.  
> Drive to the conference room.  
> Identify this skin condition.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/UMD-AIMAR/aimar```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** | [https://github.com/UMD-AIMAR/aimar](https://github.com/UMD-AIMAR/aimar)  
**Owner:** | [@UMD-AIMAR](https://github.com/UMD-AIMAR)  
**Created:** | 2019 Oct 24 21:39:40 UTC  **Last updated:** 2019 Dec 03 18:16:17 UTC  
**License:** | MIT License  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
