<!doctype html>
<html>
    <head>
    <title>Documento sin título</title>
    </head>

    <body>

    <?php
        $db_host = "localhost";
        $db_nombre = "dvwa";
        $db_usuario = "noroot";
        $db_pass = "noroot";

        $conexion = mysqli_connect($db_host, $db_usuario, $db_pass, $db_nombre);
        $consulta = "SELECT * FROM users";

        $resultados = mysqli_query($conexion, $consulta);
        $fila = mysqli_fetch_row($resultados);

        echo $fila[0] . " ";
        echo $fila[1] . " ";
        echo $fila[2] . " ";
        echo $fila[3] . " ";
        echo $fila[4] . " ";
        echo $fila[5] . " ";
        echo $fila[6] . " ";
        echo $fila[7] . " ";

    ?>

    </body>
</html>
