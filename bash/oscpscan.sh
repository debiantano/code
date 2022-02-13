#!/bin/bash
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

echo -e "\n${yellowColour}nmap -p- --open --min-rate 5000 -vv -n $1 -oG allPorts${endColour}\n"
#nmap -p- --open --min-rate 5000 -vv -n $1 -oG allPorts

# VARIABLES
ports="$(/usr/bin/cat allPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/' | xargs | tr ' ' ',')"
declare -a array_ports="( $(/usr/bin/cat allPorts | grep -oP '\d{1,5}/open' | awk '{print $1}' FS='/'| xargs) )"
ip_address="$(/usr/bin/cat allPorts | grep -oP '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' | sort -u | head -n 1)"

echo -e "\n${blueColour}-------------------------------------------------------------------------------------${endColour}\n"
echo -e "\t${greenColour}[*] IP   :${endColour} ${grayColour}$ip_address${endColour}"
echo -e "\t${greenColour}[*] Ports:${endColour} ${grayColour}$ports${endColour}"

echo -e "\n${blueColour}-------------------------------------------------------------------------------------${endColour}\n"

echo -e "${yellowColour}nmap -p$ports -sC -sV $ip_address -oN targeted${endColour}"
#nmap -p$ports -sC -sV $ip_address -oN targeted

echo -e "\n${blueColour}-------------------------------------------------------------------------------------${endColour}\n"




for port in "${array_ports[@]}";do
	if [ "$port" -eq "80" ];then


		echo -e "${yellowColour}wfuzz -c --hc=403,404 -w /usr/share/wordlists/dirb/common.txt -u 'wfuzz -c --hc=404 -w /usr/share/wordlists/dirb/common.txt -u "http://$ip_address/FUZZ" -t 45http://192.168.88.49/FUZZ' -t 35${endColour}"
	wfuzz -c --hc=404 -w /usr/share/wordlists/dirb/common.txt -u "http://$ip_address/FUZZ" -t 45

	echo -e "${yellowColour}dirsearch -u 'http://192.168.0.102/' -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e txt,php,html -f -t35${endColour}"
	dirsearch -u "http://$ip_address/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e txt,php,html -f -t 35



	elif [ "$port" -eq "3306" ]; then
		echo "mysql"
	fi
done

echo -e "\n${blueColour}-------------------------------------------------------------------------------------${endColour}\n"

