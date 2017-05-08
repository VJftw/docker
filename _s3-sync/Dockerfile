FROM python:3-alpine
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]
COPY s3-sync.sh /bin/s3-sync.sh
RUN chmod +x /bin/s3-sync.sh
CMD ["/bin/s3-sync.sh"]

RUN pip install awscli

# Can be S3://
ENV SOURCE /data

# Can be S3://
ENV DESTINATION /data

# CRON SCHEDULE
ENV SCHEDULE */15 * * * *
