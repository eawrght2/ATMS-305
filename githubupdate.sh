#!/bin/bash

git fetch upstream
git checkout master
git merge upstream/master
SSH_ASKPASS=""
git add -A
git commit -m "updated"
git pull origin master
git push origin master
