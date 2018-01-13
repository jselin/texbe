#!/bin/sh

aws ecr get-login --no-include-email --region eu-west-1 > docker-login.sh
docker-login.sh
docker-compose build
docker tag texbe_django:latest 067721458827.dkr.ecr.eu-west-1.amazonaws.com/texdesigners:latest
docker push 067721458827.dkr.ecr.eu-west-1.amazonaws.com/texdesigners:latest


