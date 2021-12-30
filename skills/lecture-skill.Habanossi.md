---
description: 
---

### _lecture-skill.Habanossi_  
## Description:  
When asked what kind of lecture there is today, mycroft answers with the right subject. this works as a teaching example for home assistants.

In "dates.txt" the user puts dates for upcoming lectures with some requirements:
> - one date per line
> - in the format YYYYMMDD
> - in the right order, with the first upcoming lecture date highest on the list, the second lecture date second and so on.

The user can modify the .dialog files to match the lectures. Files will be named "lecture1", "lecture2" and so on.
Observe that the amount of lecture.dialog files must match the amount of dates in "dates.txt". Otherwise an error will occur.

Date settings can be changed so that mycroft either uses a default answer or uses dates.txt for lecture subjects set for specific dates.
If the date of today cannot be found in "dates.txt", nolecture.dialog will be used. This means that there is no lecture today.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> What is the subject of the lecture?  
> What theme does the lecture have?  
> Change the lecture settings.  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/Habanossi/lecture-skill](https://github.com/Habanossi/lecture-skill)  
**Owner:** [@Habanossi](https://github.com/Habanossi)  
**Created:** 2019 May 08 07:05:29 UTC  **Last updated:** 2019 Aug 30 07:56:57 UTC  
**License:** No License  
  
**Categories:** [ uncategorized ]   
