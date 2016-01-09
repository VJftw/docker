#!/usr/bin/env sh
set -ex
cd /tmp
# apk upgrade
# apk update
# 
apt-get update && apt-get install -y wget

wget -O teamspeak.tar.gz http://dl.4players.de/ts/releases/3.0.11.4/teamspeak3-server_linux-amd64-3.0.11.4.tar.gz
gzip -d teamspeak.tar.gz
tar -xf teamspeak.tar
ls

# Copy to app
cp -R teamspeak3-server_linux-amd64/* /app

# chown -R 999:999 /app
chmod +x /app/ts3server_linux_amd64

apt-get clean

# apk del <applications that were used only for building, like gcc, make etc.>
# rm -rf /tmp/*
#rm -rf /var/cache/apk/*
