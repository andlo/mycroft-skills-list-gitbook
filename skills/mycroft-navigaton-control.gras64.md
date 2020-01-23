---
description: Common playback control system
---

### _mycroft-navigaton-control.gras64_  
This Skill doesn't do anything by itself, but it provides an important common
language for audio playback skills.  By handling simple phrases like
'pause', this one Skill can turn around and rebroadcast the messagebus
command mycroft.audio.service.pause, allowing several music services to share
common terminology such as "pause".
Additionally, this implements the common Play handler.  This allows playback
services to negotiate which is best suited to play back a specific request.
This capability is used by the Spotify and Pandora Skills, among others.  
**Platform:**  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
**Tags:** \#music \#play \#playback \#pause \#resume \#next \#system   
## Examples:  
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
``` mycroft-msm install https://github.com/gras64/mycroft-navigaton-control```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** | [https://github.com/gras64/mycroft-navigaton-control](https://github.com/gras64/mycroft-navigaton-control)  
**Owner:** | [@gras64](https://github.com/gras64)  
**Created:** | 2019 Dec 03 22:15:34 UTC  **Last updated:** 2019 Dec 03 22:17:09 UTC  
**License:** | Apache License 2.0  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
