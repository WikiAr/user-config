!/bin/bash
cd $HOME

# Remove the master.zip file
rm ./master.zip

# Download the pywikibot repository as a zip file from GitHub
wget https://github.com/wikimedia/pywikibot/archive/refs/heads/master.zip

# Unzip the downloaded master.zip file
unzip ./master.zip
rm ./master.zip

# Rename the extracted pywikibot-master directory to c8
mv ./pywikibot-master ./c8

# Set the file permissions to 6770 for the c8 directory and its contents
chmod -R 6770 ./c8

# Copy the 404-links.txt file from /data/project/himo/core8/ to the c8 directory
cp /data/project/himo/core8/404-links.txt ./c8/404-links.txt

# Set the file permissions to 6770 for the c8 directory and its contents
chmod -R 6770 ./c8

rm -rf ./user-config.py

# download https://github.com/MrIbrahem/user-config/blob/main/user-config.py to user-config.py
wget https://github.com/MrIbrahem/user-config/blob/main/user-config.py

# Run the pwb.py script with the API/txtlib argument using Python 3.11
python3.11 c8/pwb.py API/txtlib
