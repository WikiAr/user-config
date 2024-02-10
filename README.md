### Quick start

```` Shell
rm -rf install.sh
wget https://github.com/MrIbrahem/user-config/blob/main/install.sh
chmod -R 6770 install.sh
# sh install.sh
toolforge jobs run install --mem 1Gi --command "$HOME/install.sh" --image mariadb
toolforge list
````
