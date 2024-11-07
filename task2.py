import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [OrderedDict(row) for row in reader]

    # Сериализуем данные в JSON и записываем в файл
    with open(OUTPUT_FILENAME, mode='w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")