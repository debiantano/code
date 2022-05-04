#!/bin/bash

name=$(zenity --entry --title="ScreenShot" --ok-label="Ok" --cancel-label="Cancel" --text="Name")
ans=$?

if [ $ans -eq 0 ]; then
    scrot "$name.png" -s -e 'xclip -selection clipboard -t image/png -i $f'
else
    zenity --error --text="Missing name"
fi
