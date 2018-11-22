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
		<li><a href="custom.html" target="iframe">Custom</a></li>
	</ul><br>
	
<iframe scrolling="no" src="all.html" id="iframe" name="iframe" frameborder="none" height="410" width="510">grafikonok megjelenitése</iframe><br>
<form action="" method="post" id="buttons" name="buttons">
	<label>Tól (pl.: 2018-03-31 22:03:03): <input type="text" name="from" id="from" value="0"></label><br>
	<label>Ig (pl.: 2018-04-31 22:03:03): <input type="text" name="to" id="to" value="0"></label><br>
	<button name="Custom Graph" id="custom">Dátumok lekérdezése</button><br>
	<button name="refresh graph" id="refresh">Teljes lekérdezés</button><br>
</form>
<?php
if (isset($_POST["custom"])) {
    $from = $_POST["from"];
    $to = $_POST["to"];
    exec('python3 /var/www/html/plot.py "'. $from.'" "'.$to . '" > /dev/null 2>/dev/null &');
    sleep(3);
}
if (isset($_POST["refresh"])) {
	$command = escapeshellcmd('/var/www/html/test.py');
	shell_exec($command);
	exec('python3 /var/www/html/test.py > /dev/null 2>/dev/null &');
	sleep(5);
	header("reload:0;");
}
?>
</body>
</html>
