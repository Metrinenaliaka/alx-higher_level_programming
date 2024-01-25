#!/bin/bash
#returns status code
curl -I -L -s -o /dev/null -w "%{http_code}" "$1"
