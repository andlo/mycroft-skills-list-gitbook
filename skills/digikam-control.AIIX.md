---
titel: Digikam-Control
description: 
---
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