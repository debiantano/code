#!/bin/bash
ram=$(free -h | grep Mem | awk '{print $3}')
echo "$ram"

