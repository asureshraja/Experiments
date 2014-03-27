<?php
$asd=$_GET['ttt'];
$file = fopen("chat.txt","w");
echo fwrite($file,$_GET['ttt']);
fclose($file);
?>
