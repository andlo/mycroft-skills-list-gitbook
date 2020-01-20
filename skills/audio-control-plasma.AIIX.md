---
description: 
---
#### Installation of skill:
* Download or Clone Git (run: git clone https://github.com/AIIX/audio-control-plasma inside /opt/mycroft/skills)
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "audio-control-plasma". (Clone does not require this step)
* Copy the audio-control-plasma folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora:
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Kubuntu / KDE Neon:
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

* For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

**Github:** (https://github.com/AIIX/audio-control-plasma)

**Owner:** [@AIIX](https://github.com/AIIX) ![https://avatars3.githubusercontent.com/u/19663666?v=4]

