---
description: Installation of skill:
---

### _amarok-player-skill.AIIX_  
## Description:  
Installation of skill:

Download or Clone Git
Create optmycroftskills folder if it does not exist
Extract Downloaded Skill into a folder. "amarok-player-skill". Clone does not require this step
Copy the amarok-player-skill folder to optmycroftskills folder

Installation of requirements:
Fedora:

sudo dnf install dbus-python
sudo dnf install python-psutil
From terminal: cp -R usrlib64python2.7site-packagesdbus* home$USER.virtualenvsmycroftlibpython2.7site-packages
From terminal: cp usrlib64python2.7site-packages_dbus* home$USER.virtualenvsmycroftlibpython2.7site-packages

Kubuntu  KDE Neon:

sudo apt install python-psutil
sudo apt install python-dbus
From terminal: cp -R usrlibpython2.7dist-packagesdbus* home$USER.virtualenvsmycroftlibpython2.7site-packages

From terminal: cp usrlibpython2.7dist-packages_dbus* home$USER.virtualenvsmycroftlibpython2.7site-packages


For other distributions:

Python Dbus and Python Psutil package is required and copying the Python Dbus folder and lib from your system python install over to home$USER.virtualenvsmycroftlibpython2.7site-packages.
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Amarok play music.  
> Amarok stop music.  
> Amarok next song.  
> Amarok previous song.  
> Amarok pause music/song.  
  
{% hint style="warning" %}
This skill Did not pass the Abstract Syntax Trees testing. Skill properly do not work in current state.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/AIIX/amarok-player-skill](https://github.com/AIIX/amarok-player-skill)  
**Owner:** [@AIIX](https://github.com/AIIX)  
**Created:** 2017 Mar 31 19:11:19 UTC  **Last updated:** 2019 Jul 31 13:54:50 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ uncategorized ]   
