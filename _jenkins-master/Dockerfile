FROM blacklabelops/jenkins:preview-2.0

EXPOSE 8080 80 50000

USER root

RUN apk add --update nginx git openssh-client

# Set up S6 supervisor
ENV S6_VERSION v1.17.2.0
ADD https://github.com/just-containers/s6-overlay/releases/download/$S6_VERSION/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

ENTRYPOINT ["/init"]
CMD []


COPY start_nginx.sh /etc/services.d/nginx/run
RUN chmod 755 /etc/services.d/nginx/run
# Copy NGINX configuration
COPY nginx.conf /var/nginx.conf

COPY jenkins.sh /etc/services.d/jenkins/run
RUN chmod 755 /etc/services.d/jenkins/run
