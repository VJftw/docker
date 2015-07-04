#!/bin/bash

# Fetch and extract archive in ARCHIVE_URL to /app
echo "Fetching from Google Cloud Storage $ARCHIVE_URL"
gsutil cp $ARCHIVE_URL build.tar.gz

# Extract to temporary location
mkdir /temp/app
tar -zxvf build.tar.gz /temp/app

# Remove and copy
rm -rf /app
cp -r /temp/app /app
rm -rf /temp/app

# Sleep infinitely to keep pod awake
sleep infinity