---
description: 
---

### _mycroft-fallback-stt.jumper047_  
## Description:  
**This plugin must be configured at settings page in home.mycroft.ai**
In settings must be setted local and remote recognizer modules, and their settings strings (same as in mycroft settings file), and host which will be pinged to detect is remote server available or not. Last one must be filled with hostname only (no http/https prefix, no port).
So, after mycroft's start plugin will periodically check host's availability and will switch to local stt server if it is offline and return to remote if internet will become up.
Also supports some voice commands to check state or switch recognizer.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Switch to remote server.  
> Which engine are you using now?  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/jumper047/mycroft-fallback-stt```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/jumper047/mycroft-fallback-stt](https://github.com/jumper047/mycroft-fallback-stt)  
**Owner:** [@jumper047](https://github.com/jumper047)  
**Created:** 2020 Feb 22 19:59:16 UTC  **Last updated:** 2020 Feb 23 20:35:02 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Configuration ]   
**Tags:** \#system   
