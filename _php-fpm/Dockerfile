# docker build -t vjftw/proxy:<commit> .

FROM vjftw/alpine
MAINTAINER VJ Patel <meetthevj@gmail.com>

USER root

# Install PHP
RUN apk add --update php-ctype php-dom php-pdo_mysql php-pdo_sqlite php-json php-intl php-curl php-opcache php-fpm
RUN sed -i 's#.*date.timezone=.*#date.timezone=Europe/London#g' /etc/php/php.ini

COPY php-fpm.conf /etc/php/php-fpm.conf

# Commented out as causes several ms delay when under load
# RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/php-fpm.conf

EXPOSE 9000
CMD ["/usr/bin/php-fpm", "--nodaemonize"]
