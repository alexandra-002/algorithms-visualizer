from visualize import plot_array


def main():

    numbers = [8, 3, 5, 1, 9]

    plot_array(
        numbers,
        "Example Array",
        "images/example_array.png"
    )


if __name__ == "__main__":
    main()