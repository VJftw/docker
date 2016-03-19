FROM blacklabelops/java:jdk8
MAINTAINER VJ Patel <vj@vjpatel.me>

ENTRYPOINT ["/init"]
ADD https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /

# install git, jdk, curl
RUN apk add --update git ruby curl bash && \
    rm -rf /var/cache/apk/* && \
    gem install --no-rdoc --no-ri \
    bundler \
    rake \
    docker-api

# install swarm-slave
ENV SWARM_HOME /app
ENV SWARM_VERSION 2.0
ENV SWARM_WORKDIR=/opt/jenkins

RUN mkdir -p ${SWARM_WORKDIR} && mkdir -p ${SWARM_HOME} && \
    curl http://repo.jenkins-ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_VERSION}/swarm-client-${SWARM_VERSION}-jar-with-dependencies.jar \
    --output ${SWARM_HOME}/swarm-client.jar &&\
    chmod +x ${SWARM_HOME}/swarm-client.jar

# docker entrypoint env variables
ENV SWARM_VM_PARAMETERS=
ENV SWARM_MASTER_URL=
ENV SWARM_VM_PARAMETERS=
ENV SWARM_JENKINS_USER=
ENV SWARM_JENKINS_PASSWORD=
ENV SWARM_CLIENT_EXECUTORS=
ENV SWARM_CLIENT_LABELS=

COPY jenkins.sh /etc/services.d/jenkins/run
RUN chmod 755 /etc/services.d/jenkins/run

VOLUME ["/opt/jenkins"]
