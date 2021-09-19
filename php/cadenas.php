<!doctype html>
<html>
<head>
  <title>Documento sin titulo</title>

<style>
  .resaltar{
    color: #F00;
    font-weight: bold;
  }
</style>
</head>

<body>
<?php
  $nombre="calamardo";

  $variable="casa";
  $variable2="CASA";
  $resultado=strcmp($variable,$variable2);
  $resultado2=strcasecmp($variable,$variable2);

  echo "<p class='resaltar'>Esto es un ejemplo de frase</p>";
  echo $nombre;

  // 1 -> falso; 0 -> verdadero
  echo "El resultado es " . $resultado;
  echo "El resultado es " . $resultado2;

 ?>

</body>
</html>
