#!/bin/bash
export PATH=$PATH:/data/project/mdwiki/local/bin:/usr/local/bin:/usr/bin:/bin

cd $HOME

pip list --outdated

python3 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip3 install -U
