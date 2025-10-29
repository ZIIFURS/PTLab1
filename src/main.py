# -*- coding: utf-8 -*-
import argparse
import sys
from pathlib import Path

from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.YamlDataReader import YamlDataReader
from src.PerfectStudentFinder import PerfectStudentFinder


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    parsed_args = parser.parse_args(args)
    return parsed_args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])
    file_path = Path(path)

    if not file_path.exists():
        print(f"Ошибка: Файл не найден: {path}")
        sys.exit(1)

    if file_path.suffix == ".txt":
        reader = TextDataReader()
        students = reader.read(path)
        print("Students: ", students)

        rating = CalcRating(students).calc()
        print("Rating: ", rating)

    elif file_path.suffix == ".yaml" or file_path.suffix == ".yml":
        reader = YamlDataReader()
        data = reader.read(path)
        finder = PerfectStudentFinder(data)
        result = finder.find()
        print("ВАРИАНТ 9: Студент с 90 баллами по ВСЕМ дисциплинам: ", result)

    else:
        print(f"Ошибка: Неизвестный формат файла: {file_path.suffix}")
        print("Поддерживаются: .txt и .yaml")
        sys.exit(1)


if __name__ == "__main__":
    main()
