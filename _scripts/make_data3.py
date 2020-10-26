import requests
import json
import ast
from datetime import datetime
from pytz import timezone
import time
import re

from github import Github
from os.path import isfile

from collections import OrderedDict
from typing import Optional
from difflib import SequenceMatcher
import urllib.parse

'''
Generates a json data with all skills found nby searching github. For every skill
skills info is added so endresult is a json data with all github info and skill find_title_info

skill info is same info as used my market, and added market status and evt. pending lables.

skill __init__.py is parsed ad checked by AST to check if it looks OK.

'''
ACCESS_TOKEN = '88eba3587d247eb8d789f1aebdd64ffcad9ce3c2'

request = requests.get(
    "https://api.github.com/search/issues?q=repo:MycroftAI/mycroft-skills+state:open+type:pr&sort=created&order=asc").text
MARKET_PR = json.loads(request)

request = requests.get(
    'https://raw.githubusercontent.com/MycroftAI/mycroft-skills-data/19.08/skill-metadata.json').text
MARKET = json.loads(request)


def check_market(skill_name, skill_url):
    """ Checks ifa skill is in market  """
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
    """ Checks if a repo has __init__.py and it has def create_skill() inside """
    init_py = None
    init_py_txt = None
    init_py = repo_url.replace(
        'https://github.com/', 'https://raw.githubusercontent.com/') + '/' + branch + '/__init__.py'
    init_py_txt = requests.get(init_py).text
    if init_py_txt.find("def create_skill():") is not -1:
        return True
    else:
        return False

def check_source_code(repo_url, branch):
    """ Checks quality of code using ast """
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
    """ Generate an skil-repo entry """
    readme_url = repo['html_url'].replace(
        'https://github.com/', 'https://raw.githubusercontent.com/') + '/' + repo["default_branch"] + '/README.md'
    readme_txt = requests.get(readme_url).text
    sections = extract_sections(readme_txt)
    title, short_desc = find_title_info(
        sections, repo['name'] + '.' + repo['owner']['login'])
    entry = {
            'repo': repo['html_url'],
            'branch': repo["default_branch"],
            'tree': repo["default_branch"],
            'name': title,
            'id': repo['name'] + '.' + repo['owner']['login'],
            'github_username': repo["owner"]["login"],
            'title': title,
            'short_desc': cleanhtml(format_sentence(short_desc.replace('\n', ' ')).rstrip('.')),
            'description': cleanhtml(format_sentence(find_section('About', sections) or
                                        find_section('Description', sections) or '')),
            'examples': [parse_example(i) for i in find_examples(sections)],
            'credits': make_credits((find_section('Credits', sections, 0.9)) or repo["owner"]["login"]),
            'categories': [
                cat.replace('*', '') for cat in sorted((find_section('Category',
                                                        sections, 0.9) or '').split())],
            'platforms': (find_section('Supported Devices', sections, 0.9) or 'all').split(),
            'tags': (find_section('Tags', sections) or '').replace('#', '').split()
        }
    icon_url, icon_name, icon_color = find_icon(
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


def extract_sections(readme_content: str) -> OrderedDict:
    """ Extracts sections from README.MD """
    last_section = ''
    sections = OrderedDict({last_section: ''})
    for line in readme_content.split('\n'):
        line = line.strip()
        if line.startswith('# ') or line.startswith('## '):
            last_section = line.strip('# ')
            sections[last_section] = ''
        else:
            sections[last_section] += '\n' + line
    for section_name in list(sections):
        sections[section_name] = sections[section_name].strip()
    sections[''] = sections.pop('')  # Shift to end
    return sections

def format_sentence(s: str) -> str:
    """ 'this is a test' -> 'This is a test.' """
    s = caps(s)
    if s and s[-1].isalnum():
        return s + '.'
    return s

def find_title_info(sections: dict, skill_name: str) -> tuple:
    """ Get title from the section with an icon """
    title_section = None
    for section in sections:
        if "<img" in section:
            title_section = section
            break
    if not title_section:
        # Attempt old scheme - first section header is the title
        title_section = next(iter(sections))
        return title_section, ""   # Should never be allowed in repo!

    # Remove traces of any <img> tag that might exist, get text that follows
    title = title_section.split("/>")[-1].strip()
    short_desc = sections[title_section]
    return title, short_desc

def find_icon(sections: dict, repo: str, tree: str) -> tuple:
    """ Get first section's title (icon is in the title itself), like:
        <img src='https://rawgi...' card_color='maroon' height='50'/> Skill Name
        Get first section's title """

    # Get section name with the icon
    title_section = None
    for section in sections:
        if "<img" in section:
            title_section = section
            break
    if not title_section:
        return None, None, None

    url = None
    name = None
    color = None
    prev = ''
    for part in title_section.split("'"):
        part = part.strip()
        if prev.endswith("src="):
            url = part
        elif prev.endswith("card_color="):
            color = part
        prev = part

    # Check if URL is a Font Awesome preview image
    if url and url.startswith("https://rawgithub.com/FortAwesome/Font-Awesome"):
        # Break down down just the filename part, e.g.
        #   "https://rawgithub...vg/solid/microchip.svg" -> "microchip"
        name = url.split('/')[-1].split(".")[0]
        url = None
    elif url:
        if not urllib.parse.urlparse(url).netloc:
            # Assume this is a local reference, expand it to a full-path
            url = (repo.replace("github.com", "raw.githubusercontent.com") +
                   '/' + tree + '/' + url)

    return url, name, color

def find_section(name: str, sections: dict,
                 min_conf: float = 0.5) -> Optional[str]:
    """ Return the section with heading that matches `name` most closely """
    title, conf = max([(title, compare(title, name)) for title in sections],
                      key=lambda x: x[1])

    return None if conf < min_conf else sections[title]

def find_examples(sections: dict) -> list:
    """
    Example: {'Examples': ' - "Hey Mycroft, how are you?"\n - "Hey Mycroft, perform test" <<< Does a test'}  # nopep8
    Returns: ['How are you?', 'Perform test.']
    """
    return re.findall(
        string=(find_section('examples', sections) or
                find_section('usage', sections) or ''),
        pattern=r'(?<=[-*]).*', flags=re.MULTILINE
    )

def make_credits(lines: str) -> list:
    """ Convert multiline credits into list
        Ex: @acmcgee\nMycroftAI (@MycroftAI)\nTom's great songs """
    result = []
    for line in lines.splitlines():
        words = []
        username = None
        for word in line.split():
            word = word.strip("()")
            if word.startswith("@"):
                username = word[1:]
            else:
                words.append(word)
        if words and username:
            result.append({"name": " ".join(words),
                           "github_id": username})
        elif words:
            result.append({"name": " ".join(words)})
        elif username:
            result.append({"github_id": username})

    return result


def parse_example(example: str) -> str:
    """ "hey mycroft, what is this" -> What is this? """
    example = example.strip(' \n"\'`')
    example = re.split(r'["`]', example)[0]

    # Remove "Hey Mycroft, "
    for prefix in ['hey mycroft', 'mycroft', 'hey-mycroft']:
        if example.lower().startswith(prefix):
            example = example[len(prefix):]
    example = example.strip(' ,')  # Fix ", " from "Hey Mycroft, ..."
    if any(
            example.lower().startswith(word + suffix + ' ')
            for word in ['who', 'what', 'when', 'where']
            for suffix in ["'s", "s", "", "'d", "d" "'re", "re"]
    ):
        example = example.rstrip('?.') + '?'
    example = format_sentence(example)
    return example


def caps(s: str) -> str:
    """ Capitalize first letter without lowercasing the rest"""
    return s[:1].upper() + s[1:]

def compare(a: str, b: str) -> float:
    """ compare str a with b """
    return SequenceMatcher(a=a.lower(), b=b.lower()).ratio()


def norm(x: str) -> str:
    """ Normalize str"""
    return x.lower().replace('-', ' ')


def search_github():
    if not isfile('github.json'):
        print('Searching Github...')
        github_tokenfile = open("demofile.txt", "r")
        GITHUB_TOKEN = github_tokenfile.read()
        daterange = ['<2015-01-01',
                '2015-01-01..2018-01-01', 
                '2018-01-01..2019-01-01', 
                '2019-01-01..2020-01-01', 
                '>2020-01-01']
        skills = []
        total = 0
        added = 0
        page = 1

        for date in daterange:
            proc = 1
            page = 0
            print('Daterange: ' + date)
            GITHUB_API_URL = "https://api.github.com/search/repositories?q='Mycroft'in:readme+'Mycroft'in:description+'Mycroft'in:name+archived:false+created:" + date
            request = requests.get(GITHUB_API_URL + '&per_page=100&page=0', headers={ 'Authorization': 'Bearer ' + GITHUB_TOKEN'})
            result = request.json()
            for item in result['items']:
                skills.append(item)
                total = total +1
            while 'next' in request.links.keys():
                request=requests.get(request.links['next']['url'],headers={"Authorization": 'Bearer ef77171c9449656ca7bfb3bfe082ef2238e5b102'})
                result = request.json()
                for item in result['items']:
                    skills.append(item)
                    total = total +1
        print('total ' + str(len(skills)))
        repo_file = open('github.json', 'w')
        repo_file.write(json.dumps(skills, ensure_ascii=False, indent=2))
        repo_file.close()
        print('Total git repos: ' + str(total))

    print('Processing Github repos...')
    result = []
    f = open('github.json')
    result = json.load(f)
    skills = []
    proc = 0
    total = 0
    added = 0
    for repo in result:
        print("Processing " + str(proc) +"/" + str(len(result)) + " ")
        # + repo['full_name'])
        if check_if_skill(repo['html_url'], repo['default_branch']):
            skills.append(generate_entry(repo))
            print("Added " + repo['name'] + '.' + repo['owner']['login'] + ' Total: ' + str(len(skills)))
            added = added + 1
            total = total +1
        proc = proc +1
    return skills
    
 
def cleanhtml(raw_html):
  # cleanr = re.compile('<.*?>')
  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

skills = search_github()
skills_file = open('skills.json', 'w')
skills_file.write(json.dumps(skills, ensure_ascii=False, indent=2))
skills_file.close()

