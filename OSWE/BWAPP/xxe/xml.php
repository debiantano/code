<?php
    $xml = simplexml_load_file('test.xml');
    echo "<pre>";
    print_r($xml);
  
    echo "EDAD PERSONA [0]" . "<br>";
    echo $xml->person[0]->age . "<br>";
    
    echo "NOMBrE PERSONA [1]" . "<BR>";
    ECHO $xml->person[1]->age;
?>
