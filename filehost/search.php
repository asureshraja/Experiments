<?php
    mysql_connect("localhost", "root", "") or die("Error connecting to database: ".mysql_error());
    
     
    mysql_select_db("feed") or die(mysql_error());
  
?>
 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Search results</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
<table border="1">
 <tr>
    <th width="33%" scope="col">Filename</th>
    <th width="21%" scope="col">Filesize</th>
    <th width="46%" scope="col">Download</th>
  </tr>
<?php
    $query = $_GET['query'];
    
     
    $min_length = 3;
   
     
    if(strlen($query) >= $min_length){ 
         
        $query = htmlspecialchars($query);
       
        $query = mysql_real_escape_string($query);
       
         
        $raw_results = mysql_query("SELECT * FROM upload
            WHERE (`id` LIKE '%".$query."%') OR (`name` LIKE '%".$query."%')") or die(mysql_error());
             
        if(mysql_num_rows($raw_results) > 0){ // if one or more rows are returned do following
             
            while($results = mysql_fetch_array($raw_results)){
            
              //  echo "<p><h3>".$results['id']."</h3>".$results['name']."</p>";
               echo "<tr><td>".$results['name']."</td><td>".$results['size']." bytes</td><td>";
            echo "<a href= download.php?id=".$results['id'].">Download</td></tr></a><br>";
	 }
             
        }
        else{ 
            include('fetch1.php');
        }
         
    }
    else{
        include('fetch2.php');
    }
?>
</table>
</body>
</html>
