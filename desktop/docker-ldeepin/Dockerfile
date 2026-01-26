FROM dclong/deepin_cn

ARG url=https://download.nomachine.com/download/6.5/Linux/nomachine_6.5.6_9_amd64.deb

RUN apt-get -y update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
        dde \
        firefox \
    && wget $url -O /nomachine.deb \
    && dpkg -i /nomachine.deb \
    && rm /nomachine.deb \
    && mkdir /root/.config \
    && apt-get autoremove \
    && apt-get autoclean

EXPOSE 4000

COPY scripts /scripts

ENTRYPOINT ["/scripts/init.sh"]
