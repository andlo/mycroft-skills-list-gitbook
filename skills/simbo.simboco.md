---
description: Sets the volume depending on background noise level
---

### _simbo.simboco_  
## Description:  
This skill lets Mycroft decide when to use high, normal, or low volume. Mycrofts keeps monitoring the background sound levels using the microphone, using which it decides what volume level is the right one to use.

As it is not easy to know what is high and what is low noise level, the skill will adapt over time. The skill notices the highest and lowest measured levels over time and adjusts its settings according to those measurements.

The skill stops adjusting the volume if another skill is using the speaker or if Mycroft himself is talking.

The skill can be activated or deactivated using the command "Hey Mycroft, set auto volume off" or "Hey Mycroft, set auto volume on".  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)   
### Examples:  
> Set auto volume on.  
> Set auto volume off.  
> Clear auto volume measurements.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/simboco/simbo```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/simboco/simbo](https://github.com/simboco/simbo)  
**Owner:** [@simboco](https://github.com/simboco)  
**Created:** 2020 Feb 18 21:07:09 UTC  **Last updated:** 2020 Feb 26 16:51:20 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ Configuration ] [ Daily ]   
**Tags:** \#volume   
