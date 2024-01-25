#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | sed -n '/Allow:/ {s/Allow: //; s/, /, /gp}'
