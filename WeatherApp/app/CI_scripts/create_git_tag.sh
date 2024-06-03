#!/bin/bash
git tag -a v$new_version -m "Version $new_version"
git push origin v$new_version
