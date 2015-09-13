# docker build -t vjftw/php:cli-<commit> .
# docker tag vjftw/php-cli
FROM alpine:latest
MAINTAINER VJ Patel <meetthevj@gmail.com>

RUN mkdir -p /app

# Install PHP
RUN apk add --update php-cli php-ctype php-dom php-pdo_mysql php-pdo_sqlite php-json php-intl php-curl php-opcache

RUN sed -i 's#.*date.timezone=.*#date.timezone=Europe/London#g' /etc/php/php.ini

WORKDIR /app

CMD ["-v"]
ENTRYPOINT ["/usr/bin/php"]
