<?php
// a jsonP test
// put this on a remote server, different domain then your web client

$analog = rand(300,500);
$jsonData = "{\"a0\":\"$analog.\"}";
echo $_GET['callback'] . '(' . $jsonData . ');';
// prints: jsonp1232617941775({"symbol" : "IBM", "price" : "91.42"});

?>
