---
description: Common playback control system
---

### _skill-playback-control.MycroftAI_  
## Description:  
This Skill doesn't do anything by itself, but it provides an important common
language for audio playback skills.  By handling simple phrases like
'pause', this one Skill can turn around and rebroadcast the [messagebus](https://mycroft.ai/documentation/message-bus/)
command `mycroft.audio.service.pause`, allowing several music services to share
common terminology such as "pause".

Additionally, this implements the common Play handler.  This allows playback
services to negotiate which is best suited to play back a specific request.
This capability is used by the [Spotify](https://github.com/forslund/spotify-skill) and [Pandora](https://github.com/mycroftai/pianobar-skill) Skills, among others.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Play my summer playlist.  
> Play Pandora.  
> Pause.  
> Resume.  
> Next song.  
> Next track.  
> Previous track.  
> Previous song.  
  
## Installation:  
{% hint style="info" %}
This skill is in Mycroft Market and is thereby aproved by the Mycroft Skill testers
{% endhint %}
    
{% tabs %}
{% tab title="Install by voice" %}
> Hey Mycroft - install Playback Control
{% endtab %}
  {% tab title="Install by mycroft-msm" %}
``` mycroft-msm install Playback Control```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/MycroftAI/skill-playback-control](https://github.com/MycroftAI/skill-playback-control)  
**Owner:** [@MycroftAI](https://github.com/MycroftAI)  
**Created:** 2017 Jun 14 11:25:44 UTC  **Last updated:** 2020 Oct 06 00:27:48 UTC  
**License:** Apache License 2.0  
**Market status:** [In Market](https://market.mycroft.ai/skill/mycroft-playback-control)  
**Categories:** [ Music ]   
**Tags:** \#music \#play \#playback \#pause \#resume \#next \#system   
