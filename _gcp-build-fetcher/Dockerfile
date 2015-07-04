FROM google/cloud-sdk
MAINTAINER VJ Patel <meetthevj@gmail.com>

COPY fetch.sh /usr/bin/fetch
RUN chmod +x /usr/bin/fetch

RUN mkdir /app

WORKDIR /app

ENTRYPOINT ["/usr/bin/fetch"]
