FROM vjftw/php-cli
MAINTAINER VJ Patel <meetthevj@gmail.com>

RUN php -r "readfile('https://getcomposer.org/installer');" | php
RUN mv composer.phar /usr/local/bin/composer

# Install git
RUN echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" > /etc/apt/sources.list.d/git-core-ubuntu-ppa-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E1DF1F24
RUN apt-get update && sudo apt-get install -y git

WORKDIR /app

CMD ["--version"]
ENTRYPOINT ["/usr/local/bin/composer", "--ansi"]
