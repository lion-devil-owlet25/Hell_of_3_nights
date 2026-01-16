#!/bin/bash
echo "Enter a number:- "
read a
if ((a % 2 == 0)); then 
echo "$a is even number"
elif ((a % 2 == 1)); then 
echo "$a is odd number"
else
echo "Wrong input"
fi
