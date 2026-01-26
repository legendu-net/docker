#!/usr/bin/env bash

# maven configuration
mkdir -p $HOME/.m2
cp /settings/settings.xml $HOME/.m2/
chown -R $DOCKER_USER:$DOCKER_GROUP $HOME/.m2

