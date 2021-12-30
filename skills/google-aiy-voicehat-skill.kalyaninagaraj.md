---
description: Enables the button and LED on the Google AIY voicehat
---

### _google-aiy-voicehat-skill.kalyaninagaraj_  
## Description:  
This Mycroft skill roughly follows @andlo's code outline for the
excellent [picroft-google-aiy-voicekit](https://github.com/andlo/picroft-google-aiy-voicekit-skill) skill. It provides
the same functionality but uses the gpiozero library
instead of RPi.GPIO to operate the button-LED combo
connected to the voicehat.

Additionally, an extended button press
(> 7 seconds) forces a Linux shutdown.

The idea is to test gpiozero's ability to handle switch
bounce when polling for a button press; in my experience, RPi.GPIO
doesn't register hold times too well.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/kalyaninagaraj/google-aiy-voicehat-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/kalyaninagaraj/google-aiy-voicehat-skill](https://github.com/kalyaninagaraj/google-aiy-voicehat-skill)  
**Owner:** [@kalyaninagaraj](https://github.com/kalyaninagaraj)  
**Created:** 2020 Jan 02 10:53:30 UTC  **Last updated:** 2020 Jan 03 20:14:10 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ IoT ]   
**Tags:** \#Mycroft \#AI \#Google \#AIY \#voicehat   
