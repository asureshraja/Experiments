<?php
$dbh = mysql_connect("localhost","root","") or die("There was a problem with the database connection.");
    $dbs = mysql_select_db("feed", $dbh) or die("There was a problem selecting the categories.");



// Next, we'll run a query on the database to get the file out

$sql = "SELECT * FROM upload
            WHERE upload.id = ".$_GET['id'];
            
$result = mysql_query($sql);

// If the query was invalid or failed to return a result, an error is thrown

if(!$result || !mysql_num_rows($result)){
    echo "Invalid file chosen.";
    exit;
}

// Finally, we will send the file to the browser

$curr_file = mysql_fetch_assoc($result);

$size = $curr_file['size'];
$type = $curr_file['type'];
$name = $curr_file['name'];
$content = $curr_file['content'];

header("Content-length: ".$size."");
header("Content-type: ".$type."");
header('Content-Disposition: attachment; filename="'.$name.'"');
echo $content;
?>