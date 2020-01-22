---
description: This is a skill written for mycroft to publish commands over an mqtt broker for home automation or any other purpose
---

![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
# MQTT for MycroftAI  
### _mycroft-mymqtt.jamiehoward430_  
## About:  
Currently it will publish the action to a topic built from the commands said, for example
- say hey mycroft, turn the light on and mycroft will publish on to light/turn.
- say hey mycroft, switch the tv on and mycroft will publish on to tv/switch.

## Skill information:  
**Github:** | [https://github.com/jamiehoward430/mycroft-mymqtt](https://github.com/jamiehoward430/mycroft-mymqtt)  
**Owner:** | [@jamiehoward430](https://github.com/jamiehoward430)  
**Created:** | 2016 Nov 21 09:24:07 UTC  **Last updated:** 2019 Feb 02 11:41:51 UTC  
**License:** | Apache License 2.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
**Tags:** \#mqtt   
## Examples:  
> Command vacuum to return home.  
> Turn the light on.  
> Switch the tv on.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/jamiehoward430/mycroft-mymqtt```
{% endtab %}
  {% endtabs %}
  