# NAME: dclong/gophernotes
FROM dclong/golang
# GIT: https://github.com/legendu-net/docker-golang.git

RUN env GO111MODULE=on go install github.com/gopherdata/gophernotes@latest \
    && mkdir -p /usr/local/share/jupyter/kernels/gophernotes \
    && cd /usr/local/share/jupyter/kernels/gophernotes \
    && cp "$(go env GOPATH)"/pkg/mod/github.com/gopherdata/gophernotes@v*/kernel/*  ./ \
    && chmod +w ./kernel.json \
    && sed "s|gophernotes|$(go env GOPATH)/bin/gophernotes|" < kernel.json.in > kernel.json
