#### Teclado español
```
> sudo setxkbmap -layout 'es,es' -model pc105
> setxkbmap latam
----
loadkeys la-latin1
```

#### Cerrar sesion
```
sudo pkill -KILL -u <user>
```

#### Explorador de archivos
```nautilus - caja - thunar```

----

### Teclado Ubuntu Server
```
sudo dpkg-reconfigure keyboard-configuration
Generix 105-key PC
Spanish
latinoAmerica
No compose key
```

### Error hey
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <ERROR> 
```
