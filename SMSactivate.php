<?php

include_once("smsactivateAPI.php");

$sms = new SMSActivate('14e8cA2940563A8c5358d135b4Abe74e'); //Создать экземпляр класса SMSActivate

// $freeSlots = $sms->getNumbersStatus(0, 'mts');

// $balance = $sms->getBalance();

// $freeSlots = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getNumbersStatus&country=0&operator=tele2');

// echo "Номеров любых: " . $freeSlots['ot']."\n";

$balance = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getBalance');
$number = file_get_contents('https://sms-activate.ru/stubs/handler_api.php?api_key=14e8cA2940563A8c5358d135b4Abe74e&action=getNumber&service=ot&forward=79160593452&operator=mts&country=0&freePrice=false');

echo $balance, "\n", $number;

?>