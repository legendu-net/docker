FROM dclong/jupyterhub

#ARG url=https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar
#RUN mkdir -p /opt/selenium \
#    && wget --no-verbose $url -O /opt/selenium/selenium-server-standalone.jar

RUN curl -s -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get -y update \
    && apt-get -y install xvfb google-chrome-stable unzip

RUN CHROME_MAJOR_VERSION=$(google-chrome --version | sed -E "s/.* ([0-9]+)(\.[0-9]+){3}.*/\1/") \
    && CHROME_DRIVER_VERSION=$(wget --no-verbose -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_MAJOR_VERSION}") \
    && wget --no-verbose -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod 755 /opt/selenium/chromedriver \
    && ln -svf /opt/selenium/chromedriver /usr/bin/chromedriver
    
RUN pip3 install selenium
