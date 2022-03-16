<form method="POST" enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>">
Subida de imagen: <input type="file" name="imagen"><br>
    <input type="hidden" name="formulario">
    <input type="submit" value="Subir archivo"><br>
</form>

<?php
    $resultado=null;
    if(isset($_POST["formulario"])){
        $name = $_FILES["imagen"]["name"];
        $tmp_file = $_FILES["imagen"]["tmp_name"];
        $error = $_FILES["imagen"]["error"];
        $size = $_FILES["imagen"]["size"];
        $max_size = 1024 * 1024 * 1;
        $type = $_FILES["imagen"]["type"];
    }

    echo $name . "<br>";
    echo $tmp_file . "<br>";
    echo $error . "<br>";
    echo $size . "<br>";
    echo $type . "<br>";
?>
