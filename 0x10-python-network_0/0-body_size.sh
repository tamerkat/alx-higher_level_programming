#!/bin/bash
URL=$1
size=$(mktemp)

curl -sS -o "$size" "$URL"

bytes=$(wc -c < "$size")

echo "$bytes"

rm "$size"
