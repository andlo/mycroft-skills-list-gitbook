---
description: 
---

### _mycroft-mozilla-iot-skill.jamesmf_  
## Description:  
[Mozilla WebThings Gateway](https://iot.mozilla.org/gateway/) is an open-source framework for controlling WebThings.

This skill extends the `CommonIoTSkill` so many utterances should work. The skill registers an entity for each Thing on your gateway. It uses the name of each Thing, so your utterance should follow something like "turn on {thing.name}" or "set {thing.name} {property} to {value}".  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Turn on the office light.  
> Turn off bedroom lights.  
> Set the office lamp brightness to 50.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/jamesmf/mycroft-mozilla-iot-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/jamesmf/mycroft-mozilla-iot-skill](https://github.com/jamesmf/mycroft-mozilla-iot-skill)  
**Owner:** [@jamesmf](https://github.com/jamesmf)  
**Created:** 2020 Jul 14 03:41:57 UTC  **Last updated:** 2020 Oct 26 15:25:27 UTC  
**License:** GNU Lesser General Public License v3.0  
  
**Categories:** [ IoT ]   
**Tags:** \#homeautomation \#iot \#mozilla \#smarthome \#mozillaiot \#mozillagateway   
