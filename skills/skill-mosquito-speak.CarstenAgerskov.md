---
description: 
---
This skill has two purposes:
1) Instead of triggering a skill by asking Mycroft a question, this skill triggers when a text message is received on mqtt.
It can be used for notifications. For instance, a smart home server could publish the text "Somebody is at the door", if the doorbell is pressed.
It is possible to make Mycroft repeat the last text it received on mqtt.

2) Send an utterance in text from mqtt, to activate other skills. For instance, if your
home automation detect that a window is opened, send the text "_utterance remind me to close the window in 10 minutes" on mqtt to
trigger the "reminder" skill.


### Configuration
The skill is configured on your "Mycroft Home" page. Configure the mqtt server, port and topic that the skill will listen for text messages on.
Currently, password or certificates are not supported. (Maybe I will implement it if you promise to test it :)

A restart of the skill is needed when changing the configuration.

Optionally, it is possible to split the text, using a regular expression.

Example CamelCase: If you send the string "KitchenWindow is open",
you want to split KitchenWindow. After the split Mycroft will say "Kitchen Window is open". To do that set the parameters on "Mycroft Home" like this:
* Split text at pattern (optional): [a-z][A-Z]
* Retain characters in matched string until index: 1
* Retain characters in matched string from index: 1

What happens: The regex match "nK" in "KitchenWindow is open". We retain the characters until index 1 of "nK", which is n.
We retain the characters after index 1 of "nK", which is K. And we put a space in the middle.

Example hypen: Convert "Outside-temperature is -5 degrees" to "Outside temperature is -5 degrees"
* Split text at pattern (optional): [a-z|A-Z]-[a-z|A-Z]
* Retain characters in matched string until index: 1
* Retain characters in matched string from index: 2

What happens: The regex match "e-t" in "Outside-temperature is -5 degrees".  We retain the characters until index 1 of "e-t", which is e.
We retain the characters after index 2 of "e-t", which is t. And we put a space in the middle.

Example underscore: Convert "Kitchen_window is open" to "Kitchen Window is open"
* Split text at pattern (optional): _
* Retain characters in matched string until index: 0
* Retain characters in matched string from index: 1

What happens: The regex match "_" in "Kitchen_window is open".  We retain the characters until index 0 of "_", which is no characters.
We retain the characters after index 1 of "_", which is no characters. And we put a space in the middle.

**Github:** (https://github.com/CarstenAgerskov/skill-mosquito-speak)

**Owner:** [@CarstenAgerskov](https://github.com/CarstenAgerskov) ![https://avatars2.githubusercontent.com/u/7515935?v=4]

