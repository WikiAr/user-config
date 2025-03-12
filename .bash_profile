export PATH=$HOME/openssl/bin:$HOME/local/bin:/usr/local/bin:/usr/bin:/bin
export LD_LIBRARY_PATH=$HOME/openssl/lib
export LC_ALL="en_US.UTF-8"
export LDFLAGS="-L $HOME/openssl/lib -Wl,-rpath,$HOME/openssl/lib"