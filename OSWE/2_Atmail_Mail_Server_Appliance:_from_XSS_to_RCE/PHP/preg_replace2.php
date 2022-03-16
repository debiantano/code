<?php
	function simplifyString($string){ 
	return preg_replace("/[^a-zA-Z0-9]/", "", $string); 
	}
	echo simplifyString("texto de prueba'$%");
?>
