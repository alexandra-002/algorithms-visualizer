"""
Save benchmark results to CSV.
"""

import csv


def save_benchmark_results(results, filename):
    """
    Save benchmark data.

    Args:
        results (list): Benchmark results.
        filename (str): Output CSV file.
    """

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Algorithm",
                "Runtime_seconds"
            ]
        )

        for result in results:

            writer.writerow(
                [
                    result["algorithm"],
                    result["runtime"]
                ]
            )