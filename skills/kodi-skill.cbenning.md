---  
description:   
---  
![](../.gitbook/assets/star.png)  
# kodi-skill  
### _kodi-skill.cbenning_  
## About:  
Add the following section to your mycroft-core/mycroft/configuration/mycroft.ini file
```
[KodiSkill]
protocol = "http"
host = "<kodi-host>"
port = 80
similarity_threshold_percentage = 75
```

Also make sure your kodi is setup to be controlled via http interface.

## Skill information:  
**Github:** | [https://github.com/cbenning/kodi-skill](https://github.com/cbenning/kodi-skill)  
**Owner:** | [@cbenning](https://github.com/cbenning)  
**Created:** | 2016 Jul 12 07:13:23 UTC  **Last updated:** 2018 Aug 18 22:40:01 UTC  
**License:** | Apache License 2.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**  
 ![](../.gitbook/assets/mark-1-icon.png)  ![](../.gitbook/assets/mark-2-icon.png)  ![](../.gitbook/assets/picroft-icon.png)  ![](../.gitbook/assets/kde.png)   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
## Installation:  
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/cbenning/kodi-skill```
{% endtab %}
  {% endtabs %}
  