#!/bin/bash

# https://help.dreamhost.com/hc/en-us/articles/360001435926-Installing-OpenSSL-locally-under-your-username

wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz

wget https://www.openssl.org/source/openssl-1.1.1g.tar.gz.sha256

sha256sum openssl-1.1.1g.tar.gz

cat openssl-1.1.1g.tar.gz.sha256

tar zxvf openssl-1.1.1g.tar.gz

# tfw python3.9 shell
webservice python3.9 shell

cd openssl-1.1.1g

./config --prefix=$HOME/openssl --openssldir=$HOME/openssl no-ssl2

make
make test
make install
cd ~

exit

echo 'export PATH=$HOME/openssl/bin:$PATH
export LD_LIBRARY_PATH=$HOME/openssl/lib
export LC_ALL="en_US.UTF-8"
export LDFLAGS="-L $HOME/openssl/lib -Wl,-rpath,$HOME/openssl/lib"' >> ~/.bash_profile


which openssl

openssl version
