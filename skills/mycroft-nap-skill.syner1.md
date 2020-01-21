---  
description: Put Mycroft to sleep when you don't want to be disturbed  
---  
# Naptime  
### _mycroft-nap-skill.syner1_  
## About:  
Tell Mycroft to sleep when you don't want to be disturbed in any way.
This stops all calls to Speech to Text system, guaranteeing your voice won't
be sent anywhere on an accidental activation.

When sleeping, Mycroft will only listen locally for the phrase "Hey Mycroft,
wake up". Otherwise the system will be totally silent and won't bother you.

On a Mark 1 this also dims the eyes.

## Skill information:  
**Github:** | [https://github.com/syner1/mycroft-nap-skill](https://github.com/syner1/mycroft-nap-skill)  
**Owner:** | [@syner1](https://github.com/syner1)  
**Created:** | 2018 Oct 15 18:13:23 UTC  **Last updated:** 2018 Oct 15 18:23:52 UTC  
**License:** | Apache License 2.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
**Tags:** \#nap \#naptime \#sleep \#donotdisturb \#do-not-disturb   
## Examples:  
> Go to sleep.  
> Nap time.  
> Wake up.  
  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/syner1/mycroft-nap-skill```
{% endtab %}
  {% endtabs %}
  