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

# ESCANEO GREPEABLE
echo -e "\n${greenColour}sudo nmap -p- --open -sS -Pn -n --min-rate 5000 -vvv $1 -oG allPorts${endColour}"
sudo grc nmap -p- --open -sS -Pn -n --min-rate 5000 -vvv $1 -oG allPorts

ports="$(/usr/bin/cat allPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
ip_address="$(cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"

sleep 1
# EXTRAYENDO INFORMACION
echo -e "\n\n\n---------------------------------------"
echo -e "${yellowColour}[*] Extracting information...${endColour}\n"
echo -e "\t${yellowColour}[*]${endColour} ${grayColour}IP Address: $ip_address${endColour}"
echo -e "\t${yellowColour}[*]${endColour} ${grayColour}Open ports: $ports${endColour}\n"
echo -e "---------------------------------------\n\n"

# ESCANEO COMPLETO
echo -e "\n${greenColour}nmap -p${ports} -sC -sV ${ip_address} -oN targeted${endColour}"
sudo grc nmap -p${ports} -sC -sV ${ip_address} -oN targeted


# WHATWEB
echo -e "\n\n\n"
whatweb http://192.168.0.106|tr "," "\n"| tee whatweb.log
