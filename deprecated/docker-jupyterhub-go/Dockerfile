# NAME: dclong/jupyterhub-go
FROM dclong/jupyterhub
# GIT: https://github.com/legendu-net/docker-jupyterhub.git

# GoLANG Kernel
COPY --from=dclong/gophernotes:next /usr/local/go/ /usr/local/go/
COPY --from=dclong/gophernotes:next /root/go/bin/gophernotes /usr/local/go/bin/
COPY --from=dclong/gophernotes:next /usr/local/share/jupyter/kernels/gophernotes/kernel.json.in /usr/local/share/jupyter/kernels/gophernotes/kernel.json
ENV PATH=/usr/local/go/bin:$PATH

