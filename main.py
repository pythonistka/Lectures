from datetime import datetime
import random
from time import sleep
import os

base_path = os.getcwd() #путь, где лежит документ (если путь не указывать, файл создастся в той же папке, где лежит сам проект
print(base_path)
log_dir = "logs" #название каталога
file_name_utf = "log_utf.txt" #название файла(который создастся)
file_name_cp = "log_cp.txt"

full_path_utf = os.path.join(base_path, log_dir, file_name_utf)
full_path_cp = os.path.join(base_path, log_dir, file_name_cp)


def file_worker(file_name: str, mode: str, encoding: str, data: str): # ввели переменную для смены кодировки
    with open(file_name, mode, encoding=encoding) as file:
        file.write(data)

file_worker(full_path_utf, "w", 'utf-8', 'Привет') # создали файл в папке Logs в кодировке utf-8
file_worker(full_path_cp, "w", 'cp1251', 'Привет') # создали файл в папке Logs в кодировке cp1251

