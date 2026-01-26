# [dclong/conda](https://hub.docker.com/r/dclong/conda/)

Mini Anaconda 3 in Docker. 

## Details 

OS: Ubuntu

Additional: Anaconda Python 3 minimal.

## Usage in Linux/Unix

```
docker run -it --init \
    --hostname=conda \
    --log-opt max-size=50m \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/workdir \
    dclong/conda /bin/bash
```

```
docker run -it --init \
    --hostname=conda \
    --log-opt max-size=50m \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/workdir \
    dclong/conda:next /bin/bash
```

## About the Author

[Personal Blog](http://www.legendu.net)   |   [GitHub](https://github.com/dclong)   |   [Bitbucket](https://bitbucket.org/dclong/)   |   [LinkedIn](http://www.linkedin.com/in/ben-chuanlong-du-1239b221/)
