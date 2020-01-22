import io
import json
import urllib.request
from PIL import Image
from bs4 import BeautifulSoup
from markdown import markdown
import re


json_data = open('../_data/skills.json')
skillsdata = json.load(json_data)

def make_skillsfiles(skills):
    for skill in skills:
        txt = []
        txt.append('---    \n')
        #of.write('titel: ' + skill["skill_info"]["title"] + '\n')
        short_desc = clean_txt(skill["skill_info"]["short_desc"])
        txt.append('description: ' + short_desc + '  \n')
        txt.append('---    \n')
        if not skill["stargazers_count"] == 0: 
            for x in range(skill["stargazers_count"]):
                txt.append('![](../.gitbook/assets/star.png)')
            txt.append('  \n')               
        txt.append('# ' + skill["skill_info"]["name"] + '  \n')
        txt.append('### _' + skill["skill_info"]["id"] + '_  \n')
        
        #icon_img = '../img/' + skill["owner"]["login"] + '_icon.png'
        #get_img(skill["skill_info"]["icon_img"], icon_img)
        #resize_img(icon_img, 50)
        #txt.append(skill["skill_info"]["title"] + '\n\n')
        txt.append('## About:  \n')
        txt.append(skill["skill_info"]["description"] + '\n\n')
        #avatar = '../img/' + skill["owner"]["login"] + '_avatar.png'
        #avatar = get_img(skill["owner"]["avatar_url"], avatar)
        #resize_img(avatar, 50)
        
        txt.append('## Skill information:  \n')
        txt.append('**Github:** | [' + skill["html_url"] + ']' + '(' + skill["html_url"] + ')  \n') 
        txt.append('**Owner:** | [@' + skill["owner"]["login"] + 
                   '](' + skill["owner"]["html_url"] + 
                   ')  \n')
        txt.append('**Created:** | ' + nice_time(skill["created_at"]) + 
                   '  **Last updated:** ' + nice_time(skill["updated_at"]) + '  \n')
        

        try:
            txt.append('**License:** | ' + skill["license"]["name"] + '  \n')
            license = True
        except Exception:
            txt.append('**License:** | No License  \n')
            license = False
        try:
            txt.append('**Market status:** | ' + 
                       '[' + skill["skill_info"].get("market_status") + ']' +
                       '(' + skill["skill_info"]["market_url"] + ')')
            if skill["skill_info"]["market_status"] == 'In Market':
                market = True
            else:
                market = False
        except Exception:
            market = False
            pass
        if skill["skill_info"]["market_status"] == 'Pending Market':
            try:
                for label in skill["skill_info"]["market_pending"]:
                    txt.append(' ' + label)
            except Exception:
                pass
        txt.append('  \n')
        try:
            mk1 = ' ![](../.gitbook/assets/mark-1-icon.png) '
            mk2 = ' ![](../.gitbook/assets/mark-2-icon.png) '
            pi = ' ![](../.gitbook/assets/picroft-icon.png) '
            kde = ' ![](../.gitbook/assets/kde.png) '
            txt.append('**Platform:**  \n')
            for device in skill["skill_info"].get("platforms"):
                if device == 'all':
                    txt.append(mk1 + mk2 + pi + kde)
                if device == 'platform_mark1':
                    txt.append(mk1)
                if device == 'platform_mark2':
                    txt.append(mk2)
                if device == 'platform_plasmoid':
                    txt.append(kde)
                if device == 'platform_picroft':
                    txt.append(pi)
            txt.append('  \n')
            if not skill["skill_info"]["tags"] == []:
                txt.append('**Tags:** ')
                for tag in skill["skill_info"]["tags"]:
                    txt.append('\#' + tag + ' ')
                txt.append('  \n')
        except Exception:
            pass

        if not skill["skill_info"]["examples"] == []:
            txt.append('## Examples:  \n')
            for example in skill["skill_info"]["examples"]:
                txt.append('> ' + example + '  \n')
            txt.append('  \n')

        ast = skill["skill_info"]["ast_passed"]
        if not ast:
            txt.append('{% hint style="warning" %}\n')                
            txt.append('This skill Did not pass the Abstract Syntax Trees testing. Skill properly do not work in current state.\n')
            txt.append('{% endhint %}\n')
        if not license:
            txt.append('{% hint style="danger" %}\n')                
            txt.append('This skill dosnt have any license attatched. It is not adviasable to use this skill')
            txt.append('nor fork or clone, as you dont know if you are legaly allowed to do so by the auhtor.\n')
            txt.append('{% endhint %}\n')
        if market and license and ast:
            txt.append('{% hint style="info" %}\n')
            txt.append('This skill is in Mycroft Market. That means it is aproved by the Mycroft Skill testers\n')
            txt.append('{% endhint %}\n  ')
            txt.append('  \n')
            txt.append('## Installation:  \n')
            txt.append('{% tabs %}\n')
            txt.append('{% tab title="Install by voice" %}\n' + 
                       '> Hey Mycroft - install ' + skill["skill_info"]["name"] + '\n')
            txt.append('{% endtab %}\n  ')
            txt.append('{% tab title="Install by mycroft-msm" %}\n' + 
                       '``` mycroft-msm install ' + skill["skill_info"]["name"] + '```\n')
            txt.append('{% endtab %}\n  ')
            txt.append('{% endtabs %}\n  ')
        if not market and license and ast:
            txt.append('{% hint style="warning" %}\n')
            txt.append('This skill is not aproved by Mycroft skill tester.\n')
            txt.append('{% endhint %}\n  ')
            txt.append('  \n')
            txt.append('## Installation:  \n')
            txt.append('{% tabs %}\n')
            txt.append('{% tab title="Install by mycroft-msm" %}\n' + 
                       '``` mycroft-msm install ' + skill["html_url"] + '```\n')
            txt.append('{% endtab %}\n  ')
            txt.append('{% endtabs %}\n  ')

        skillfile = '../skills/' + skill["name"] + '.' + skill["owner"]["login"] + '.md' 
        of = open(skillfile, 'w')
        of.writelines(txt)
        of.close()


def nice_time(timestamp):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for c in ['T', 'Z', '-', ':']:
        timestamp = timestamp.replace(c, ' ')
    out = timestamp.split()
    out[1] = months[int(out[1]) - 1]
    return "{} {} {} {}:{}:{} UTC".format(*out)

  
def clean_txt(txt):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    result = re.sub(cleanr, '', txt)
    html = markdown(result)
    result =  ''.join(BeautifulSoup(html,features="html.parser").findAll(text=True))
    result = re.sub(r'http\S+', '', result)
    return result     

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
    return categorylist

def make_summary():
    summary = open('../SUMMARY.md', 'w')
    summary.write('# Table of contents\n')
    summary.write('* [Introduction](README.md)\n')
    summary.write('* [FAQ](FAQ.md)\n')
    summary.write('## Skills\n')


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

    summary.write('## Skill Writers\n')

make_summary()
make_skillsfiles(skillsdata)

print(len(skillsdata))
#resize_img('../.gitbook/assets/star.png', 30)


