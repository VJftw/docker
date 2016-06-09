import os
import time
from invoke import task
from docker import Client
from idflow import Utils, Docker

Utils.print_system_info()


def __check_service(service):
    if not service:
        exit("Please define a service")


@task
def build(ctx, service):
    __check_service(service)
    cli = Client(
        base_url='unix://var/run/docker.sock', timeout=600, version='auto')
    cli, username = Docker.login(cli)

    os.chdir("_{0}".format(service))

    base_name = "{0}/{1}".format(
        username,
        service
    )
    time_name = "{0}:{1}".format(base_name, time.strftime("%Y%m%d"))

    # print("Building {0}".format(time_name))
    Docker.build(cli, "Dockerfile", time_name)

    print("#")
    print("# Tagging as {0}".format(base_name))
    print("#")
    print()
    cli.tag(
        image=time_name,
        repository=base_name,
        tag="latest"
    )

    Docker.push(cli, [time_name, base_name])
