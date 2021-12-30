---
description: 
---

### _robomove-skill.KirkPatrick2020_  
## Description:  
Makes bb8 look-a-like move by sending motor controls via udp from one Raspberry PI to another Raspberry PI based on the input of a t-shirt color that someone is wearing.

One Raspberry PI is located in the head of the robot, acquiring input via Picamera to determine the area of color captured. The other Raspberry pi is located in the main chassis, providing an output in the form of motor controls.

This works using the Linux Distribution 'MyCroft' which is an Open-Source voice assistant that supports the ability to create custom "skills" which are Python class files that interact with MyCroft to perform various commands. By using MyCroft's intent parser, I can then create custom voice commands that when performed after saying "Hey MyCroft", will perform the commands outlined below:  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/KirkPatrick2020/robomove-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/KirkPatrick2020/robomove-skill](https://github.com/KirkPatrick2020/robomove-skill)  
**Owner:** [@KirkPatrick2020](https://github.com/KirkPatrick2020)  
**Created:** 2020 Mar 25 21:29:55 UTC  **Last updated:** 2020 May 29 19:35:23 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ IoT ] [ Robots ]   
