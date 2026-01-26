# dclong/nfs [@DockerHub](https://hub.docker.com/r/dclong/nfs/) | [@GitHub](https://github.com/dclong/docker-nfs)

NFS in Ubuntu. 

## Prerequisite
You need to [install Docker](http://www.legendu.net/en/blog/docker-installation/) before you use this Docker image.


## Usage in Linux/Unix

### Start a Container

```
docker run -it \
    --log-opt max-size=50m \
    -p 111:111 \
    -p 2049:2049 \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_GROUP_ID=`id -g` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/nfs \
    dclong/nfs
```

## [Detailed Information](http://www.legendu.net/en/blog/my-docker-images/#list-of-images-and-detailed-information) 

## [Known Issues](http://www.legendu.net/en/blog/my-docker-images/#known-issues)

## [About the Author](http://www.legendu.net/pages/about)
