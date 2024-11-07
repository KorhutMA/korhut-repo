import json


def task() -> float:
    total_sum = 0.0
    filename = "input.json"
    with open(filename) as file:
        data = json.load(file)
        for item in data:
            if 'score' in item and 'weight' in item:
                total_sum += item['score'] * item['weight']

    return round(total_sum, 3)

print(task())
