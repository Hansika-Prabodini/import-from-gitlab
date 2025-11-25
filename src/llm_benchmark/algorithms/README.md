# Algorithms Module

This module provides algorithm implementations for benchmarking LLM code generation capabilities. It contains fundamental computational algorithms commonly used in programming challenges and interviews.

## Components

### Primes (`primes.py`)

Prime number operations including detection, summation, and factorization.

#### Methods

##### `is_prime(n: int) -> bool`
Checks if a number is prime using a straightforward algorithm.

**Parameters:**
- `n` (int): The number to check for primality

**Returns:**
- `bool`: True if the number is prime, False otherwise

**Example:**
```python
from llm_benchmark.algorithms.primes import Primes

result = Primes.is_prime(17)  # Returns: True
result = Primes.is_prime(20)  # Returns: False
```

**Algorithm:** Iterates from 2 to n-1, checking if any number divides n evenly.

---

##### `is_prime_ineff(n: int) -> bool`
Deliberately inefficient prime checking implementation for benchmarking purposes.

**Parameters:**
- `n` (int): The number to check for primality

**Returns:**
- `bool`: True if the number is prime, False otherwise

**Example:**
```python
from llm_benchmark.algorithms.primes import Primes

result = Primes.is_prime_ineff(1700)  # Returns: False (but much slower)
```

**Note:** This method includes unnecessary calculations to simulate inefficient code patterns. Useful for comparing performance optimization.

---

##### `sum_primes(n: int) -> int`
Calculates the sum of all prime numbers from 0 to n (exclusive).

**Parameters:**
- `n` (int): The upper bound (exclusive) for prime summation

**Returns:**
- `int`: Sum of all prime numbers less than n

**Example:**
```python
from llm_benchmark.algorithms.primes import Primes

result = Primes.sum_primes(10)  # Returns: 17 (2 + 3 + 5 + 7)
result = Primes.sum_primes(210)  # Returns: 4227
```

---

##### `prime_factors(n: int) -> List[int]`
Finds the prime factorization of a number.

**Parameters:**
- `n` (int): The number to factorize

**Returns:**
- `List[int]`: List of prime factors (with repetition for powers)

**Example:**
```python
from llm_benchmark.algorithms.primes import Primes

result = Primes.prime_factors(12)   # Returns: [2, 2, 3]
result = Primes.prime_factors(840)  # Returns: [2, 2, 2, 3, 5, 7]
```

---

### Sort (`sort.py`)

Sorting and partitioning operations on lists.

#### Methods

##### `sort_list(v: List[int]) -> None`
Sorts a list of integers in-place using a simple bubble sort algorithm.

**Parameters:**
- `v` (List[int]): The list to sort (modified in-place)

**Returns:**
- None (modifies the input list)

**Example:**
```python
from llm_benchmark.algorithms.sort import Sort

numbers = [5, 3, 2, 1, 4]
Sort.sort_list(numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

**Algorithm:** Bubble sort with O(n²) time complexity.

---

##### `dutch_flag_partition(v: List[int], pivot_value: int) -> None`
Partitions a list using the Dutch National Flag algorithm around a pivot value.

**Parameters:**
- `v` (List[int]): The list to partition (modified in-place)
- `pivot_value` (int): The pivot value for partitioning

**Returns:**
- None (modifies the input list)

**Example:**
```python
from llm_benchmark.algorithms.sort import Sort

numbers = [5, 3, 2, 1, 4]
Sort.dutch_flag_partition(numbers, 3)
print(numbers)  # Output: [2, 1, 3, 5, 4] (values < 3, then = 3, then > 3)
```

**Algorithm:** Three-way partitioning that groups elements less than, equal to, and greater than the pivot.

---

##### `max_n(v: List[int], n: int) -> List[int]`
Finds the N largest elements in a list.

**Parameters:**
- `v` (List[int]): The list to search
- `n` (int): Number of maximum values to find

**Returns:**
- `List[int]`: List containing the N largest values

**Example:**
```python
from llm_benchmark.algorithms.sort import Sort

numbers = [5, 3, 2, 1, 4]
result = Sort.max_n(numbers, 3)
print(result)  # Output: [5, 4, 3]
```

**Algorithm:** Iteratively finds and removes maximum values.

---

## Usage in Benchmarking

These algorithms are designed to test:
- **Correctness**: Can the LLM generate code that produces correct results?
- **Efficiency**: Does the generated code use appropriate algorithms?
- **Edge Cases**: How well does the code handle boundary conditions?

## Performance Characteristics

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| `is_prime` | O(n) | O(1) |
| `is_prime_ineff` | O(n² × 10000) | O(1) |
| `sum_primes` | O(n²) | O(1) |
| `prime_factors` | O(n²) | O(log n) |
| `sort_list` | O(n²) | O(1) |
| `dutch_flag_partition` | O(n) | O(1) |
| `max_n` | O(n × m) where m=n | O(n) |

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/algorithms/
```

Run benchmarks:

```bash
poetry run pytest --benchmark-only tests/llm_benchmark/algorithms/
```
