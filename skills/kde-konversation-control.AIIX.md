---
description: Installation of skill
---

### _kde-konversation-control.AIIX_  
## Description:  
Installation of skill

Download or Clone Git run git clone  inside optmycroftskills
Create optmycroftskills folder if it does not exist
Extract Downloaded Skill into a folder. "kde-konversation-control". Clone does not require this step
Copy the kde-konversation-control folder to optmycroftskills folder

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
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Show Konversation.  
> Quit Konversation.  
> Show Konversation Server List.  
> Manage Konversation Identity.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/AIIX/kde-konversation-control```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/AIIX/kde-konversation-control](https://github.com/AIIX/kde-konversation-control)  
**Owner:** [@AIIX](https://github.com/AIIX)  
**Created:** 2017 Oct 31 12:00:04 UTC  **Last updated:** 2017 Oct 31 12:02:05 UTC  
**License:** GNU General Public License v3.0  
**Market status:** [Not in Market](https://market.mycroft.ai/skill/)  
**Categories:** [ uncategorized ]   
