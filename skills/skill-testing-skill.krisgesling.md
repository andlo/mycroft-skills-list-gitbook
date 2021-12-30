---
description: Internal utterance testing tool
---

### _skill-testing-skill.krisgesling_  
## Description:  
### "read all utterances"
Enter a list of phrases in Skill settings to verify which Skill and intent handler is triggered. Phrase list should be in format:
> phrase one, phrase two, phrase three

Alternatively provide a csv of phrases at: `~/.mycroft/skills/SkillTesting/utterances.csv`

If a phrase contains a comma it must be surrounded with quotation marks:
> phrase one, "phrase, two", phrase three

Additional options include:
- test_identifier - title of the test for your benefit eg 'weather phrases' - default timestamp of test comppletion time.
- delay - the period in seconds between each phrase - default 30

Results will be uploaded to termbin.com in csv format and the link will be emailed to you. A csv file of the results will also be saved on the device at: `~/.mycroft/skills/SkillTesting/reading-output/{test_identifier}.csv`. Note that when creating the filename, characters not in [a-z, A-Z, 0-9, [.\_-]] will be removed eg "weather phrases" will become "weatherphrases.csv". This file can be used to generate integration tests for all phrases.  
  
![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Read all utterances.  
> Generate integration tests.  
> Run integration tests.  
> Remove generated tests.  
  
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skill nor fork or clone, as you don't know if you are legaly allowed to do so by the auhtor.
{% endhint %}
  
## Summary:  
**Github:** [https://github.com/krisgesling/skill-testing-skill](https://github.com/krisgesling/skill-testing-skill)  
**Owner:** [@krisgesling](https://github.com/krisgesling)  
**Created:** 2019 Apr 19 03:46:49 UTC  **Last updated:** 2020 Jul 09 05:57:00 UTC  
**License:** No License  
  
**Categories:** [ Configuration ]   
**Tags:** \#testing   
