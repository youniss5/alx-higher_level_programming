#!/bin/bash
# sends a POST request to the passed URL , ( post it )
curl "$1" -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD"
