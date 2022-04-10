CONFIGURAR IDIOMA TECLADO
loadkeys la-latin1

WIFI
ip link
ip link set wlan0 up
iwlist wlan0 scan
wpa_passphrase ESSID PASSWORD > /etc/wifi
wpa_supplicant -B -i wlan0 -D wext -c /etc/wifi
dhclient

