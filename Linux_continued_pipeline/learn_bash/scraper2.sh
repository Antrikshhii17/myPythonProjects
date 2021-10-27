#!/usr/bin/bash

url=https://blog.knoldus.com/creating-a-dag-in-apache-airflow/
xpath='/html/body/div[3]/div[3]/div/div/div[1]/main/article/div[2]/div[2]/div[2]/pre/code'

curl $url | tac | tac | xpath -e $xpath > parsed03.txt

if [ -f parsed03.txt ]; then
        echo "Success! The file has been downloaded."
fi
