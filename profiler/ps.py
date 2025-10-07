import time
import psutil

def check():
    cpu_usage = psutil.cpu_percent(interval=1)  # процент загрузки за 1 секунду
    memory_info = psutil.virtual_memory()
    return cpu_usage, memory_info

while True:
    cpu_usage, memory_info = check()
    print(f"Загрузка процессора: {cpu_usage}%")
    memory_usage = memory_info.percent  # процент использования памяти
    total_memory = memory_info.total / (1024 ** 2)  # общее количество памяти в МБ
    used_memory = memory_info.used / (1024 ** 2)  # использованная память в МБ
    available_memory = memory_info.available / (1024 ** 2)  # доступная память в МБ

    print(f"Использование памяти: {memory_usage}%")
    print(f"Общая память: {total_memory:.2f} МБ")
    print(f"Использованная память: {used_memory:.2f} МБ")
    print(f"Доступная память: {available_memory:.2f} МБ")

    time.sleep(10)
