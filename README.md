### Quick start

# python 11
```` Shell
rm -rf bootstrap_venv.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/bootstrap_venv.sh
chmod ug+x bootstrap_venv.sh
toolforge jobs run bootstrap-venv --command "cd $PWD && ./bootstrap_venv.sh" --image python3.11 --wait

rm -rf py_311.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/py_311.sh
chmod ug+x py_311.sh
toolforge jobs run py311 --command "cd $PWD && ./py_311.sh" --image python3.11 --wait

````
# Extra
```` Shell

mv pyvenv/lib/python3.11/site-packages pyvenv/lib/python3.11/site-packages1 -v

cp -r local/lib/python3.11/site-packages pyvenv/lib/python3.11


mv local old_local -v
ln -s $HOME/pyvenv $HOME/local -v

````

# update packages
```` Shell
rm -rf shs/pips.sh
rm updatepips.err updatepips.out
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/pips.sh -O shs/pips.sh
chmod ug+x shs/pips.sh
toolforge jobs run updatepips --command "$HOME/shs/pips.sh" --image mariadb
toolforge jobs list
````

```` Shell
toolforge jobs delete install
rm -rf install.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/install.sh
chmod ug+x install.sh
# sh install.sh
toolforge jobs run install --mem 1Gi --command "$HOME/install.sh" --image mariadb
toolforge jobs list

````



