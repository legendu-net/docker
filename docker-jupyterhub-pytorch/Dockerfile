# NAME: dclong/jupyterhub-pytorch
FROM dclong/jupyterhub-cuda
# GIT: https://github.com/legendu-net/docker-jupyterhub-cuda.git

RUN pip3 install loguru pyarrow pandas \
    && icon pytorch -ic --copy --extra-pip-options break-system-packages --cuda-version 11.1 \
    && /scripts/sys/purge_cache.sh
