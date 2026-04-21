# NAME: dclong/conda
FROM dclong/base:next
# GIT: https://github.com/legendu-net/docker-base.git

ENV PATH=/opt/conda/bin:$PATH

RUN apt-get -y update \
    && apt-get -y install --no-install-recommends \
        gcc \
    && /scripts/sys/purge_cache.sh
      
RUN curl -sSL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /scripts/miniconda.sh \
    && bash /scripts/miniconda.sh -bfp /opt/conda \
    && rm -rf /scripts/miniconda.sh \
    && conda update -n base conda \
    && conda install -c conda-forge pip conda-pack \
    && conda init bash \
    && /scripts/sys/purge_cache.sh

RUN echo 'export PATH=/opt/conda/bin:$PATH' >> /etc/profile
