FROM dclong/lubuntu

RUN add-apt-repository ppa:cwchien/gradle 

RUN apt-get -y update \
    && apt-get -y install openjdk-8-jdk maven gradle \
    && apt-get autoremove \
    && apt-get autoclean
