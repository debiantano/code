#!/bin/bash

name1="John"
name2="Jason"

name_change(){
    local name1="Edward"
    echo "Dentro de esta funcion, nombre1 es $name1 y nombre2 es $name2"
    name2="Lucas"
}


echo "Antes de la llamada a la funcion, nombre1 es $name1 y nombre2 es $name2"
name_change
echo "Despues de la llamadaa la funcion, nombre1 es $name1 y nombre2 es $name2"
