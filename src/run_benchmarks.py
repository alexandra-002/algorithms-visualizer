from algorithms import (
    bubble_sort,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort
)

from benchmark import benchmark_algorithm
from save_benchmarks import save_benchmark_results


def main():

    numbers = list(range(1000, 0, -1))


    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }


    results = []


    for name, algorithm in algorithms.items():

        runtime = benchmark_algorithm(
            algorithm,
            numbers
        )

        print(
            f"{name}: {runtime:.6f} seconds"
        )


        results.append(
            {
                "algorithm": name,
                "runtime": runtime
            }
        )


    save_benchmark_results(
        results,
        "results/benchmark_results.csv"
    )


if __name__ == "__main__":
    main()