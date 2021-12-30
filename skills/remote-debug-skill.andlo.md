---
description: Enable Debugpy - Visual Studio Python debug server
---

### _remote-debug-skill.andlo_  
## Description:  
This skill adds Debugpy - Visual Studio Python debug server to make it posible to
debug running skills.
It is made as a companion to the THEIA IDE skill to enable debugging from there. But if you
use another IDE like VS Code you can use this skill to inject the debug adaptor in the
mycroft.skills service and attach to it on port 5678.

When you activate debugging by saying "Run debug adaptor" the skill will change Settings for
padatious single_thread = true so skills service runs in single thread.

THEIA IDE is already setup so you just have to start debug from debug menu

When finish debugging say "End debug adaptor" and skill restore single_thread settings and
restart mycroft.skills service

[https://github.com/Microsoft/ptvsd](https://github.com/Microsoft/ptvsd)

### This skills requeue using mycroft.core 19.8.7 or newer releases

### launch.json
To use the debug adaptor from THEIA IDE or VS Code make sure ou use Python
remote attach setting in launch.json
```
{
"name": "Python: Remote Attach",
"type": "python",
"request": "attach",
"port": 5678,
"host": "localhost",
}
```  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Start (remote|ptvsd|debugpy|) debug adaptor.  
> Enable (remote|ptvsd|debugpy|) debug adaptor.  
> Run (remote|ptvsd|debugpy|) debug adaptor.  
> Stop (remote|ptvsd|debugpy|) debug adaptor.  
> Exit (remote|ptvsd|debugpy|) debug adaptor.  
> End (remote|ptvsd|debugpy|) debug adaptor.  
  
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
**Created:** 2020 Jan 01 14:22:26 UTC  **Last updated:** 2020 Feb 27 21:57:10 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Pending Market](https://market.mycroft.ai/skill/) [ PR-1194 ] [ new ] [ needs validation ]  
**Categories:** [ Productivity ]   
**Tags:** \#VSCode \#Code \#debug \#debugging \#THEIA \#ptvsd \#IDE   
