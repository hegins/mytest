

<?php
#数据库配置
$servername = "localhost";
$username = "apache";
$password = "apache";
$dbname = "wolsystem";

#字段信息
$ip = "";
$Cmac = "";
$Cname = "";
$user = "";
$position = "";
$server ="";
$OS ="";

if ($_SERVER[ "REQUEST_METHOD"] == "GET")
{
        $ip = test_intput($_GET["ip"]);
	$Cmac = test_intput($_GET["Cmac"]);
	$Cname = test_intput($_GET["Cname"]);
	$user = test_intput($_GET["user"]);
	$position = test_intput($_GET["position"]);
	$server = test_intput($_GET["server"]);
	$OS = test_intput($_GET["OS"]);

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

#操作语句
$sql = "INSERT INTO hostinfo (ip, Cmac, Cname, user, position, server, OS) VALUES ( '$ip', '$Cmac', '$Cname', '$user', '$position', '$server', '$OS' )";

if ($conn->query($sql) === TRUE) {
echo "<br><br><br><center><h1>添加成功</h1></center>";
echo "<br><br> <center> <a href='admintest.html'> <h2>确定<h2></a></center>";

} else {

    echo "<<br><br><br><center><h1>添加失败</h1></center>";
echo "<br><br> <center> <a href='admintest.html'> <h2>确定<h2></a></center>";

echo "Error: " .$sql ."<br>" .$conn->error ;


}
$conn->close();
?>
