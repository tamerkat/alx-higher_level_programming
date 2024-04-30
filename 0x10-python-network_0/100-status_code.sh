#!/bin/bash
# Print curl size
curl -sI | grep "status_code" | cut -d' ' -f2
