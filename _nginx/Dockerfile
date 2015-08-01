# docker build -t vjftw/nginx:<commit> .
FROM vjftw/ubuntu:14.04
MAINTAINER VJ Patel <meetthevj@gmail.com>

USER root

# Add nginx mainline source
RUN echo "deb http://ppa.launchpad.net/nginx/development/ubuntu trusty main" > /etc/apt/sources.list.d/nginx-development-trusty.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C300EE8C

RUN apt-get update && apt-get install -y nginx

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN rm /etc/nginx/sites-enabled/default
VOLUME /etc/nginx/sites-enabled

USER docker

EXPOSE 80
CMD ["/usr/sbin/nginx"]
