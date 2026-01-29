#!/bin/bash
pattern="python"
file="notes.txt"
if [ ! -f "$file" ]; then
  echo "File $file does not exist!"
  exit 1
fi
count=$(grep -o -w "$pattern" "$file" | wc -l)
echo "The word '$pattern' occurs $count times in $file"

