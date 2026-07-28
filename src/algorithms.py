"""
Sorting algorithms used throughout the project.
"""


def bubble_sort(numbers):
    """
    Sort a list in ascending order using Bubble Sort.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):

        for j in range(0, n - i - 1):

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

    return numbers