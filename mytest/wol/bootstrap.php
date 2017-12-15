

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

$sql = "SELECT * FROM host where hostname='$hostname'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // 输出每行数据
    while($row = $result->fetch_assoc()) {
	$ip =  $row["ip"];
	$mac = $row["mac"];
    }
} else {
    echo '<meta http-equiv="refresh" content="0;url=http://helpme.cyberway.net.cn:8090/wol/index_res.html">';
}
$conn->close();

echo $ip;
//在线查询
$a = exec("sh scan.sh $ip");
echo $a;
if( $a == '1'){
echo "已经开机";
echo '<meta http-equiv="refresh" content="0;url=http://helpme.cyberway.net.cn:8090/wol/index2.html">';
exit;
}
if( $a == '0'){
$b = exec("python magic-packet.py $mac $ip");
echo '<meta http-equiv="refresh" content="0;url=http://helpme.cyberway.net.cn:8090/wol/index3.html">';

}
?>
