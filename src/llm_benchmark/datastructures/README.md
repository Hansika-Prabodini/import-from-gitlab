# Data Structures Module

This module provides list manipulation operations for benchmarking LLM code generation capabilities with common data structure operations. It focuses on fundamental list operations that form the basis of many algorithmic problems.

## Components

### DsList (`dslist.py`)

Comprehensive list operations including modification, searching, sorting, and transformation.

#### Methods

##### `modify_list(v: List[int]) -> List[int]`
Creates a new list with each element incremented by 1.

**Parameters:**
- `v` (List[int]): The input list

**Returns:**
- `List[int]`: A new list with all elements increased by 1

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.modify_list([1, 2, 3, 4, 5])
print(result)  # Output: [2, 3, 4, 5, 6]
```

**Note:** Original list remains unchanged; returns a new list.

---

##### `search_list(v: List[int], n: int) -> List[int]`
Finds all indices where a specific value appears in the list.

**Parameters:**
- `v` (List[int]): The list to search
- `n` (int): The value to search for

**Returns:**
- `List[int]`: List of indices where the value was found (empty if not found)

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.search_list([1, 2, 3, 2, 5], 2)
print(result)  # Output: [1, 3]

result = DsList.search_list([1, 2, 3], 5)
print(result)  # Output: []
```

**Algorithm:** Linear search returning all matching indices.

---

##### `sort_list(v: List[int]) -> List[int]`
Sorts a list and returns a new sorted copy.

**Parameters:**
- `v` (List[int]): The list to sort

**Returns:**
- `List[int]`: A new sorted list (ascending order)

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.sort_list([5, 3, 1, 4, 2])
print(result)  # Output: [1, 2, 3, 4, 5]
```

**Algorithm:** Simple bubble sort with O(n²) complexity.  
**Note:** Original list remains unchanged; returns a sorted copy.

---

##### `reverse_list(v: List[int]) -> List[int]`
Reverses a list and returns a new reversed copy.

**Parameters:**
- `v` (List[int]): The list to reverse

**Returns:**
- `List[int]`: A new list with elements in reverse order

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.reverse_list([1, 2, 3, 4, 5])
print(result)  # Output: [5, 4, 3, 2, 1]
```

**Note:** Original list remains unchanged; returns a new reversed list.

---

##### `rotate_list(v: List[int], n: int) -> List[int]`
Rotates a list left by n positions.

**Parameters:**
- `v` (List[int]): The list to rotate
- `n` (int): Number of positions to rotate left

**Returns:**
- `List[int]`: A new rotated list

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.rotate_list([1, 2, 3, 4, 5], 2)
print(result)  # Output: [3, 4, 5, 1, 2]

result = DsList.rotate_list([1, 2, 3, 4, 5], 0)
print(result)  # Output: [1, 2, 3, 4, 5]
```

**Algorithm:** Takes elements from index n to end, then appends elements from start to n.

---

##### `merge_lists(v1: List[int], v2: List[int]) -> List[int]`
Merges two lists by concatenating them.

**Parameters:**
- `v1` (List[int]): First list
- `v2` (List[int]): Second list

**Returns:**
- `List[int]`: A new list containing all elements from v1 followed by all elements from v2

**Example:**
```python
from llm_benchmark.datastructures.dslist import DsList

result = DsList.merge_lists([1, 2, 3], [4, 5, 6])
print(result)  # Output: [1, 2, 3, 4, 5, 6]

result = DsList.merge_lists([1], [])
print(result)  # Output: [1]
```

**Note:** Simple concatenation; does not sort or interleave elements.

---

## Usage in Benchmarking

These data structure operations test:
- **Immutability Patterns**: Creating new structures vs. modifying in-place
- **List Comprehension**: Ability to generate transformed lists
- **Index Manipulation**: Correct handling of array indices
- **Search Algorithms**: Implementation of linear search
- **Collection Operations**: Merging and transforming collections

## Performance Characteristics

| Method | Time Complexity | Space Complexity |
|--------|----------------|------------------|
| `modify_list` | O(n) | O(n) |
| `search_list` | O(n) | O(k) where k = matches |
| `sort_list` | O(n²) | O(n) |
| `reverse_list` | O(n) | O(n) |
| `rotate_list` | O(n) | O(n) |
| `merge_lists` | O(n + m) | O(n + m) |

## Common Operations Tested

1. **Mapping**: Transforming each element (modify_list)
2. **Filtering/Searching**: Finding elements (search_list)
3. **Sorting**: Ordering elements (sort_list)
4. **Reversing**: Inverting order (reverse_list)
5. **Rotation**: Circular shifting (rotate_list)
6. **Merging**: Combining collections (merge_lists)

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/datastructures/
```

Run benchmarks:

```bash
poetry run pytest --benchmark-only tests/llm_benchmark/datastructures/
```

## Complete Demo

```python
from llm_benchmark.datastructures.dslist import DsList

test_list = [1, 2, 3, 4, 5]
print("Original:", test_list)

# Modify (add 1 to each element)
print("Modified:", DsList.modify_list(test_list))

# Search for value
print("Search 3:", DsList.search_list(test_list, 3))

# Sort
print("Sorted:", DsList.sort_list([5, 3, 1, 4, 2]))

# Reverse
print("Reversed:", DsList.reverse_list(test_list))

# Rotate
print("Rotated by 2:", DsList.rotate_list(test_list, 2))

# Merge
print("Merged:", DsList.merge_lists(test_list, [6, 7, 8]))
```

**Output:**
```
Original: [1, 2, 3, 4, 5]
Modified: [2, 3, 4, 5, 6]
Search 3: [2]
Sorted: [1, 2, 3, 4, 5]
Reversed: [5, 4, 3, 2, 1]
Rotated by 2: [3, 4, 5, 1, 2]
Merged: [1, 2, 3, 4, 5, 6, 7, 8]
```

## Design Notes

- All methods return new lists rather than modifying in-place (except where noted)
- Implementations use explicit loops to demonstrate algorithmic patterns
- Intentionally avoids Python built-ins like `reversed()` or list slicing for benchmarking purposes
