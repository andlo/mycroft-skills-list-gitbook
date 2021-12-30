---
description: 
---

### _digikam-control.AIIX_  
## Description:  
#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/DigiKam-control inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "DigiKam-control". (Clone does not require this step)
* Copy the DigiKam-control folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora:
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Ubuntu / KDE Neon:
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> In digicam next image.  
> In digicam previous image.  
> In digicam rotate clockwise.  
> In digicam rotate counter clockwise.  
> Horizontally.  
> In digicam flip horizontally.  
> Vertically.  
> In digicam flip vertically.  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/AIIX/digikam-control](https://github.com/AIIX/digikam-control)  
**Owner:** [@AIIX](https://github.com/AIIX)  
**Created:** 2018 Mar 27 09:36:10 UTC  **Last updated:** 2018 May 29 11:52:44 UTC  
**License:** No License  
  
**Categories:** [ uncategorized ]   
