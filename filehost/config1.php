<?php
$host['host'] = 'localhost';                // my host
$host['username'] = 'root';       // my database username
$host['password'] = '';   // my database password
$host['databasename'] = 'simple_login';       // my database name

$db = mysql_connect($host['host'], $host['username'], $host['password']) OR die ('Cant connect to the database');
mysql_select_db($host['databasename'], $db);
?>