<?php


// Открываем файл для чтения, записываем в переменные id и номер(на всякий случай)), закрываем
$fd = fopen("telephones.txt", 'r') or die("не удалось открыть файл");
$numberGet = htmlentities(fgets($fd));
$number = explode(":", $numberGet)[1];
$id = explode(":", $numberGet)[0];
fclose($fd);

// получаем статус и код
$status = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getStatus&id=$id');

// открываем файл и дозаписываем туда код, закрываем
$fd = fopen("telephones.txt", 'a+') or die("не удалось открыть файл");
$toFile = implode(" ", explode(":", $status)[1]);
fwrite($fd, $toFile);    
fclose($fd);

// пишем на сервак что все збс
file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=setStatus&status=6&id=$id&forward=79160593452');

?>