FROM vjftw/ubuntu
MAINTAINER VJ Patel <vj@vjpatel.me>

# install jdk
RUN apt-add-repository ppa:nginx/stable -y
RUN apt-get update && apt-get install -y wget openjdk-7-jdk git nginx
RUN apt-get clean

# Copy NGINX configuration
COPY nginx.conf /var/nginx.conf

ENV JAVA_VM_PARAMETERS=-Xmx512m
ENV JENKINS_MASTER_EXECUTORS=
ENV JENKINS_SLAVEPORT=500
ENV JENKINS_ADMIN_USER=
ENV JENKINS_ADMIN_PASSWORD=
ENV JENKINS_PLUGINS=swa
ENV JENKINS_PARAMETERS=
ENV JENKINS_KEYSTORE_PASSWORD=
ENV JENKINS_CERTIFICATE_DNAME=
ENV JENKINS_ENV_FILE=
ENV JENKINS_HOME=/app
ENV JENKINS_DELAYED_START=
ENV JENKINS_VERSION=latest
ENV JENKINS_RELEASE=war

RUN wget --directory-prefix=/usr/bin/jenkins http://mirrors.jenkins-ci.org/${JENKINS_RELEASE}/${JENKINS_VERSION}/jenkins.war

RUN chown -R app:app /usr/bin/jenkins && chmod ug+x /usr/bin/jenkins/jenkins.war
RUN mkdir -p mkdir -p ${JENKINS_HOME} && chown -R app:app ${JENKINS_HOME}

EXPOSE 80 50000

# Copy NGINX service script
COPY start_nginx.sh /etc/services.d/nginx/run
RUN chmod 755 /etc/services.d/nginx/run

COPY jenkins.sh /etc/services.d/jenkins/run
RUN chmod 755 /etc/services.d/jenkins/run

VOLUME ["/app"]
