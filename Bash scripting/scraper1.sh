#!/usr/bin/bash

url=https://www.education.gov.in/en/iits
curl $url --output newfile.html
xidel newfile.html -e '/html/body/div[5]/div/div/div[1]/section/div[2]/div/div/div/div/div/div/div/table' > parsed2.csv
rm -f newfile.html

