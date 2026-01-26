# dclong/conda-build [@DockerHub](https://hub.docker.com/r/dclong/conda-build/) | [@GitHub](https://github.com/dclong/docker-conda-build)

Mini Anaconda 3 with conda-build (for building and publishing conda packages) in Docker. 

## Prerequisite
You need to [install Docker](http://www.legendu.net/en/blog/docker-installation/) before you use this Docker image.


## Usage in Linux/Unix

Please refer to the Section
[Usage](http://www.legendu.net/en/blog/my-docker-images/#usage)
of the post [My Docker Images](http://www.legendu.net/en/blog/my-docker-images/) 
for detailed instruction on how to use the Docker image.

The following command starts a container 
and mounts the current working directory and `/home` on the host machine 
to `/workdir` and `/home_host` in the container respectively.

```
docker run -it --init \
    --hostname conda-build \
    --log-opt max-size=50m \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/workdir \
    -v "$(dirname $HOME)":/home_host \
    dclong/conda-build /scripts/sys/init.sh
```
Use the image with the `next` tag (which is the testing/next version of dclong/conda-build).
```
docker run -it --init \
    --hostname conda-build \
    --log-opt max-size=50m \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/workdir \
    -v "$(dirname $HOME)":/home_host \
    dclong/conda-build:next /scripts/sys/init.sh
```
## Build a conda Package

It is suggested that you work in the directory `/workdir`. 
You can mount your directory on the host machine into this directory.

1. Login to Anaconda Cloud.

        anaconda login
        
2. Build your recipe. 

3. Run the following command to build and upload your conda package.

        conda build <recipe-dir>
        
Please refer to [conda/conda-build](https://github.com/conda/conda-build#building-your-own-packages) 
for more detailed information.

## [Log Information](http://www.legendu.net/en/blog/my-docker-images/#docker-container-logs)

## [Detailed Information](http://www.legendu.net/en/blog/my-docker-images/#list-of-images-and-detailed-information) 

## [Known Issues](http://www.legendu.net/en/blog/my-docker-images/#known-issues)

## [About the Author](http://www.legendu.net/pages/about)


