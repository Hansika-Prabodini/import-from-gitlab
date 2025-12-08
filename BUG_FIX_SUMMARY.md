# Bug Fix Summary

## Bug Description

**Location:** `src/llm_benchmark/datastructures/dslist.py`, function `rotate_list`

**Issue:** The `rotate_list` function did not properly handle edge cases:
1. When `n` (rotation amount) is negative
2. When `n` is greater than the length of the list
3. When the list is empty

### Symptoms Before Fix

1. **Negative rotation values:** For `rotate_list([1, 2, 3, 4, 5], -1)`, the function would return an empty list `[]` instead of performing a right rotation to get `[5, 1, 2, 3, 4]`.

2. **Large rotation values:** For `rotate_list([1, 2, 3, 4, 5], 7)`, the function would crash with an `IndexError` when trying to access indices beyond the list bounds.

3. **Empty list:** Would cause a division by zero error when computing modulo.

## The Fix

**File:** `src/llm_benchmark/datastructures/dslist.py`

Added normalization logic to handle all edge cases:

```python
if len(v) == 0:
    return []

# Normalize n to handle negative values and values > len(v)
n = n % len(v)
```

### How it works:

- **Empty list check:** Returns an empty list immediately if the input is empty
- **Modulo operation:** `n % len(v)` normalizes the rotation amount:
  - For positive `n > len(v)`: wraps around (e.g., `7 % 5 = 2`)
  - For negative `n`: converts to equivalent positive rotation (e.g., `-1 % 5 = 4`)
  - For `n == 0` or `n == len(v)`: results in 0 (no rotation)

## Unit Tests Added

**File:** `tests/llm_benchmark/datastructures/test_dslist.py`

Added comprehensive test cases for `rotate_list`:

```python
@pytest.mark.parametrize(
    "v, n, ref",
    [
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),      # Normal rotation
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),      # No rotation
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),      # Full rotation
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),      # n > len(v)
        ([1, 2, 3, 4, 5], -1, [5, 1, 2, 3, 4]),     # Negative (right rotation)
        ([1, 2, 3, 4, 5], -2, [4, 5, 1, 2, 3]),     # Negative rotation
        ([1, 2, 3], 10, [2, 3, 1]),                 # Large n
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    assert DsList.rotate_list(v, n) == ref
```

Also added a benchmark test:
```python
def test_benchmark_rotate_list(benchmark) -> None:
    benchmark(DsList.rotate_list, [1, 2, 3, 4, 5], 2)
```

## Testing Status

✅ **Before the patch:** Tests would fail or crash
- `rotate_list([1, 2, 3, 4, 5], 7)` → `IndexError`
- `rotate_list([1, 2, 3, 4, 5], -1)` → Returns `[]` instead of `[5, 1, 2, 3, 4]`

✅ **After the patch:** All tests pass correctly
- Edge cases are handled properly
- Normal rotations continue to work as expected
- The function is now robust and reliable
