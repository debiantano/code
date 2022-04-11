# CONFIGURAR IDIOMA TECLADO
loadkeys la-latin1

# WIFI
```
ip link
ip link set wlan0 up
iwlist wlan0 scan
wpa_passphrase ESSID PASSWORD > /etc/wifi
wpa_supplicant -B -i wlan0 -D wext -c /etc/wifi
dhclient
```

# PARTICIONES
```
cfdisk
seleccionar dos(porque estamos en una vm)
new 512M
new 55G
new 4.5G (swap)
type -> 82 Linuxswap solaris
write
yes
quit
lsblk
```

# FORMATEAR LAS PARTICIONES
```
mkfs.vfat -F 32 /dev/sda1
mkfs.ext4 /dev/sda2
mkswap /dev/sda3
swapon
```

# PAQUETES CON PACSTRAP
```
mount /dev/sda2 /mnt
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
pacstrap /mnt linux linux-firmware netwrokmanager  grub wpa_supplicant base base-devel nano dhcp
```

# COMPATIBILIDAD CON WIFI
```
pacstrap /mnt netctl dialog
```

# FSTAB
```
genfstab -U /mnt
genfstab -U /mnt > /mnt/etc/fstab
```

# INGRESO AL SISTEMA
```
arch-chroot /mnt
passwd (2710)
useradd -m noroot
ls /home
password noroot (noroot)
```

# GRUPO WHEEL
```
usermod -aG wheel noroot
pacman -S sudo
pacman -S vim nano
nano /etc/sudoers
(descomentar linea 82)
```

# ZONA HORARIA
```
timedatectl list-timezones | less (America/Lima)
ln -sf /usr/share/zoneinfo/America/Lima 7etc/localtime
```

```
nano /etc/locale.gen
(descomentar es_ES.UTF-8 UTF-8 (201))
locale-gen
```

# HORA
hwclock -w

# TECLADO
```
nano /etc/vconsole.conf 
KEYMAP=es
echo LANG=es_ES.UTF8 > /etc/locale.conf
```

# INSTALL GRUP
```
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
echo blackarch > /etc/hostname
nano /etc/hosts
127.0.0.1 localhost
::1	localhost
127.0.0.1 blackarch
```

# NEOFETCH
```
pacman -S neofetch

exit
umount -R /mnt
reboot now
[sacar el DVD]
```

# RED
systemctl start NetworkManager
systemctl enable NetworkManager
ping 8.8.8.8
systemctl start wpa_supplicant.service
systemctl enable wpa_supplicant.service

# AUR
pacman -S git
[como noroot]
mkdir -p Desktop/repos
cd !$
git clone https://aur.archlinux/paru-bin.git
cd [tab]
makepkg -si

# BLACK_ARCH
[directorio repos]
mkdir blackarch
cd !$
curl -O https://blackarch.org/strap.sh
./strap.sh [como root]
pacman -Sy
pacman -Sgg | grep blackarch
pacman -S impacket
pacman -S blackarch-bluetooth // ejemplo

INTERFAZ GRAFICA
pacman -S xorg xorg-server
pacman -S gnome

systemctl start gdm.service
systemctl enable gdm.service
pacman -S kitty

VMWARE TOOLS
pacman -S gtkmm
pacman -S open-vm-tools
pacman -S xf86-video-vmware xf86-input-vmmouse
systemctl enable vmtoolsd
reboot now

FONTS
wget http://fontlot.com/downfile/5baeb08d06494fc84dbe36210f6f0ad5.105610
https://dropbox.com/s/hrkub2yo9iapljz/icommon.zip?dl=0
paru -S nerd-fonts-jetbrains-mono ttf-font-awesome ttf-font-awesome-4 ttf-material-design-icons





