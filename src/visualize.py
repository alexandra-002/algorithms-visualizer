"""
Visualization tools for sorting algorithms.
"""

import matplotlib.pyplot as plt


def plot_array(numbers, title, filename):
    """
    Create a bar chart visualization of an array.

    Args:
        numbers (list): Numbers to display.
        title (str): Chart title.
        filename (str): Output image path.
    """

    plt.figure(figsize=(8, 4))

    plt.bar(
        range(len(numbers)),
        numbers
    )

    plt.title(title)

    plt.xlabel("Index")

    plt.ylabel("Value")

    plt.tight_layout()

    plt.savefig(filename)

    plt.close()