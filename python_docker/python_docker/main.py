import argparse


def get_user():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="user's name")
    args = parser.parse_args()
    return args.name


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    print_hi(get_user())

