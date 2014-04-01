<form name="user" id="user">
<?php
session_start();
echo('<input type="hidden" name="username" id="username" value='.$_SESSION['username'].">");
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
    document.getElementById("ccc").innerHTML=xmlhttp.responseText;
    var obj = document.getElementById("ccc");
	obj.scrollTop = obj.scrollHeight;
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
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("GET","write.php?msg="+document.user.username.value+">"+document.sender.msg.value+"<br>",true);
xmlhttp.send();
}
</script>
<body onload="window.setInterval(function(){
show();
}, 500);">
</body>
<div id="ccc" style="overflow-y: auto; height:400px;width:400px;">
</div>
<form name="sender" method="GET" action="">
<input type="text" id="msg" name="msg"/>
<input type="button" value="send" onclick="dosend()"/>
</form>

</html>