# docker build -t vjftw/php:cli-<commit> .
# docker tag vjftw/php-cli
FROM vjftw/ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

USER root

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Add deb.sury php5.6 source
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" > /etc/apt/sources.list.d/ondrej-php5-5_6-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN apt-get update && apt-get install -y php5-cli php5-intl php5-curl php5-mysql php5-sqlite php5-json

RUN sed -i 's#.*date.timezone=.*#date.timezone=Europe/London#g' /etc/php5/cli/php.ini

USER docker

WORKDIR /app

CMD ["-v"]
ENTRYPOINT ["/usr/bin/php"]
