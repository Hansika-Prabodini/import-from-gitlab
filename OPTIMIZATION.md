# Performance Optimization Report

## Overview

This document describes the performance optimizations made to address the worst-ranked bottleneck in the llm-benchmarking-py project.

## Bottleneck Identification

Based on benchmark analysis, the following bottlenecks were identified in order of severity:

### Primary Bottleneck: `sum_primes` (OPTIMIZED)
- **Benchmark time**: 132.8 µs (mean) - the slowest among all tested functions
- **Original complexity**: O(n²)
- **Location**: `src/llm_benchmark/algorithms/primes.py`
- **Status**: ✅ Optimized to O(n log log n)

### Secondary Bottleneck: `prime_factors` (OPTIMIZED)
- **Original complexity**: O(n²) worst case
- **Location**: `src/llm_benchmark/algorithms/primes.py`
- **Status**: ✅ Optimized to O(√n)

## Root Cause Analysis

The performance bottleneck stemmed from two inefficiencies:

1. **`is_prime(n)`** function: O(n) complexity
   - Checked all numbers from 2 to n-1 for divisibility
   - Performed unnecessary checks for even numbers
   - Didn't utilize the mathematical property that divisors come in pairs

2. **`sum_primes(n)`** function: O(n²) complexity
   - Called `is_prime(i)` for every number from 0 to n
   - Each `is_prime` call was O(n), resulting in O(n²) overall
   - Repeated primality checks for each number

## Optimizations Implemented

### 1. Optimized `is_prime` Function: O(n) → O(√n)

**Changes:**
- Only check divisors up to √n (if a number has a divisor > √n, it must also have a divisor < √n)
- Skip even numbers after checking for 2
- Early return for n=2

**Code changes:**
```python
# Before: O(n)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# After: O(√n)
def is_prime(n: int) -> bool:
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
```

**Expected improvement:** ~√n times faster for large n

### 2. Optimized `sum_primes` Function: O(n²) → O(n log log n)

**Changes:**
- Implemented Sieve of Eratosthenes algorithm
- Find all primes in a single pass
- Eliminate repeated primality checks

**Code changes:**
```python
# Before: O(n²)
def sum_primes(n: int) -> int:
    sum_ = 0
    for i in range(n):
        if Primes.is_prime(i):
            sum_ += i
    return sum_

# After: O(n log log n)
def sum_primes(n: int) -> int:
    if n <= 2:
        return 0
    
    # Sieve of Eratosthenes
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return sum(i for i in range(n) if is_prime[i])
```

**Trade-off:** Uses O(n) memory but achieves dramatic speed improvement

### 3. Optimized `prime_factors` Function: O(n²) → O(√n)

**Changes:**
- Handle factor 2 separately to avoid checking even numbers
- Only check odd divisors up to √n
- Divide out each factor completely before moving to the next
- If n > 1 after all checks, n itself is a prime factor

**Code changes:**
```python
# Before: O(n²)
def prime_factors(n: int) -> List[int]:
    ret = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                ret.append(i)
                n = n // i
                break
    return ret

# After: O(√n)
def prime_factors(n: int) -> List[int]:
    ret = []
    
    # Handle edge cases
    if n <= 1:
        return ret
    
    # Handle 2 separately to avoid even numbers later
    while n % 2 == 0:
        ret.append(2)
        n = n // 2
    
    # Check odd numbers from 3 to sqrt(n)
    i = 3
    while i * i <= n:
        while n % i == 0:
            ret.append(i)
            n = n // i
        i += 2
    
    # If n > 1, then it's a prime factor
    if n > 1:
        ret.append(n)
    
    return ret
```

**Expected improvement:** 10-1000x faster for large numbers

## Performance Comparison

### Complexity Analysis

| Function        | Original Complexity | Optimized Complexity | Space Complexity |
|-----------------|--------------------|--------------------|------------------|
| `is_prime`      | O(n)               | O(√n)              | O(1)             |
| `sum_primes`    | O(n²)              | O(n log log n)     | O(n)             |
| `prime_factors` | O(n²)              | O(√n)              | O(1)             |

### Benchmark Results

Run the micro-benchmark to see actual performance improvements:

```bash
python benchmark_primes.py
```

**Expected improvements:**
- `is_prime`: ~√n times faster (e.g., 100x faster for n=10,000)
- `sum_primes`: 10-100x faster depending on input size
- `prime_factors`: 10-1000x faster depending on the number being factorized

## Testing & Validation

All existing tests pass without modification:
- ✅ `test_is_prime` - Correctness verified for edge cases
- ✅ `test_sum_primes` - Results match expected values
- ✅ `test_prime_factors` - Correctness verified for all test cases

Run tests:
```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py -v
```

Run benchmarks:
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/algorithms/test_primes.py
```

## Micro-Benchmark Script

A dedicated benchmark script (`benchmark_primes.py`) has been created to demonstrate the improvements:

**Features:**
- Compares original vs optimized implementations
- Tests multiple input sizes (is_prime, sum_primes, and prime_factors)
- Shows detailed timing and speedup metrics
- Verifies correctness of optimizations
- Displays complexity analysis for all three functions

**Usage:**
```bash
python benchmark_primes.py
# or
poetry run python benchmark_primes.py
```

## Impact Summary

✨ **Key Achievements:**
1. Reduced `sum_primes` from O(n²) to O(n log log n)
2. Reduced `is_prime` from O(n) to O(√n)
3. Reduced `prime_factors` from O(n²) to O(√n)
4. Maintained backward compatibility (same API)
5. All tests pass without modification
6. Created comprehensive benchmark script covering all three optimizations

⚠️ **Trade-offs:**
- `sum_primes` now uses O(n) memory (previously O(1))
- This is acceptable as the speed improvement is dramatic

## Future Optimization Opportunities

Other potential bottlenecks that could be optimized:

1. **`Sort.sort_list`**: Uses bubble sort O(n²)
   - Could use quicksort or merge sort for O(n log n)

3. **`DoubleForLoop` functions**: Various O(n²) operations
   - Some could benefit from algorithmic improvements

## References

- [Sieve of Eratosthenes - Wikipedia](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
- [Primality test - Wikipedia](https://en.wikipedia.org/wiki/Primality_test)
- [Time complexity - Big O notation](https://en.wikipedia.org/wiki/Time_complexity)

---

**Author**: Optimization completed as part of performance improvement task  
**Date**: 2024  
**Files Modified**:
- `src/llm_benchmark/algorithms/primes.py`
- `benchmark_primes.py` (new)
- `OPTIMIZATION.md` (new)
