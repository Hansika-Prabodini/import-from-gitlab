# Generator Module

This module provides test data generation utilities for creating random lists and matrices. These generators are used throughout the benchmarking suite to create consistent, reproducible test data for other modules.

## Components

### GenList (`gen_list.py`)

Random data generation for lists and matrices.

#### Methods

##### `random_list(n: int, m: int) -> List[int]`
Generates a list of random integers.

**Parameters:**
- `n` (int): Number of integers to generate (list length)
- `m` (int): Maximum value for random integers (exclusive upper bound)

**Returns:**
- `List[int]`: List of n random integers, each in range [0, m]

**Example:**
```python
from llm_benchmark.generator.gen_list import GenList

# Generate 10 random numbers between 0 and 99
result = GenList.random_list(10, 100)
print(result)  # Output: [42, 17, 93, 8, 55, 71, 34, 2, 88, 15] (example)

# Generate 5 random numbers between 0 and 9
result = GenList.random_list(5, 10)
print(result)  # Output: [7, 3, 9, 1, 4] (example)

# Generate small list
result = GenList.random_list(3, 5)
print(result)  # Output: [2, 4, 0] (example)
```

**Algorithm:** Uses Python's `random.randint()` with list comprehension.

**Range:** Values are inclusive of 0 and m (using `randint(0, m)`).

---

##### `random_matrix(n: int, m: int) -> List[List[int]]`
Generates a square matrix of random integers.

**Parameters:**
- `n` (int): Number of rows in the matrix (also determines columns for square matrix)
- `m` (int): Maximum value for random integers (exclusive upper bound)

**Returns:**
- `List[List[int]]`: An n×n matrix (list of lists) with random integers in range [0, m]

**Example:**
```python
from llm_benchmark.generator.gen_list import GenList

# Generate 3x3 matrix with values 0-9
result = GenList.random_matrix(3, 10)
print(result)
# Output (example):
# [[7, 2, 9],
#  [4, 1, 6],
#  [8, 3, 5]]

# Generate 2x2 matrix with small values
result = GenList.random_matrix(2, 5)
print(result)
# Output (example):
# [[3, 1],
#  [4, 2]]
```

**Algorithm:** Generates n lists, each containing n random integers.

**Note:** Creates square matrices (n×n). For rectangular matrices, modify the implementation.

---

## Usage in Benchmarking

These generators are used to:
- **Create Test Data**: Generate reproducible input for benchmarking
- **Stress Testing**: Create large datasets to test performance
- **Consistency**: Ensure all tests use similar data distributions
- **Randomization**: Avoid hardcoded test cases that might not represent real usage

## Common Use Cases

### Testing Control Flow Functions
```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop

# Generate random data for pair counting
test_data = GenList.random_list(30, 10)
pairs = DoubleForLoop.count_pairs(test_data)
print(f"Found {pairs} pairs in random data")
```

### Testing Matrix Operations
```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop

# Generate random matrix for sum testing
matrix = GenList.random_matrix(10, 100)
total = DoubleForLoop.sum_matrix(matrix)
print(f"Sum of 10x10 matrix: {total}")
```

### Testing Duplicate Detection
```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop

# Generate two lists to compare
list1 = GenList.random_list(10, 5)
list2 = GenList.random_list(10, 5)
duplicates = DoubleForLoop.count_duplicates(list1, list2)
print(f"Duplicates at same index: {duplicates}")
```

## Performance Characteristics

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| `random_list(n, m)` | O(n) | O(n) |
| `random_matrix(n, m)` | O(n²) | O(n²) |

## Random Number Generation

**Module Used:** Python's `random` module  
**Function:** `random.randint(a, b)` - Returns random integer in range [a, b] inclusive

**Seed:** Not explicitly set, so results vary between runs. For reproducible results, set seed before calling:

```python
import random
random.seed(42)  # Use any integer

from llm_benchmark.generator.gen_list import GenList
result = GenList.random_list(5, 10)  # Will be same every time with seed 42
```

## Design Notes

- **Simple Implementation**: Uses list comprehensions for concise, readable code
- **Inclusive Range**: `randint(0, m)` includes both 0 and m
- **Square Matrices Only**: `random_matrix` creates n×n matrices, not n×m
- **No Validation**: Assumes positive integers for n and m

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/generator/
```

## Complete Demo

```python
from llm_benchmark.generator.gen_list import GenList
import random

# Set seed for reproducible output
random.seed(42)

print("=== Random Lists ===")
print(f"10 numbers (0-99): {GenList.random_list(10, 100)}")
print(f"5 numbers (0-9): {GenList.random_list(5, 10)}")
print(f"3 numbers (0-4): {GenList.random_list(3, 5)}")

print("\n=== Random Matrices ===")
matrix_2x2 = GenList.random_matrix(2, 10)
print("2x2 matrix:")
for row in matrix_2x2:
    print(row)

matrix_3x3 = GenList.random_matrix(3, 5)
print("\n3x3 matrix:")
for row in matrix_3x3:
    print(row)

print("\n=== Statistics ===")
large_list = GenList.random_list(1000, 100)
print(f"Generated 1000 numbers")
print(f"Min: {min(large_list)}")
print(f"Max: {max(large_list)}")
print(f"Average: {sum(large_list) / len(large_list):.2f}")
```

## Potential Extensions

Future additions could include:
- **Rectangular Matrices**: `random_matrix(rows, cols, max_value)`
- **Custom Ranges**: Specify min and max values
- **Distribution Control**: Normal, exponential, etc.
- **Sorted Lists**: Generate pre-sorted or partially sorted lists
- **String Generation**: Random strings for string operation testing
- **Duplicate Control**: Specify percentage of duplicates
- **Type Variations**: Float, boolean, mixed-type lists

## Integration with Main Demo

Used in `main.py`:

```python
from llm_benchmark.generator.gen_list import GenList
from llm_benchmark.control.double import DoubleForLoop

# Generate random test data
random_list = GenList.random_list(30, 10)
random_matrix = GenList.random_matrix(10, 10)

# Use in benchmarks
pairs = DoubleForLoop.count_pairs(random_list)
matrix_sum = DoubleForLoop.sum_matrix(random_matrix)
```

This ensures the demo runs with varied, non-hardcoded data each time.
