# docker build -t vjftw/nginx:<commit> .
# docker tag vjftw/nginx

FROM vjftw/alpine
MAINTAINER VJ Patel <meetthevj@gmail.com>

USER root

RUN apk add --update nginx
COPY nginx.conf /etc/nginx/nginx.conf
# Fix logs
RUN mkdir -p /var/log/nginx && touch /var/log/nginx/error.log && chmod -R -v 6666 /var/log/nginx && chown -R -v docker:docker /var/log/nginx

VOLUME /etc/nginx/conf.d

#USER docker

EXPOSE 80
CMD ["/usr/sbin/nginx"]
