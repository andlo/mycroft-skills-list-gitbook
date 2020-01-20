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
        #of.write('titel: ' + skill["skill_info"]["title"] + '\n')
        of.write('description: ' + skill["skill_info"]["short_desc"] + '\n')
        of.write('---\n')
        of.write(skill["skill_info"]["description"] + '\n\n')
        of.write('**Github:** (' + skill["html_url"] + ')\n\n') 
        of.write('**Owner:** [@' + skill["owner"]["login"] + 
                 '](' + skill["owner"]["html_url"] + 
                 ') ![avatart](' + skill["owner"]["avatar_url"] + 
                 ')\n\n')
        of.close()

"""
 <p>Github: <a href='{{ skill.html_url }}'>{{ skill.html_url }}</a> </p>
    <p>Owner: <a href='{{ skill.owner.html_url }}'>@{{ skill.owner.login }}  <img src='{{ skill.owner.avatar_url }}' width='20' style='vertical-align:bottom'/></a></p>
    <p>Created: {{ skill.created_at | date_to_string }}    Updated: {{ skill.updated_at | date_to_string }} </p>
    {% if skill.license.size >= 1 %}
    <p>License: {{ skill.license.name }} </p>
    {% endif %}
    {% if skill.skill_info.market_status == 'In Market' %}
    <p>Market status: <a href='{{ skill.skill_info.market_url }}'>{{ skill.skill_info.market_status }}</a></p>
    {% endif %}
    {% if skill.skill_info.market_status == 'Not in Market' %}
    <p>Market status: {{ skill.skill_info.market_status }} </p>
    {% endif %}
    {% if skill.skill_info.market_status == 'Pending Market' %}
    <p>Market status: Pending
        {% if skill.skill_info.market_pending.size >= 1 %}
           {% for label in skill.skill_info.market_pending %} [{{ label  }}] {% endfor %}
        {% endif %}
    </p>
    {% endif %}
   
""" 
   

"""
{% for skill in site.data.skills %}
{% if skill.skill_info.icon.size >= 1  %}
    <span style="font-size: 3em; color: {{ skill.skill_info.icon.color }} ;margin-bottom: 0;">
    <i class="fas fa-{{ skill.skill_info.icon.icon }}"></i>
    </span>
{% else %}
    {% if skill.skill_info.icon_img.size >= 1 %}
    <img src='{{ skill.skill_info.icon_img }}' height='50' style='vertical-align:bottom'/>&nbsp;&nbsp;
    {% else %}
    <span style="font-size: 3em; color: lightgray ; margin-bottom: 0;">
    <i class="fas fa-comment-alt"></i>
    </span>
    {% endif %}
{% endif %}
{% if skill.skill_info.title != "" %}
    <span style="font-size: 2.3em; margin-bottom: 0;">{{ skill.skill_info.title }}<br></span>
{% else %}
    <span style="font-size: 2.3em; margin-bottom: 0;">{{ skill.name }}<br></span>
{% endif %}
{% if skill.skill_info.short_desc != "" %}
    <span style="font-size: 1.5em; margin-bottom: 0; margin-top: 0;">{{ skill.skill_info.short_desc }}<br></span>
{% else %}
    {% if skill.description != "" or skill.description != null %}
        <span style="font-size: 1.5em; margin-bottom: 0; margin-top: 0;">{{ skill.description }}<br></span>
    {% endif %}
{% endif %}
<div class="skill-info">
    {% if skill.skill_info.categories.size >= 1 %}
    <p>Category: {% for category in skill.skill_info.categories %} [{{ category  }}] {% endfor %}</p>
    {% endif %}
    <p>Github: <a href='{{ skill.html_url }}'>{{ skill.html_url }}</a> </p>
    <p>Owner: <a href='{{ skill.owner.html_url }}'>@{{ skill.owner.login }}  <img src='{{ skill.owner.avatar_url }}' width='20' style='vertical-align:bottom'/></a></p>
    <p>Created: {{ skill.created_at | date_to_string }}    Updated: {{ skill.updated_at | date_to_string }} </p>
    {% if skill.license.size >= 1 %}
    <p>License: {{ skill.license.name }} </p>
    {% endif %}
    {% if skill.skill_info.market_status == 'In Market' %}
    <p>Market status: <a href='{{ skill.skill_info.market_url }}'>{{ skill.skill_info.market_status }}</a></p>
    {% endif %}
    {% if skill.skill_info.market_status == 'Not in Market' %}
    <p>Market status: {{ skill.skill_info.market_status }} </p>
    {% endif %}
    {% if skill.skill_info.market_status == 'Pending Market' %}
    <p>Market status: Pending
        {% if skill.skill_info.market_pending.size >= 1 %}
           {% for label in skill.skill_info.market_pending %} [{{ label  }}] {% endfor %}
        {% endif %}
    </p>
    {% endif %}
    {% if skill.skill_info.platforms.size >= 1 %}
    <p>Platforms:
        {% for device in skill.skill_info.platforms %}
            {% if device == 'all' %}<img src='images/mark-1-icon.png' style='vertical-align:top'> <img src='images/mark-2-icon.png' style='vertical-align:top'> <img src='images/picroft-icon.png' style='vertical-align:top'> <img src='images/kde.png' style='vertical-align:top'>{% endif %}
            {% if device == 'platform_mark1' %} <img src='images/mark-1-icon.png' style='vertical-align:top'> {% endif %} {% if device == 'platform_mark2' %} <img src='images/mark-2-icon.png'> {% endif %}
            {% if device == 'platform_picroft' %} <img src='images/picroft-icon.png' style='vertical-align:top'> {% endif %}
            {% if device == 'platform_plasmoid' %} <img src='images/kde.png' style='vertical-align:top'> {% endif %}
        {% endfor %}
    </p>
    {% endif %}
    {% if skill.skill_info.ast_passed != true %}
    <p>AST: Did not pass the Abstract Syntax Trees testing. Skill properly do not work in current state. </p>
    {% endif %}
</div>
{% endfor %}
</div>
"""

"""
from PIL import Image

basewidth = 300
img = Image.open('somepic.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('sompic.jpg') 
"""


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
summary.write('* In Market\n')
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'In Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])
summary.write('* Pending Market\n')
skillslist = []
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'Pending Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])
summary.write('* Not in Market\n')
skillslist = []
for skill in skillsdata:
    if skill["skill_info"].get("market_status") == 'Not in Market':
        skillslist.append(skill)
categorylist = make_categorylist(skillslist)
for category in categorylist:
    summary.write('  * ' + category + '\n')
    summary.writelines(categorylist[category])


print(len(skillsdata))


#make_categorylist()

