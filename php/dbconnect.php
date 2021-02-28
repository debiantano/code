<?php
$servername = "localhost";
$database = "test";
$username = "root";
$password = "";

//ESTABLECER UNA CONEXION CON MYSQL
$conn = mysqli_connect($servername, $username, $password, $database);

// SI LA CONEXION NO ES EXITOSA
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

// CERRAR LA CONEXION A MYSQL MANUALMENTE
mysqli_close($conn);
?>
