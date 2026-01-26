# dclong/samba [@DockerHub](https://hub.docker.com/r/dclong/samba/) | [@GitHub](https://github.com/dclong/docker-samba)

Samba in Ubuntu. 

## Prerequisite
You need to [install Docker](http://www.legendu.net/en/blog/docker-installation/) before you use this Docker image.


## Usage in Linux/Unix

### Start a Container

```
docker run -it \
    --log-opt max-size=50m \
    -p 137-139:137-139 \
    -p 445:445 \
    -e DOCKER_USER=`id -un` \
    -e DOCKER_USER_ID=`id -u` \
    -e DOCKER_GROUP_ID=`getent group nogroup | cut -d: -f3` \
    -e DOCKER_PASSWORD=`id -un` \
    -v "$(pwd)":/smbshare \
    dclong/samba
```

### Mount the Samba Share

You can mount the Samba share using the command below
```
sudo mount -t cifs -o user=samba_user,password=samba_password server_ip/smbshare /path_to_mount_point
```
where `samba_user` is the Samba user, i.e., `DOCKER_USER` (by default the output of `id -un` on the host)
and `samba_password` is the Samba password, i.e., `DOCKER_PASSWORD` (by default the output of `id -un` on the host).

### Possible Issues 

mount error(115): Operation now in progress

## [Detailed Information](http://www.legendu.net/en/blog/my-docker-images/#list-of-images-and-detailed-information) 

## [Known Issues](http://www.legendu.net/en/blog/my-docker-images/#known-issues)

## [About the Author](http://www.legendu.net/pages/about)
