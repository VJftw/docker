# docker build -t vjftw/ubuntu:14.04-<commit>
# docker tag vjftw/ubuntu:14.04
FROM ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

# Add docker user and group
RUN addgroup --gid 999 docker
RUN adduser --no-create-home --uid 999 --gid 999 --disabled-login --disabled-password --gecos "" docker

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Create AppData directory
RUN mkdir /app_data
RUN chmod -R 770 /app_data
RUN chown -R docker:docker /app_data

USER docker
