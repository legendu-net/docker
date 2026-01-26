# NAME: dclong/ubuntu_cn
FROM dclong/base
# GIT: https://github.com/legendu-net/docker-base.git

# locale
RUN apt-get -y update \
    # && DEBIAN_FRONTEND=noninteractive apt-get -y install locales \
    && locale-gen zh_CN.UTF-8 \
    && apt-get autoremove \
    && apt-get autoclean
    
# ENV LANG=zh_CN.UTF-8 LANGUAGE=zh_CN:zh LC_ALL=zh_CN.UTF-8 
