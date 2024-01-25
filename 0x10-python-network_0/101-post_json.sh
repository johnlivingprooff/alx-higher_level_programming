#!/bin/bash
# json POST
curl -s -X POST -H "Content-Type: application/json" "$1" -d @"$2"