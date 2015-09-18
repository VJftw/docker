# docker build -t vjftw/alpine:3.2-<commit>
# docker tag vjftw/alpine:3.2
# docker tag vjftw/alpine

FROM alpine:3.2
MAINTAINER VJ Patel <vj@vjpatel.me>

# Add docker user and group
RUN addgroup -g 999 docker
RUN adduser -H -u 999 -G docker -D -g "" -S docker

# Create /app directory
RUN mkdir -p /app && chmod -R 770 /app && chown -R docker:docker /app
WORKDIR /app

USER docker

