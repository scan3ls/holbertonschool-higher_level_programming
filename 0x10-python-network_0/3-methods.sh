#!/bin/bash
# sends a request to URL, and displays the size of the body of the response
curl -sI $1 | grep "Allow:" | sed 's/.*:\s//'