<?php
// a CORS test
// put this on a remote server, different domain then your web client

// the CORS header
header("Access-Control-Allow-Origin: *");

$analog = rand(300,500);
$jsonData = "{\"a0\":\"$analog\"}";
echo $jsonData;
// prints: jsonp1232617941775({"symbol" : "IBM", "price" : "91.42"});

?>
