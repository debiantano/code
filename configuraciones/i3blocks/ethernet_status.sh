#!/bin/sh
 
IFACE=$(/usr/sbin/ifconfig | grep wlan0 | awk '{print $1}' | tr -d ':')
 
if [ "$IFACE" = "wlan0" ]; then
        echo  " $(/usr/sbin/ifconfig | grep inet | grep "192.168.0" | awk '{printf $2}')  "
else
        echo " "
fi
