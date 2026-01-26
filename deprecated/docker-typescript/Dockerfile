FROM dclong/nodejs

RUN sudo npm install -g typescript

COPY scripts /scripts

ENTRYPOINT ["/scripts/sys/init.sh"]
