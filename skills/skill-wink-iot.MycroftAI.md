--- 
description: Control lights and switches connected to a Wink Hub
---

![](../.gitbook/assets/star.png)  
# Wink IoT  
### _skill-wink-iot.MycroftAI_  
## About:  
Interact with your smart home using the [Wink system](https://www.wink.com/).  Wink hubs can work with virtually any brand of lights, including [Philips Hue](https://www2.meethue.com/en-us), [GE](https://www.gelighting.com/), [Sylvania](https://www.sylvania.com/en-us/Pages/default.aspx), [Cree](https://creebulb.com/connected), and many more.  Use Mycroft to easily interact with nearby lights and light groups you create within the Wink ecosystem.

Your can easily find the right light or lights based on the names of lights and groups.  The Mycroft device's Name (set at [Home](https://home.mycroft.ai/ -- check by asking "what is your name?")
can be used to find lights and/or groups with begin with that same name. For example, if your Mycroft device's location is set to 'Kitchen' and you say "Turn on the light", lights with the following names would be turned on:

* Kitchen
* Kitchen sink
* Kitchen fan (group consisting of 'Fan 1', 'Fan 2', 'Fan 3')
It will NOT turn on a light called "Porch off the kitchen".

You can also include the light/group name in your request, along with intensity words, such as: `bright`, `dim`, `full`, `half`, `completely`, `partially`

## Skill information:  
**Github:** | [https://github.com/MycroftAI/skill-wink-iot](https://github.com/MycroftAI/skill-wink-iot)  
**Owner:** | [@MycroftAI](https://github.com/MycroftAI)  
**Created:** | 2017 Dec 10 10:04:12 UTC  **Last updated:** 2019 Feb 11 09:16:47 UTC  
**License:** | Apache License 2.0  
**Market status:** | [In Market](https://market.mycroft.ai/skill/mycroft-wink-iot)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
**Tags:** \#wink \#winkhub \#iot \#home-automation \#smarthome \#smart-home \#LED \#light \#lightbulb \#lighting   
## Examples:  
> Flip on the light.  
> Turn on the bedroom lights dimly.  
> Dim the lights.  
> Switch off the light.  
> Raise the light in the kitchen.  
> Dimmer (conversationally)  
> Brighter (conversationally)  
  
{% hint style="info" %}
This skill is in Mycroft Market. That means it is aproved by the Mycroft Skill testers
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Wink IoT
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Wink IoT```
{% endtab %}
  {% endtabs %}
  