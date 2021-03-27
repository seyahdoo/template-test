import git
import re
import os

template_repository_url = "https://github.com/seyahdoo/template-test"

local_repo_url:str = git.Repo("./", search_parent_directories=True).remotes[0].url
if local_repo_url == template_repository_url:
    exit(1)
git_project_name = local_repo_url.split('/')[-1]

with open("processed_text.txt", "w") as text_file:
    text_file.write(f"{local_repo_url} {git_project_name} hello from on template script")

os.remove("on-template.py")
os.remove(".github/workflows/on-template.yml")

