trap ctrl_c INT

tput civis

if [ "1" == "1" ]; then
        declare -r token=$1
        declare -r contador=$2
        declare -r main_url="http://192.168.0.105"

        echo
        for i in $(seq 1 $contador); do
                echo -en "[*] User [$i]:  "
                curl -s -H "$token" -X GET "$main_url/dvwa/vulnerabilities/sqli/?id=$i&Submit=Submit" | grep "First name" | awk '{print $3,$4}' | cut -d "<" -f 1
        done
else
        echo -e "\n[*] Uso: ./sqli.sh <token> <valor>\n"
fi

tput cnorm
