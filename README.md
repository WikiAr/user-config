### Quick start

# python 3.11.4
```` Shell
rm -rf py314.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/py314.sh
chmod ug+x py314.sh
toolforge jobs run py314 --command "cd $PWD && ./py314.sh" --image python3.11

./local/bin/python3 -V

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



# pyvenv
```` Shell
rm -rf bootstrap_venv.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/bootstrap_venv.sh
chmod ug+x bootstrap_venv.sh
toolforge jobs run bootstrap-venv --command "cd $PWD && ./bootstrap_venv.sh" --image python3.11 --wait


mv pyvenv/lib/python3.11/site-packages pyvenv/lib/python3.11/site-packages1 -v

cp -r local/lib/python3.11/site-packages pyvenv/lib/python3.11
s
mv local old_local -v
ln -s $HOME/pyvenv $HOME/local -v


````
