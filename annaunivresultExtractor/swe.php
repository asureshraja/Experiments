
<?php
$i=109530011;
echo "<table>";
while($i<=109530020)
  {
   $str = "http://schools9.com/triannagrade1808.aspx?htno=".$i;
$content = file_get_contents($str);

echo "<tr><td>";
$pos = strpos($content,"Hall Ticket No </td><td>");
echo substr($content,$pos+24,9)." ";
echo "</td><td>";
$pos = strpos($content,"Name </td><td>");
$pos1 = strpos($content,"</td></tr><tr><td><b> Course");
echo substr($content,$pos+14,$pos1-($pos+14))." ";
echo "</td>";
///////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"UCS62</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"UCS66</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"UCS67</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"UMA62</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"UMG65</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"USE63</td><td>");
echo substr($content,$pos+14,1);
echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"USE64</td><td>");
echo substr($content,$pos+14,1);

echo "</td>";
////////////////////////////////////////
////////////////////////////////////////
echo "<td>";
$pos = strpos($content,"USE68</td><td>");
echo substr($content,$pos+14,1);

echo "</td></tr>";
////////////////////////////////////////
   $i++;
echo "\n";
  }
echo"</table>";
?>
