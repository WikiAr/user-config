#!/bin/bash

# use bash strict mode
set -euo pipefail

# delete the venv, if it already exists
rm -rf pyvenv

# create the venv
/usr/bin/python3 -m venv pyvenv --copies

# activate it
source pyvenv/bin/activate

# upgrade pip inside the venv and add support for the wheel package format
pip install -U pip wheel

# install some concrete packages
pip install requests packaging wikitextparser python-dateutil certifi --upgrade
