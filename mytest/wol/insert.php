

<?php
$servername = "localhost";
$username = "apache";
$password = "apache";
$dbname = "wolsystem";

$user = "";
$hostname = "";
$ip = "";
$mac = "";

if ($_SERVER[ "REQUEST_METHOD"] == "GET")
{
        $user = test_intput($_GET["username"]);
        $hostname = test_intput($_GET["hostname"]);
        $ip = test_intput($_GET["ip"]);
	$mac = test_intput($_GET["mac"]);
}

function test_intput($data)
{
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
}

// 创建连接
$conn = new mysqli($servername, $username, $password, $dbname);
// 检测连接
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "INSERT INTO host ( user,  hostname, ip, mac) VALUES ( '$user', '$hostname', '$ip', '$mac' )";

if ($conn->query($sql) === TRUE) {
echo "<br><br><br><center><h1>添加成功</h1></center>";
echo "<br><br> <center> <a href='admin.html'> <h2>确定<h2></a></center>";

} else {

    echo "<<br><br><br><center><h1>添加失败</h1></center>";
echo "<br><br> <center> <a href='admin.html'> <h2>确定<h2></a></center>";

echo "Error: " .$sql ."<br>" .$conn->error ;


}
$conn->close();
?>
