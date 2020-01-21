---
description: 
---
Lecture Subjects

When asked what kind of lecture there is today, mycroft answers with the right subject. this works as a teaching example for home assistants.

In "dates.txt" the user puts dates for upcoming lectures with some requirements:
> - one date per line
> - in the format YYYYMMDD
> - in the right order, with the first upcoming lecture date highest on the list, the second lecture date second and so on.

The user can modify the .dialog files to match the lectures. Files will be named "lecture1", "lecture2" and so on.
Observe that the amount of lecture.dialog files must match the amount of dates in "dates.txt". Otherwise an error will occur.

Date settings can be changed so that mycroft either uses a default answer or uses dates.txt for lecture subjects set for specific dates.
If the date of today cannot be found in "dates.txt", nolecture.dialog will be used. This means that there is no lecture today.

**Github:** | (https://github.com/Habanossi/lecture-skill)  
**Owner:** | [@Habanossi](https://github.com/Habanossi)  
**Created:** | 2019-05-08T07:05:29Z  **Last updated:** 2019-08-30T07:56:57Z  
**License:** | No License - dont use this skill !  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
