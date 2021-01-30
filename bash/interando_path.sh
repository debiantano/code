#!/bin/bash

my_path=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/usr/local/go/bin:/home/noroot/.local/bin
echo -e "\nITERANDO EL PATH"
for path in $(echo $my_path | tr ":" " "); do
    echo $path 
done
echo -e "\nCAMBIAR CARACTERES"
echo "cconvirtiendo los espacion en mas" | sed 's/ /+/g'
echo "cconvirtiendo los espacion en mas" | tr ' ' '+'
