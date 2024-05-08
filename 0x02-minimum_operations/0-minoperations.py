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
    
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(n // i)

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
