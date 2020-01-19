import io
import json

json_data = open('../_data/skills.json')
skillsdata = json.load(json_data)

def make_skillsfiles(skills):
    categorylist = {}
    for skill in skills:
        skillfile = '../skills/' + skill["name"] + '.' + skill["owner"]["login"] + '.md' 
        of = open(skillfile, 'w')
        of.write('---\n')
        of.write('titel: ' + skill["skill_info"]["title"] + '\n')
        of.write('description: ' + skill["skill_info"]["short_desc"] + '\n')
        of.write('---\n')
        of.write(skill["skill_info"]["description"] + '\n')
        of.close()

def make_categorylist(skills):
    categorylist = {}
    for skill in skills:
        skillfile = 'skills/' + skill["name"] + '.' + skill["owner"]["login"] + '.md' 
        if not skill["skill_info"].get("categories"):
            skill["skill_info"]["categories"] = ['uncategorized']
        for category in skill["skill_info"]["categories"]:
            text = "    * [" + skill["skill_info"]["title"] + "](" + skillfile + ")\n"
            #print(category)
            categoryitem = [text]
            if categorylist.get(category):
                #print(category)
                cat =  categorylist.get(category)
                cat.append(text)
                #print(cat)
                #print(cat.append(categoryitem))
                categorylist[category] = cat
            else:
                categorylist[category] = categoryitem
    categories_pop = []
    for category in categorylist:
        if len(categorylist[category]) is 1:
            cat =  categorylist.get('uncategorized')
            cat.append(text)
            categorylist['uncategorized'] = cat
            categories_pop.append(category)
    for cat in categories_pop:
        categorylist.pop(cat)
    #catfile = open('categories.json', 'w')
    #catfile.write(json.dumps(categorylist, ensure_ascii=False, indent=2))
    #catfile.close()
    return categorylist

summary = open('../SUMMARY.md', 'w')
summary.write('# Table of contents\n')
summary.write('* [Introduction](README.md)\n')
summary.write('* [FAQ](FAQ.md)\n')
summary.write('## Skills\n')

make_skillsfiles(skillsdata)

skillslist = []
summary.write('[In Market]\n')
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'In Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])
summary.write('[Pending Market]\n')
skillslist = []
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'Pending Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])
summary.write('[Not in Market]\n')
skillslist = []
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'Not in Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])





#make_categorylist()

