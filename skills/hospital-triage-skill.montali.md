---
description: Help ER patients by understanding why they're there
---

### _hospital-triage-skill.montali_  
## Description:  
This skill was born to help er patients on their arrival at the hospital. It asks the patient basic questions about his health.

### How it works

The skill is activated by saying the wake word (which, by default is `hey mycroft` but will be changed) and asking help:

`Hey Mycroft, puoi aiutarmi?`

Then, the interaction begins: the bot asks if it's talking directly with the patient. This helps us understands if he/she's conscious. Then, it asks about the main symptom. Right now, it recognises:

- Faints
- Hemorrhages
- Shocks
- Breathing difficulties
- Fractures (extracting the affected limb)
- Fevers
- Burns
- Abdominal pains

If the declared symptom is compatible with the COVID19, the bot asks some questions to determine the `covid_score`, an index determining how likely the patient is affected by COVID19.

It then assigns the patient a color code, according to the CESIRA index, and asks him/her to quantify the pain. Finally, it asks the patient his/her age and creates a `med_record` object containing all the gathered informations. This `med_record` can then be exported to assist the doctor during the checks.  
  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/montali/hospital-triage-skill```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/montali/hospital-triage-skill](https://github.com/montali/hospital-triage-skill)  
**Owner:** [@montali](https://github.com/montali)  
**Created:** 2020 Apr 08 09:55:26 UTC  **Last updated:** 2020 Jun 24 10:18:34 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ Information ]   
**Tags:** \#Hospital \#Triage \#Health \#Er   
