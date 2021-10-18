<?php

// $balance = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getBalance');
// Создаем номер телефона
$numberGet = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getNumber&service=ot&forward=0&operator=mts&ref=null&country=0&freePrice=false');

// делим вывод на id и номер телефона, стыкуем для записи в файл
$number = explode(":", $numberGet)[2];
$id = explode(":", $numberGet)[1];
$toFile = implode(" ", array($id, $number));
    
// создаем файл и пишем туда "id number", закрываем
$fd = fopen("telephones.txt", 'w+') or die("не удалось открыть файл");
fwrite($fd, $toFile);
fclose($fd);
?>