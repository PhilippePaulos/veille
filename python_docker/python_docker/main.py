import argparse
from typing import Tuple, Any


def get_args() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="user's name")
    parser.add_argument("--file", help="file's path")
    args = parser.parse_args()
    return args.name, args.file


def print_hi(input_name):
    print(f'Hi, {input_name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_file(path):
    with open(path) as file:
        print(file.read())


if __name__ == '__main__':
    name, file_path = get_args()

    print_hi(name)
    print_file(file_path)

