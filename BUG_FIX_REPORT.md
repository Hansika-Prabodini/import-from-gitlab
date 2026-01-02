# Bug Fix Report

## Bug Description

**File:** `src/llm_benchmark/generator/gen_list.py`  
**Function:** `random_matrix(n: int, m: int)`  
**Line:** 30

### The Issue

The `random_matrix` function was creating an **n×n matrix** instead of an **n×m matrix** as specified in its docstring.

According to the function's documentation:
- Parameter `n`: Number of rows
- Parameter `m`: Number of columns

However, the implementation was:
```python
return [GenList.random_list(n, m) for _ in range(n)]
```

This creates `n` rows (correct), but each row contains `n` elements instead of `m` elements, because `random_list(n, m)` generates `n` integers (where the first parameter is the count).

### Example of the Bug

Before the fix:
```python
matrix = GenList.random_matrix(3, 5)  # Should be 3 rows × 5 columns
# Actually created: 3 rows × 3 columns (wrong!)
```

## The Fix

Changed line 30 from:
```python
return [GenList.random_list(n, m) for _ in range(n)]
```

To:
```python
return [GenList.random_list(m, m) for _ in range(n)]
```

This now correctly creates `n` rows, each with `m` columns. Each element will have a maximum value of `m`.

## Unit Test

Created `tests/llm_benchmark/generator/test_gen_list.py` with test cases that verify:

1. **Non-square matrices**: Tests with 3×5, 2×7, and 5×2 matrices to ensure rows and columns are correct
2. **Square matrices**: Tests with 4×4 to ensure square matrices still work
3. **Element count verification**: Tests that verify each row has the correct number of columns

### Test Behavior

- **Before the patch**: The test `test_random_matrix_dimensions()` would fail because:
  - `GenList.random_matrix(3, 5)` creates a 3×3 matrix instead of 3×5
  - Assertion `assert len(row) == 5` would fail with actual value of 3

- **After the patch**: All tests pass because:
  - `GenList.random_matrix(3, 5)` correctly creates a 3×5 matrix
  - All dimension assertions pass

## Impact

This bug would affect any code that relies on `random_matrix` to generate non-square matrices. The function would produce incorrect dimensions, potentially causing:
- Index out of bounds errors
- Incorrect test data generation
- Wrong benchmark results
