#!/bin/bash
git config --global user.name "github-actions"
git config --global user.email "github-actions@github.com"
git add VERSION
git commit -m "Bump version to $new_version"
git push
