# FIDO_Drone
FIDO Hackathon project

drone : parse & send drone's FC data and FIDO Auth info to log server


Setting

sudo su
sudo apt-get install asciidoc autoconf lib tool automate make libykclient3 libusb-1.0-0-dev libcurl4-openssl-dev help2man

mkdir yubikey
git clone git://github.com/Yubico/yubico-c.git cd yubico-c autoreconf —install ./configrue && make check && make install

git clone git://github.com/Yubico/yubico-c-client.git cd yubico-c-client autoreconf — install ./configure && make check && make install

git clone git://github.com/Yubico/yubikey-personalization.git cd yubikey-personalization
git submodule init git submodule update autoreconf —install ./configure && make check && make install

git clone git://github.com/Yubico/yubico-pam.git cd yubico-pam autoreconf —install
./configrue && make check && make install


