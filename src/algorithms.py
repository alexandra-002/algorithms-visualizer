"""
Sorting algorithms used throughout the project.
"""


def bubble_sort(numbers, history=None):
    """
    Sort a list using Bubble Sort.

    Args:
        numbers (list): List of numbers.
        history (list): Stores sorting steps.

    Returns:
        list: Sorted list.
    """

    numbers = numbers.copy()

    n = len(numbers)

    for i in range(n):

        for j in range(0, n - i - 1):

            if history is not None:
                history.append(numbers.copy())

            if numbers[j] > numbers[j + 1]:

                numbers[j], numbers[j + 1] = (
                    numbers[j + 1],
                    numbers[j]
                )

    if history is not None:
        history.append(numbers.copy())

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


def insertion_sort(numbers):
    """
    Sort a list in ascending order using Insertion Sort.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    numbers = numbers.copy()

    for i in range(1, len(numbers)):

        current_value = numbers[i]

        position = i - 1

        while position >= 0 and numbers[position] > current_value:

            numbers[position + 1] = numbers[position]

            position -= 1

        numbers[position + 1] = current_value

    return numbers


def merge_sort(numbers):
    """
    Sort a list in ascending order using Merge Sort.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    if len(numbers) <= 1:
        return numbers.copy()

    middle = len(numbers) // 2

    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])

    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted lists into one sorted list.

    Args:
        left (list): Sorted list.
        right (list): Sorted list.

    Returns:
        list: Combined sorted list.
    """

    merged = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] <= right[right_index]:

            merged.append(left[left_index])
            left_index += 1

        else:

            merged.append(right[right_index])
            right_index += 1


    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def quick_sort(numbers):
    """
    Sort a list in ascending order using Quick Sort.

    Args:
        numbers (list): List of numbers.

    Returns:
        list: Sorted list.
    """

    numbers = numbers.copy()

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    smaller = []
    equal = []
    larger = []

    for number in numbers:

        if number < pivot:
            smaller.append(number)

        elif number == pivot:
            equal.append(number)

        else:
            larger.append(number)

    return (
        quick_sort(smaller)
        + equal
        + quick_sort(larger)
    )