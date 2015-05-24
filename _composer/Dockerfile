FROM vjftw/php-cli
MAINTAINER VJ Patel <meetthevj@gmail.com>

RUN php -r "readfile('https://getcomposer.org/installer');" | php
RUN mv composer.phar /usr/local/bin/composer

CMD ["--version"]
ENTRYPOINT ["/usr/local/bin/composer", "--ansi"]
