
import base64

def js_to_b64(js_code: str) -> str:
    """Кодирует JS-строку в base64"""
    return base64.b64encode(js_code.encode('utf-8')).decode('utf-8')

def b64_to_js(b64_str: str) -> str:
    """Декодирует base64 обратно в JS (для отладки)"""
    return base64.b64decode(b64_str.encode('utf-8')).decode('utf-8')

def generate_level(decoded_payload: str, method: str = 'script_text') -> str:
    """Генерирует один уровень — код, который расшифровывает payload и выполняет его"""
    if method == 'script_text':
        # Создаёт <script> с текстом внутри
        return f'''(function() {{
    const payload = "{decoded_payload}";
    const decoded = atob(payload);
    const script = document.createElement('script');
    script.textContent = decoded;
    document.head.appendChild(script);
}})();'''

    elif method == 'blob':
        # Создаёт Blob и подключает через URL.createObjectURL
        return f'''(function() {{
    const payload = "{decoded_payload}";
    const decoded = atob(payload);
    const blob = new Blob([decoded], {{ type: 'text/javascript' }});
    const url = URL.createObjectURL(blob);
    const script = document.createElement('script');
    script.src = url;
    document.head.appendChild(script);
}})();'''

def generate_chain(final_code: str, levels: int = 3, method: str = 'script_text') -> str:
    """
    Генерирует цепочку из `levels` уровней.
    Каждый уровень — base64-код следующего.
    Возвращает стартовый JS-код (уровень 1).
    """
    if levels < 1:
        raise ValueError("Уровней должно быть >= 1")

    # Начинаем с финального кода
    current_code = final_code

    # Собираем цепочку с конца: от финала к старту
    for i in range(levels):
        # Кодируем текущий код в base64
        b64 = js_to_b64(current_code)
        # Генерируем код уровня, который будет его расшифровывать
        current_code = generate_level(b64, method)

    # После цикла current_code — это самый первый (стартовый) уровень
    return current_code

# ========================
# Пример использования
# ========================

if __name__ == "__main__":
    FINAL_CODE = 'alert("HelloWorld");'
    # FINAL_CODE = 'console.log("HelloWorld");'
    LEVELS = 10
    METHOD = 'script_text'  # или 'blob'

    print("🚀 Генерация цепочки самораспаковки...\n")

    start_code = generate_chain(FINAL_CODE, LEVELS, METHOD)

    print("✅ Стартовый JS-код (уровень 1):\n")
    print(start_code)
    exit()

    print(f"\n📦 Размер стартового кода: {len(start_code)} символов")

    # Для отладки: покажем, что внутри каждого уровня
    print("\n🔍 Отладка: содержимое уровней (после расшифровки)")

    temp_code = start_code
    for lvl in range(1, LEVELS + 1):
        print(f"\n--- Уровень {lvl} ---")
        # Извлекаем base64 строку между `payload = "` и `";`
        try:
            start_idx = temp_code.index('payload = "') + len('payload = "')
            end_idx = temp_code.index('";', start_idx)
            b64_payload = temp_code[start_idx:end_idx]
            decoded = b64_to_js(b64_payload)
            print(decoded)
            temp_code = decoded
        except Exception as e:
            print(f"Ошибка при парсинге уровня {lvl}: {e}")
            break

    print(f"\n🏁 Финальный уровень (уровень {LEVELS + 1}):")
    print(temp_code)