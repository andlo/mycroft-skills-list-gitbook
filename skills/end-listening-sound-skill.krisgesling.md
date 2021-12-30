---
description: Play sound when microphone stops listening
---

### _end-listening-sound-skill.krisgesling_  
## Description:  
This enables support for the `end_listening` configuration parameter, playing a sound at the end of the microphone recording.

By default it will attempt to play the file: `mycroft-core/mycroft/res/snd/end_listening.wav`. If the file isn't found it will play the standard `acknowledge.mp3`.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> <All phrases>  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/krisgesling/end-listening-sound-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/krisgesling/end-listening-sound-skill](https://github.com/krisgesling/end-listening-sound-skill)  
**Owner:** [@krisgesling](https://github.com/krisgesling)  
**Created:** 2020 Jan 07 07:31:44 UTC  **Last updated:** 2020 Jan 07 07:55:59 UTC  
**License:** Apache License 2.0  
**Market status:** [Pending Market](https://market.mycroft.ai/skill/) [ PR-1158 ] [ new ] [ needs validation ]  
**Categories:** [ Configuration ]   
**Tags:** \#System \#Microphone   
