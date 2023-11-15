import json


def task(json_file_path='input.json') -> float:
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        product_sum = sum(item['score'] * item['weight']
                          for item in data if 'score' in item and 'weight' in item)
        return round(product_sum, 3)


print(task('input.json'))
