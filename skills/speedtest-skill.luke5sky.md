---  
description: Ask Mycroft to run a simple speedtest  
---  
# Speedtest  
### _speedtest-skill.luke5sky_  
## About:  
Run a speedtest with Mycroft.
This skill uses the speedtest-cli (https://github.com/sivel/speedtest-cli) which runs an internet bandwidth test using speedtest.net.

Be aware that this speedtest relies on the capability of the network-adapter of your Mycroft device.

Examples for Raspberry Pi:
- Raspberry Pi 3 B  onboard WiFi: max. ~40 Mbit/s, onboard LAN: max. ~100 Mbit/s
- Raspberry Pi 3 B+ onboard WiFi: max. ~100 Mbit/s, onboard LAN: max. ~225 Mbit/s

If a Raspberry Pi 3 B - connected to WiFi - runs Mycroft you won't get more than 40 Mbit/s from the speedtest despite your internet connection may have more bandwith.

## Skill information:  
**Github:** | [https://github.com/luke5sky/speedtest-skill](https://github.com/luke5sky/speedtest-skill)  
**Owner:** | [@luke5sky](https://github.com/luke5sky)  
**Created:** | 2019 Jan 03 15:37:35 UTC  **Last updated:** 2019 Jan 24 10:07:17 UTC  
**License:** | Apache License 2.0  
**Market status:** | [In Market](https://market.mycroft.ai/skill/speedtest)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
**Tags:** \#ínternet \#speed \#bandwith   
## Examples:  
> Run a speedtest.  
  
{% hint style="info" %}
This skill is in Mycroft Market. That means it is aproved by the Mycroft Skill testers
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Speedtest
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Speedtest```
{% endtab %}
  {% endtabs %}
  