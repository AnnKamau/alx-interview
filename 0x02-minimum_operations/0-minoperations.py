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
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0
