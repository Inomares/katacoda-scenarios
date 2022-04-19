import os

import requests

PATH = "/root/build_logs"
os.makedirs(PATH, exist_ok=True)
commits = requests.get("https://api.github.com/repos/KTH/devops-course/commits?per_page=100").json()

for commit in commits:
    with open(f"{PATH}/{commit['sha']}", "w") as f:
        f.write(str(commit))
