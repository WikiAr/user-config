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
make altinstall prefix=~/local

# Remove the extracted Python directory
cd ../
rm -r -f Python-3.11.4

# Create a symbolic link to the Python 3.11 executable in the local/bin directory
if [ -f "$HOME/local/bin/python3.11" ]; then
    ln -s "$HOME/local/bin/python3.11" "$HOME/local/bin/python311"
    ln -s "$HOME/local/bin/python3.11" "$HOME/local/bin/python3"
    echo "Symbolic links created successfully."
else
    echo "Python 3.11 executable not found. Please make sure it's installed in $HOME/local/bin."
fi

# Display the version of Python 3.11
./local/bin/python3 -V

# Upgrade pip to the latest version
./local/bin/python3 -m pip install -U pip requests packaging wikitextparser python-dateutil certifi gorilla gorilla-cli

# Install the Python packages
./local/bin/python3 -m pip install -r c8/requirements.txt

# echo 'export PATH=$HOME/local/bin:$HOME/local/bin:/usr/local/bin:/usr/bin:/bin' > ~/.bash_profile
