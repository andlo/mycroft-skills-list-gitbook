---
description: Start a web Terminal andor Web CLI client
---

### _web-terminal-skill.andlo_  
## Description:  
This skill installs and run a web terminal and/or a web CLI client.

After install there should be a running web CLI client wich you can acces from a browser on
http://device:8080 where device is the hostname of your mycroft device.

Yo can start at terminal by saying "hey mycroft - run web terminal". Then there will be a full
shell running wich you can access from a browser on http://device:8022 where device is the
hostname of your mycroft device.

On settings on home.mycroft.ai you can change ports and set if CLI and/or Terminal should auto start or not.

The skill uses the ttyd from Shuanglei Tao - https://github.com/tsl0922/ttyd.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Run web terminal.  
> Run web CLI client.  
> Exit web cli client.  
> Exit web terminal.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/andlo/web-terminal-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/andlo/web-terminal-skill](https://github.com/andlo/web-terminal-skill)  
**Owner:** [@andlo](https://github.com/andlo)  
**Created:** 2020 Jan 02 12:42:23 UTC  **Last updated:** 2020 Feb 17 16:52:38 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Pending Market](https://market.mycroft.ai/skill/) [ PR-1157 ] [ new ] [ needs validation ]  
**Categories:** [ Productivity ] [ Configuration ]   
**Tags:** \#Ssh \#Shell \#Terminal \#Cli-client   
