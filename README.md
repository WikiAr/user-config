### Quick start

```` Shell
toolforge jobs delete install
rm -rf install.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/install.sh
chmod -R 6770 install.sh
# sh install.sh
toolforge jobs run install --mem 1Gi --command "$HOME/install.sh" --image mariadb
toolforge jobs list

````
# only python 11
```` Shell
rm -rf py_3114_x.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/py_3114_x.sh
chmod -R 6770 py_3114_x.sh
# sh py_3114_x.sh
toolforge jobs run installpy11 --mem 1Gi --command "$HOME/py_3114_x.sh" --image mariadb
toolforge jobs list

````
