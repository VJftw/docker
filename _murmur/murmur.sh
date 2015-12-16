#!/usr/bin/env sh
cd /app

sleep 10
exec s6-applyuidgid -u 999 -g 999 ./murmur.x86 -v -fg
