---
description: Common playback control system
---

### _skill-playback-control.AVA-USP_  
## Description:  
This Skill doesn't do anything by itself, but it provides an important common
language for audio playback skills.  By handling simple phrases like
'pause', this one Skill can turn around and rebroadcast the [messagebus](https://mycroft.ai/documentation/message-bus/)
command `mycroft.audio.service.pause`, allowing several music services to share
common terminology such as "pause".

Additionally, this implements the common Play handler.  This allows playback
services to negotiate which is best suited to play back a specific request.
This capability is used by the [Spotify](https://github.com/forslund/spotify-skill) and [Pandora](https://github.com/mycroftai/pianobar-skill) Skills, among others.  
  
  
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
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/AVA-USP/skill-playback-control```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/AVA-USP/skill-playback-control](https://github.com/AVA-USP/skill-playback-control)  
**Owner:** [@AVA-USP](https://github.com/AVA-USP)  
**Created:** 2020 Apr 02 22:22:14 UTC  **Last updated:** 2020 Jul 02 23:00:20 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Music ]   
**Tags:** \#music \#play \#playback \#pause \#resume \#next \#system   
