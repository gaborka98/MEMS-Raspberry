<html>
	<head>
		<meta charset="utf-8" lang="hu">
		<title>Raspberry weather station</title>
		<link rel="stylesheet" href="style.css">
	</head>
<body>
	<ul>
		<li><a href="all.html" target="iframe">All</a></li>
		<li><a href="avg.html" target="iframe">Average</a></li>
		<li><a href="min.html" target="iframe">Minimum</a></li>	
		<li><a href="max.html" target="iframe">Maximum</a></li>
	</ul><br>
	
<iframe scrolling="no" src="all.html" id="iframe" name="iframe" frameborder="none" heigth="410" width="510">grafikonok megjelenitése</iframe><br>
<button onclick="refresh()" id="refresh">1, refresh data</button>
<button onlick="reload()" id="reload">2, refresh page</button><br>
<?php
	function refresh() {
		$output shell_exec("python3 /home/pi/Project/plot.py");
		echo $output;
	}
	
	function reload() {
		header("Refresh:0");
	} ?>
</body>
</html>
