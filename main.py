from datetime import datetime
import random
from time import sleep
import os

base_path = os.getcwd() #путь, где лежит документ
print(base_path)
log_dir = "logs" #название каталога
file_name = "logs.txt" #название файла(который создастся

full_path = os.path.join(base_path, log_dir, file_name)
print(f"=====> {full_path}")

def file_worker(file_name: str, mode: str, data: str):
    with open(file_name, mode) as file:
        file.write(data)

for i in range(10):
    date_time = datetime.now()
    log_str = f"{date_time} - {random.randint(1, 1000)} \n"
    sleep(1)
    file_worker(full_path, "a", log_str)
