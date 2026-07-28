import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from src.algorithms import bubble_sort, selection_sort


def test_bubble_sort():

    numbers = [5, 2, 8, 1, 4]

    sorted_numbers = bubble_sort(numbers)

    assert sorted_numbers == [1, 2, 4, 5, 8]


def test_empty_list():

    assert bubble_sort([]) == []


def test_single_element():

    assert bubble_sort([7]) == [7]


def test_already_sorted():

    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_duplicates():

    assert bubble_sort([4, 2, 4, 1]) == [1, 2, 4, 4]


def test_selection_sort():

    numbers = [64, 25, 12, 22, 11]

    sorted_numbers = selection_sort(numbers)

    assert sorted_numbers == [11, 12, 22, 25, 64]


def test_selection_sort_duplicates():

    numbers = [5, 3, 5, 1, 2]

    sorted_numbers = selection_sort(numbers)

    assert sorted_numbers == [1, 2, 3, 5, 5]