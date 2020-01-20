---
description: 
---
This skill is made to work with the full Habits Automation project https://github.com/PFE1718/mycroft-skills-automation.

Its role is to log mycroft intents when the user launches a skill. It runs continuously in the background and calls the other two skills of the project by utterance when necessary.
Different cases :
- Skill trigger detected (calls the automation handler skill)
- Frequency habit detected (calls the automation handler skill)
- Habit completed for the first time (calls the automation handler skill)
- Inactivity for more than 5 minutes after last command (calls the data mining skill)

**Github:** (https://github.com/PFE1718/PFE1718-skill-listener)

**Owner:** [@PFE1718](https://github.com/PFE1718) ![https://avatars0.githubusercontent.com/u/32484958?v=4]

