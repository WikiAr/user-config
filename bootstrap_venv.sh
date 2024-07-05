#!/bin/bash
# toolforge jobs run bootstrapvenv --command "cd $PWD && ./jobs/bootstrap_venv.sh" --image python3.11 --wait

$HOME/local/bin/python3 -m pip freeze > last_req.txt

# use bash strict mode
set -euo pipefail

# delete the venv, if it already exists
rm -rf pyvenv

# create the venv
/usr/bin/python3 -m venv pyvenv
# --copies

# activate it
source pyvenv/bin/activate

# upgrade pip inside the venv and add support for the wheel package format
pip install -U pip wheel

# install some concrete packages
pip install -U requests packaging wikitextparser python-dateutil certifi gorilla gorilla-cli
# pip install -r requirements_new.txt
pip install -r c8/requirements.txt

# python3 -m pip install -r requirements_311.txt
python3 -m pip install -r last_req.txt
