### openITCOCKPIT 3.7.2

```
wget https://github.com/nice-registry/all-the-package-names/raw/master/names.json
jq '.[0:10000]' names.json | grep ","| cut -d'"' -f 2 > npm-10000.txt
gobuster dir -w ./npm-10000.txt -u https://openitcockpit/js/vendor/ -k
```

#### Salida de GoBuster
```
kali@kali:~$ cat packages.txt 
https://openitcockpit/js/vendor/fineuploader https://openitcockpit/js/vendor/gauge 
https://openitcockpit/js/vendor/gridstack https://openitcockpit/js/vendor/lodash 
https://openitcockpit/js/vendor/UUID.js-4.0.3 
https://openitcockpit/js/vendor/bootstrap-daterangepicker
```

#### Busqueda de README.md
```
> while read line; do echo "===$line==="; gobuster dir -w /usr/share/seclists/Discovery/Web-Content/quickhits.txt -k -q -u $l; done < packages.txt
```

#### PAQUETES CON README.md
```
> cat packages.txt
https://openitcockpit/js/vendor/gridstack 
https://openitcockpit/js/vendor/lodash 
https://openitcockpit/js/vendor/bootstrap-daterangepicker
```

#### VERSION DEL PAQUETE
```
while read line; do echo "===$line==="; curl $line/README.md -k; done < packages.txt
```

#### Descarga del paquete
```
• UUID.js: https://github.com/LiosK/UUID.js/archive/v4.0.3.zip 
• Lodash: https://github.com/lodash/lodash/archive/3.9.3.zip 
• Gridstack: https://github.com/gridstack/gridstack.js/archive/v0.2.3.zip 
```

#### Busqueda de posible XSS
```
> find ./ -iname "*.html"
grep -r "document.write" ./ --include *.html
```

