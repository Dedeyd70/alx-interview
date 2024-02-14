#!/usr/bin/python3
"""BOXES BOXES"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing boxes, where
            each inner list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Check if the boxes list is empty or None
    if not boxes:
        return False

    # Get the total number of boxes
    num_boxes = len(boxes)

    # Create a list to track unlocked boxes, initialized with all False

    unlocked = [False] * num_boxes

    # Mark the first box (box 0) as unlocked
    unlocked[0] = True

    # Initialize a list to store the keys we have
    keys = [0]

    # Continue until there are no more keys to explore
    while keys:
        # Take a key from the list of keys
        current_box = keys.pop()

        # Iterate through the keys in the current box
        for key in boxes[current_box]:
            # Check if the key corresponds to a valid box index and if that
            # box is not already unlocked
            if 0 <= key < num_boxes and not unlocked[key]:
                # Mark the corresponding box as unlocked
                unlocked[key] = True
                # Add the key to the list of keys to explore
                keys.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
