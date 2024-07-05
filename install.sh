!/bin/bash
cd $HOME

wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/bootstrap_venv.sh

chmod ug+x bootstrap_venv.sh

sh bootstrap_venv.sh

wget https://raw.githubusercontent.com/MrIbrahem/user-config/main/install_c8.sh

chmod ug+x ./install_c8.sh

sh ./install_c8.sh
