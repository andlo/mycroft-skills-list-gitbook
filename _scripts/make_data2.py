import harvest
import requests
import json
import ast
from datetime import datetime
from pytz import timezone
import time

'''
Generates a json data with all skills found nby searching github. For every skill
skills info is added so endresult is a json data with all github info and skill find_title_info

skill info is same info as used my market, and added market status and evt. pending lables.

skill __init__.py is parsed ad checked by AST to check if it looks OK.

'''

# github username and password or place a token.txt with github token inside next to script
github_username = ''
github_password = ''
harvest.load_github()

GITHUB_API_URL = "https://api.github.com/search/repositories?q='Mycroft'in:readme+archived:false&per_page=100"

request = requests.get(
    "https://api.github.com/search/issues?q=repo:MycroftAI/mycroft-skills+state:open+type:pr&sort=created&order=asc").text
MARKET_PR = json.loads(request)

request = requests.get(
    'https://raw.githubusercontent.com/MycroftAI/mycroft-skills-data/18.08/skill-metadata.json').text
MARKET = json.loads(request)


def check_market(skill_name, skill_url):
    status = 'Not in Market'
    labels = []
    name = ""
    for item in MARKET:
        if MARKET[item]["repo"] == skill_url:
            status = "In Market"
            name = item
    for pull_request in MARKET_PR['items']:
        if pull_request['body'].find(skill_url) >= 0:
            if status == 'Not in Market':
                status = 'Pending Market'
            labels = ['PR-' + str(pull_request['number'])]
            for label in pull_request['labels']:
                labels.append(label['name'])
    return name, status, labels


def check_if_skill(repo_url, branch):
    init_py = None
    init_py_txt = None
    init_py = repo_url.replace(
        'https://github.com/', 'https://raw.githubusercontent.com/') + '/' + branch + '/__init__.py'
    init_py_txt = requests.get(init_py).text
    if init_py_txt.find("def create_skill():") is not -1 and init_py_txt.find("MycroftSkill") is not -1:
        return True
    else:
        return False


def check_source_code(repo_url, branch):
    init_py = None
    init_py_txt = None
    init_py = repo_url.replace(
        'https://github.com/', 'https://raw.githubusercontent.com/') + '/' + branch + '/__init__.py'
    init_py_txt = requests.get(init_py).text
    try:
        result = ast.parse(init_py_txt)
        return True
    except SyntaxError as exc:
        return False


def generate_entry(repo):
        readme_url = repo['html_url'].replace(
            'https://github.com/', 'https://raw.githubusercontent.com/') + '/' + repo["default_branch"] + '/README.md'
        readme_txt = requests.get(readme_url).text
        sections = harvest.extract_sections(readme_txt)
        title, short_desc = harvest.find_title_info(
            sections, repo['name'] + '.' + repo['owner']['login'])
        entry = {
                'repo': repo['html_url'],
                'branch': repo["default_branch"],
                'tree': repo["default_branch"],
                'name': title,
                'id': repo['name'] + '.' + repo['owner']['login'],
                'github_username': repo["owner"]["login"],
                'title': title,
                'short_desc': harvest.format_sentence(short_desc.replace('\n', ' ')).rstrip('.'),
                'description': harvest.format_sentence(harvest.find_section('About', sections) or
                                            harvest.find_section('Description', sections) or ''),
                'examples': [harvest.parse_example(i) for i in harvest.find_examples(sections)],
                'credits': harvest.make_credits((harvest.find_section('Credits', sections, 0.9)) or repo["owner"]["login"]),
                'categories': [
                    cat.replace('*', '') for cat in sorted((harvest.find_section('Category',
                                                            sections, 0.9) or '').split())],
                'platforms': (harvest.find_section('Supported Devices', sections, 0.9) or 'all').split(),
                'tags': (harvest.find_section('Tags', sections) or '').replace('#', '').split()
            }
        icon_url, icon_name, icon_color = harvest.find_icon(
            sections, repo['html_url'], repo["default_branch"])
        if icon_url:
            icon_url = icon_url.replace('https://rawgit.com/FortAwesome/Font-Awesome/master/advanced-options/raw-svg/solid/',
                                        'https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/')
            entry["icon_img"] = icon_url
        elif icon_name:
            entry["icon"] = {"icon": icon_name, "color": icon_color}
            entry["icon_img"] = "https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/" + icon_name + ".svg"

        market_status = check_market(repo['name'], repo['html_url'])
        if market_status[2] is not []:
            entry["market_pending"] = market_status[2]
        if market_status[1] is not 'Not in Market':
            entry["market_name"] = market_status[0]
            entry["market_url"] = 'https://market.mycroft.ai/skill/' + market_status[0]
        entry["market_status"] = market_status[1]
        entry['ast_passed'] = check_source_code(repo["html_url"], repo["default_branch"])
        repo['skill_info'] = entry
        entry = {
            'updated_at': str(datetime.now(timezone('UTC'))),
            'version': '1'
            }
        repo['skill_list'] = entry

        return repo


def search_github():
    skills = []
    proc = 1
    added = 1
    page = 1
    while page <= 10:
        request = requests.get(GITHUB_API_URL + "&page=" + str(page))
        result = json.loads(request.text)
        for repo in result["items"]:
            print("Processing " + str(proc) +"/" + str(result["total_count"]))
            if check_if_skill(repo["html_url"], repo["default_branch"]):
                skills.append(generate_entry(repo))
                print("Added " + repo['name'] + '.' + repo['owner']['login'])
                added = added + 1
            proc = proc +1
        page = page + 1
    ## Add if skill is in market but are missing from skillslist
    for item in MARKET:
        in_list = False
        for skill in skills:
            if MARKET[item]['repo'] != skill['html_url']:
                    in_list = True
        if in_list is False:
            request = requests.get('https://api.github.com/search/repositories?q=repo:' + MARKET[item]['repo'].replace('https://github.com/', ''))
            result = json.loads(request.text)
            for repo in result["items"]:
                skills.append(generate_entry(repo))
                print("Added from market " + MARKET[item]['name'])
                added = added + 1
            print("Added from market " + MARKET[item]['name'])
    return skills


skills = search_github()
skills_file = open('skills.json', 'w')
skills_file.write(json.dumps(skills, ensure_ascii=False, indent=2))
skills_file.close()

