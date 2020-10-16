# Dependencies
## Python dependencies
pip3 install -r requirements.txt
## Redis
```bash
sudo docker run \
    -p 6379:6379 \
    --name rederly-redis \
    -d \
    redis
```

# Environment
| Environment Variable | Description | Default value |
| --- | --- | --- |
| redis_host | REDIS_HOST | 'localhost'
| redis_port | REDIS_PORT | '6379'
| server_port | SERVER_PORT | 3003


# Docker helpful commands
## Interfacing
To communicate with a local redis connection I use the following command:
```bash
`ifconfig docker0 | grep "inet\b" | awk '{print $2}'`
```
On my VM docker0 interface seems to be an interface that a docker container can use to interact with the host machine
## Building
```bash
sudo docker build --tag rederly-scheduler .
```
## Running
```bash
sudo docker run -d \
    -p 3003:3003 \
    -e REDIS_HOST=`ifconfig docker0 | grep "inet\b" | awk '{print $2}'` \
    --name=rederly-scheduler \
    rederly-scheduler
```

## Debugging issues
Using the following command will start you directly into shell.  
When python failed the container just exited
```bash
sudo docker run \
    -p 3003:3003 \
    -e SERVER_PORT=3000 \
    -e REDIS_HOST=`ifconfig docker0 | grep "inet\b" | awk '{print $2}'` \
    -it rederly-scheduler /bin/sh
```
