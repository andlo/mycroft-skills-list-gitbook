---
description: Talks to a roomba that is connected to something running roomba-serial-command-service
---

### _roomba-serial-command-skill.JonStratton_  
## Description:  
This skill is to be used with a roomba with a serial connection to a small single board computer running the roomba-serial-command-service. This device must also be connected to the same local network that mycroft is running from. The mycoft skill will use zeroconf to try to locate the service.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> List robots.  
> Tell roomba to clean.  
> Tell roomba to dock.  
> Tell robot off.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/JonStratton/roomba-serial-command-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/JonStratton/roomba-serial-command-skill](https://github.com/JonStratton/roomba-serial-command-skill)  
**Owner:** [@JonStratton](https://github.com/JonStratton)  
**Created:** 2019 Jan 13 22:45:51 UTC  **Last updated:** 2019 Jan 22 01:15:10 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ IoT ]   
**Tags:** \#roomba   
