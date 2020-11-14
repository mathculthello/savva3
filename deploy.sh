#!/bin/bash
set -ex

export DOMAIN=savvateev.xyz
export CONFIG=./settings/production.py
export CONFIG_TAG=$(shasum $CONFIG -a 512 | cut -c1-16)
docker stack deploy -c stack.yml -c traefik.yml savva3
