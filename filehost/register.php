<?php
$name = $_POST['name'];
$age = $_POST['age'];
$username = $_POST['username'];
$password = $_POST['password'];
$confirm = $_POST['confirm'];
$email = $_POST['email'];
{
        if($password == $confirm)
        {
        include ('config1.php');
        $sql='INSERT INTO simple_login(name,age,username,password,confirm,email) VALUES ("'.$name.'", "'.$age.'","'.$username.'", "'.$password.'","'.$confirm.'", "'.$email.'")';
        $result=mysql_query($sql) or die(mysql_error());          
        include('main_login.php');     
        }
        else 
 include('registration1.php');
}
?>