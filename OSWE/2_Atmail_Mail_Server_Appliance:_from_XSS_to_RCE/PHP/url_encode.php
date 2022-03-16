<?php
    function url_encode($string){
        return urlencode(utf8_encode($string));
    }
   
    function url_decode($string){
        return utf8_decode(urldecode($string));
    }

	echo url_encode("http://192.168.0.1/url?=file.php");
	echo "<br>";
	echo url_decode("http%3A%2F%2F192.168.0.1%2Furl%3F%3Dfile.php");
?>
