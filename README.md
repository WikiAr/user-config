### Quick start

```` Shell
rm -rf install.sh
wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/install.sh
chmod -R 6770 install.sh
# sh install.sh
toolforge jobs run install --mem 1Gi --command "$HOME/install.sh" --image mariadb
toolforge jobs list

````
