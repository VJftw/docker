FROM ubuntu
MAINTAINER VJ Patel <vj@vjpatel.me>

# Proper permissions
ENV CONTAINER_USER jenkins
ENV CONTAINER_UID 1000
ENV CONTAINER_GROUP jenkins
ENV CONTAINER_GID 1000

RUN groupadd --gid $CONTAINER_GID jenkins && \
    useradd --uid $CONTAINER_UID --gid $CONTAINER_GID --create-home --shell /bin/bash jenkins

RUN groupadd --gid 999 docker && usermod -aG docker jenkins

# install git, jdk, curl
RUN apt-get install -y curl wget software-properties-common
RUN apt-add-repository ppa:git-core/ppa
RUN apt-add-repository ppa:brightbox/ruby-ng

RUN apt-get update && apt-get install -y git ruby2.2
RUN apt-get install -y openjdk-7-jdk

# install swarm-slave
ENV SWARM_HOME /home/jenkins
ENV SWARM_VERSION 2.0
RUN wget --no-check-certificate --directory-prefix=${SWARM_HOME} \
      http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_VERSION}/swarm-client-${SWARM_VERSION}-jar-with-dependencies.jar  && \
    mv ${SWARM_HOME}/swarm-client-${SWARM_VERSION}-jar-with-dependencies.jar ${SWARM_HOME}/swarm-client-jar-with-dependencies.jar && \
    chown -R jenkins:jenkins ${SWARM_HOME} && \
    chmod +x ${SWARM_HOME}/swarm-client-jar-with-dependencies.jar

RUN apt-get clean

RUN gem install rake

# docker entrypoint env variables
ENV JAVA_VM_PARAMETERS=
ENV JENKINS_MASTER_URL=
ENV SWARM_CLIENT_PARAMETERS=
ENV JENKINS_USER=
ENV JENKINS_PASSWORD=
ENV SWARM_CLIENT_EXECUTORS=
ENV SWARM_CLIENT_LABELS=

COPY docker-entrypoint.sh /home/jenkins/docker-entrypoint.sh
RUN chmod +x /home/jenkins/docker-entrypoint.sh

USER $CONTAINER_UID
WORKDIR /home/jenkins
ENTRYPOINT ["/home/jenkins/docker-entrypoint.sh"]
CMD ["swarm"]
