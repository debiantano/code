<?php
        include("user.class.php");

        if(!isset($_COOKIE['user'])) {
                setcookie("user", base64_encode(serialize(new User('TUXITO'))));
        } else {
                unserialize(base64_decode($_COOKIE['user']));
        }
        echo " Esta es una prueba beta para un nuevo controlador de cookies\n";
?>

