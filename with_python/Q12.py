from typing import List
import numpy as np
import numpy.random as random


def generate_10_numbers_from_0_until_100() -> List[int]:
    lists = []
    for i in range(10):
        x = random.randint(0, 100, 1, int)
        lists.append(x)

    return lists


def print_list(numbers: List[int]):
    for i in numbers:
        print(i)


def sort_in_ascending_order(numbers: List[int]) -> List[int]:
    numbers.sort()
    for i in numbers:
        print(i)


def remove_content_which_number_is_under_50(numbers: List[int]) -> List[int]:
    lists_rm = []
    for i in numbers:
        if i > 50:
            lists_rm.append(i)

    return lists_rm


if __name__ == '__main__':
    print("Q1.2.1 + Q1.2.2")
    lists = generate_10_numbers_from_0_until_100()
    print_list(lists)
    print("Q1.2.3_sort")
    sort_in_ascending_order(lists)
    print("Q1.2.3_remove")
    print(remove_content_which_number_is_under_50(lists))
