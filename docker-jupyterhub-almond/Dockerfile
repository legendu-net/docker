FROM dclong/jupyterhub-jdk

RUN curl -L -o /usr/local/bin/coursier https://git.io/coursier-cli \
    && chmod +x /usr/local/bin/coursier \
    && /usr/local/bin/coursier launch almond --quiet -- --install --global
