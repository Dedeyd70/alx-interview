#!/usr/bin/python3
'''Minimum Operations'''


def min_operations(target_chars):
    '''Calculate the fewest number of operations needed to result in exactly
    'target_chars' 'H' characters in this file.

    Args:
        target_chars (int): The target number of 'H' characters.

    Returns:
        int: The fewest number of operations needed. If 'target_chars' is
        impossible to achieve, return 0.
    '''

    # Initialize variables
    current_chars = 1  # Number of characters in the file
    copied_chars = 0  # Number of 'H' characters copied
    operations = 0  # Operations counter

    # Loop until the desired number of 'H' characters is reached
    while current_chars < target_chars:
        # If nothing is copied yet
        if copied_chars == 0:
            # Copy all
            copied_chars = current_chars
            # Increment operations counter
            operations += 1

        # If nothing is pasted yet
        if current_chars == 1:
            # Paste
            current_chars += copied_chars
            # Increment operations counter
            operations += 1
            continue

        remaining_chars = target_chars - current_chars  # Calculate remaining 'H' characters to paste

        # Check if it's impossible to achieve the target number of characters
        if remaining_chars < copied_chars:
            return 0

        # If the remaining cannot be divided evenly
        if remaining_chars % current_chars != 0:
            # Paste the current clipboard
            current_chars += copied_chars
            # Increment operations counter
            operations += 1
        else:
            # Copy all
            copied_chars = current_chars
            # Paste
            current_chars += copied_chars
            # Increment operations counter
            operations += 2

    # Check if the desired result is achieved
    if current_chars == target_chars:
        return operations
    else:
        return 0
