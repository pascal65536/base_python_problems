import markdown
import sys


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Использование: {sys.argv[0]} входной_файл.md выходной_файл.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Подключаем расширения fenced_code и codehilite для поддержки блоков кода и подсветки
    html = markdown.markdown(text, extensions=['fenced_code', 'codehilite'])
    # html = markdown.markdown(text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Файл {input_file} успешно конвертирован в {output_file}")

# python md2html.py example.md example.html
