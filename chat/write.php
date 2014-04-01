<?php
$file = fopen("chat.txt","a");
echo fwrite($file,$_GET['msg']);
fclose($file);
?>
