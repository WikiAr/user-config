#!/bin/bash

python3 -m pip freeze > last_req.txt

# activate it
source pyvenv/bin/activate

# install some concrete packages
pip install -U requests packaging wikitextparser python-dateutil certifi gorilla gorilla-cli
pip install -r requirements_new.txt
pip install -r c8/requirements.txt

python3 -m pip list --outdated
python3 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 ./pyvenv/bin/pip311 install -U

echo 'export PATH=$HOME/pyvenv/bin:$HOME/pyvenv/bin:/usr/pyvenv/bin:/usr/bin:/bin' > ~/.bash_profile

python3 -m pip install -r requirements_311.txt
python3 -m pip install -r last_req.txt

# echo 'export PATH=$HOME/pyvenv/bin:$HOME/pyvenv/bin:/usr/pyvenv/bin:/usr/bin:/bin' > ~/.bash_profile

ln -s /usr/bin/toolforge      $HOME/pyvenv/bin/tf
ln -s /usr/bin/toolforge-jobs $HOME/pyvenv/bin/tfj
ln -s /usr/bin/toolforge-webservice $HOME/pyvenv/bin/tfw
