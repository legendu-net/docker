FROM dclong/jupyterhub-jdk

RUN apt-get -y update \
    && apt-get -y install antlr4 \
    && apt-get autoremove \
    && apt-get autoclean 

RUN pip3 install \
        antlr4-python3-runtime==4.5
