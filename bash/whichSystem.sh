#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
whiteColour="\e[1;37m"

function help(){
	echo -e "Use: ./whichSystem.sh <ip-host>"
}

function main(){
	ttl=$(ping -c 1 $host | grep -oP "ttl=\d{1,3}" | cut -d "=" -f 2)
	echo
	if [ $ttl -le 64 ]; then
		echo -e "${whiteColour}Linux${endColour} ${greenColour}-> ttl : $ttl${endColour}"

	elif [ $ttl -gt 64 ] && [ $ttl -le 128 ]; then
		echo -e "${whiteColour}Windows${endColour} ${greenColour}-> ttl : $ttl${endColour}"
	fi
}


if [ $1 ]; then
	host=$1
	main
else
	help
fi
