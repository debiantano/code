<?php
    $cadena = 'Abril 15, 2003';
    $patrón = '/(\w+) (\d+), (\d+)/i';
    $sustitución = '${1}1,$3';
    echo preg_replace($patrón, $sustitución, $cadena);
    // Abril1,2003
?>
