# NAME: dclong/conda-build
FROM dclong/conda
# GIT: https://github.com/legendu-net/docker-conda.git

RUN conda install conda-build anaconda-client \
    && conda update conda-build \
    && conda install patch \
    && conda config --set anaconda_upload yes

COPY scripts/ /scripts/
