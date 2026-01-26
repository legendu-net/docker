# NAME: dclong/python
FROM dclong/base
# GIT: https://github.com/legendu-net/docker-base.git

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
        python3-all-dev python3-venv build-essential \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip3 install \
        ipython \
    && curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh \
    && /scripts/sys/purge_cache.sh

ENV PATH="/opt/venv/bin:$PATH"

COPY scripts/ /scripts/
