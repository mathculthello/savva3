#!/bin/bash
set -ex

export DOMAIN=savva.bhyve.cloud
export CONFIG=./settings/production.py
export CONFIG_TAG=$(shasum $CONFIG -a 512 | cut -c1-16)
docker stack deploy -c stack.yml -c traefik.yml savva3
