```bash

sudo docker run \
    -p 6379:6379 \
    --name some-redis \
    -d \
    redis

sudo apt install python3-pip
pip3 install rq
pip3 install moment
pip3 install flask
```

```bash
export PATH=$PATH:/home/luigi/.local/bin
```


```bash
rq worker --with-scheduler
```

```
sudo docker build . --tag tomtom
```

```
sudo docker run \
    -p 3000:3000 \
    -e SERVER_PORT=3000 \
    -e REDIS_HOST=`ifconfig docker0 | grep "inet\b" | awk '{print $2}'` \
    -it tomtom /bin/sh
```
```
sudo docker run -d \
    -p 3000:3000 \
    -e SERVER_PORT=3000 \
    -e REDIS_HOST=`ifconfig docker0 | grep "inet\b" | awk '{print $2}'` \
    --name=testest \
    tomtom
```
```
sudo docker exec -it testest /bin/sh
```
Environment
redis_host = os.environ.get('REDIS_HOST') or 'localhost'
redis_port = os.environ.get('REDIS_PORT') or '6379'
server_port = os.environ.get('SERVER_PORT') or 3003



