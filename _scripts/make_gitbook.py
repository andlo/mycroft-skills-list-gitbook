import io
import json
import urllib.request
from PIL import Image

json_data = open('../_data/skills.json')
skillsdata = json.load(json_data)

def make_skillsfiles(skills):
    for skill in skills:
        txt = []
        txt.append('---\n')
        #of.write('titel: ' + skill["skill_info"]["title"] + '\n')
        txt.append('description: ' + skill["skill_info"]["short_desc"] + '\n')
        txt.append('---\n')
        
        #icon_img = '../img/' + skill["owner"]["login"] + '_icon.png'
        #get_img(skill["skill_info"]["icon_img"], icon_img)
        #resize_img(icon_img, 50)
        txt.append(skill["skill_info"]["title"] + '\n\n')
        txt.append(skill["skill_info"]["description"] + '\n\n')
        #avatar = '../img/' + skill["owner"]["login"] + '_avatar.png'
        #avatar = get_img(skill["owner"]["avatar_url"], avatar)
        #resize_img(avatar, 50)

        txt.append('**Github:** | (' + skill["html_url"] + ')  \n') 
        txt.append('**Owner:** | [@' + skill["owner"]["login"] + 
                   '](' + skill["owner"]["html_url"] + 
                   ')  \n')
        txt.append('**Created:** | ' + skill["created_at"] + 
                   '  **Last updated:** ' + skill["updated_at"] + '  \n')
        

        try:
            txt.append('**License:** | [' + skill["license"]["name"] + '](' +
                       skill["license"]["url"] + ')  \n')
        except Exception:
            txt.append('**License:** | No License - dont use this skill !  \n')
        try:
            txt.append('**Market status:** | ' + 
                       '[' + skill["skill_info"].get("market_status") + ']' +
                       '(' + skill["skill_info"]["market_url"] + ')')
        except Exception:
            pass
        try:
            for label in skill["skill_info"]["market_pending"]:
                txt.append(' ' + label)
        except Exception:
            pass
        txt.append('  \n')
        try:
            mk1 = ' ![.gitbook/assets/mark-1-icon.png] '
            mk2 = ' ![.gitbook/assets/mark-2-icon.png] '
            pi = ' ![.gitbook/assets/picroft-icon.png] '
            kde = ' ![.gitbook/assets/kde.png]'
            for device in skill["skill_info"].get("platforms"):
                if device == 'all':
                    txt.append(mk1 + mk2 + pi + kde)
                if device == 'platform_mark1':
                    txt.append(mk1)
                if device == 'platform_mark2':
                    txt.append(mk2)
                if device == 'platform_plasmoid':
                    txt.append(kde)
            txt.append('  \n')
        except Exception:
            pass
        

        
        skillfile = '../skills/' + skill["name"] + '.' + skill["owner"]["login"] + '.md' 
        of = open(skillfile, 'w')
        of.writelines(txt)
        of.close()

def get_img(url, filename):
        print(url)
        result = urllib.request.urlretrieve(url, filename)

def resize_img(imgfile, size):
    print(imgfile)
        
    basewidth = size
    img = Image.open(imgfile)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(imgfile) 

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

