#!/usr/bin/bash

# if [ find ~/learn_bash/ -size +200c -size -10k | wc -l -gt 1 ]; then

count=$(find ~/learn_bash/ -size +200c -size -10k | wc -l)

if [ $count -gt 1 ]; then
	echo "More than 1 file"
else
	echo "Just 1 file is present"
fi

