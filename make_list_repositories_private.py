#!/usr/bin/env python

from __future__ import print_function
import requests

## https://stackoverflow.com/questions/68200480/github-api-get-private-repositories-of-user

token = '' ## added by hand
username = 'ryuikaneko'
headers = {'Authorization': 'token {}'.format(token)}
npage = 2 ## assume (#repositories)<=200
json_list = []
for page in range(1,npage+1):
    request = requests.get('https://api.github.com/user/repos?per_page=100&page='+'{}'.format(page)+'&visibility=all',headers=headers)
    json_items = request.json()
    #print(json_items)
    for i in range(len(json_items)):
#        json_list.append((json_items[i]['name'],json_items[i]['svn_url']))
        if json_items[i]['owner']['login'] == username:
            json_list.append((json_items[i]['name'],json_items[i]['svn_url']))
#print(json_list)

json_list = list(set(json_list)) ## unique
json_list = sorted(json_list) ## sort
#print(json_list)

print("---")
print("layout: default")
print("---")
print("")
print("# my repositories (both public and private)")
print("")
for i in range(len(json_list)):
    print("- [{}]".format(json_list[i][0]),end="")
    print("({})".format(json_list[i][1]))

## https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
##  GHUSER=ryuikaneko; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*'
##  GHUSER=ryuikaneko; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git'
##  GHUSER=ryuikaneko; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | sed 's/^/- /g'
##  https://github.com/darshanc99/Python-Scraps-WT-purpose-/blob/master/git.py

## [my memo]
## - public only
##   curl "https://api.github.com/users/ryuikaneko/repos?per_page=10000"
## - private and public
##   curl -H "Authorization: token [MYTOKEN]" "https://api.github.com/search/repositories?q=user:ryuikaneko&per_page=10000"

## https://stackoverflow.com/questions/13825278/python-request-with-authentication-access-token
