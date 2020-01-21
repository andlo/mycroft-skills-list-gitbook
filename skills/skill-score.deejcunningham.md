---
description: 
---
score

Skill-score is an application that enables Mycroft to answer user questions about Major League Baseball (MLB) scores. [Mycroft](https://mycroft.ai) is an open-source AI voice assistant. Skill-score uses [panzarino's mlbgame API](https://github.com/panzarino/mlbgame) to report an MLB team's latest final scores, including live scores.

User input has the format:
<br />"What is the {team}'s score?"

If a game is in progress, Mycroft will respond:
<br />"The {team} are winning/losing {score} to {score} against the {opponent} in the top/middle/bottom/end of the {inning}."

If a game is not in progress, Mycroft will respond:
<br />"The {team} won/lost {score} to {score} against the {opponent} {number-of-days} ago."

### Next Goals

The next goals for skill-score are the ability to:
* give the time of the next MLB game; and
* support more leagues (e.g., National Football League, National Basketball League), depending on available APIs.

**Github:** | (https://github.com/deejcunningham/skill-score)  
**Owner:** | [@deejcunningham](https://github.com/deejcunningham)  
**Created:** | 2018-05-17T23:56:07Z  **Last updated:** 2019-10-29T21:49:58Z  
**License:** | [MIT License](https://api.github.com/licenses/mit)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
