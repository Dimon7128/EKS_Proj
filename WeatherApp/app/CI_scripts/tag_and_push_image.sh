#!/bin/bash
docker tag myweatherapp:latest $DOCKER_USERNAME/myweatherapp:latest
docker push $DOCKER_USERNAME/myweatherapp:latest
