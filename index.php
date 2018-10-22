<html>
	<head>
		<meta charset="utf-8" lang="hu">
		<title>Raspberry weather station</title>
		<link rel="stylesheet" href="style.css">
	</head>
<body bgcolor="darkgrey">
	<ul>
		<li><a href="all.html" target="iframe">All</a></li>
		<li><a href="avg.html" target="iframe">Average</a></li>
		<li><a href="min.html" target="iframe">Minimum</a></li>	
		<li><a href="max.html" target="iframe">Maximum</a></li>
	</ul><br>
	
<iframe scrolling="no" src="all.html" id="iframe" name="iframe" frameborder="none" height="410" width="510">grafikonok megjelenitése</iframe><br>
<form action="" method="post" id="buttons" name="buttons">
	<!--<label>Mérési időköz percben: <input type="number" name="time" id="time" min="1" max="5000" value="60"></label><br>
	<label>Fájl helye, neve, kiterjesztése: <input type="text" name="name" id="name" maxlength="150"></label><br>-->
	<button name="start" id="start">start</button><br>
	<button name="stop" id="stop">stop</button><br>
	<button name="refresh" id="refresh">refresh data</button><br>
</form>
<?php
if (isset($_POST["refresh"])) {
	exec('python3 /var/www/html/plot.py > /dev/null 2>/dev/null &');
	sleep(5);
	header("reload:0;");
}
else if (isset($_POST["stop"])) {
	// exec('touch /var/www/html/stop');
	exec('sudo systemctl stop weather.service');
}
else if (isset($_POST["start"])) {
	exec('sudo systemctl start weather.service');
	/* $time = $_POST["time"];
	$name = $_POST["name"];
	$n_arg = "";
	$t_arg = "";
	if ($time != 60) {
		$t_arg = " -t ";
	}
	else {
		$time = "";
	}
	if ($name != "") {
		$n_arg = " -o ";
	}
	echo $time, $t_arg;
	echo $name, $n_arg;
	TODO run fucking python script */
}
?>
</body>
</html>
