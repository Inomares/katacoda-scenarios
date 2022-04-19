import os

import requests

PATH = "/root/build_logs"
os.makedirs(PATH, exist_ok=True)
try:
    commits = requests.get("https://api.github.com/repos/KTH/devops-course/commits?per_page=100").json()
except: # in case of github's api changing or network error etc
    commits = [{'sha': '9a59d3e51333948c58688a275799b5676fe957a3', 'node_id': 'C_kwDOB9ujYNoAKDlhNTlkM2U1MTMzMzk0OGM1ODY4OGEyNzU3OTliNTY3NmZlOTU3YTM', 'commit': {'author': {'name': 'Martin Monperrus', 'email': 'martin.monperrus@gnieh.org', 'date': '2022-04-18T19:32:31Z'}, 'committer': {'name': 'GitHub', 'email': 'noreply@github.com', 'date': '2022-04-18T19:32:31Z'}, 'message': 'Update README.md', 'tree': {'sha': '1130fb4cb7aff192efb4db6f6b22b4e1f2fc5602', 'url': 'https://api.github.com/repos/KTH/devops-course/git/trees/1130fb4cb7aff192efb4db6f6b22b4e1f2fc5602'}, 'url': 'https://api.github.com/repos/KTH/devops-course/git/commits/9a59d3e51333948c58688a275799b5676fe957a3', 'comment_count': 0, 'verification': {'verified': True, 'reason': 'valid', 'signature': '-----BEGIN PGP SIGNATURE-----\n\nwsBcBAABCAAQBQJiXbzPCRBK7hj4Ov3rIwAA9nMIACLNRpyE7yyqL1jsJfQ+x1B3\nkg4NTI2OWch6OgSR9fb0S2V8UyDKvTzLB+U/LBalOprOv00AzKX5WPUWC11dNHkw\n9sALAxYDUasdYERBz+YphL1+6G2slMpBt1T5ynWNQHmJWEO0lxbaSTZ1YMZLiVne\nkz9bQfsWGrLWJq1BrFdEZNm80FDCl3li7agHnhWO/1YgrPqELO17XlQlQtVZDQi/\n7fs80upTkvvILWouhsUoCxBT0SQA6lWgWIP/V1grDfMk4mmCtA3tuBFEGQPlptky\nefM/3PPJ3GjxW3OdAorrug5hsVaK77IYtBHZ6X9VYZ6An622IVrUP6Xtc8Q+JPw=\n=ABoD\n-----END PGP SIGNATURE-----\n', 'payload': 'tree 1130fb4cb7aff192efb4db6f6b22b4e1f2fc5602\nparent 3b884f0cf568cbacd637496de16c785c190f3545\nauthor Martin Monperrus <martin.monperrus@gnieh.org> 1650310351 +0000\ncommitter GitHub <noreply@github.com> 1650310351 +0000\n\nUpdate README.md'}}, 'url': 'https://api.github.com/repos/KTH/devops-course/commits/9a59d3e51333948c58688a275799b5676fe957a3', 'html_url': 'https://github.com/KTH/devops-course/commit/9a59d3e51333948c58688a275799b5676fe957a3', 'comments_url': 'https://api.github.com/repos/KTH/devops-course/commits/9a59d3e51333948c58688a275799b5676fe957a3/comments', 'author': {'login': 'monperrus', 'id': 803666, 'node_id': 'MDQ6VXNlcjgwMzY2Ng==', 'avatar_url': 'https://avatars.githubusercontent.com/u/803666?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/monperrus', 'html_url': 'https://github.com/monperrus', 'followers_url': 'https://api.github.com/users/monperrus/followers', 'following_url': 'https://api.github.com/users/monperrus/following{/other_user}', 'gists_url': 'https://api.github.com/users/monperrus/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/monperrus/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/monperrus/subscriptions', 'organizations_url': 'https://api.github.com/users/monperrus/orgs', 'repos_url': 'https://api.github.com/users/monperrus/repos', 'events_url': 'https://api.github.com/users/monperrus/events{/privacy}', 'received_events_url': 'https://api.github.com/users/monperrus/received_events', 'type': 'User', 'site_admin': False}, 'committer': {'login': 'web-flow', 'id': 19864447, 'node_id': 'MDQ6VXNlcjE5ODY0NDQ3', 'avatar_url': 'https://avatars.githubusercontent.com/u/19864447?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/web-flow', 'html_url': 'https://github.com/web-flow', 'followers_url': 'https://api.github.com/users/web-flow/followers', 'following_url': 'https://api.github.com/users/web-flow/following{/other_user}', 'gists_url': 'https://api.github.com/users/web-flow/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/web-flow/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/web-flow/subscriptions', 'organizations_url': 'https://api.github.com/users/web-flow/orgs', 'repos_url': 'https://api.github.com/users/web-flow/repos', 'events_url': 'https://api.github.com/users/web-flow/events{/privacy}', 'received_events_url': 'https://api.github.com/users/web-flow/received_events', 'type': 'User', 'site_admin': False}, 'parents': [{'sha': '3b884f0cf568cbacd637496de16c785c190f3545', 'url': 'https://api.github.com/repos/KTH/devops-course/commits/3b884f0cf568cbacd637496de16c785c190f3545', 'html_url': 'https://github.com/KTH/devops-course/commit/3b884f0cf568cbacd637496de16c785c190f3545'}]}]

for commit in commits:
    with open(f"{PATH}/{commit['sha']}", "w") as f:
        f.write(str(commit))
