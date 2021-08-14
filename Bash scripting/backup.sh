#!/usr/bin/bash

# This bash script is used to backup a user's home directory to /tmp/

user=$(whoami)
input=/home/$user
output=/tmp/${user}_home_$(date +%Y-%m-%d_%H%M%S).tar.gz

# The function total_files gives total number of files in a directory
function total_files {
	find \$1 -type f | wc -l
}

# This function will give total number of directories in a directory
function total_directories {
	find \$1 -type d | wc -l
}

tar -czf $output $input

echo -n "Files to be included:"
total_files $input

echo -n "Directories to be included:"
total_directories $input

echo "Backu of $input completed! Details about the backup file:"
ls -l $output

