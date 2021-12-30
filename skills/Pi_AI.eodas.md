---
description: 
---

### _Pi_AI.eodas_  
## Description:  
This Skill demonstrates how to interact with the Raspberry Pi GPIO pins using a Mycroft Skill. This Skill shows both reading data from a GPIO port (detecting a button press) and writing data to the port (illuminating an LED).

### Preparation

[You will need to first install the GPIO libraries for Picroft, and add some additional permissions](https://mycroft.ai/documentation/picroft/#using-the-gpio-pins-on-the-raspberry-pi-3).

### Installing from the `makefile`

* Change the Makefile IP address for the RPi installation to the IP address of your RPi.

That is, edit the file `makefile` using your favorite editor like `nano` or `vi`.

The line you will need to change is `scp -r * pi@192.168.205.115:/opt/mycroft/skills/skill-gpio`.

Change this to have the IP address of your RPi.

* Create the folder ```/opt/mycroft/skills/skill-gpio``` on the RPi for the installer.

You can do this by using the command `mkdir /opt/mycroft/skills/skill-gpio`

* Build the code using the `makefile`.  ```make install.pi```

### Notes

If the LED blinking is too fast, it will be difficult to get a command to execute because there will be a voice response when the the LED turns off and on. Turn the blinking to a lower frequency to be able to execute commands.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)   
### Examples:  
> Turn Device on.  
> Turn Device off.  
> Blink Device.  
> Device status.  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/eodas/Pi_AI](https://github.com/eodas/Pi_AI)  
**Owner:** [@eodas](https://github.com/eodas)  
**Created:** 2020 Jul 25 16:51:40 UTC  **Last updated:** 2020 Sep 27 14:51:13 UTC  
**License:** No License  
  
**Categories:** [ IoT ]   
**Tags:** \#IoT \#GPIO \#RPi   
