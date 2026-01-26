# NAME: dclong/tensorboard
FROM dclong/python
# GIT: https://github.com/legendu-net/docker-python.git

RUN pip3 install tensorboard pandas \
    && /scripts/sys/purge_cache.sh

COPY scripts/ /scripts/

