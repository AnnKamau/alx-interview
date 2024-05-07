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
        return n

    operations = 0
    current_h = 1
    while current_h < n:
        if n % current_h == 0:
            operations += current_h
            current_h *= n // current_h
        else:
            operations += current_h
            current_h += current_h

    return operations