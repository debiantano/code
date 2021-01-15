#!/bin/bash

#COLOR
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
yellowColour="\e[0;33m\033[1m"

trap ctrl_c INT
function ctrl_c(){
        echo -e "\n${yellowColour}[*]${endColour}${greenColour} Saliendo ... ${endColour}"
        tput cnorm
        exit 0
}

tput civis; for port in $(seq 1 65535); do
        timeout 1 bash -c "echo > /dev/tcp/$1/$port" 2>/dev/null && echo "Port $port - OPEN" &
        done; wait; tput cnorm
