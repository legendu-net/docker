FROM dclong/python

RUN apt-get -y update \
    && apt-get -y install \
        openjdk-21-jdk maven gradle \
    && apt-get autoremove \
    && apt-get autoclean 

COPY scripts /scripts
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV PATH="$PATH:$JAVA_HOME/bin"
