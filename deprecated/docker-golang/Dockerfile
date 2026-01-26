# NAME: dclong/golang
FROM dclong/python
# GIT: https://github.com/legendu-net/docker-base.git

ENV PATH=/usr/local/go/bin:$PATH
RUN icon golang -i \
    && go install golang.org/x/tools/gopls@latest \
    && /scripts/sys/purge_cache.sh
