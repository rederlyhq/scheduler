# https://www.docker.com/blog/containerized-python-development-part-1/
# set base image (host OS)
FROM python:3.8

ARG REDIS_HOST_ARG='localhost'
ARG REDIS_PORT_ARG=6379
ARG SERVER_PORT_ARG=3003

ENV REDIS_HOST=$REDIS_HOST_ARG
ENV REDIS_PORT=$REDIS_PORT_ARG
ENV SERVER_PORT=$SERVER_PORT_ARG

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "./index.py" ]