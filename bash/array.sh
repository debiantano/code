#!/bin/bash

numeros=(11 12 13 14 15)
declare -a cadenas=("ruby" "perl" "python3" "gcc")
cifrasLetras=({A..Z} {a..z} {0..9})

echo -e "\nMOSTRAR ELEMENTOS DEL ARRAY"
echo ${numeros[@]}
echo ${numeros[*]}

echo -e "\nACCEDER UN ELEMENTO DEL ARRAY"
echo ${numeros[1]}

echo -e "\nAÑADIR ELEMENTO"
numeros[5]=16
echo ${numeros[*]}


echo -e "\nINDICE DEL ARRAY"
echo ${!numeros[*]}

echo -e "\nCANTIDAD DE ELEMENTOS DEL ARRAY"
echo ${#numeros[@]}

echo -e "\nAHORRANDO TECLAS AL CREAR ARRAY"
echo ${cifrasLetras[*]}
