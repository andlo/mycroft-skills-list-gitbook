---
description: AMZN Music Player Makes Mycroft play your amaz*n music library as if its name was Alexa -
---

### _amzn-music-skill.domcross_  
## Description:  
This skill requires an Amaz*n Music account and a subscription of type "music unlimited" or "prime music" - even if you want to stream music from your own library only.

After skill is installed is you must either:

a) enter your login credentials at home.mycroft.ai > Skills > Amzn music
WARNING: with this option your Amaz\*n username and password will be stored i) on a server hosted by mycroft.ai and ii) in clear text in the skills 'settings.json' file.

b) run './credentials.py' in the skills directory and enter your login credentials there.
In this case your credentials will be stored encoded & pickled in file 'credentials.store' - this option is recommended if you care for privacy.
NOTE: file 'credentials.store' must be owned by mycroft:mycroft - either run credentials.py as user 'mycroft' or sudo chown mycroft:mycroft credentals.store afterwards.

NOTE: this was tested only on Mycroft Mark-1 and PiCroft (both running Debian Jessie) and will probably run (not tested yet) on PiCroft with Debian Stretch.
Most likely this will not run on Ubuntu or other OS without tweaking requirements.sh at least (any assistance here is welcome)

NOTE: this will install 'VLC media player' as a requirement, which is a approx. 70MB download an will require additinal 250MB on your sd-card when unpacked...  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Hey ~~Alexa~~ Mycroft, play the song purple rain by prince on amaz*n music.  
> Play the album 25 by adele.  
> Play something by the foo fighters.  
> Play some jazz.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/domcross/amzn-music-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/domcross/amzn-music-skill](https://github.com/domcross/amzn-music-skill)  
**Owner:** [@domcross](https://github.com/domcross)  
**Created:** 2018 Dec 15 15:59:03 UTC  **Last updated:** 2020 Oct 07 06:22:38 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Music ]   
**Tags:** \#amzn \#music   
