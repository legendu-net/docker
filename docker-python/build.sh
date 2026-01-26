#!/bin/bash

docker pull dclong/base:next
docker build -t dclong/python:next .
