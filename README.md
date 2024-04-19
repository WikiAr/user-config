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
wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/py_3114_x.sh
chmod -R 6770 py_3114_x.sh
# sh py_3114_x.sh
toolforge jobs run installpy11 --mem 1Gi --command "$HOME/py_3114_x.sh" --image mariadb
toolforge jobs list

````


# only python 12
```` Shell
rm -rf py_312_x.sh
wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/py_312_x.sh
chmod -R 6770 py_312_x.sh
# sh py_312_x.sh
toolforge jobs run installpy11 --mem 1Gi --command "$HOME/py_312_x.sh" --image mariadb
toolforge jobs list

````




