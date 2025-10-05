import os

def collect_files_to_one(output_file, root_dir):
    # Расширения файлов для сбора
    extensions = {'.js', '.html', '.css', '.md', '.py'}
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for subdir, _, files in os.walk(root_dir):
            if '.venv' in subdir:
                continue
            for filename in files:
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    file_path = os.path.join(subdir, filename)
                    out_f.write(f"=== Path: {file_path} ===\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8') as in_f:
                            content = in_f.read()
                        out_f.write(content + "\n\n")
                    except Exception as e:
                        out_f.write(f"Error reading file: {e}\n\n")

if __name__ == '__main__':
    root_directory = '/home/pascal65536/Загрузки/course'  # Можно изменить на путь к нужной папке
    output_filename = 'collected_files.txt'
    collect_files_to_one(output_filename, root_directory)
    print(f"Сборка файлов завершена. Итог записан в {output_filename}")
