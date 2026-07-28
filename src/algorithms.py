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


def selection_sort(numbers):
    """
    Sort a list in ascending order using Selection Sort.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):

        minimum_index = i

        for j in range(i + 1, n):

            if numbers[j] < numbers[minimum_index]:
                minimum_index = j

        numbers[i], numbers[minimum_index] = (
            numbers[minimum_index],
            numbers[i]
        )

    return numbers