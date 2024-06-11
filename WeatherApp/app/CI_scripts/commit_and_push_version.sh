#!/bin/bash
git config --global user.name "github-actions"
git config --global user.email "github-actions@github.com"
git add WeatherApp/app/VERSION
git commit -m "Bump version to $new_version"
git push

#Pull the latest changes to ensure the local repo is up to date
git pull origin main