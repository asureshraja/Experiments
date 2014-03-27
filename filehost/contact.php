<?php
$email = $_POST['email'];
$subject = $_POST['subject'];
$query = $_POST['query'];
{
        include ('config2.php');
        $sql='INSERT INTO feedback(email,subject,query) VALUES ("'.$email.'", "'.$subject.'","'.$query.'")';
        $result=mysql_query($sql) or die(mysql_error());          
        include('sent.php');     
        }

?>