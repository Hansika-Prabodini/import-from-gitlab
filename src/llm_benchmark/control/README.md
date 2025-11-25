# Control Flow Module

This module provides control flow benchmarking operations that test LLM code generation capabilities with loops and conditional structures. It includes both single and nested loop patterns commonly found in algorithmic problems.

## Components

### SingleForLoop (`single.py`)

Operations using a single loop for basic iteration patterns.

#### Methods

##### `sum_range(n: int) -> int`
Calculates the sum of numbers from 0 to n (exclusive).

**Parameters:**
- `n` (int): The upper bound (exclusive) for summation

**Returns:**
- `int`: Sum of all integers from 0 to n-1

**Example:**
```python
from llm_benchmark.control.single import SingleForLoop

result = SingleForLoop.sum_range(10)  # Returns: 45 (0+1+2+...+9)
result = SingleForLoop.sum_range(5)   # Returns: 10 (0+1+2+3+4)
```

**Algorithm:** Builds a list of values then sums them, demonstrating basic loop usage.

---

##### `max_list(v: List[int]) -> int`
Finds the maximum value in a list using manual iteration.

**Parameters:**
- `v` (List[int]): The list to search (must not be empty)

**Returns:**
- `int`: The maximum value in the list

**Example:**
```python
from llm_benchmark.control.single import SingleForLoop

result = SingleForLoop.max_list([1, 5, 3, 2])  # Returns: 5
result = SingleForLoop.max_list([10])          # Returns: 10
```

**Algorithm:** Iterates through the list tracking the maximum value seen.

---

##### `sum_modulus(n: int, m: int) -> int`
Calculates the sum of all numbers from 0 to n (exclusive) that are divisible by m.

**Parameters:**
- `n` (int): The upper bound (exclusive) for the range
- `m` (int): The divisor to check (modulus value)

**Returns:**
- `int`: Sum of all numbers divisible by m in the range

**Example:**
```python
from llm_benchmark.control.single import SingleForLoop

result = SingleForLoop.sum_modulus(10, 3)   # Returns: 18 (0+3+6+9)
result = SingleForLoop.sum_modulus(100, 3)  # Returns: 1683
```

**Algorithm:** Iterates through range, filtering values divisible by m.

---

### DoubleForLoop (`double.py`)

Operations using nested loops for more complex iteration patterns.

#### Methods

##### `sum_square(n: int) -> int`
Calculates the sum of squares of numbers from 0 to n (exclusive) using nested loops.

**Parameters:**
- `n` (int): The upper bound (exclusive)

**Returns:**
- `int`: Sum of squares (0² + 1² + 2² + ... + (n-1)²)

**Example:**
```python
from llm_benchmark.control.double import DoubleForLoop

result = DoubleForLoop.sum_square(5)   # Returns: 30 (0+1+4+9+16)
result = DoubleForLoop.sum_square(10)  # Returns: 285
```

**Algorithm:** Uses nested loops where i==j to calculate squares.

---

##### `sum_triangle(n: int) -> int`
Calculates a triangular sum using nested loops.

**Parameters:**
- `n` (int): The upper bound (exclusive)

**Returns:**
- `int`: Triangular sum value

**Example:**
```python
from llm_benchmark.control.double import DoubleForLoop

result = DoubleForLoop.sum_triangle(5)   # Returns: 20
result = DoubleForLoop.sum_triangle(10)  # Returns: 165
```

**Algorithm:** For each i, sums all values from 0 to i.

---

##### `count_pairs(arr: List[int]) -> int`
Counts the number of pairs in an array where exactly two elements have the same value.

**Parameters:**
- `arr` (List[int]): The array to analyze

**Returns:**
- `int`: Number of distinct pairs found

**Example:**
```python
from llm_benchmark.control.double import DoubleForLoop

result = DoubleForLoop.count_pairs([1, 1, 2, 3, 3])  # Returns: 2 (pairs: 1,1 and 3,3)
result = DoubleForLoop.count_pairs([5, 5, 5])        # Returns: 0 (triple, not pair)
```

**Algorithm:** Uses nested loops to count occurrences of each value.

---

##### `count_duplicates(arr0: List[int], arr1: List[int]) -> int`
Counts elements at matching indices that have the same value in two arrays.

**Parameters:**
- `arr0` (List[int]): First array
- `arr1` (List[int]): Second array

**Returns:**
- `int`: Number of matching values at same indices

**Example:**
```python
from llm_benchmark.control.double import DoubleForLoop

result = DoubleForLoop.count_duplicates([1, 2, 3], [1, 0, 3])  # Returns: 2
result = DoubleForLoop.count_duplicates([1, 2], [3, 4])        # Returns: 0
```

**Algorithm:** Compares elements where i == j in the nested loops.

---

##### `sum_matrix(m: List[List[int]]) -> int`
Calculates the sum of all elements in a 2D matrix.

**Parameters:**
- `m` (List[List[int]]): The matrix to sum

**Returns:**
- `int`: Total sum of all matrix elements

**Example:**
```python
from llm_benchmark.control.double import DoubleForLoop

matrix = [[1, 2], [3, 4]]
result = DoubleForLoop.sum_matrix(matrix)  # Returns: 10
```

**Algorithm:** Uses nested loops to iterate through rows and columns.

---

## Usage in Benchmarking

These control flow operations test:
- **Loop Construction**: Can the LLM generate correct loop structures?
- **Index Management**: Proper handling of loop indices and boundaries
- **Nested Iteration**: Ability to work with nested loop patterns
- **Conditional Logic**: Combining loops with conditional statements

## Performance Characteristics

### SingleForLoop

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| `sum_range` | O(n) | O(n) |
| `max_list` | O(n) | O(1) |
| `sum_modulus` | O(n) | O(n) |

### DoubleForLoop

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| `sum_square` | O(n²) | O(1) |
| `sum_triangle` | O(n²) | O(1) |
| `count_pairs` | O(n²) | O(1) |
| `count_duplicates` | O(n²) | O(1) |
| `sum_matrix` | O(n × m) | O(1) |

## Common Patterns Tested

1. **Range Iteration**: Basic for-loop over range
2. **List Iteration**: Iterating with indices
3. **Conditional Filtering**: Using if statements within loops
4. **Nested Loops**: Two-level iteration patterns
5. **Accumulation**: Building up results during iteration

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/control/
```

Run benchmarks:

```bash
poetry run pytest --benchmark-only tests/llm_benchmark/control/
```

## Demo

```python
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.control.double import DoubleForLoop

# Single loop examples
print(SingleForLoop.sum_range(10))      # 45
print(SingleForLoop.max_list([1,2,3]))  # 3

# Double loop examples
print(DoubleForLoop.sum_square(10))     # 285
print(DoubleForLoop.count_pairs([1,1,2,2]))  # 2
```
