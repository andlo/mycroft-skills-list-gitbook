---
description: Controls the aimar robot
---
Controls the aimar robot with commands for movement, navigation, image recognition, and more.

The AIMAR skill runs alongside Mycroft. Mycroft uses Python 3 and runs on the TurtleBot.

The skill executes arm movements using the uArm-Python-SDK. \_\_init\_\_.py (skill file) should not directly call SDK functions.
Instead, \_\_init\_\_.py imports aimar_arm.py and the SDK is imported in aimar_arm.py.

To send ROS messages (if we are using a library that uses ROS subscribers), we have to write ROS publishser/subscriber code.
This has to be written in the robot-server application, since ROS Kinetic uses Python 2.
We can then make a call to robot-server by using a web request.

For functions like database access and skin image classification, we send a web request to desk-server.

**Github:** | (https://github.com/UMD-AIMAR/aimar)  
**Owner:** | [@UMD-AIMAR](https://github.com/UMD-AIMAR)  
**Created:** | 2019-10-24T21:39:40Z  **Last updated:** 2019-12-03T18:16:17Z  
**License:** | [MIT License](https://api.github.com/licenses/mit)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
**Tags:** \#Robot \#Medical   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/UMD-AIMAR/aimar```
{% endtab %}
  {% endtabs %}
  