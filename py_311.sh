#!/bin/bash
cd $PWD

$HOME/local/bin/python3 -m pip freeze > last_req.txt

set -euo pipefail

# activate it
source pyvenv/bin/activate

# install some concrete packages
pip install -U requests packaging wikitextparser python-dateutil certifi gorilla gorilla-cli
# pip install -r requirements_new.txt
pip install -r c8/requirements.txt

pyvenv/bin/python3 -m pip list --outdated
python3 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 ./pyvenv/bin/pip install -U

echo 'export PATH=$HOME/local/bin:$HOME/local/bin:/usr/local/bin:/usr/bin:/bin' > ~/.bash_profile

# python3 -m pip install -r requirements_311.txt
python3 -m pip install -r last_req.txt
