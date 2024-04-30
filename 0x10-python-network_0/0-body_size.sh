#!/bin/bash
curl -sl "$1" | grep "Content-Length" | cut -d " " -f2
