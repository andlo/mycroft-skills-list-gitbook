---
description: Capture information for Mycroft support
---

### _skill-support.MycroftAI_  
## Description:  
This Skill generates a package with debugging information and emails it to the email address registered in your [home.mycroft.ai](https://home.mycroft.ai) account. This package can be used for debugging issues yourself, or alternatively it can be emailed to Mycroft to create a support request.

The package contains all of your `mycroft-core` logs on the Device, and information about active Skills and Intents at the time the support request was generated.

This uses the [0x0.st](https://0x0.st/) service for storing the debugging information.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Create a support ticket.  
> You're not working!  
> Send me debug info.  
  
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Support
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Support```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/MycroftAI/skill-support](https://github.com/MycroftAI/skill-support)  
**Owner:** [@MycroftAI](https://github.com/MycroftAI)  
**Created:** 2017 Dec 13 06:06:46 UTC  **Last updated:** 2020 Oct 26 02:44:20 UTC  
**License:** Apache License 2.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/mycroft-support-helper)  
**Categories:** [ Configuration ]   
**Tags:** \#support \#support-request \#help \#assistance \#logs \#troubleshooting \#system   
