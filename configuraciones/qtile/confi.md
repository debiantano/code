WINDOWS 10 INSTALL
C y D (formateado)

> loadkeys la-latin1

> cfdisk /dev/nvme0n1-pX
512M	->	boot
27G	->	/ home
2.5G	->	SWAP

> mkfs.vfat -F 32 /dev/nvme0n1p5

> mkfs.ext4 /dev/nvme0n1p6
> mkswap /dev/nvme0n1p7
> swapon /dev/nvme0n1p5

> mount /dev/nvme0n1p6 /mnt
> mkdir /mnt/boot
> mount /dev/nvme0n1p5 /mnt/boot

> mkdir -p /mnt/win/DATOS
> mount /dev/nvme0n1p3 /mnt/win/DATOS

> pacstrap /mnt linux linux-firmware networkmanager grub wpa_supplicant base base-devel nano dhcp os-prober ntfs-3g

> genfstab -U /mnt
> genfstab -U /mnt > /mnt/etc/fstab

[#SYSTEM]
> arch-chroot /mnt
> passwd (2710)
> useradd -m noroot
> ls /home
> password noroot (noroot)
> systemctl enable NetworkManager

> usermod -aG wheel noroot
> pacman -S sudo
> pacman -S vim nano
> nano /etc/sudoers
(descomentar linea 82)

> ln -sf /usr/share/zoneinfo/America/Lima /etc/localtime
> nano /etc/locale.gen
(descomentar (214))
> hwclock -w
> nano /etc/vconsole.conf 
KEYMAP=es
echo LANG=es_ES.UTF-8 > /etc/locale.conf
> export LANG=es_PE.UTF-8
> locale-gen

> grub-install /dev/sda
> grub-mkconfig -o /boot/grub/grub.cfg
> echo blackarch > /etc/hostname
> nano /etc/hosts
127.0.0.1 localhost arch
::1	localhost

> pacman -S neofetch

> nano /etc/default/grub
(ultima linea)
> pacman -S git
> git clone https://aur.archlinux.org/paru-bin.git
> cd [tab]
> makepkg -si
> paru -S update-grub

> exit
> umount -R /mnt
> swapoff /dev/nvme0n1p7
> reboot now
[sacar el DVD]

[DESPUES DE ESTAR INSTALADO]
[VIDEO]
pacman -S xf86-video-vesa
pacman -S xf86-video-intel intel-ucode

[XORG]
xorg-server xorg-xinit mesa mesa-demos

qtile tmux rofi code feh wget gnome-terminal p7zip thunar man lxappearance scrot
[LIGHTDM]
lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings
nano /etc/lightdm/lightdm.conf (line 62)
systemctl enable lightdm.service

[NERDFONTS]
Hack Nerd Fonts download
cd /usr/share/fonts
7z x [HNF]

[ROFI]
rofi -show drun -show-icons

[FUENTES FIREFOX]
pacman -S noto-fonts // ttf-liberation ttf-dejav
Extension: traductor,foxyproxy,adblock

[ZSH]
pacman -S zsh bat lsd
paru -S zsh-syntax-highlighting zsh-autosuggestions
powerlevel10k
[zshrc conf]
fzf github

[TMUX]
github themes tmux

[NANO]
.nanorc 
/etc/nanorc (243)

[BRILLO]
echo 75 > /sys/class/backlight/intel_backlightbrightness

------------------------

[BLACKARCH]
mkdir blackarch 
cd !$
curl -O https://blackarch.org/strap.sh
./strap.sh
[como root]
pacman -Sy pacman -Sgg | grep blackarch 
pacman -S impacket 
pacman -S blackarch-bluetooth // ejemplo

pacman -S burpsuite python-pip impacket netcat wireshark-qt nmap html2text whatweb openvpn crackmapexec dirsearch wfuzz ffuf mousepad
man steghide cherrytree neovim openssh

[DRACULA]
gtk icons

[PHP]
> pacman -S php php-apache
> nano /etc/httpd/conf/httpd.conf
LoadModule mpm_prefork_module modules/mod_mpm_prefork.so (67)
LoadModule php_module modules/libphp.so
Include conf/extra/php5_module.conf (final de archivo)

[MySQL]
pacman -S mysql
mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql


[APACHE]
pacman -S apache
systemctl start httpd

[WIFI CONNECT]
nmcli dev wifi list
nmcli dev wifi connect RODRIGO password "B974Ab29#"

[JAVA ERROR]
pacman -sS java | grep jre
pacman -S jre17-openjdk
archlinux-java status
archlinux-java set java-17-openjdk
DESCARGAR BURP 2021.12.1 (releases portswiger

