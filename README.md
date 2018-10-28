# Docker_flask

This example show how to setup a docker container with flask

to build in folder app

```
├── app
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt

```


```

docker build -t my_docker_flask:latest .

docker run -d -p 9999:5000 my_docker_flask:latest
```

For test

```
curl http:\\localhost:9999
```
