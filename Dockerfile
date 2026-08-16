FROM python:3.13-slim

LABEL mainainer=""

# by default all operations are performed with root privileges. This is not good practice.
# docs I found in ru that explains why: https://habr.com/ru/post/448480/
# the next six lines are needed to create a non-root user for VPS
ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}

RUN useradd -m -u $UID docker_user
# here we create a user named docker_user, which is not root, and its UID will be
# 1000 by default (previously it was ARG UID=1000 ENV UID=${UID}), it can be
# replaced when starting the container by passing a variable either in the docker-compose.yaml file
# or as an argument to the docker command

USER docker_user

WORKDIR /home/docker_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1