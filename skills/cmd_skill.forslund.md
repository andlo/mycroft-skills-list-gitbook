--- 
description: 
---

![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
# Usage  
### _cmd_skill.forslund_  
## About:  
This is a very old skill so it uses the now depricated skill config in mycroft.conf.
The skill can be configured to run scripts from easily pronouncable human utterances, such as "generate report" by adding the following to the `~/.mycroft/mycroft.conf`

```json
"CmdSkill": {
"alias": {
"generate report": "/home/forslund/scripts/generate_report.sh"
}
}
```

(The config needs to be valid json so be careful). The config usually contains a

The configuration above will launch `/home/forslund/scripts/generate_report.sh` when the second utterance under usage is invoked.

## Skill information:  
**Github:** | [https://github.com/forslund/cmd_skill](https://github.com/forslund/cmd_skill)  
**Owner:** | [@forslund](https://github.com/forslund)  
**Created:** | 2017 Jan 26 06:49:16 UTC  **Last updated:** 2019 Dec 12 21:10:33 UTC  
**License:** | GNU General Public License v3.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
## Examples:  
> Launch command echo TEST*  
>   
> Run script generate report*  
>   
  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/forslund/cmd_skill```
{% endtab %}
  {% endtabs %}
  