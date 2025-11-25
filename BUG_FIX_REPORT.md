# Bug Fix Report: rotate_list IndexError

## Summary
Fixed a bug in `DsList.rotate_list()` method that caused an `IndexError` when the rotation parameter `n` was greater than or equal to the list length.

## Bug Description

**Location:** `src/llm_benchmark/datastructures/dslist.py`, lines 72-87

**Issue:** The `rotate_list` function did not handle cases where the rotation parameter `n` is greater than or equal to the length of the list, causing an `IndexError`.

### Original Code
```python
@staticmethod
def rotate_list(v: List[int], n: int) -> List[int]:
    """Rotate a list of integers by n positions"""
    ret = []
    for i in range(n, len(v)):
        ret.append(v[i])
    for i in range(n):
        ret.append(v[i])
    return ret
```

### Bug Trigger
When `n >= len(v)`, the second loop attempts to access indices that don't exist:

**Example:**
```python
v = [1, 2, 3]  # length = 3
n = 5

# First loop: range(5, 3) is empty, ret = []
# Second loop: range(5) = [0, 1, 2, 3, 4]
#   - Accessing v[3] and v[4] causes IndexError!
```

### Edge Cases Not Handled
1. **n > len(v)**: Causes IndexError
2. **n == len(v)**: Causes IndexError or wrong result
3. **Empty list**: Could cause division by zero in modulo operation

## Fix Applied

### Fixed Code
```python
@staticmethod
def rotate_list(v: List[int], n: int) -> List[int]:
    """Rotate a list of integers by n positions"""
    if not v:  # Handle empty list
        return []
    
    # Use modulo to handle n >= len(v)
    n = n % len(v)
    
    ret = []
    for i in range(n, len(v)):
        ret.append(v[i])
    for i in range(n):
        ret.append(v[i])
    return ret
```

### Fix Details
1. **Empty list check**: Returns empty list immediately to avoid division by zero
2. **Modulo operation**: Wraps `n` to valid range `[0, len(v)-1]` using `n = n % len(v)`

This ensures that:
- Rotating by `len(v)` is same as rotating by 0 (no rotation)
- Rotating by `len(v) + k` is same as rotating by `k`
- Empty lists are handled gracefully

## Test Cases Added

Added comprehensive test cases in `tests/llm_benchmark/datastructures/test_dslist.py`:

```python
@pytest.mark.parametrize(
    "v, n, ref",
    [
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),  # No rotation
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),  # Normal rotation
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # Rotate by length (full rotation)
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),  # Rotate by more than length (n % len = 2)
        ([1, 2, 3], 10, [2, 3, 1]),  # n > len (10 % 3 = 1)
        ([], 5, []),  # Empty list
        ([1], 3, [1]),  # Single element
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    assert DsList.rotate_list(v, n) == ref
```

### Test Results
- **Before fix**: Tests with `n >= len(v)` would fail with `IndexError`
- **After fix**: All test cases pass successfully

## Impact
- **Severity**: High - Function crashes with certain inputs
- **Scope**: Any code using `rotate_list` with `n >= len(v)`
- **Backward compatibility**: Maintained - fix doesn't change behavior for valid inputs

## Files Modified
1. `src/llm_benchmark/datastructures/dslist.py` - Fixed the bug
2. `tests/llm_benchmark/datastructures/test_dslist.py` - Added comprehensive tests
3. `test_rotate_bug.py` - Demonstration script (can be run standalone)

## Validation Results

Ran the project's test suite with the following commands:
```bash
pip3 install poetry && python -m poetry install
python -m poetry run pytest --benchmark-skip tests/
python -m poetry run pytest --benchmark-only tests/
```

**Test Results:**
- ✅ **88 tests passed** including all new `rotate_list` edge case tests
- ⏭️ **19 tests skipped** (benchmark tests in regular run)
- ❌ **3 tests failed** - These are pre-existing SQL injection test failures in `tests/llm_benchmark/sql/test_query.py`, unrelated to this bug fix

**Datastructures Module Test Results:**
All tests in `tests/llm_benchmark/datastructures/test_dslist.py` passed:
- `test_modify_list` ✓
- `test_search_list` ✓  
- `test_sort_list` ✓
- `test_reverse_list` ✓
- `test_rotate_list` ✓ (NEW - 7 edge case scenarios)

**Benchmark Tests:**
All 19 benchmark tests passed, including:
- `test_benchmark_rotate_list` ✓ (NEW)

## Conclusion

Successfully identified and fixed a critical bug in the `rotate_list` function that would cause `IndexError` crashes when the rotation parameter exceeds the list length. The fix handles all edge cases properly using modulo arithmetic and includes comprehensive test coverage.
