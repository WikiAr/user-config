#!/bin/bash
export PATH=$PATH:/data/project/mdwiki/local/bin:/usr/local/bin:/usr/bin:/bin

cd $HOME

pip3 list --outdated

$HOME/local/bin/python3.11 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 $HOME/local/bin/pip3 install -U
