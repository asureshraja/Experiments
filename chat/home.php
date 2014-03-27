<form name="user" id="user">
<?php
session_start();
echo('welcome '.$_SESSION['username']);
?>
</input>
</form>
<html>
<script type="text/javascript">

function show()
{
xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("ttt").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","retrieve.php",true);
xmlhttp.send();
} 
function dosend()
{
var xmlhttp;
  xmlhttp=new XMLHttpRequest();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
   
    }
  }
xmlhttp.open("GET","write.php?ttt="+document.sender.ttt.value,true);
xmlhttp.send();

}
</script>
<body onload="self.setInterval(function(){show();dosend();},500);">
</body>

<div id="ccc" >
</div>
<form name="sender" method="GET" action="">
<textarea name="ttt" id="ttt" rows=15 cols=30>
</textarea>
</form>

</html>