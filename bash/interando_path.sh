#!/bin/bash

my_path=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/usr/local/go/bin:/home/noroot/.local/bin
for path in $(echo $my_path | tr ":" " "); do
    echo $path 
done
