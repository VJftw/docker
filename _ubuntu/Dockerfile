# docker build -t vjftw/ubuntu:14.04-<commit>
# docker tag vjftw/ubuntu:14.04
FROM ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Set up local
RUN locale-gen en_GB.UTF-8
ENV LANG en_GB.UTF-8

# Set up S6 supervisor
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]
CMD []

# Add ppa, curl and syslogd
RUN apt-get update && apt-get install -y software-properties-common curl inetutils-syslogd && apt-get clean
COPY syslog.sh /etc/services.d/syslog/run
RUN chmod 755 /etc/services.d/syslog/run

# Add app user and group
RUN addgroup --gid 1000 app
RUN adduser --no-create-home --uid 1000 --gid 1000 --disabled-login --disabled-password --gecos "" app

# Create app directory
RUN mkdir -p /app
RUN chmod -R 770 /app
RUN chown -R app:app /app

WORKDIR /app
