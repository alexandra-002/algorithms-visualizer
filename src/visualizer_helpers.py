def record_step(history, numbers):
    """
    Save a snapshot of the current array state.

    Args:
        history (list): List storing previous states.
        numbers (list): Current array state.
    """

    history.append(numbers.copy())