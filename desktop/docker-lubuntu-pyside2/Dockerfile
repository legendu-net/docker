FROM dclong/lubuntu-qt5

RUN apt-get -y update \
    && apt-get -y install \
        python3 python3-pip python3-venv \
        python3-all-dev python3-setuptools build-essential python3-wheel \
    && pip3 install --upgrade pip \
    && apt-get autoremove \
    && apt-get autoclean 

RUN pip3 install pyside2 pyqt5

ENTRYPOINT ["/scripts/sys/init.sh"]
