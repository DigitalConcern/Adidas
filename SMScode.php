<?php

// Открываем файл для чтения, записываем в переменные id и номер(на всякий случай)), закрываем
$fd = fopen("telephones.txt", 'r') or die("не удалось открыть файл");
$numberGet = htmlentities(fgets($fd));
$number = explode(" ", $numberGet)[1];
$id = explode(" ", $numberGet)[0];
fclose($fd);

$fd = fopen("telephones.txt", 'a+') or die("не удалось открыть файл");

do {
    // получаем статус и код
    $format = 'https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getStatus&id=%d';
    $status = file_get_contents(sprintf($format, $id));

    // открываем файл и дозаписываем туда код, закрываем
    if (explode(":", $status)[0] == "STATUS_OK") {
        $toFile1 = " ";
        $toFile2 = explode(":", $status)[1];
        fwrite($fd, $toFile1);
        fwrite($fd, $toFile2);
    }
    sleep(2);

} while(explode(":", $status)[0] != "STATUS_OK");
fclose($fd);

// пишем на сервак что все збс
// file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=setStatus&status=6&id=$id'); // &forward=79160593452
// echo $status
?>