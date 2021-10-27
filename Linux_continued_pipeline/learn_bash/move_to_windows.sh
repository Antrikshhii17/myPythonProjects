#!/usr/bin/bash

target=/c/Users/antriksh.chourasia/Documents
file=processed_data1.csv

mv $file $target

if [ -f $target/$file ]; then
	echo "Success! File has been moved to $target"
fi

