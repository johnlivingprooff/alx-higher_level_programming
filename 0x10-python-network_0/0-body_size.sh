#!/bin/bash
# this script that takes in a URL,
curl -sI "0.0.0.0:5000" | grep Content-Length | cut -d ' ' -f2
