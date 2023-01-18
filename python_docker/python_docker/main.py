import argparse
import os


def get_args() -> tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="user's name")
    parser.add_argument("--file", help="file's path")
    args = parser.parse_args()
    name = os.getenv('JOB_USER') if os.getenv('JOB_USER') else args.name

    return name, args.file


def print_hi(input_name: str) -> None:
    print(f'Hi, {input_name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_file(path: str) -> None:
    with open(path) as file:
        print(file.read())


if __name__ == '__main__':

    user_name, file_path = get_args()

    print_hi(user_name)
    print_file(file_path)

