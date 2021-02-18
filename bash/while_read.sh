#!/bin/bash

i=0
while read line;
do
    ((i+=1))
    echo "$line"
done < list.txt
