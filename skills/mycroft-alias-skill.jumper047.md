---
description: Create aliases and simple scripts
---

### _mycroft-alias-skill.jumper047_  
## Description:  
This skill implements rudimental scripting language for mycroft.
Scripts consists of two parts: trigger and action. Trigger is, in fact, padatious intent and described with almost same syntax. Action activated when recognized speech triggered script. Scripts stored in yaml config file on mycroft locally in ~/.mycroft/skills/ScriptingSkill/scripts.yaml

### Triggers
Triggers syntax almost same as mycroft's padatious intents. You can read about them here:  https://mycroft-ai.gitbook.io/docs/skill-development/user-interaction/intents/padatious-intents
The only difference is phrases separator - instead of new line you should use semicolon, ";"
Also it is possible to capture some input with `{placeholder}` syntax and use it later in actions.

### Actions
Commands in action string can be separated with two separator types: "&&" and "&!". First one means next command will be sent to mycroft immediately after previous, second one - next command will be executed next to answer to previous command. At this moment there are three types of commands:
* Plain command - simple text, it will be sent to mycroft messagebus as is.
* `sleep([number])`, where number is number of seconds to wait.
* `one_of([some phrase] | [some other phrase])` - randomly choose one of alternate phrases and then send it to messagebus
Also, as mentioned above, it is possible to pass some input to script with `{placeholder}` syntax.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> (please|) flip a coin.  
> One_of(say tails|say heads)  
> (switch|turn) on {switch} temporarliy; turn on.  
> Say switch on {switch} && sleep(50) && say switch off {switch}  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/jumper047/mycroft-alias-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/jumper047/mycroft-alias-skill](https://github.com/jumper047/mycroft-alias-skill)  
**Owner:** [@jumper047](https://github.com/jumper047)  
**Created:** 2020 May 16 08:27:54 UTC  **Last updated:** 2020 Jul 12 11:24:06 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ uncategorized ]   
