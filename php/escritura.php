<?php
    $fichero=fopen("datos.txt","w");

    fputs($fichero, "Line1\n");
    fputs($fichero, "text end");
    fclose($fichero);

    echo "[*] Se ha escrito el fichero correctamente"

?>
