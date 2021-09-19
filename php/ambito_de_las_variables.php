<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Escribiendo en php</title>
</head>
<body>
    <?php
    
    $nombre="Jack";

        function dame_nombre(){
            global $nombre;
            $nombre="El nombre es " . $nombre;
        }

        dame_nombre();
        echo $nombre;

    ?>
</body>
</html>
