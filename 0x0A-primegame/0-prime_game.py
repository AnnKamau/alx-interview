#!/usr/bin/python3
"""
prime numbers based on a game.
"""

def sieve_of_eratosthenes(max_num):
    """
    Prime numbers
    Arguments:
    where x is the number of rounds and nums is an array of n

    Returns:
    name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """

    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        if (is_prime[p] == True):
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    is_prime[0], is_prime[1] = False, False
    return [p for p, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_set = set(primes)
        current_set = set(range(1, n + 1))

        while prime_set:
            # Maria's turn
            maria_choice = min(prime_set)
            for num in range(maria_choice, n + 1, maria_choice):
                if num in current_set:
                    current_set.remove(num)
                    prime_set.discard(num)

            if not prime_set:
                break

            # Ben's turn
            ben_choice = min(prime_set)
            for num in range(ben_choice, n + 1, ben_choice):
                if num in current_set:
                    current_set.remove(num)
                    prime_set.discard(num)

            if not prime_set:
                break

        # Determine the winner of this round
        if len(prime_set) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
