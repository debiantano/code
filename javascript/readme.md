#### CallBack
> Recibir como parámetro a una función  
> Es una forma de asegurarnos de q un determinando codigo no se ejecuta hasta que otro codigo haya terminado de ejecutarse

### Modificar HTML
**getElementsByTagName()** acepta un nombre de etiqueta y devuelve una colección HTML en vivo de elementos con el nombre de etiqueta coincidente en el orden en que aparecen en el documento.

```
document.getElementsByTagName("button")[0].innerHTML="JAVASCRIPT";
document.getElementsByTagName("h1")[0].innerHTML="Found";
```

### Modificar los links
```
var links = document.getElementsByTagName("a");
for  (i=0; i<links.length; i++){
  links[i].href = "http://debiantano.github.io";
  links[i].innerHTML = "Link Modificado";
}
```


