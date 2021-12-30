---
description: 
---

### _skill-mosquito-broadcast.RdeLange_  
## Description:  
This skill has three purposes:
1) Broadcast messages to other mycroft devices
2) Receive broadcast messages from other mycroft devices
3) Repeat the last broadcast message which was send to the mqtt topic specified

And a warning: Due to the way this skill is implemented, it may stop working in case of a live update, under certain circumstances. A workaround is restarting the skill (or restarting Mycroft).
The problem only affects this skill. I am still looking for a solution to this.


### Configuration
The skill is configured on your "Mycroft Home" page. Configure the mqtt server, port and topic that the skill will listen for text messages on.
Currently, password or certificates are not supported. (Maybe I will implement it if you promise to test it :)

A restart of the skill is needed when changing the configuration.

Optionally, it is possible to split the text, using a regular expression.

Example CamelCase: If you send the string "KitchenWindow is open",
you want to split KitchenWindow. After the split Mycroft will say "Kitchen Window is open". To do that set the parameters on "Mycroft Home" like this:
* Split text at pattern (optional): [a-z][A-Z]
* Retain characters in matched string until index: 1
* Retain characters in matched string from index: 1

What happens: The regex match "nK" in "KitchenWindow is open". We retain the characters until index 1 of "nK", which is n.
We retain the characters after index 1 of "nK", which is K. And we put a space in the middle.

Example hypen: Convert "Outside-temperature is -5 degrees" to "Outside temperature is -5 degrees"
* Split text at pattern (optional): [a-z|A-Z]-[a-z|A-Z]
* Retain characters in matched string until index: 1
* Retain characters in matched string from index: 2

What happens: The regex match "e-t" in "Outside-temperature is -5 degrees".  We retain the characters until index 1 of "e-t", which is e.
We retain the characters after index 2 of "e-t", which is t. And we put a space in the middle.

Example underscore: Convert "Kitchen_window is open" to "Kitchen Window is open"
* Split text at pattern (optional): _
* Retain characters in matched string until index: 0
* Retain characters in matched string from index: 1

What happens: The regex match "_" in "Kitchen_window is open".  We retain the characters until index 0 of "_", which is no characters.
We retain the characters after index 1 of "_", which is no characters. And we put a space in the middle.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Out/text.  
> You:  
> (on your device):  
> (on other devices): <DINGDONG>  
> You:  
> (on your device):  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/RdeLange/skill-mosquito-broadcast```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/RdeLange/skill-mosquito-broadcast](https://github.com/RdeLange/skill-mosquito-broadcast)  
**Owner:** [@RdeLange](https://github.com/RdeLange)  
**Created:** 2018 May 23 21:32:47 UTC  **Last updated:** 2020 Jan 23 22:50:38 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ uncategorized ]   
