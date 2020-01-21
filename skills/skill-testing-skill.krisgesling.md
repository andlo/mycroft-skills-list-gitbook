---
description: Internal utterance testing tool
---
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

**Github:** | (https://github.com/krisgesling/skill-testing-skill)  
**Owner:** | [@krisgesling](https://github.com/krisgesling)  
**Created:** | 2019-04-19T03:46:49Z  **Last updated:** 2019-12-17T13:47:17Z  
**License:** | No License  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
**Tags:** \#testing   
{% hint style="danger" %}
This skill dosnt have any license attatched. It is not adviasable to use this skillnor fork or clone, as you dont know if you are legaly allowed to do so by the auhtor.
{% endhint %}