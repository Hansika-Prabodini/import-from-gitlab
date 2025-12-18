"""
Test for the count_duplicates bug fix.

This test would fail before the patch (when i == j condition was present)
but passes after the patch (when the condition was removed).
"""
import pytest
from llm_benchmark.control.double import DoubleForLoop


def test_count_duplicates_all_elements():
    """
    Test that count_duplicates correctly counts all matching elements
    between two arrays, not just elements at the same index.
    
    Before the bug fix, the function only counted matches where i == j,
    so [1, 2, 3] and [2, 3, 1] would return 0 (no matches at same index).
    
    After the bug fix, it correctly counts all occurrences:
    - arr0[0]=1 appears 1 time in arr1 (at index 2)
    - arr0[1]=2 appears 1 time in arr1 (at index 0)
    - arr0[2]=3 appears 1 time in arr1 (at index 1)
    Total: 3 duplicates
    """
    arr0 = [1, 2, 3]
    arr1 = [2, 3, 1]
    expected = 3  # Each element in arr0 appears once in arr1
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected, f"Expected {expected} duplicates, got {result}"


def test_count_duplicates_multiple_occurrences():
    """
    Test counting when elements appear multiple times.
    
    arr0 = [1, 1, 2]
    arr1 = [1, 2, 3]
    
    - arr0[0]=1 appears 1 time in arr1 (at index 0) → 1
    - arr0[1]=1 appears 1 time in arr1 (at index 0) → 1
    - arr0[2]=2 appears 1 time in arr1 (at index 1) → 1
    Total: 3 duplicates
    
    With the bug (i == j condition), only arr0[1]=1 and arr1[1]=2 would be
    compared, resulting in 0 matches.
    """
    arr0 = [1, 1, 2]
    arr1 = [1, 2, 3]
    expected = 3
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected, f"Expected {expected} duplicates, got {result}"


def test_count_duplicates_with_repetitions():
    """
    Test with repeated values in both arrays.
    
    arr0 = [1, 2, 2]
    arr1 = [2, 2, 3]
    
    - arr0[0]=1 appears 0 times in arr1 → 0
    - arr0[1]=2 appears 2 times in arr1 (at indices 0 and 1) → 2
    - arr0[2]=2 appears 2 times in arr1 (at indices 0 and 1) → 2
    Total: 4 duplicates
    """
    arr0 = [1, 2, 2]
    arr1 = [2, 2, 3]
    expected = 4
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected, f"Expected {expected} duplicates, got {result}"


def test_count_duplicates_no_matches():
    """
    Test with no common elements.
    
    This should work correctly both before and after the fix.
    """
    arr0 = [1, 2, 3]
    arr1 = [4, 5, 6]
    expected = 0
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected, f"Expected {expected} duplicates, got {result}"
