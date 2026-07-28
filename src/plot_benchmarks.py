"""
Create benchmark performance visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt


def plot_benchmarks():

    data = pd.read_csv(
        "results/benchmark_results.csv"
    )


    plt.figure(figsize=(8, 5))


    plt.bar(
        data["Algorithm"],
        data["Runtime_seconds"]
    )


    plt.xlabel(
        "Sorting Algorithm"
    )

    plt.ylabel(
        "Runtime (seconds)"
    )

    plt.title(
        "Sorting Algorithm Runtime Comparison"
    )


    plt.xticks(
        rotation=45
    )


    plt.tight_layout()


    plt.savefig(
        "images/runtime_comparison.png"
    )


    plt.close()


if __name__ == "__main__":
    plot_benchmarks()