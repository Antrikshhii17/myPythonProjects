#!/usr/bin/bash

target=/c/Users/antriksh.chourasia/Documents
file=parsed2.csv

mv $file $target

if [ ! -f $file ]; then
	echo "Success! File has been moved to $target"
fi

