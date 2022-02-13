#!/bin/sh

# Set Session Name
SESSION="OSCP"
SESSIONEXISTS=$(tmux list-sessions | grep $SESSION)

# Only create tmux session if it doesn't already exist
if [ "$SESSIONEXISTS" = "" ]
then
    # Start New Session with our name
    tmux new-session -d -s $SESSION

    tmux rename-window -t 1 'VPN'
    tmux send-keys -t 'VPN' 'cd /home/noroot/Descargas/vpn' C-m "clear" C-m

    tmux new-window -t $SESSION:2 -n 'HACK'
    tmux send-keys -t 'HACK' "cd /home/noroot/boxes/" C-m "clear" C-m # Switch to bind script?

    tmux new-window -t $SESSION:3 -n 'TRIX'
    tmux send-keys -t 'TRIX' "cd /home/noroot/km4l30n/CHEATSHEET/" C-m "clear" C-m
fi

# Attach Session
tmux attach-session -t $SESSION:1
