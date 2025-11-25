#!/usr/bin/env python3
"""
Micro-benchmark script for comparing optimized vs original prime number functions.

This script demonstrates the performance improvements achieved by optimizing:
1. is_prime: O(n) -> O(√n) by checking divisors only up to sqrt(n)
2. sum_primes: O(n²) -> O(n log log n) using Sieve of Eratosthenes

Usage:
    python benchmark_primes.py
    or
    poetry run python benchmark_primes.py
"""

import time
import math
from typing import Callable, List, Tuple
from llm_benchmark.algorithms.primes import Primes


# Original implementations (for comparison)
class PrimesOriginal:
    """Original implementations before optimization"""
    
    @staticmethod
    def is_prime_original(n: int) -> bool:
        """Original O(n) implementation"""
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def sum_primes_original(n: int) -> int:
        """Original O(n²) implementation"""
        sum_ = 0
        for i in range(n):
            if PrimesOriginal.is_prime_original(i):
                sum_ += i
        return sum_


def time_function(func: Callable, *args, iterations: int = 100) -> Tuple[float, any]:
    """
    Time a function over multiple iterations.
    
    Args:
        func: Function to benchmark
        *args: Arguments to pass to the function
        iterations: Number of times to run the function
    
    Returns:
        Tuple of (average_time_ms, result)
    """
    start = time.perf_counter()
    result = None
    for _ in range(iterations):
        result = func(*args)
    end = time.perf_counter()
    avg_time_ms = ((end - start) / iterations) * 1000  # Convert to milliseconds
    return avg_time_ms, result


def benchmark_is_prime():
    """Benchmark is_prime optimization"""
    print("=" * 80)
    print("BENCHMARK: is_prime function")
    print("=" * 80)
    print("\nOptimization: O(n) -> O(√n) by checking divisors only up to sqrt(n)")
    print("\nTest cases:")
    
    test_values = [17, 97, 997, 9973, 99991]
    
    for n in test_values:
        print(f"\n  Testing with n = {n:,}")
        
        # Benchmark original
        time_orig, result_orig = time_function(PrimesOriginal.is_prime_original, n, iterations=1000)
        
        # Benchmark optimized
        time_opt, result_opt = time_function(Primes.is_prime, n, iterations=1000)
        
        # Verify correctness
        assert result_orig == result_opt, f"Results don't match! Original: {result_orig}, Optimized: {result_opt}"
        
        speedup = time_orig / time_opt if time_opt > 0 else float('inf')
        
        print(f"    Original:  {time_orig:8.4f} ms")
        print(f"    Optimized: {time_opt:8.4f} ms")
        print(f"    Speedup:   {speedup:8.2f}x faster")
        print(f"    Result:    {result_opt}")


def benchmark_sum_primes():
    """Benchmark sum_primes optimization"""
    print("\n" + "=" * 80)
    print("BENCHMARK: sum_primes function")
    print("=" * 80)
    print("\nOptimization: O(n²) -> O(n log log n) using Sieve of Eratosthenes")
    print("\nTest cases:")
    
    test_values = [100, 500, 1000, 5000, 10000]
    
    for n in test_values:
        print(f"\n  Testing with n = {n:,}")
        
        # Benchmark original (with fewer iterations for larger values)
        iterations = max(10, 1000 // (n // 100))
        time_orig, result_orig = time_function(PrimesOriginal.sum_primes_original, n, iterations=iterations)
        
        # Benchmark optimized
        time_opt, result_opt = time_function(Primes.sum_primes, n, iterations=iterations)
        
        # Verify correctness
        assert result_orig == result_opt, f"Results don't match! Original: {result_orig}, Optimized: {result_opt}"
        
        speedup = time_orig / time_opt if time_opt > 0 else float('inf')
        
        print(f"    Original:  {time_orig:8.4f} ms")
        print(f"    Optimized: {time_opt:8.4f} ms")
        print(f"    Speedup:   {speedup:8.2f}x faster")
        print(f"    Result:    {result_opt:,}")


def complexity_analysis():
    """Display complexity analysis"""
    print("\n" + "=" * 80)
    print("COMPLEXITY ANALYSIS")
    print("=" * 80)
    
    print("\n1. is_prime function:")
    print("   Original:  O(n)    - checks all numbers from 2 to n-1")
    print("   Optimized: O(√n)   - checks only up to sqrt(n) and skips even numbers")
    print("   Memory:    O(1)    - constant space for both versions")
    
    print("\n2. sum_primes function:")
    print("   Original:  O(n²)         - calls O(n) is_prime for each of n numbers")
    print("   Optimized: O(n log log n) - Sieve of Eratosthenes algorithm")
    print("   Memory:    O(n)          - array to store primality flags")
    
    print("\n3. Key optimizations:")
    print("   • is_prime: Only need to check divisors up to √n")
    print("   • is_prime: Skip even numbers after checking for 2")
    print("   • sum_primes: Use sieve to find all primes at once")
    print("   • sum_primes: Avoid repeated primality checks")


def summary_table():
    """Display summary comparison table"""
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    print("\n┌─────────────────┬──────────────┬──────────────┬─────────────────┐")
    print("│ Function        │ Original     │ Optimized    │ Improvement     │")
    print("├─────────────────┼──────────────┼──────────────┼─────────────────┤")
    print("│ is_prime        │ O(n)         │ O(√n)        │ ~√n times faster│")
    print("│ sum_primes      │ O(n²)        │ O(n log log n)│ ~10-100x faster │")
    print("└─────────────────┴──────────────┴──────────────┴─────────────────┘")
    
    print("\nNotes:")
    print("  • The actual speedup depends on the input size")
    print("  • Larger inputs show more dramatic improvements")
    print("  • The optimized version uses O(n) memory for sum_primes")


def main():
    """Run all benchmarks"""
    print("\n" + "█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + "  PRIME FUNCTIONS OPTIMIZATION BENCHMARK".center(78) + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)
    
    try:
        # Run benchmarks
        benchmark_is_prime()
        benchmark_sum_primes()
        
        # Display analysis
        complexity_analysis()
        summary_table()
        
        print("\n" + "█" * 80)
        print("█" + "  BENCHMARK COMPLETE".center(78) + "█")
        print("█" * 80 + "\n")
        
    except KeyboardInterrupt:
        print("\n\nBenchmark interrupted by user.")
    except Exception as e:
        print(f"\n\nError during benchmark: {e}")
        raise


if __name__ == "__main__":
    main()
