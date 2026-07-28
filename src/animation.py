"""
Create animations from sorting algorithm steps.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_animation(history, filename):
    """
    Create a GIF animation from sorting steps.

    Args:
        history (list): List of array states.
        filename (str): Output GIF path.
    """

    fig, ax = plt.subplots(figsize=(8, 4))


    def update(frame):

        ax.clear()

        ax.bar(
            range(len(history[frame])),
            history[frame]
        )

        ax.set_title(
            f"Sorting Step {frame + 1}/{len(history)}"
        )

        ax.set_xlabel("Index")

        ax.set_ylabel("Value")


    anim = animation.FuncAnimation(
        fig,
        update,
        frames=len(history),
        interval=500
    )


    anim.save(
        filename,
        writer="pillow"
    )

    plt.close()