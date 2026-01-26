FROM dclong/jupyterhub

#ARG url=https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar
#RUN mkdir -p /opt/selenium \
#    && wget --no-verbose $url -O /opt/selenium/selenium-server-standalone.jar

ARG GECKODRIVER_VERSION=0.25.0
ARG URL=https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-linux64.tar.gz
RUN apt-get -y update \
    && apt-get -y install xvfb firefox \
    && curl -L $URL -o /tmp/geckodriver.tar.gz \
    && tar -C /opt -zxf /tmp/geckodriver.tar.gz \
    && rm /tmp/geckodriver.tar.gz \
    && chmod 755 /opt/geckodriver \
    && ln -svf /opt/geckodriver /usr/bin/geckodriver

RUN pip3 install selenium
