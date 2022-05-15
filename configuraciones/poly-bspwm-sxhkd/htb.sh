#!/bin/sh

target=$(ifconfig | grep tun0 -A 1 | awk '{print $NF}' | awk NR==2)

if [ $target ]; then
    echo "%{F#e51d0b}ﲅ%{F#ffffff} $target%{u-}"
else
    echo "%{F#e51d0b}ﲅ %{u-}%{F#ffffff}"
fi
