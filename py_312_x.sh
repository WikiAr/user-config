#!/bin/bash
cd $HOME

# Download Python 3.12.3 from the Python website
if [ ! -f Python-3.12.3.tgz ]; then
    wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
fi

if [ ! -f Python-3.12.3.tgz ]; then
    echo "Unable to download the Python file. Please ensure your internet connection."
    exit 1
fi
# Extract the downloaded archive
tar xzf Python-3.12.3.tgz
rm Python-3.12.3.tgz

# Navigate to the extracted directory
cd Python-3.12.3

# Configure the build with optimizations and specify the installation prefix as the user's home directory
./configure --enable-optimizations --prefix=$HOME

# Build and install Python
make altinstall prefix=~/local12

# Remove the extracted Python directory
cd ../
rm -r -f Python-3.12.3

# Save the currently installed Python packages to a file named "requirements_new.txt"
pip freeze > requirements_new.txt

# Create a symbolic link to the Python 3.12 executable in the local12/bin directory
if [ -f "$HOME/local12/bin/python3.12" ]; then
    ln -s "$HOME/local12/bin/python3.12" "$HOME/local12/bin/python312"
    ln -s "$HOME/local12/bin/python3.12" "$HOME/local12/bin/python3"
    echo "Symbolic links created successfully."
else
    echo "Python 3.12 executable not found. Please make sure it's installed in $HOME/local12/bin."
fi

# Display the version of Python 3.12
./local12/bin/python3.12 -V

# Upgrade pip to the latest version
./local12/bin/python3.12 -m pip install --upgrade pip

# Install Gorilla
./local12/bin/python3.12 -m pip install packaging
./local12/bin/python3.12 -m pip install gorilla
./local12/bin/python3.12 -m pip install gorilla-cli

# Install the Python packages
./local12/bin/python3.12 -m pip install -r requirements_new.txt
./local12/bin/python3.12 -m pip install -r c8/requirements.txt

./local12/bin/python3.12 -m pip list --outdated
./local12/bin/python3.12 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 ./local12/bin/pip3.12 install -U


# Install packages
./local12/bin/python3.12 -m pip install wikitextparser
./local12/bin/python3.12 -m pip install python-dateutil
./local12/bin/python3.12 -m pip install certifi --upgrade
# ./local12/bin/python3.12 -m pip install --upgrade regex==2022.10.31


./local12/bin/python3.11 -m pip freeze > requirements_311.txt

./local12/bin/python3.12 -m pip install -r requirements_311.txt

# echo 'export PATH=$HOME/local12/bin:$HOME/local/bin:/usr/local/bin:/usr/bin:/bin' > ~/.bash_profile


ln -s /usr/bin/toolforge      $HOME/local12/bin/tf
ln -s /usr/bin/toolforge-jobs $HOME/local12/bin/tfj
ln -s /usr/bin/toolforge-webservice $HOME/local12/bin/tfw
