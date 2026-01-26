# NAME: dclong/rust-cicd
FROM dclong/python

RUN pip3 install github-rest-api

ENV RUSTUP_HOME=/usr/local/rustup PATH=/usr/local/cargo/bin:$PATH
COPY --from=dclong/rust /usr/local/rustup/ /usr/local/rustup/
COPY --from=dclong/rust \
        /usr/local/cargo/bin/rustc \
        /usr/local/cargo/bin/rustdoc \
        /usr/local/cargo/bin/cargo \
        /usr/local/cargo/bin/cargo-fmt \
        /usr/local/cargo/bin/rustfmt \
    /usr/local/cargo/bin/
COPY --from=dclong/rust-utils /usr/local/cargo/bin/cargo-criterion /usr/local/cargo/bin/
COPY --from=dclong/rust-utils /usr/bin/nperf /usr/bin/
COPY settings/sysctl.conf /etc/sysctl.conf
