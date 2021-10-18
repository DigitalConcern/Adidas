import subprocess
import os
from json import JSONDecoder


def php_script_runner(script_path):
    p = subprocess.Popen(['D:/Program Files/PHP/php.exe', script_path], shell=True)
    result = p.communicate()[0]
    return result


php_script_runner('SMSactivate.php')
