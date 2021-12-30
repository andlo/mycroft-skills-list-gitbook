---
description: Updates original Mark 1 devices so they can upgrade to the latest version of Mycroft
---

### _skill-platform-patch.MycroftAI_  
## Description:  
Some of the earliest shipping Mark 1 devices require this platform patch in order to begin automatically updating.

You can tell if you need the patch by following this guide:

```
Hey Mycroft, install version checker
"Attempting to install"
```
(wait a minute)
```
Hey Mycroft, what version are you running?
"I'm runing mycroft-core version 0.8.19"
```
If your version is less than 0.9.0, you should install this platform patch.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)   
### Examples:  
> Install platform patch.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/MycroftAI/skill-platform-patch```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/MycroftAI/skill-platform-patch](https://github.com/MycroftAI/skill-platform-patch)  
**Owner:** [@MycroftAI](https://github.com/MycroftAI)  
**Created:** 2017 Jul 03 16:24:57 UTC  **Last updated:** 2018 Aug 29 18:29:59 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Configuration ]   
**Tags:** \#mark1 \#mycroft-mark1 \#platform-patch \#update \#patch   
