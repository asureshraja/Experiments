<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<style type="text/css">
<!--
body {
	background-image: url(my.jpg);
	color: #000;
	font-size: 10;
	font-weight: bold;
	font-family: "Adobe Caslon Pro";
	background-repeat: no-repeat;
}
.log {
	font-size: 16px;
	font-family: "Adobe Caslon Pro";
	color: #F00;
}
.password {
	color: #000;
}
.username {
	text-align: left;
}
.password blockquote p {
}
.password {
}
.user {
	text-align: left;
	font-family: "Adobe Caslon Pro";
}
.name {
	text-align: right;
	font-family: "Adobe Caslon Pro";
}
.date {
	text-align: left;
	font-family: "Adobe Caslon Pro";
}
.gender {
	text-align: left;
	font-family: "Adobe Caslon Pro";
}
.email {
	text-align: right;
	font-family: "Adobe Caslon Pro";
}
.password {
	text-align: left;
	font-family: "Adobe Caslon Pro";
}
.male {
	font-family: "Adobe Caslon Pro";
}
.female {
	font-family: "Adobe Caslon Pro";
}
.mm {
	font-family: "Adobe Caslon Pro";
}
male {
	font-family: "Adobe Caslon Pro";
}
.mm {
	font-family: "Adobe Caslon Pro";
}
.name {
	text-align: left;
}
.email {
	text-align: left;
}
.name {
	font-size: 18px;
}
.date {
	font-size: 18px;
}
.gender {
	font-size: 18px;
}
.email {
	font-size: 18px;
}
.pass {
	font-size: 18px;
}
body,td,th {
	font-size: 20px;
}
.mm {
	font-size: 18px;
}
.register {
	font-size: 24px;
}
.register {
	color: #C10173;
}
-->
</style>
<script type="text/javascript">
<!--
function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}
//-->
</script>
<script type="text/javascript">
function validateForm()
	{
	var a=document.forms["form2"]["name"].value;
	var b=document.forms["form2"]["age"].value;
	var c=document.forms["form2"]["username"].value;
	var d=document.forms["form2"]["password"].value;
	var e=document.forms["form2"]["confirm"].value;
	var f=document.forms["form2"]["email"].value;
if ((a==null || a=="") && (b==null || b=="") && (c==null || c=="") && (d==null || d=="") && (e==null || e=="") && (f==null || f==""))
	  {
	  alert("All Field must be filled out");
	  return false;
	  }
	if (a==null || a=="")
	  {
	  alert("name must be filled out");
	  return false;
	  }
	if (b==null || b=="")
	  {
	  alert("age must be filled out");
	  return false;
	  }
	if (c==null || c=="")
	  {
	  alert("username must be filled out");
	  return false;
	  }
	if (d==null || d=="")
	  {
	  alert("password must be filled out");
	  return false;
	  }
	if (e==null || e=="")
	  {
	  alert("confirm password must be filled out");
	  return false;
	  }
	if (f==null || f=="")
	  {
	  alert("email must be filled out");
	  return false;
	  }
		}
	</script>
</head>

<body>
<table width="101%" height="106" border="0">
  <tr>
    <th width="17%" height="102" scope="col"><img src="neew jus.png" width="200" height="100" /></th>
    <th width="83%" scope="col"><blockquote>
      <blockquote>
        <blockquote>
          <p>&nbsp;</p>
          </blockquote>
        </blockquote>
    </blockquote></th>
  </tr>
</table>
<p class="register">Registration</p>
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
                      <blockquote>
                        <p class="log">(password doesn't match)</p>
                      </blockquote>
                    </blockquote>
                  </blockquote>
                </blockquote>
              </blockquote>
            </blockquote>
          </blockquote>
        </blockquote>
      </blockquote>
    </blockquote>
  </blockquote>
</blockquote>
<form id="form2" name="form2" method="post" action="register.php" onsubmit="return validateForm();">
  <table width="72%" height="282" border="0">
    <tr>
      <th width="46%" scope="row">&nbsp;</th>
      <td width="23%">Name</td>
      <td width="31%"><label>
        <input name="name" type="text" id="textfield" maxlength="20" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>Age</td>
      <td><label>
        <input name="age" type="text" id="textfield2" maxlength="20" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>Username</td>
      <td><label>
        <input name="username" type="text" id="textfield3" maxlength="20" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>Password</td>
      <td><label>
        <input name="password" type="password" id="textfield4" maxlength="20" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>Confirm password</td>
      <td><label>
        <input name="confirm" type="password" id="textfield5" maxlength="20" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>Email</td>
      <td><label>
        <input name="email" type="text" id="textfield6" maxlength="30" />
      </label></td>
    </tr>
    <tr>
      <th scope="row">&nbsp;</th>
      <td>&nbsp;</td>
      <td><label>
        <input type="submit" name="button" id="button" value="Submit" />
      </label></td>
    </tr>
  </table>
</form>
<blockquote>
  <blockquote>
    <blockquote>
      <blockquote>
        <blockquote>
          <p class="log">&nbsp;</p>
        </blockquote>
      </blockquote>
    </blockquote>
  </blockquote>
</blockquote>
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
                      <blockquote>
                        <blockquote>
                          <blockquote>
                            <blockquote>
                              <blockquote>
                                <blockquote>
                                  <blockquote>&nbsp; </blockquote>
                                </blockquote>
                              </blockquote>
                            </blockquote>
                          </blockquote>
                        </blockquote>
                      </blockquote>
                    </blockquote>
                  </blockquote>
                </blockquote>
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
