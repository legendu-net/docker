# [dclong/conda-yarn](https://hub.docker.com/r/dclong/conda-yarn/)

`conda` and `yarn` in Docker. 

## About the Author

[Personal Blog](http://www.legendu.net)   |   [GitHub](https://github.com/dclong)   |   [Bitbucket](https://bitbucket.org/dclong/)   |   [LinkedIn](http://www.linkedin.com/in/ben-chuanlong-du-1239b221/)

## Details 

OS: Ubuntu

Additional: Anaconda Python 3 minimal and yarn.

## Usage in Linux/Unix

```
docker run -d --init \
    --log-opt max-size=50m \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_PASSWORD=`id -un` \
    -v /wwwroot:/wwwroot \
    dclong/conda-yarn
```
