#!/usr/bin/python3
"""
prime numbers based on a game.
"""

def isWinner(x, nums):
    def is_prime(num):
        """Helper function to check if a number is prime"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while (i * i) <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_primes_up_to(n):
        """Helper function to generate all prime numbers up to n"""
        sieve = [True] * (n + 1)
        p = 2
        while (p * p) <= n:
            if sieve[p] == True:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        return [p for p in range(2, n + 1) if sieve[p]]

    def play_game(n):
        """Simulate the game and return the winner for the given n"""
        primes = generate_primes_up_to(n)
        turn = 0  # Maria starts
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
