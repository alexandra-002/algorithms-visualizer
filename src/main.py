from algorithms import bubble_sort
from animation import create_animation


def main():

    numbers = [8, 3, 5, 1, 9]

    history = []


    bubble_sort(
        numbers,
        history
    )


    create_animation(
        history,
        "images/bubble_sort_animation.gif"
    )


if __name__ == "__main__":
    main()