# dclong/jupyterhub-antlr4 [@DockerHub](https://hub.docker.com/r/dclong/jupyterhub-antlr4/) | [@GitHub](https://github.com/dclong/docker-jupyterhub-antlr4)

JupyterHub with ANTLR4 in Docker. 

## About the Author

[Personal Blog](http://www.legendu.net)   |   [GitHub](https://github.com/dclong)   |   [Bitbucket](https://bitbucket.org/dclong/)   |   [LinkedIn](http://www.linkedin.com/in/ben-chuanlong-du-1239b221/)

## Usage in Linux/Unix

```
docker run -d \
    --log-opt max-size=50m \
    -p 8000:8000 \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v /wwwroot:/workdir \
    dclong/jupyterhub-antlr4
```
