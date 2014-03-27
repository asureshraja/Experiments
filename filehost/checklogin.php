<?php
$host="localhost"; // Host name
$username="root"; // Mysql username
$password=""; // Mysql password
$db_name="simple_login"; // Database name
$tbl_name="simple_login"; // Table name
mysql_connect("$host", "$username", "$password")or die("cannot connect");
mysql_select_db("$db_name")or die("cannot select DB");
$username1=$_POST['username1'];
$password1=$_POST['password1'];
$sql="SELECT username,password FROM simple_login WHERE username='$username1' and password='$password1'";
$result=mysql_query($sql);
$count=mysql_num_rows($result);
if($count==1)
{
include('home.php');
}
else
 {
include('main_login1.php');
}
?>