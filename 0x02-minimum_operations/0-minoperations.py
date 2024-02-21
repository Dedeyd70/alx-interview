#!/usr/bin/python3
'''Minimum Operations'''


def min_operations(n):
    '''
    Calculate the minimum number of operations required to achieve
    exactly 'n' H characters in the file.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The minimum number of operations needed. Returns 0 if 'n'
        is impossible to achieve.
    '''

    # If n is 1, no operations are needed
    if n == 1:
        return 0

    # Initialize a list to store the minimum operations for each
    # number of H characters
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: 1 H character requires 0 operations

    # Iterate over each number from 2 to n
    for i in range(2, n + 1):
        # For each number, try to find the minimum operations required
        for j in range(1, i):
            # Check if j is a divisor of i (i.e., if i can be obtained
            # by copying j and pasting it a certain number of times)
            if i % j == 0:
                # Update the minimum operations required for i
                dp[i] = min(dp[i], dp[j] + (i // j))

    # Return the minimum operations required to obtain n H characters,
    # or 0 if it's impossible
    return dp[n] if dp[n] != float('inf') else 0
