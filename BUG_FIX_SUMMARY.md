# Bug Fix Summary

## Bug Identified
**File:** `src/llm_benchmark/datastructures/dslist.py`  
**Function:** `rotate_list()`  
**Line:** 72-87 (original implementation)

### Description
The `rotate_list()` function had a critical bug that caused an `IndexError` when:
1. The rotation amount `n` was greater than or equal to the list length (`n >= len(v)`)
2. The list was empty and `n > 0`

### Root Cause
The function attempted to access list indices beyond the list's bounds when the rotation amount exceeded the list length. For example:
- Input: `v = [1, 2, 3]`, `n = 5`
- The second loop would try to access `v[3]` and `v[4]`, which don't exist
- Result: `IndexError: list index out of range`

## The Fix
Added two key improvements to the function:

### 1. Empty List Handling
```python
if not v:  # Handle empty list
    return []
```

### 2. Rotation Normalization
```python
n = n % len(v)  # Normalize rotation amount to handle n >= len(v)
```

This ensures that:
- Rotating by the list length returns the original list
- Rotating by more than the list length is equivalent to rotating by `n % len(v)`
- Empty lists are handled gracefully

## Test Cases Added
Added comprehensive test cases in `tests/llm_benchmark/datastructures/test_dslist.py`:

```python
@pytest.mark.parametrize(
    "v, n, ref",
    [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),  # No rotation
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),  # Normal rotation
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # Rotate by length (full cycle)
        ([1, 2, 3], 5, [3, 1, 2]),  # n > len(v), equivalent to n % len(v) = 2
        ([1, 2, 3], 7, [2, 3, 1]),  # n > len(v), equivalent to n % len(v) = 1
        ([], 1, []),  # Empty list
        ([1], 5, [1]),  # Single element
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    assert DsList.rotate_list(v, n) == ref
```

Also added benchmark test:
```python
def test_benchmark_rotate_list(benchmark) -> None:
    benchmark(DsList.rotate_list, [1, 2, 3, 4, 5], 2)
```

## Verification
The bug fix can be verified by running:
```bash
python test_rotate_fix.py
```

Or by running the full test suite:
```bash
python -m poetry run pytest tests/llm_benchmark/datastructures/test_dslist.py::test_rotate_list -v
```

## Impact
- **Before Fix:** Function would crash with `IndexError` for edge cases
- **After Fix:** Function handles all edge cases gracefully and correctly rotates lists regardless of rotation amount

## Files Modified
1. `src/llm_benchmark/datastructures/dslist.py` - Fixed the `rotate_list()` function
2. `tests/llm_benchmark/datastructures/test_dslist.py` - Added comprehensive test cases
3. `test_rotate_fix.py` - Created demonstration script (can be removed after verification)
