FROM ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Add Docker user and group
FROM ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Add Docker user and group
RUN addgroup --gid 999 docker && adduser --uid 999 --gid 999 --shell /bin/bash --disabled-password docker && adduser docker sudo
