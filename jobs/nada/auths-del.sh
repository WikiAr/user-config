#!/bin/bash
#set -euo pipefail
# toolforge jobs run cc --command "cd $PWD && ./jobs/auths-del.sh" --image python3.11 --wait

. "$HOME"/pyvenv/bin/activatex
# source pyvenv/bin/activate

export PYWIKIBOT_DIR="$HOME/core8"

# python3 $HOME/core8/pwb.py auths/del
python3 $HOME/bots/core1/auths/del.py

# deactivate

exit 0
