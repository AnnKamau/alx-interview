#!/usr/bin/python3
"""
Minimum Operations
"""
def minOperations(n):
    """
    Minimum Operations

    Arguments:
    n (int): Number of operations

    Return:
    Returns an integer
    If n is impossible to achieve, return 0
    """
   if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
