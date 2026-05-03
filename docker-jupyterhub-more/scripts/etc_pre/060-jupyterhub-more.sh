#!/usr/bin/env bash

su -m $DOCKER_USER -c "icon zellij -c"

if [ -e "/workdir/.gemini" ]; then
    ln -snf "/workdir/.gemini" "$HOME/.gemini"
fi
