import os
import time
from invoke import task
from docker import APIClient
from invoke_tools import lxc, system, vcs

cli = APIClient(base_url='unix://var/run/docker.sock', timeout=600, version='auto')

system.Info.print_all()

repo = vcs.Git()
repo.print_all()


def __check_service(service):
    if not service:
        exit("Please define a service")

def __get_base_name(service):
    return "{0}/{1}".format(
        os.getenv("DOCKER_USERNAME") or "vjftw",
        service
    )

@task
def build(ctx, service):
    __check_service(service)

    os.chdir("_{0}".format(service))

    time_name = "{0}:{1}".format(
        __get_base_name(service),
        time.strftime("%Y%m%d")
    )

    lxc.Docker.build(cli,
        dockerfile="Dockerfile",
        tag=time_name
    )

@task
def publish(ctx, service):
    __check_service(service)

    if repo.get_branch() != "master":
        exit("Not on master")

    base_name = __get_base_name(service)

    lxc.Docker.login(cli)

    print("#")
    print("# Tagging as {0}".format(base_name))
    print("#")
    print()
    cli.tag(
        image=time_name,
        repository=base_name,
        tag="latest"
    )

    lxc.Docker.push(cli, [
        time_name,
        base_name
    ])
