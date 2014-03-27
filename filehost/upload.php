<?php
if(isset($_POST['upload']) && $_FILES['fileField']['size'] > 0)
{
$fileName = $_FILES['fileField']['name'];
$tmpName  = $_FILES['fileField']['tmp_name'];
$fileSize = $_FILES['fileField']['size'];
$fileType = $_FILES['fileField']['type'];

$fp      = fopen($tmpName, 'r');
$content = fread($fp, filesize($tmpName));
$content = addslashes($content);
fclose($fp);

if(!get_magic_quotes_gpc())
{
    $fileName = addslashes($fileName);
}

include ('config.php');
include ('opendb.php');

$query = "INSERT INTO upload (name, size, type, content ) ".
"VALUES ('$fileName', '$fileSize', '$fileType', '$content')";

mysql_query($query) or die('Error, query failed');
include ('closedb.php');

include('feed1.php');
}
?>