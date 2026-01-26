# NAME: dclong/r-base
FROM dclong/base
# GIT: https://github.com/legendu-net/docker-base.git

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get -y update \
    && apt-get -y install \
        r-base-dev \
    && apt-get autoremove \
    && apt-get autoclean

# ADD settings/Renviron.site /etc/R/Renviron.site
