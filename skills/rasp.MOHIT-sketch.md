---
description: Example of interacting with GPIO pins on a Raspberry Pi
---
This Skill demonstrates how to interact with the Raspberry Pi GPIO pins using a Mycroft Skill. This Skill shows both reading data from a GPIO port (detecting a button press) and writing data to the port (illuminating an LED).

### Preparation

[You will need to first install the GPIO libraries for Picroft, and add some additional permissions](https://mycroft.ai/documentation/picroft/#using-the-gpio-pins-on-the-raspberry-pi-3).

### Generation

The documentation is done using Sphinx, which picks up comments from the code.  The following will generate the html docs.

```make docs```

You can then find the generated html in ```docs/build/html/index.html```.  Open that file in your browser and you should be able to navigate to the docs.

### Installing from the `makefile`

* Change the Makefile IP address for the RPi installation to the IP address of your RPi.

That is, edit the file `makefile` using your favorite editor like `nano` or `vi`.

The line you will need to change is `scp -r * pi@192.168.205.115:/opt/mycroft/skills/skill-gpio`.

Change this to have the IP address of your RPi.

* Create the folder ```/opt/mycroft/skills/skill-gpio``` on the RPi for the installer.

You can do this by using the command `mkdir /opt/mycroft/skills/skill-gpio`

* Build the code using the `makefile`.  ```make install.pi```

### Testing the `makefile`

```make test.pi```

This will run a test to be sure you have access to the GPIO and will report any errors that are identified.

### Notes

If the LED blinking is too fast, it will be difficult to get a command to execute because there will be a voice response when the the LED turns off and on. Turn the blinking to a lower frequency to be able to execute commands.

### Circuit
Please use the below image as a guide to the circuit layout:

![](https://github.com/MycroftAI/picroft_example_skill_gpio/blob/master/IMG_20170706_153744.jpg)

**Github:** | (https://github.com/MOHIT-sketch/rasp)  
**Owner:** | [@MOHIT-sketch](https://github.com/MOHIT-sketch)  
**Created:** | 2019-08-05T09:10:55Z  **Last updated:** 2019-08-05T09:21:02Z  
**License:** | [Apache License 2.0](https://api.github.com/licenses/apache-2.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/picroft-icon.png)   
**Tags:** \#IoT \#GPIO \#RPi   
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
  {% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/MOHIT-sketch/rasp```
{% endtab %}
  {% endtabs %}
  