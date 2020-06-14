#!/bin/sh

# Download and Install Python 3 from Source on CentOS 7
yum groupinstall -y "Development Tools"
yum install -y zlib-devel
cd /usr/src
wget https://python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar xf Python-3.7.3.tar.xz
cd Python-3.7.3
./configure --enable-optimizations --with-ensurepip=install
make altinstall
exit

# Download and Install Python 3 from Source on Debian
sudo -i
apt update -y
apt install -y \
  wget \
  build-essential \
  libffi-dev \
  libgdbm-dev \
  libc6-dev \
  libssl-dev \
  zlib1g-dev \
  libbz2-dev \
  libreadline-dev \
  libsqlite3-dev \
  libncurses5-dev \
  libncursesw5-dev \
  xz-utils \
  tk-dev

cd /usr/src
wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
tar xf Python-3.7.3.tar.xz
cd Python-3.7.3.tar.xz
./configure --enable-optimizations --with-ensurepip=install
make altinstall
exit

# Ensure Python 3 Works with sudo
secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin

# Upgrade Pip
pip3.7 install --upgrade pip
