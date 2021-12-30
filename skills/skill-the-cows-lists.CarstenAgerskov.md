---
description: 
---

### _skill-the-cows-lists.CarstenAgerskov_  
## Description:  
This skill adds [Remember The Milk](https://www.rememberthemilk.com/) support to [Mycroft](https://mycroft.ai/).
The skill use Remember The Milk's [rest interface](https://www.rememberthemilk.com/services/api/).
The purpose if the skill is to allow operations suited for a voice interface. It is not an attempt to cover all functionality of remember the milk.

An authentication flow must be executed before other operations can be
done, see section [Configuration](##Configuration)
Some advice on installation can be found in section [Installation](##Installation)

### The dialog
The cows lists work with lists and tasks. When you mention a list or a task in a command to the cows lists,
it will be remenbered for a short time (2 minutes). The task or list is said to be in context. Whthin this time, further commands to the cows list will refer to the list and/or task in context.
For instance:

* You: "Hey Mycroft, find bananas on the grocery list"
* Mycroft: "I found bananas on list grocery"
* You: "Hey Mycroft, complete it"
* Mycroft: "bananas on list grocery was marked complete"
* You: "Hey Mycroft, read the list"
* Mycroft: "List grocery has 3 tasks on it, potatos, apples, oranges"
* You: "Hey Mycroft, complete oranges"
* Mycroft: "oranges on list grocery was marked complete"

Some commands support special dialogs. For instance
* You: "Hey Mycroft, add bananas to the grocery list"
* Mycroft: "bananas was added to list grocery"
* You: "Hey Mycroft, add oranges"
* Mycroft: "oranges, anything else?"
* You: "appels"
* Mycroft: "apples, anything else?"
* You: "potatos"
* Mycroft: "potatos, anything else?"
* You: "no"
* Mycroft: "okay, the tasks are added to list grocery"

The skill will try to recognize mispronounced list or task names, for example:
* You: "Hey Mycroft, find call back on my bin box list"
* Mycroft: "I can't find a list called bin box, do you want to use the list inbox instead?"
* You: "yes"
* Mycroft: "I did not find call back, but i did find call home on list inbox"


#### Commands
This section lists all available commands.

In general, for all operations below, you can substitute "my" list with "the" list, i.e. "add milk to the grocery list" and "add milk to my grocery list" are both valid.

Be careful about using the word 'list' when you name the lists in Remember The Milk. For instance, the skill can handle a list called 'grocery' OR a list called 'grocery list', but if you have BOTH, the skill will only find the 'grocery list'.

#### Add a task
For example:
* "Hey Mycroft, add milk to my grocery list"
* "Hey Mycroft, add remember to call home to list Inbox"

The skill is using Remember The Milk ["smart add"](https://www.rememberthemilk.com/help/?ctx=basics.smartadd.whatis.) For example:

* "Hey Mycroft, add remember to call home tomorrow at 9 to list Inbox"

will add a task called "remember to call home" to the Remember The Milk's Inbox, and set the due date to tomorrow at 9. See also the due command later in this section.

#### Complete task
Complete a task on a list, the operation can be undone within 2 minutes:
* You: "Hey Mycroft, complete call home on my personal list"
* Mycroft: "Call home on list personal was marked complete"
* You: "Hey Mycroft, restore"
* Mycroft: "I have restored call home on list personal again"

#### Complete all tasks on a list
Complete all tasks on a list, this operation may take a while if there are many tasks. The operation can be undone within 2 minutes:
* You: "Hey Mycroft, complete all tasks on my grocery list"
* Mycroft: "3 tasks on list grocery was marked complete"
* You: "Hey Mycroft, restore"
* Mycroft: "I have restored 3 tasks on list grocery again"

To keep processing time down, a maximum of 40 tasks can be deleted for each complete list command. The
RTM api has a rate limit of 1 call per second, 40 tasks will take approximately 40 seconds to complete.
If you use the Mycroft "stop" command during processing, it may not be possible to undo the operation.

#### Due tasks
Find out what tasks are due. Due date can be one of: "now, yesterday, today, tomorrow, monday, tuesday, wedensday, thursday, friday, saturday, sunday"

* You: "Hey Mycroft, what is on my inbox list today"
* Mycroft: "List inbox has 2 tasks on it, call home, go fishing"

* You: "Hey Mycroft, add go fishing today to the inbox list"
* Mycroft: "go fishing today was added to list inbox"
* You: "Hey Mycroft, what is due today"
* Mycroft: "List inbox has 1 task on it, that are due today, go fishing"

#### Find task on list
Find a task on a list:
* You: "Hey Mycroft, find milk on my grocery list"
* Mycroft: "I found milk on list grocery"

#### Read list
Read the tasks on a list:
* You: "Hey Mycroft, read list inbox"
* Mycroft: "List inbox has 2 tasks on it, call home, go fishing"

#### Undo
If an operation makes changes to your lists or tasks, it can be undone within 2 minutes, for example:

* You: "Hey Mycroft, add call home to list inbox"
* Mycroft: "call home was added to list inbox"
* You: "Hey Mycroft, undo"
* Mycroft: "I have removed call home from list inbox again"

The words "undo", "revert", "roll back" and "restore" can be used

#### Report an error
In case of a technical error, the cows lists will ask you if you want a mail with the details. Answer yes, and you will receive a mail from Mycroft with further details on how to report the issue, and all the details about the error.
You receive the mail, it is not sent the skill developer. The mail contains detalis about how to report the error to the skill developer,
and you decide what information to put in the issue report.

Other issues that are not caught as describe above, can be reported as well, on https://github.com/CarstenAgerskov/skill-the-cows-lists/issues.  
  
![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)![](../.gitbook/assets/star.png)  
  
### Platform:  
 ![Mark I](../.gitbook/assets/mark-1-icon.png)  ![Mark II](../.gitbook/assets/mark-2-icon.png)  ![Picroft](../.gitbook/assets/picroft-icon.png)  ![plasmoid](../.gitbook/assets/kde.png)   
### Examples:  
> Add milk to my grocery list.  
> Add remember to call home tomorrow at 9 to list Inbox.  
  
## Installation:  
{% hint style="warning" %}
This skill is not aproved by Mycroft skill tester.
{% endhint %}
    
{% tabs %}
{% tab title="Install by mycroft-msm" %}
``` mycroft-msm install https://github.com/CarstenAgerskov/skill-the-cows-lists```
{% endtab %}
  {% endtabs %}
    
## Summary:  
**Github:** [https://github.com/CarstenAgerskov/skill-the-cows-lists](https://github.com/CarstenAgerskov/skill-the-cows-lists)  
**Owner:** [@CarstenAgerskov](https://github.com/CarstenAgerskov)  
**Created:** 2017 Nov 26 15:48:44 UTC  **Last updated:** 2019 May 10 00:51:51 UTC  
**License:** GNU General Public License v3.0  
  
**Categories:** [ uncategorized ]   
