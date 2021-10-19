import subprocess
import time
import os
from json import JSONDecoder

struct = {
    'id': 'null',
    'telephone': 'null', # Структура должна быть сформирована в main.py
    'code': ''
}


def php_script_runner(script_path):
    p = subprocess.Popen(['D:/Program Files/PHP/php.exe', script_path], shell=True) # Скрипт запуска .php
    p.wait()


def code_receiver(p_struct):
    php_script_runner('D:/Programms/SMSactivate/SMScode.php')
    string_from_file = open('telephones.txt', encoding='utf-8').readline() # ф-ция вызова php файла с кодом для принятия кода
    if string_from_file.split(' ')[2] != '':                               # и записи в структуру
        p_struct['code'] = string_from_file.split(' ')[2]


def telephone_receiver(p_struct):
    php_script_runner('D:/Programms/SMSactivate/SMSactivate.php')
    string_from_file = open('telephones.txt', encoding='utf-8').readline() # ф-ция вызова php файла с кодом для принятия телефона
    p_struct['id'] = string_from_file.split(' ')[0]                        # и id и записи в структуру
    p_struct['telephone'] = string_from_file.split(' ')[1]


telephone_receiver(struct)
print(struct)
code_receiver(struct)
print(struct)
