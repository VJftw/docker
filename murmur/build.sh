#!/usr/bin/env sh
set -ex
cd /tmp
apk upgrade
apk update

wget -O murmur.tar.bz2 https://github.com/mumble-voip/mumble/releases/download/1.2.11/murmur-static_x86-1.2.11.tar.bz2
bzip2 -d murmur.tar.bz2
tar -xf murmur.tar
ls

# Copy to app
cp -R murmur-static_x86-1.2.11/* /app

chown -R 999:999 /app

# apk del <applications that were used only for building, like gcc, make etc.>
rm -rf /tmp/*
rm -rf /var/cache/apk/*
