---
description: 
---

### _audio-control-plasma.AIIX_  
## Description:  
Installation of skill:

Download or Clone Git (run: git clone  inside /opt/mycroft/skills)
Create /opt/mycroft/skills folder if it does not exist
Extract Downloaded Skill into a folder. "audio-control-plasma". (Clone does not require this step)
Copy the audio-control-plasma folder to /opt/mycroft/skills/ folder

Installation of requirements:
Fedora:

sudo dnf install dbus-python
From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

Kubuntu / KDE Neon:

sudo apt install python-dbus
From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/


For other distributions:

Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Increase the volume.  
> Increase volume.  
> Increase to maximum volume.  
> Maximum volume.  
> Decrease the volume.  
> Decrease volume.  
> Decrease to minimum volume.  
> Minimum volume.  
> Increase the microphone volume.  
> Increase microphone volume.  
> Increase microphone to maximum volume.  
> Maximum microphone volume.  
> Decrease the microphone volume.  
> Decrease microphone volume.  
> Decrease microphone to minimum volume.  
> Minimum microphone volume.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/AIIX/audio-control-plasma```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/AIIX/audio-control-plasma](https://github.com/AIIX/audio-control-plasma)  
**Owner:** [@AIIX](https://github.com/AIIX)  
**Created:** 2017 Oct 05 08:38:57 UTC  **Last updated:** 2018 May 10 15:52:02 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ uncategorized ]   
