<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<style type="text/css">
<!--
body {
	background-image: url(my.jpg);
	font-size: 24px;
	color: #000;
}
.log {
	font-family: "Adobe Caslon Pro";
	color: #C10173;
	font-size: 24px;
	font-weight: bold;
}
#form1 table tr th {
	font-family: "Adobe Caslon Pro";
	font-size: 18px;
}
.you {
	font-family: "Adobe Caslon Pro";
}
-->
</style>
<script type="text/javascript">
	function validateForm()
	{
	var a=document.forms["form1"]["username1"].value;
	var b=document.forms["form1"]["password1"].value;
	if ((a==null || a=="") && (b==null || b==""))
                   {
	  alert("All Field must be filled out");
	  return false;
	  }
	if (a==null || a=="")
	  {
	  alert("username must be filled out");
	  return false;
	  }
	if (b==null || b=="")
	  {
	  alert("password must be filled out");
	  return false;
	  }
	}
	</script></head>

<body>
<p><img src="neew jus.png" width="200" height="100" />
</p>
<blockquote>
  <blockquote>
    <blockquote>
      <blockquote>
        <blockquote>
          <blockquote>
            <blockquote>
              <blockquote>
                <blockquote>
                  <blockquote>
                    <blockquote>
                      <p class="you">you are successfully logged out</p>
                      <blockquote>
                        <blockquote>
                          <blockquote>
                            <p class="log"> LOG IN</p>
                          </blockquote>
                        </blockquote>
                      </blockquote>
                    </blockquote>
                  <form id="form1" name="form1" method="post" action="checklogin.php" onsubmit="return validateForm();">
                    <table width="108%" border="0">
                      <tr>
                        <th width="38%" scope="row">username</th>
                        <td width="62%"><label>
                          <input name="username1" type="text" id="textfield2" maxlength="20" />
                          </label></td>
                        </tr>
                      <tr>
                        <th scope="row">password</th>
                        <td><input name="password1" type="password" id="textfield" maxlength="20" /></td>
                      </tr>
                      <tr>
                        <th scope="row"><p>(not user?<a href="registration.php">register</a>)</p></th>
                        <td><label>
                          <p>
                            <input type="submit" name="button" id="button" value="Login" />
                          </p>
                        </label></td>
                        </tr>
                      </table>
                  </form>
                  </blockquote>
                </blockquote>
                <p>&nbsp; </p>
              </blockquote>
            </blockquote>
          </blockquote>
        </blockquote>
      </blockquote>
    </blockquote>
  </blockquote>
</blockquote>
</body>
</html>
