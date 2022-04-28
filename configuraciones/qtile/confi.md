# DE FLOTANTE REGRESE A NO FLOTANTE
# ABRIR UNA APLICACION EN UN DETERMINADO PANEL

# WIFI
ip link
ip link set wlp6s0 up
nmcli dev wifi connect RODRIGO password B974Ab29#

# VIDEO
pacman -S xf86-video-vesa

# LIGHTDM
pacman -S lightdm lightdm-gtk-greeter
nano /etc/lightdm/lightdm.conf (line 62)
systemctl enable lightdm.service

# QTILE
pacman -S qtile

# PROG
firefox rofi code feh burpsuite neovim
lsd bat

# ZSH
pacman -S zsh
paru -S zsh-syntax-highlighting zsh-autosuggestions

# DRACULA
lxappearance

# SERVICIOS
openssh mysql apache php php-apache

# ERROR MYSQL (AL INICIAR)
systemctl stop mariadb 
rm -R /var/lib/mysql/*
mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
systemctl start mariadb



# INIT SERVICES
systemctl start httpd

# PHP (CONF ADD)
oadModule mpm_prefork_module modules/mod_mpm_prefork.so
oadModule php_module modules/libphp.so
ddHandler php-script php
nclude conf/extra/php_module.conf

# LIGHTDM
sudo pacman -S lightdm-gtk-greeter-settings
sudo nano /usr/share/themes/Default/gtk-3.0/gtk.css
Fondo imagen /etc/lightdm (path image)

# TMUX
tpm github
tmux themepack github

# FONTS FIREFOX
ttf-liberation ttf-dejavu // noto-fonts

# JAVA ERROR
pacman -sS java | grep jre
pacman -S jre17-openjdk
archlinux-java status
archlinux-java set java-17-openjdk

[17]
OpenJDK 64-Bit Server VM warning: Ignoring option --illegal-access=permit; support was removed in 17.0
Could not start Burp: java.lang.NullPointerException
set _JAVA_AWT_WM_NONREPARENTING=1 in /etc/profile.d/jre.sh
[no solucionado]

pacman -S man steghide cherrytree

# BURP SOLUCION
DESCARGAR BURP 2021.12.1 (releases portswiger)

# SCREESHOT
scrot
fzf github