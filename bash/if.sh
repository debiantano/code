#!/bin/bash

read -p "What is your age?: " name

if [ $name -lt 19 ]; then
    echo "You are a minor"
else
    echo "You're of age"
fi
