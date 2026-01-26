#!/usr/bin/env sh

# set samba password for the Docker user
smbpasswd -a $DOCKER_USER << EOF
$DOCKER_PASSWORD
$DOCKER_PASSWORD
EOF
sed -i "s/^valid users\s*=\s*\${DOCKER_USER}/valid users = ${DOCKER_USER}/g" /etc/samba/smb.conf
