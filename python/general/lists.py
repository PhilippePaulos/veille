from typing import List


def reverse(chain: str) -> None:
    """
    Reverse a given string
    :param chain:
    :return:
    """
    def reverse_words() -> str:
        return ' '.join(word[::-1] for word in chain.split())

    def reverse_all() -> str:
        return chain[::-1]

    def reverse_all_2() -> str:
        return ' '.join(word[::-1] for word in chain.split()[::-1])

    print(reverse_words())
    print(reverse_all())
    print(reverse_all_2())


def list_manipulation(list_str: List[str]):
    """
    Simple list manipulation
    :param chain:
    :return:
    """
    list1 = list_str
    list2 = list1.copy()
    # list2 = list1[:]
    del list2[0]
    # list2.remove("J'aime")

    print(list2.count('Python'))
    print(f"Python index: {list1.index('Python')}")
    print(f"Python index: {list2.index('Python')}")

    print(sorted(list1, reverse=True))


if __name__ == "__main__":
    reverse("J'aime Python")
    list_manipulation("J'aime Python".split())
