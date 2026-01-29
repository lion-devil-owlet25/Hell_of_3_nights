#!/bin/bash
echo "Enter a number:"
read num
rev=0
temp=$num
while [ $temp -gt 0 ]
do
  rem=$((temp % 10))
  rev=$((rev * 10 + rem))
  temp=$((temp / 10))
done
if [ $num -eq $rev ]; then
  echo "$num is a Palindrome number"
else
  echo "$num is NOT a Palindrome number"
fi
