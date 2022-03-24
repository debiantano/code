<!DOCTYPE html>
<html lang="es" dir="ltr">
  <head>
    <meta charset="utf-8">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </head>

    <script type="text/javascript">
      function inicializar(){
        var btnRojo;
        btnRojo = document.getElementById('btnRojo');
        btnRojo.addEventListener("click", btnRojoClick);
      }

      function btnRojoClick(){
        var titulo;
        titulo = document.getElementById("encabezado");
        titulo.style.color = "red";
      }
    </script>

  <body onload="inicializar()">
    <div class="container mt-3">
      <h1 id="encabezado">Eventos con javaScript</h1>
      <input type="button" class="btn btn-success" id="btnRojo" value="Color Rojo"/>
    </div>
  </body>
</html>
