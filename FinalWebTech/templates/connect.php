<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if (isset($_POST['submit'])) {
    $firstn = $_POST['firstn'];
    $lastn = $_POST['lastn'];
    $email = $_POST['email'];
    $address = $_POST['address'];
    $city = $_POST['city'];
    $pc = $_POST['pc'];
    $password = $_POST['password'];

    $conn = new mysqli('127.0.0.1', 'root', '', 'patel');

    if ($conn->connect_error) {
        die('Connection Failed: ' . $conn->connect_error);
    }

    $stmt = $conn->prepare("INSERT INTO Registration (firstn, lastn, email, address, city, pc, password) VALUES (?, ?, ?, ?, ?, ?, ?");

    if (!$stmt) {
        die('Prepare failed: ' . $conn->error);
    }

    $stmt->bind_param("sssssis", $firstn, $lastn, $email, $address, $city, $pc, $password);

    if ($stmt->execute()) {
        echo "Registration successful";
    } else {
        die('Execute failed: ' . $stmt->error);
    }

    $stmt->close();
    $conn->close();
}
?>
