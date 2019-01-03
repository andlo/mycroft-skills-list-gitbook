import io
import json

json_data = open('../_data/skills.json')
skills = json.load(json_data)

for skill in skills:
    of = open('../docs/skills/' + skill["name"] + '.' + skill["owner"]["login"] + '.md', 'w')
    img = ""
    if skill["skill_info"].get("icon"):
        if skill["skill_info"]["icon"].get("icon"):
            img = "<span style=font-size: 3em; color: " + skill["skill_info"]["icon"]["color"] + " ;margin-bottom: 0;><i class=fas fa-" + skill["skill_info"]["icon"]["icon"] + "></i></span>"
    elif skill["skill_info"].get("icon_img"):
        img = "<img src='" + skill["skill_info"]["icon_img"] + " height='50' style='vertical-align:bottom'/>&nbsp;&nbsp;"
    else:
        img = "<span style=font-size: 3em; color: lightgray ; margin-bottom: 0;><i class=fas fa-comment-alt></i></span>"
    of.write('---\n')
    of.write('titel: ' + skill["skill_info"]["title"] + '\n')
    of.write('description: ' + skill["skill_info"]["short_desc"] + '\n')
    of.write('---\n')
    of.write(skill["skill_info"]["description"] + '\n')
    of.close()