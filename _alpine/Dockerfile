FROM alpine:latest
MAINTAINER VJ Patel <vj@vjpatel.me>

# Add app user and group
RUN addgroup -g 999 app
RUN adduser -H -u 999 -G app -D -g "" -S app

# Create /app directory
RUN mkdir -p /app && chmod -R 770 /app && chown -R app:app /app
WORKDIR /app

# Set up S6 supervisor
ENV S6_VERSION v1.17.2.0
ADD https://github.com/just-containers/s6-overlay/releases/download/$S6_VERSION/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]
CMD []

# add syslog
COPY syslog.sh /etc/services.d/syslog/run
RUN chmod 755 /etc/services.d/syslog/run

WORKDIR /app
