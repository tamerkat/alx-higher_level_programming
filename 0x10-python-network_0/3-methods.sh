#!/bin/bash
# Print curl size
curl -sI "$1" | grep "Allow:" | cut -d' ' -f2-
