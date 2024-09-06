import time

# Словарь для хранения времени последнего вызова функции для каждого пользователя
last_call_times = {}


def limit_calls_per_minute(user_id, max_calls_per_minute):
    current_time = time.time()
    print(last_call_times)

    if user_id in last_call_times:
        time_diff = current_time - last_call_times[user_id]
        if time_diff < 60:
            if last_call_times[user_id] == current_time:
                print("Вызов функции слишком частый. Попробуйте позже.")
                return False
            elif time_diff < 60 / max_calls_per_minute:
                print(
                    f"Превышен лимит вызовов функции. Подождите {60 / max_calls_per_minute - time_diff} секунд."
                )
                return False

    last_call_times[user_id] = current_time
    return True


# Пример использования
user_id = "user123"
max_calls_per_minute = 5

i = 0
while i < 20:
    time.sleep(1)
    if limit_calls_per_minute(user_id, max_calls_per_minute):
        print(f"Вызов функции {i}")
        i += 1
