#!/bin/bash

docker build -t pullfred .
docker run -it --rm -v /mnt/raid/research/freddata/data/processed:/app/output -u `id -u $USER`:`id -g $USER` pullfred
