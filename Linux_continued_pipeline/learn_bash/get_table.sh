#!/usr/bin/bash

echo -n "Enter the number upto which you want to print table: "
read -r n
i=1
while [ $i -ne 10 ]; do
	i=$((i + 1))
	table=$((i * n))
	echo "$table"
done
