#!/bin/bash
cd $HOME

# Download Python 3.11.4 from the Python website
if [ ! -f Python-3.11.4.tgz ]; then
    wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
fi

if [ ! -f Python-3.11.4.tgz ]; then
    echo "Unable to download the Python file. Please ensure your internet connection."
    exit 1
fi
# Extract the downloaded archive
tar xzf Python-3.11.4.tgz
rm Python-3.11.4.tgz

# Navigate to the extracted directory
cd Python-3.11.4

# Configure the build with optimizations and specify the installation prefix as the user's home directory
./configure --enable-optimizations --prefix=$HOME

# Build and install Python
make altinstall prefix=~/localx

# Remove the extracted Python directory
cd ../
rm -r -f Python-3.11.4

# Save the currently installed Python packages to a file named "requirements_new.txt"
pip freeze > requirements_new.txt

if [ -f "$HOME/localx/bin/python311" ]; then
    rm -rf $HOME/localx/bin/python311
fi

# Create a symbolic link to the Python 3.11 executable in the localx/bin directory
if [ -f "$HOME/localx/bin/python3.11" ]; then
    ln -s "$HOME/localx/bin/python3.11" "$HOME/localx/bin/python311"
    ln -s "$HOME/localx/bin/python3.11" "$HOME/localx/bin/python3"
    echo "Symbolic links created successfully."
else
    echo "Python 3.11 executable not found. Please make sure it's installed in $HOME/localx/bin."
fi

# Display the version of Python 3.11
./localx/bin/python3.11 -V

# Upgrade pip to the latest version
./localx/bin/python3.11 -m pip install --upgrade pip

# Install Gorilla
./localx/bin/python3.11 -m pip install packaging
./localx/bin/python3.11 -m pip install gorilla

# Install the Python packages
./localx/bin/python3.11 -m pip install -r requirements_new.txt
./localx/bin/python3.11 -m pip install -r c8/requirements.txt

./localx/bin/python3.11 -m pip list --outdated
./localx/bin/python3.11 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 ./localx/bin/pip3.11 install -U


# Install packages
./localx/bin/python3.11 -m pip install wikitextparser
./localx/bin/python3.11 -m pip install python-dateutil
./localx/bin/python3.11 -m pip install certifi --upgrade
# ./localx/bin/python3.11 -m pip install --upgrade regex==2022.10.31

echo 'export PATH=$HOME/localx/bin:$HOME/local/bin:/usr/local/bin:/usr/bin:/bin' > ~/.bash_profile
