# NAME: dclong/nfs
FROM dclong/base:next
# GIT: https://github.com/legendu-net/docker-base.git

RUN apt-get -y update \
    && apt-get -y install nfs-kernel-server \
    && apt-get autoremove \
    && apt-get autoclean

RUN mkdir -p /nfs \
    && chmod 777 /nfs 

COPY settings/exports /etc/exports
COPY scripts /scripts/

EXPOSE 111 2049

ENTRYPOINT ["/scripts/sys/init.sh"]
