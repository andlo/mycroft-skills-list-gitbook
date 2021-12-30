---
description: Give voice commands to Mycroft to control a MagicMirror
---

### _magic-mirror-voice-control-skill.dmwilsonkc_  
## Description:  
This mycroft skill passes commands to an accessible MagicMirror installed anywhere on the same network as Mycroft. It requires a working install of [MagicMirror](https://github.com/MichMich/MagicMirror) and the [MMM-Remote-Control module](https://github.com/Jopyth/MMM-Remote-Control). It must be installed AND ACCESSIBLE ON THE SAME NETWORK AS MYCROFT.

This skill requires MMM-Remote-Control be installed and working properly on the MagicMirror.

You must configure the MagicMirror's config.js file to properly whitelist the ip address of your Mycroft.

In the MagicMirror's config.js:

Replace: address: "localhost", With: address: "0.0.0.0", and

Replace: ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], with ipWhitelist: ["127.0.0.1", "192.168.X.1/24"],

You can use this skill to hide or show modules, update the mirror or individual modules,
refresh or restart the mirror, list installed modules, install modules by name (will still require you
to configure the MagicMirror config.js by SSH or VNC for the particular skill you install), change pages of modules by either swipe commands or telling mycroft to "go to page [number]"(requires that [MMM-pages](https://github.com/edward-shen/MMM-pages) be installed), restart or reboot the Raspberry Pi.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> : hide clock.  
> Show clock.  
> Turn on weather.  
> Turn off weather.  
> Show [insert module name]  
> Hide [insert module name]  
> Update mirror.  
> Update [insert module name]  
> Restart pi.  
> Restart mirror.  
> Refresh mirror.  
> Reboot raspberry pi.  
> Show article details.  
> Hide article details.  
> Swipe left.  
> Swipe right.  
> List installed modules.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/dmwilsonkc/magic-mirror-voice-control-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/dmwilsonkc/magic-mirror-voice-control-skill](https://github.com/dmwilsonkc/magic-mirror-voice-control-skill)  
**Owner:** [@dmwilsonkc](https://github.com/dmwilsonkc)  
**Created:** 2018 May 30 02:09:43 UTC  **Last updated:** 2020 Aug 29 00:29:16 UTC  
**License:** Apache License 2.0  
**Market status:** [Pending Market](https://market.mycroft.ai/skill/) [ PR-933 ] [ waiting ] [ new ] [ override autotester ]  
**Categories:** [ IoT ]   
