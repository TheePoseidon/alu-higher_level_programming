#!/bin/bash
# sends request to given URL and displays the size of the body of response
curl -so /dev/null -w '%{size_download}\n' "$1"
