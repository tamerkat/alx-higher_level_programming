#!/bin/bash
# Print curl size
curl -sLIw '%{http_code}' "$1" -o /dev/null
