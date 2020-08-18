#!/bin/bash
# curl cheese
curl -sI $1 | grep "HTTP" | grep -o '[0-9][0-9][0-9]' | tr '\n' '\0'