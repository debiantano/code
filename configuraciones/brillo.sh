#!/bin/bash

echo "75" > /sys/class/backlight/intel_backlight/brightness && sysctl -w kernel.unprivileged_userns_clone=1
exit
