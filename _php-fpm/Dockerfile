FROM vjftw/ubuntu
MAINTAINER VJ Patel <meetthevj@gmail.com>

# Disable frontend dialogs
ENV DEBIAN_FRONTEND noninteractive

# Add deb.sury php5.6 source
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" > /etc/apt/sources.list.d/ondrej-php5-5_6-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

RUN apt-get update && apt-get install -y php5-fpm php5-intl php5-curl php5-mysql php5-sqlite php5-json

RUN sed -i 's#.*date.timezone=.*#date.timezone=Europe/London#g' /etc/php5/fpm/php.ini
RUN sed -i 's#.*listen =.*#listen=9000#g' /etc/php5/fpm/pool.d/www.conf
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php5/fpm/pool.d/www.conf

EXPOSE 9000
CMD ["/usr/sbin/php5-fpm", "--nodaemonize"]
