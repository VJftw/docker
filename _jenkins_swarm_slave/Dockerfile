FROM blacklabelops/jenkins-swarm
MAINTAINER VJ Patel <vj@vjpatel.me>

# install toolset
COPY tools.sh /tmp/tools.sh
USER root
RUN chmod +x /tmp/tools.sh
RUN /tmp/tools.sh


USER jenkins

ENTRYPOINT ["/home/jenkins/docker-entrypoint.sh"]
CMD ["swarm"]
