# NAME: dclong/python-nodejs
FROM dclong/python
# GIT: https://github.com/legendu-net/docker-python.git

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
        nodejs npm \
    && npm install -g n \
    && n lts \
    #&& npm cache clean --force \
    && /scripts/sys/purge_cache.sh
