# FAQ
### Who made this list?
This list is made by Andreas Lorensen (@andlo).

### How often does this list get updated?
For the time beeing it is only manual updated. In time it will be updatet at least once every 24 hour
The plan is that the list is going to be updatet by a mycroft skill running on a mycroft device. Just
because it is fun that mycroft himself is making the list :) 

### How does a skill get to this list?
This list is made from searching Github for skills repositories. It is done by searching every repo that
mention Mycroft somewhere in tittle, reponame, or in README.md. Then each repo is analyzed to see if it
is a skill. That is done by looking into __init__.py. If it is a skills the README.md file is parsed and
used combined with Github info and Mycroft market info to make the json data that is used to make the list.

### Is the data free to use?
Yes - data is free tu use. The json data file can be found 
[here](https://github.com/andlo/mycroft-skills-list-gitbook/raw/master/_data/skills.json)

### How do I install the skills onto my device?
First it is most recomended only to install skills from official Mycroft Market. But if you want or need to 
install a sill found on this list anyway, then follow the instruction found on the specifik page.

### Can the skills listed be installed onto a device?
Yes - if the skill isnt in the Mycroft market, you can install the skill using mycroft-msm or git clone as 
stated on the specifik page. But do this carefully and read on each skills own github page for how to 
install, use and what does work etc. If a skill isnt working for you, open a issue on the github page 
or even better fork the skill, make It work and make a pull request back upstream.

### Can I install sill by voice?
Not for the time beeing. But plans are made for adding a skill that do let you search and install skills
found on this list. Proberly only skills that looks good like having a proper license and complete readme.md
file. 

### Why does the list containing skills that arent working or outdated?
The list is made to get overview over what exists and make a way to search for skills.

### I made a fork from a skill, but it isnt listet. Why?
The list does not include forks. If you did fork a skill, and did make it better, please make a pull 
request to the original github repo. If you made a fork, and changed it into a new skill, do use github 
copy to make a new reposotry that arent a fork.
