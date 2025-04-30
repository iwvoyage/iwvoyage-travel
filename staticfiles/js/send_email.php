<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST["name"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];
    $destination = $_POST["destination"];
    $date = $_POST["date"];
    $travelers = $_POST["travelers"];
    $message = $_POST["message"];

    $to = "your-email@example.com"; // Change this to your email
    $subject = "New Travel Inquiry";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nDestination: $destination\nTravel Date: $date\nNumber of Travelers: $travelers\nMessage: $message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Inquiry submitted successfully.";
    } else {
        echo "Error sending inquiry.";
    }
}
?>
