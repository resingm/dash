#!/usr/bin/env bash

docker run \
  --rm \
  --name local-proxy \
  -p 80:80 \
  --net="host" \
  -v $PWD/nginx.conf:/etc/nginx/nginx.conf:ro \
  nginx:1.19.10-alpine


