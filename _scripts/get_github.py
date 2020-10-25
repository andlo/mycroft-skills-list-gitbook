import requests
import json

from github import Github

def search_github():
    print('Searching Github...')
    ACCESS_TOKEN = '88eba3587d247eb8d789f1aebdd64ffcad9ce3c2'
    g = Github(ACCESS_TOKEN)
    query = "'Mycroft'in:readme+in:description+in:name+archived:false"
    #query = "'Lorensen'in:readme+archived:false"
    result = g.search_repositories(query)
    print(f'Found {result.totalCount} repo(s)')
    skills = []
    entry = {}
    proc = 0
    total = 0
    added = 0
    for line in result:
        print(proc)
        entry = g.get_repo(line.id).raw_data
        skills.append(entry)
        proc = proc +1
    return skills


repo = search_github()
repo_file = open('github.json', 'w')
repo_file.write(json.dumps(repo, ensure_ascii=False, indent=2))
repo_file.close()


