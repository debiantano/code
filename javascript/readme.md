#### CallBack
> Recibir como parámetro a una función  
> Es una forma de asegurarnos de q un determinando codigo no se ejecuta hasta que otro codigo haya terminado de ejecutarse

### 1. Modificar HTML
**getElementsByTagName()** acepta un nombre de etiqueta y devuelve una colección HTML en vivo de elementos con el nombre de etiqueta coincidente en el orden en que aparecen en el documento.

```
document.getElementsByTagName("button")[0].innerHTML="JAVASCRIPT";
document.getElementsByTagName("h1")[0].innerHTML="Found";
```

### 2. Modificar los links
```
var links = document.getElementsByTagName("a");
for  (i=0; i<links.length; i++){
  links[i].href = "http://debiantano.github.io";
  links[i].innerHTML = "Link Modificado";
}
```

### 3. Hijack form submit
### 4. Modify form fields
### 5. Ingenieria social
### 6. Capture all clicks
### 7. Keystroke logging
### 8. Event listener
### 9. Include external
### 10. Include external js using
### 11. Solution replace banner
### 12. Solution Stealing from autocomplete
### 13. Posting with xmlHTTPrequest
### 14. Fetching data with xmlHTTPrequest
### 15. Data exfiltration with xmlHTTPrequest
### 16. Extraching CSRF tokens
### 17. CSRF token stealing
### 18. HTML parsing of xmlHTTPrequest response
### 19. Solution multilevel html parsing
### 20. Solution multilevel js parsing
### 21. Solution multilevel xml parsing

