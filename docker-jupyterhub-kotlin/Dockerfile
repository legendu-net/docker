# NAME: dclong/jupyterhub-kotlin
FROM dclong/jupyterhub-jdk:next
# GIT: https://github.com/legendu-net/docker-jupyterhub-jdk.git

# Kotlin kernel
RUN pip3 install kotlin-jupyter-kernel \
    && /scripts/sys/purge_cache.sh
