ip=$1

# NMAP

nmap -p- --open --min-rate 5000 -n -vv -sS -Pn $ip -oG allPorts

extractPorts allPorts

nmap -p$ports -sC -sV $ip targeted


# WHATWEB
whatweb http://$ip -v

# ENUMERACION WEB 
wfuzz -c --hc=404 -w /usr/share/wordlists/dirb/common.txt -u "http://$ip/FUZZ" -t 50

dirsearch -u "http://172.17.0.2/cgi-bin/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e html,php,txt -f -t 35 -x 404
