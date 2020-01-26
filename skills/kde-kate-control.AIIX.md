---
description: 
---

### _kde-kate-control.AIIX_  
## Description:  
Installation of skill

Download or Clone Git run git clone  inside optmycroftskills
Create optmycroftskills folder if it does not exist
Extract Downloaded Skill into a folder. "kde-kate-control". Clone does not require this step
Copy the kde-kate-control folder to optmycroftskills folder

Installation of requirements
Fedora

sudo dnf install dbus-python
From terminal cp -R usrlib64python2.7site-packagesdbus* home$USER.virtualenvsmycroftlibpython2.7site-packages
From terminal cp usrlib64python2.7site-packages_dbus* home$USER.virtualenvsmycroftlibpython2.7site-packages

Ubuntu  KDE Neon

sudo apt install python-dbus
From terminal cp -R usrlibpython2.7dist-packagesdbus* home$USER.virtualenvsmycroftlibpython2.7site-packages

From terminal cp usrlibpython2.7dist-packages_dbus* home$USER.virtualenvsmycroftlibpython2.7site-packages


For other distributions

Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to home$USER.virtualenvsmycroftlibpython2.7site-packages.
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Create new file.  
> Close file.  
> Save documents.  
> Goto next tab.  
> Goto previous tab.  
> Split view horizontally.  
> Split view vertically.  
> Goto next view.  
> Goto previous view.  
> Show config.  
  
{% hint style="warning" %}
This skill Did not pass the Abstract Syntax Trees testing. Skill properly do not work in current state.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/AIIX/kde-kate-control](https://github.com/AIIX/kde-kate-control)  
**Owner:** [@AIIX](https://github.com/AIIX)  
**Created:** 2017 Nov 28 13:32:40 UTC  **Last updated:** 2017 Dec 08 08:54:08 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ uncategorized ]   
