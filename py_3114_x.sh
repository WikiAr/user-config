!/bin/bash
cd $HOME

# Download Python 3.11.4 from the Python website
wget https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz

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

rm -rf ./local/bin/python311
# Create a symbolic link to the Python 3.11 executable in the local/bin directory
ln -s ./localx/bin/python3.11 ./localx/bin/python311

# Display the version of Python 3.11
./localx/bin/python3.11 -V

# Upgrade pip to the latest version
./localx/bin/python3.11 -m pip install --upgrade pip

# Install Gorilla
./localx/bin/python3.11 -m pip install packaging
./localx/bin/python3.11 -m pip install gorilla

# Install the Python packages
./localx/bin/python3.11 -m pip install -r requirements_new.txt

./localx/bin/python3.11 -m pip list --outdated
./localx/bin/python3.11 -m pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U


# Install packages
./localx/bin/python3.11 -m pip install wikitextparser
./localx/bin/python3.11 -m pip install python-dateutil
# ./localx/bin/python3.11 -m pip install --upgrade regex==2022.10.31