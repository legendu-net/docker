# NAME: dclong/jupyterhub-ganymede
FROM dclong/jupyterhub-jdk
# GIT: https://github.com/legendu-net/docker-jupyterhub-jdk.git

# The Ganymede kernel
RUN icon download_github_release -r allen-ball/ganymede -k jar -K asc -o /tmp/ganymede.jar \
    && java -jar /tmp/ganymede.jar -i --sys-prefix \
    && mkdir -p /usr/local/share/jupyter/kernels/ \
    && mv /opt/venv/share/jupyter/kernels/ganymede-*-java-*/ /usr/local/share/jupyter/kernels/ \
    && sed -i 's_/opt/venv/share/jupyter/kernels/_/usr/local/share/jupyter/kernels/_g' /usr/local/share/jupyter/kernels/ganymede*/kernel.json \
    && /scripts/sys/purge_cache.sh
