"""
Benchmark sorting algorithm performance.
"""

import time


def benchmark_algorithm(sort_function, numbers):
    """
    Measure execution time of a sorting algorithm.

    Args:
        sort_function: Sorting algorithm function.
        numbers (list): Input numbers.

    Returns:
        float: Execution time in seconds.
    """

    start_time = time.time()

    sort_function(numbers)

    end_time = time.time()

    return end_time - start_time