---
description: Sets the volume depending on background noise level
---

### _auto-volume-skill.andlo_  
## Description:  
This skill lets Mycroft decide when to use high, normal, or low volume. Mycrofts keeps monitoring the background sound levels using the microphone, using which it decides what volume level is the right one to use.

As it is not easy to know what is high and what is low noise level, the skill will adapt over time. The skill notices the highest and lowest measured levels over time and adjusts its settings according to those measurements.

The skill stops adjusting the volume if another skill is using the speaker or if Mycroft himself is talking.

The skill can be activated or deactivated using the command "Hey Mycroft, set auto volume off" or "Hey Mycroft, set auto volume on".  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)   
### Examples:  
> Set auto volume on.  
> Set auto volume off.  
> Clear auto volume measurements.  
  
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Auto volume
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Auto volume```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/andlo/auto-volume-skill](https://github.com/andlo/auto-volume-skill)  
**Owner:** [@andlo](https://github.com/andlo)  
**Created:** 2018 Oct 16 18:13:54 UTC  **Last updated:** 2020 Jul 24 15:03:38 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/auto-volume)  
**Categories:** [ Configuration ] [ Daily ]   
**Tags:** \#volume   
