import json
import math
from collections import defaultdict, Counter
from typing import List

import pandas as pd
import requests


def compute_square(data: List[int]) -> List[int]:
    return [nb * nb for nb in data]


def compute_celsius(data: List[float]) -> List[float]:
    def convert(nb: float) -> float:
        return (nb - 32) * 5 // 9

    return list(map(convert, data))


def count_occurences_default_dict(data: str) -> dict[str, int]:
    dict_result = defaultdict(int)
    for d in data.split(" "):
        dict_result[d] = dict_result[d] + 1
    return dict(dict_result)


def count_occurences(data: str) -> dict[str, int]:
    c = Counter(data.split())
    return dict(c)


def inspect_file(file_path: str):
    with open(file_path) as file:
        lines = file.readlines()
    num_lines = len(lines)
    num_words = sum((len(line.split()) for line in lines))
    num_chars = sum((len(line) for line in lines))
    print(f"Num lines: {num_lines}, Num words: {num_words}, Num chars: {num_chars}")


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return self.radius * self.radius * math.pi

    def compute_perimeter(self):
        return self.radius * 2


def compute_circle():
    c = Circle(10)
    print(f"Circle of radius: {c.radius} has an area of {c.compute_area()} and a perimeter of {c.compute_perimeter()}")


def compute_dataframe():
    def compute_df(row):
        return (row['B'] + row['C']) / row['A']

    df = pd.DataFrame([[1, 1, 2]], columns=["A", "B", "C"])
    df['D'] = (df['B'] + df['C']) / df['A']
    print(df)

    df['D'] = df.apply(compute_df, axis=1)
    print(df)


def request_api():
    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    if result.status_code == 200:
        data = json.loads(result.content)
        print(f'The max id is: {max((d["id"]for d in data))}')
    else:
        raise Exception('Could not load API')


if __name__ == '__main__':
    print(f'Square result = {compute_square([1,2,3,4,5])}')
    print(f'Celsius result: {compute_celsius([32, 212, 98.6])}')
    print(f'Occurences: {count_occurences("apple banana apple strawberry banana lemon")}')
    inspect_file('../Pipfile')
    compute_circle()
    compute_dataframe()
    request_api()
