---
description: 
---

### _fhem-skill.domcross_  
## Description:  
This skill utilizes the skillsettings.json file which allows you to configure this skill via home.mycroft.ai after a few minutes of having the skill installed you should see something like below in the https://home.mycroft.ai/#/skill location:

Fill this out with your appropriate Fhem information and hit save.
(Note: SSL options are currently not supported.)

![Screenshot](skill-settings.jpg?raw=true)


When using option "Use Mycroft device description as location" don't forget to enter the location info in home.mycroft.ai >  > devices

![Screenshot](device-info.jpg?raw=true)  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Device*  
> Check if given room has exactly one device of desired type (e.g. only one.  
> Search for closest matching device ID or alias name.  
> Prefer devices that are in the desired room.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/domcross/fhem-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/domcross/fhem-skill](https://github.com/domcross/fhem-skill)  
**Owner:** [@domcross](https://github.com/domcross)  
**Created:** 2018 Jun 07 16:55:28 UTC  **Last updated:** 2020 Oct 11 17:27:08 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ uncategorized ]   
