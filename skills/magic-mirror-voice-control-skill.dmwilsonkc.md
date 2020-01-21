---
description: Give voice commands to Mycroft to control a MagicMirror
---
Magic Mirror Voice Control

This mycroft skill passes commands to an accessible MagicMirror installed anywhere on the same network as Mycroft. It requires a working install of [MagicMirror](https://github.com/MichMich/MagicMirror) and the [MMM-Remote-Control module](https://github.com/Jopyth/MMM-Remote-Control). It must be installed AND ACCESSIBLE ON THE SAME NETWORK AS MYCROFT.

This skill requires MMM-Remote-Control be installed and working properly on the MagicMirror.

You must configure the MagicMirror's config.js file to properly whitelist the ip address of your Mycroft.

In the MagicMirror's config.js:

Replace: address: "localhost", With: address: "0.0.0.0", and

Replace: ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1"], with ipWhitelist: ["127.0.0.1", "192.168.X.1/24"],

You can use this skill to hide or show modules, update the mirror or individual modules,
refresh or restart the mirror, list installed modules, install modules by name (will still require you
to configure the MagicMirror config.js by SSH or VNC for the particular skill you install), change pages of modules by either swipe commands or telling mycroft to "go to page [number]"(requires that [MMM-pages](https://github.com/edward-shen/MMM-pages) be installed), restart or reboot the Raspberry Pi.

**Github:** | (https://github.com/dmwilsonkc/magic-mirror-voice-control-skill)  
**Owner:** | [@dmwilsonkc](https://github.com/dmwilsonkc)  
**Created:** | 2018-05-30T02:09:43Z  **Last updated:** 2019-12-28T22:46:02Z  
**License:** | [Apache License 2.0](https://api.github.com/licenses/apache-2.0)  
**Market status:** | [Pending Market](https://market.mycroft.ai/skill/) PR-933 new override autotester waiting  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
