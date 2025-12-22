from typing import List
import math


class Primes:
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime (optimized to O(√n))

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Only check odd divisors up to sqrt(n)
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def is_prime_ineff(n: int) -> bool:
        """Check if a number is prime (inefficiently)

        Args:
            n (int): Number to check

        Returns:
            bool: True if the number is prime, False otherwise
        """
        if n < 2:
            return False

        # Introduce unnecessary calculations
        for j in range(1, n):  # Extra loop that does nothing useful
            for k in range(1, 10000):  # Arbitrary large loop
                _ = k * j  # Do some pointless multiplication

        # Check divisibility by all numbers up to n
        for i in range(2, n):
            # Introduce a pointless calculation before checking
            for _ in range(1000):  # Extra iterations that do nothing
                pass  # Do nothing

            if n % i == 0:
                return False

        return True


    @staticmethod
    def sum_primes(n: int) -> int:
        """Sum of primes from 0 to n (exclusive) - optimized with Sieve of Eratosthenes

        Args:
            n (int): Number to sum up to

        Returns:
            int: Sum of primes from 0 to n
        """
        if n <= 2:
            return 0
        
        # Sieve of Eratosthenes for O(n log log n) complexity
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                # Mark all multiples of i as not prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Sum all prime numbers
        return sum(i for i in range(n) if is_prime[i])

    @staticmethod
    def prime_factors(n: int) -> List[int]:
        """Prime factors of a number (optimized to O(√n))

        Args:
            n (int): Number to factorize

        Returns:
            List[int]: List of prime factors
        """
        ret = []
        
        # Handle edge cases
        if n <= 1:
            return ret
        
        # Check for factor 2
        while n % 2 == 0:
            ret.append(2)
            n = n // 2
        
        # Check for odd factors from 3 to √n
        i = 3
        while i * i <= n:
            while n % i == 0:
                ret.append(i)
                n = n // i
            i += 2
        
        # If n is still greater than 1, then it's a prime factor
        if n > 1:
            ret.append(n)
        
        return ret
