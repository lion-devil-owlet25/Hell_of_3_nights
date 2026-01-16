#!/bin/bash
echo "Enter a number"
read a
echo "The number you have enter is $a"
case $((a % 2)) in 
0)
echo "$a is even number";;
1)
echo "$a is odd number";;
*)
echo "Wrong input";;
esac
