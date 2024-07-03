#!/usr/bin/python3
"""
Prime numbers game.
"""

def isWinner(x, nums):
    """
    Determine the winner of the game.

    Args:
    x (int): number of rounds
    nums (list): array of n values for each round

    Returns:
    str: name of the player that won the most rounds
    None: if the winner cannot be determined
    """
    
    def generate_primes_up_to(n):
        """Helper function to generate all prime numbers up to n"""
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return [p for p in range(2, n + 1) if sieve[p]]
    
    def play_game(n):
        """Simulate the game and return the winner for the given n"""
        if n < 2:
            return "Ben"
        
        primes = generate_primes_up_to(n)
        turn = 0
        
        while primes:
            prime = primes[0]
            primes = [num for num in primes if num % prime != 0]
            turn = 1 - turn

        return "Maria" if turn == 1 else "Ben"
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
