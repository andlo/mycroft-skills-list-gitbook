---
description: 
---
Usage

This is a very old skill so it uses the now depricated skill config in mycroft.conf.
The skill can be configured to run scripts from easily pronouncable human utterances, such as "generate report" by adding the following to the `~/.mycroft/mycroft.conf`

```json
"CmdSkill": {
"alias": {
"generate report": "/home/forslund/scripts/generate_report.sh"
}
}
```

(The config needs to be valid json so be careful). The config usually contains a

The configuration above will launch `/home/forslund/scripts/generate_report.sh` when the second utterance under usage is invoked.

**Github:** | (https://github.com/forslund/cmd_skill)  
**Owner:** | [@forslund](https://github.com/forslund)  
**Created:** | 2017-01-26T06:49:16Z  **Last updated:** 2019-12-12T21:10:33Z  
**License:** | [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)  
**Market status:** | [Not in Market](https://market.mycroft.ai/skill/)  
**Platform:**   ![](.gitbook/assets/mark-1-icon.png)  ![](.gitbook/assets/mark-2-icon.png)  ![](.gitbook/assets/picroft-icon.png)  ![](.gitbook/assets/kde.png)   
