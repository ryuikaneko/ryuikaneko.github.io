#!/usr/bin/env python

from __future__ import print_function
import requests

username = 'ryuikaneko'
request = requests.get('https://api.github.com/users/'+username+'/repos?per_page=1000')
json = request.json()

print("---")
print("layout: default")
print("---")
print("")
print("# my repositories")
print("")
for i in range(len(json)):
    print("- [{}]".format(json[i]['name']),end="")
    print("({})".format(json[i]['svn_url']))

## https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
##  GHUSER=ryuikaneko; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*'
##  GHUSER=ryuikaneko; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git'
##  GHUSER=ryuikaneko; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git' | sed 's/^/- /g'
##  https://github.com/darshanc99/Python-Scraps-WT-purpose-/blob/master/git.py
