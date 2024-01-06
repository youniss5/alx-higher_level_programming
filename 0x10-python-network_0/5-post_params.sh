#!/bin/bash
# sends a POST request to the passed URL , ( post it )
curl "$1" -sX POST -d "test@gmail.com&subject=I will always be here for PLD"
