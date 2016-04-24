from invoke import task
from docker import Client
import os
import json
import getpass
import time

cli = Client(base_url='unix://var/run/docker.sock', timeout=600, version='auto')
CI = True if os.getenv('CI') else False

def __print_line(line):
    if "stream" in line:
        print(line["stream"], end="", flush=True)
    elif "status" in line:
        o = line["status"]
        if "progress" in line:
            o += " " + line["progress"]
        if "id" in line:
            o = line["id"] + " " + o
        print(o)
    else:
        print(line)

def __build_service(dockerfile, tag):
    for line in cli.build(
        dockerfile=dockerfile,
        pull=True,
        path=".",
        rm=True,
        tag=tag
    ):
        line = line.decode('utf-8')
        line = json.loads(line)
        __print_line(line)

def __push_service(tag, username, email, password):

    cli.login(
        username=username,
        email=email,
        password=password,
        registry='https://index.docker.io/v1/'
    )

    print("# Pushing to Registry")
    for line in cli.push(tag, stream=True):
        line = line.decode('utf-8')
        line = json.loads(line)
        __print_line(line)

def __check_service(service):
    if not service:
        exit("Please define a service")

@task
def build(service):
    __check_service(service)
    if CI:
        email = os.getenv('DOCKER_EMAIL')
        username = os.getenv('DOCKER_USERNAME')
        password = os.getenv('DOCKER_PASSWORD')
    else:
        email = input('Docker email:')
        username = input('Docker username:')
        password = getpass.getpass('Docker password:')

    os.chdir("_{0}".format(service))

    base_name = "{0}/{1}".format(
        username,
        service
    )
    time_name = "{0}:{1}".format(base_name, time.strftime("%Y%m%d"))

    print("Building {0}".format(time_name))
    __build_service("Dockerfile", time_name)

    print("Tagging as {0}".format(base_name))
    cli.tag(
        image=time_name,
        repository=base_name,
        tag="latest"
    )
    __push_service(time_name, username, email, password)
    __push_service(base_name, username, email, password)
