<?php

$user = "root";
$pass = "";
$host = "localhost";

// CONECTARSE CON MYSQL (bool)
$connection = mysqli_connect($host, $user, $pass);

if(!$connection) {
    echo "No se ha podido conectar con el servidor" . mysql_error();
}else{
    echo "Hemos conectado al servidor <br>" ;
}
// SELECCIONAR BASE DE DATOS
$datab = "test";

// SELECCIONA LA DDBB POR DEFECTO PARA REALIZAR LAS CONSULTAS
$db = mysqli_select_db($connection,$datab);

if (!$db){
    echo "No se ha podido encontrar la Tabla";
}else{
    echo "Tabla seleccionada" ;
};

// QUERYS A LAS TABLAS
$consulta = "SELECT * FROM universidad";
$result = mysqli_query($connection,$consulta); // (V-F)

if(!$result){
    echo "No se ha podido realizar la consulta";
}

echo "<table>";
echo "<tr>";
echo "<th><h1>ID</th></h1>";
echo "<th><h1>Oficio</th></h1>";
echo "</tr>";

// REGRESAR UNA MATRIZ
while ($colum = mysqli_fetch_array($result))
 {
    echo "<tr>";
    echo "<td><h3>" . $colum['nombre']. "</td></h3>";
    echo "<td><h3>" . $colum['correo'] . "</td></h3>";
    echo "</tr>";
}
echo "</table>";


mysqli_close( $connection );
echo "Fuera" ;

?>
