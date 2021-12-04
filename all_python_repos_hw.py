import json
import requests

url = 'https://api.github.com/users/GreatRaksin/repos'
response = requests.get(url)
repositories = json.loads(response.text)

repos = {

}
repo_count = 1

for repo in repositories:
    if repo['language'] == 'Python':
        name = repo['name']
        link = repo['svn_url']
        clone_url = repo['clone_url']
        created_at = repo['created_at']

        repos[f'repo_{repo_count}'] = {}
        repos[f'repo_{repo_count}']['name'] = name
        repos[f'repo_{repo_count}']['link'] = link
        repos[f'repo_{repo_count}']['clone_url'] = clone_url
        repos[f'repo_{repo_count}']['created_at'] = created_at

        repo_count += 1

with open('all_python_repos.json', 'w') as file:
    json.dump(repos, file)

