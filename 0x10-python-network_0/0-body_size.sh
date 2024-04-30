#!/bin/bash
#curl size
curl -sI "$1" | grep "Content-Length" | cut -d' ' -f2
