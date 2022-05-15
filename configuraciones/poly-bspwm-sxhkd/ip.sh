#!/bin/sh

target=$(ifconfig | grep eth0 -A 1 | awk '{print $NF}' | awk NR==2)

if [ $target ]; then
    echo "%{F#e51d0b}%{F#ffffff} $target%{u-}"
else
    echo "%{F#e51d0b} %{u-}%{F#ffffff} No target"
fi
