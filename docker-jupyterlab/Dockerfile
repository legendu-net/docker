# NAME: dclong/jupyterlab
FROM dclong/python-nodejs:next
# GIT: https://github.com/legendu-net/docker-python-nodejs.git

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends procps \
    && useradd -m -s /bin/bash linuxbrew \
    && echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && su - linuxbrew -c 'NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"' \
    && su - linuxbrew -c '/home/linuxbrew/.linuxbrew/bin/brew install fish' \
    && /scripts/sys/purge_cache.sh

ENV PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:${PATH}"
#RUN echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /etc/bash.bashrc \
#    && mkdir -p /etc/fish && echo 'eval (/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /etc/fish/config.fish
RUN pip3 install \
      nbdime jinja2 nbconvert "jupyterlab>=2.1.0,<4.6.0" \
      jupyterlab_widgets ipywidgets jupyterlab_myst \
      jupyterlab-lsp python-lsp-server[all] \
      jupyterlab-code-formatter ruff \
      jupyterlab_vim \
      jupyter-resource-usage \
      jupyter_ai[all] \
    && jupyter labextension disable @axlair/jupyterlab_vim \
    && /scripts/sys/purge_cache.sh \
    && npm cache clean --force

COPY scripts /scripts
#COPY settings/themes.jupyterlab-settings /etc/jupyter/lab/user-settings/@jupyterlab/apputils-extension/themes.jupyterlab-settings
COPY settings/*jupyterlab-* /settings/
COPY settings/jupyter_server_config.py /etc/jupyter/

