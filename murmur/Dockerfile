FROM sillelien/base-alpine:0.10

COPY build.sh /build.sh
RUN chmod 755 /build.sh
RUN /build.sh

RUN rm /build.sh

COPY murmur.sh /etc/services.d/murmur/run
RUN chmod 755 /etc/services.d/murmur/run
