<html>
	<head>
		<meta charset="utf-8" lang="hu">
		<title>Raspberry weather station</title>
		<style>
			ul {
				width: 500px;
				list-style-type: none;
				margin: 0;
				padding: 0;
				overflow: hidden;
				background-color: #848484;
			}

			li {
				float: left;
			}

			li a {
				display: block;
				color: white;
				text-align: center;
				padding: 16px;
				text-decoration: none;
			}

			li a:hover {
				background-color: #2e2e2e;
			}

			li a:active {
				background-color: #08088a;
			}

			button {
				color: white;
				background-color: #848484;
			}
		</style>
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
	<label>Mérési időköz percben: <input type="number" name="time" id="time" min="1" max="5000" value="60"></label><br>
	<label>Tól (pl.: 2018-03-31 22:03:03): <input type="datetime" name="from" id="from" value="0"></label><br>
	<label>Ig (pl.: 2018-03-31 22:03:03): <input type="datetime" name="to" id="to" value="0"></label><br>
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
	exec('sudo killall weather.py');
}
else if (isset($_POST["start"])) {
	$time = "-t ". $_POST["time"];
	exec('sudo systemctl start weather@"'.$time.'"');
}
?>
</body>
</html>
