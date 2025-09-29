#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Рекурсивный обход каталога, объединение всех *.py, *.html, *.css, *.js файлов
в один «bigfile.txt».  Файлы, лежащие в каталогах, начинающихся с точки
(.git, .venv и т.д.), игнорируются.  Каждый блок текста начинается строкой
с названием файла (относительно корневого каталога).

Использование:
    python merge_files.py /путь/к/директории   # результат в ./merged.txt
"""

import os
import sys
from pathlib import Path

# ---------- Конфигурация ----------
EXTENSIONS = {".py", ".html", ".css", ".js"}      # какие файлы читать
OUT_FILE   = "merged.txt"                         # имя итогового файла
ENCODING   = "utf-8"                              # кодировка исходных файлов

# -----------------------------------


def should_skip_dir(dir_name: str) -> bool:
    """
    Возвращает True, если каталог начинается с точки.
    """
    return '.' in dir_name


def collect_files(root: Path):
    """
    Генератор, отдающий (relative_path, absolute_path)
    для всех подходящих файлов в дереве root.
    """
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in EXTENSIONS:
            yield path.relative_to(root), path.resolve()


def merge_files(src_root: Path, dst_path: Path):
    """Объединяет файлы из src_root в один файл dst_path."""
    with dst_path.open("w", encoding=ENCODING) as out_f:
        for rel_path, abs_path in collect_files(src_root):
            # Заголовок
            # out_f.write(f"\n=== {rel_path.as_posix()} ===\n\n")
            out_f.write(f"\n\n{rel_path.as_posix()}\n\n")
            with abs_path.open("r", encoding=ENCODING) as f:
                fr = f.read()
                fr = ' '.join(fr.split())
                out_f.write(fr)
    print(f"Готово: {dst_path}")


def main():
    if len(sys.argv) < 2:
        print("Использование: python merge_files.py /путь/к/директории")
        sys.exit(1)

    src_root = Path(sys.argv[1]).resolve()
    if not src_root.is_dir():
        print(f"Ошибка: {src_root} – не каталог")
        sys.exit(2)

    # Перезаписать существующий файл, если нужно
    dst_path = src_root / OUT_FILE

    merge_files(src_root, dst_path)


if __name__ == "__main__":
    main()
