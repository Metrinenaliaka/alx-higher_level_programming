#!/bin/bash
#Makes a request to 0.0.0.0:5000/catch_me to get it!
curl -sLX POST http://0.0.0.0:5000/catch_me | grep -o "You got me!"
