#!/usr/bin/python3
"""
Fewest number of coins needed to meet a given amount 
"""
def makeChange(coins, total):
  """
  Prints the changes made to get total
  
  Arguments:
  n (int): The value of a coin will always be an integer greater than 0
  
  Return:
  If total is 0 or less, return 0
  If total cannot be met by any number of coins you have, return -1
  """
    if total <= 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
