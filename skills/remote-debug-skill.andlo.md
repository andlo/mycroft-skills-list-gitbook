---
description: Enable PTVSD - Python Tools for Visual Studio debug server
---

### _remote-debug-skill.andlo_  
## Description:  
This skill adds PTVSD - Python Tools for Visual Studio debug server to make it posible to
debug running skills.
It is made as a companion to the THEIA IDE skill to enable debugging from there. But if you
use a nother IDE liek VS Code you can use this skill to inject the debugadaptor in the
mycroft.skills service and attatch to it on port 5678.

When you activate debugging by saying "Run debug adaptor" the skill will change Settings for
padatious single_thread = true so skillsservice runs in single thread.

THEIA IDE is alreddy setup so you just have to start debug from debug menu

When finish debugging SAY "End debug apdaptor" and skill restore single_thread settings and
restart mycroft.skills skillservice

[https://github.com/Microsoft/ptvsd](https://github.com/Microsoft/ptvsd)

### This skills requere using the dev branch and PR #2449 to work
https://github.com/MycroftAI/mycroft-core/pull/2449.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Start (remote|ptvsd) debug adaptor.  
> Enable (remote|ptvsd) debug adaptor.  
> Run (remote|ptvsd) debug adaptor.  
> Stop (remote|ptvsd) debug adaptor.  
> Exit (remote|ptvsd) debug adaptor.  
> End (remote|ptvsd) debug adaptor.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/andlo/remote-debug-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/andlo/remote-debug-skill](https://github.com/andlo/remote-debug-skill)  
**Owner:** [@andlo](https://github.com/andlo)  
**Created:** 2020 Jan 01 14:22:26 UTC  **Last updated:** 2020 Jan 12 16:51:44 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ Productivity ]   
**Tags:** \#Vsode \#debug \#debugging \#THEIA \#ptvsd \#IDE   
