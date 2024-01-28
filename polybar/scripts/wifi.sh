#!/bin/sh

target=$(ifconfig | grep eth0 -A 1 | tail -n 1 | xargs | cut -d ' ' -f 2)

if [ $target ]; then
    echo "%{F#8FBCBB}%{F#ffffff}  $target%{u-}"
else
    echo "%{F#8FBCBB} %{u-}%{F#ffffff} "
fi
