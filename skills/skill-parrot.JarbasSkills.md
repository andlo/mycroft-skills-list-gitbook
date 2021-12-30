---
description: Turn Mycroft into a echoing parrot!  Make Mycroft repeat whatever you want  Repeats recent audio tra
---

### _skill-parrot.JarbasSkills_  
## Description:  
Turn Mycroft into a parrot. Speak a phrase and listen to it repeated in Mycroft's voice.

"Hey Mycroft, start parrot"
"hello"
hello
"what"
what
"who are you"
who are you
"Stop parrot"

Also provides an idle screen with parrot images and a random previous STT
transcription

NOTES:

- This will blacklist and replace the functionality
of [MycroftAI/skill-speak](https://github.com/MycroftAI/skill-speak),
see [Issue#24](https://github.com/MycroftAI/skill-speak/issues/24)
- This will blacklist and replace the functionality
of [MatthewScholefield/skill-repeat-recent](https://github.com/MatthewScholefield/skill-repeat-recent)
- When asking to repeat what was previously said source is taken into
consideration, if you ask in cli, gui, hivemind or STT response will vary
accordingly, ie. using voice satellite wont respond with STT from device,
only same source is taken into consideration
- Previous transcriptions are not persisted to disk.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Say Goodnight, Gracie.  
> Repeat Once upon a midnight dreary, while I pondered, weak and weary, Over.  
> Speak I can say anything you'd like!  
> Repeat what you just said.  
> Repeat that.  
> Can you repeat that?  
> What did I just say?  
> Tell me what I just said.  
> Start parrot.  
> Stop parrot.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/JarbasSkills/skill-parrot```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/JarbasSkills/skill-parrot](https://github.com/JarbasSkills/skill-parrot)  
**Owner:** [@JarbasSkills](https://github.com/JarbasSkills)  
**Created:** 2017 Mar 04 22:33:40 UTC  **Last updated:** 2020 Jul 06 21:49:30 UTC  
**License:** Apache License 2.0  
  
**Categories:** [ Entertainment ]   
