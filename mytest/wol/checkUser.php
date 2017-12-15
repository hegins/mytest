<?php

$servername = "localhost";
$username = "apache";
$password = "apache";
$dbname = "wolsystem";

$user = "";
$hostname = "";
$ret ="";

if ($_SERVER[ "REQUEST_METHOD"] == "GET")
{
        $user = test_intput($_GET["username"]);
        $hostname = test_intput($_GET["hostname"]);
}

function test_intput($data)
{
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
}

// ´´½¨Á¬½Ó
$conn = new mysqli($servername, $username, $password, $dbname);
// ¼ì²âÁ¬½Ó
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM host where hostname='$hostname'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
           $ret = "1";
		   ####主机名存在，查检是否已在线
         while($row = $result->fetch_assoc() ) {
           $ip=$row['ip'];
           $a = exec("sh scan.sh $ip"); 
           if($a == '1') { $ret = "2"; }   
        }

} else {
    $ret= "0";
}
$conn->close();

echo $ret;

?>
      
