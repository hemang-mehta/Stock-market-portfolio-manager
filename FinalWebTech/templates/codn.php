<?php
$firstn = $_POST['firstn'];
$lastn = $_POST['lastn'];
$email = $_POST['email'];
$address = $_POST['address'];
$city = $_POST['city'];
$pc = $_POST['pc'];
$password = $_POST['password'];

$conn = new mysqli('localhost', 'root', '', 'patel');

if ($conn->connect_error) {
    die('Connection Failed: ' . $conn->connect_error);
}

$stmt = $conn->prepare("Insert into Registration(firstn, lastn, email, address, city, pc , password) VALUES ('$firstn','$lastn','$email','$address','$city','$pc','$password')");

if (!$stmt) {
    die('Prepare failed: ' . $conn->error);
}

$stmt->bind_param("sssssis", $firstn, $lastn, $email, $address, $pc, $city, $password);

if ($stmt->execute()) {
    echo "Registration successful";
} else {
    die('Execute failed: ' . $stmt->error);
}

$stmt->close();
$conn->close();
?>
