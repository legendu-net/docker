FROM dclong/python

RUN apt-get -y update \
    && apt-get -y install \
        qt5-default libqt5webkit5-dev build-essential xvfb \
    && apt-get autoremove \
    && apt-get autoclean 

RUN pip3 install dryscrape

COPY scripts /scripts

ENTRYPOINT ["/scripts/sys/init.sh"]
