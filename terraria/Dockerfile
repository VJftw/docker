# FROM ubuntu:xenial
FROM alpine:latest

ENV TSHOCK_VERSION 4.3.26

# RUN apt-get update && apt-get install -y mono-complete unzip
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && apk add --update mono@testing unzip tzdata

ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD https://github.com/Pryaxis/TShock/releases/download/v${TSHOCK_VERSION}/tshock_${TSHOCK_VERSION}.zip /tshock.zip
RUN unzip tshock.zip -d /tshock

VOLUME /world

WORKDIR /tshock
ENV WORLD ""
ENTRYPOINT ["mono", "--server", "--gc=sgen", "-O=all", "TerrariaServer.exe", "-configpath", "/world", "-worldpath", "/world", "-logpath", "/world"]
