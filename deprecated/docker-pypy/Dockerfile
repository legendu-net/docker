# NAME: dclong/pypy
FROM dclong/ubuntu_b
# GIT: https://github.com/legendu-net/docker-ubuntu_b.git

ARG ver=pypy3.7-v7.3.4-linux64
RUN curl -sSL https://downloads.python.org/pypy/$ver.tar.bz2 -o /tmp/pypy.tar.bz2 \
    && tar -jxvf /tmp/pypy.tar.bz2 -C /opt/ \
    && ln -s /opt/$ver/bin/pypy /usr/local/bin/pypy \
    && pypy -m ensurepip \
    && pypy -m pip install --no-cache-dir \
        pylint yapf pytest ipython
