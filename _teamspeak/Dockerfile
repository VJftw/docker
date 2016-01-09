FROM vjftw/ubuntu

COPY build.sh /tmp/build.sh
RUN chmod 755 /tmp/build.sh
RUN /tmp/build.sh

RUN rm /tmp/build.sh

COPY teamspeak.sh /etc/services.d/teamspeak/run
RUN chmod 755 /etc/services.d/teamspeak/run

EXPOSE 9987/udp
EXPOSE 30033/tcp
EXPOSE 10011/tcp
EXPOSE 41144/tcp
EXPOSE 2011/udp
