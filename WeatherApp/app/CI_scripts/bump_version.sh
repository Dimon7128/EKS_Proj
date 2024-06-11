#!/bin/bash
current_version=$(cat VERSION)
IFS='.' read -r -a version_parts <<< "$current_version"
version_parts[2]=$((version_parts[2]+1))
new_version="${version_parts[0]}.${version_parts[1]}.${version_parts[2]}"
echo "New version: $new_version"
echo $new_version > VERSION
echo "new_version=$new_version" >> $GITHUB_ENV
