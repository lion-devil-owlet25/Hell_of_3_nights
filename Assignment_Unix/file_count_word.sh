#!/bin/bash
echo "Enter the word to search:"
read word
echo "Enter the filename:"
read file
if [ ! -f "$file" ]; then
  echo "File does not exist!"
  exit 1
fi
count=$(grep -o -w "$word" "$file" | wc -l)
echo "The word '$word' occurs $count times in $file"
