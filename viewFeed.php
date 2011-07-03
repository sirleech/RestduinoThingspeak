<html>
<?php 

$feed = htmlspecialchars($_GET["feed"]);
$hours = htmlspecialchars($_GET["hours"]);
$points = $hours*60;

echo "
<iframe width=1000 height=500 style=\"border: 1px solid #cccccc;\" src=\"http://api.thingspeak.com/channels/$feed/charts/1?results=$points&width=900&height=400&dynamic=true\"></iframe>";
?>
</html>