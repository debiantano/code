<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Escribiendo en php</title>
</head>
<body>
    <?php
    
    function incrementa_variable(){
        static $contador=0;
        $contador++;
        echo $contador . "<br>";
    }

    incrementa_variable();
    incrementa_variable();
    incrementa_variable();
    incrementa_variable();

    ?>
    
</body>
</html>
