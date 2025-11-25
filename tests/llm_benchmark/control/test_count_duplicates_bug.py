"""
Unit test that demonstrates the bug in count_duplicates function.

This test would FAIL with the buggy version (which had 'if i == j and arr0[i] == arr1[j]')
but PASSES with the fixed version (which has 'if arr0[i] == arr1[j]').

The bug was that the function only counted duplicates at the same index position,
rather than counting all occurrences of elements from arr0 that appear in arr1.
"""

import pytest
from llm_benchmark.control.double import DoubleForLoop


def test_count_duplicates_different_positions():
    """
    Test that count_duplicates correctly counts elements that appear in both arrays,
    regardless of their position.
    
    This test demonstrates the bug: with the old code (i == j condition),
    this would return 0 because the elements are at different positions.
    With the fix, it correctly returns 3.
    """
    arr0 = [1, 2, 3]
    arr1 = [3, 2, 1]  # Same elements but in different positions
    
    # Each element in arr0 appears exactly once in arr1
    # 1 from arr0 matches 1 in arr1 (1 match)
    # 2 from arr0 matches 2 in arr1 (1 match)
    # 3 from arr0 matches 3 in arr1 (1 match)
    # Total: 3 matches
    expected = 3
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected, (
        f"Expected {expected} duplicates but got {result}. "
        "The function should count all occurrences where elements from arr0 appear in arr1, "
        "regardless of position."
    )


def test_count_duplicates_multiple_occurrences():
    """
    Test that count_duplicates correctly counts when the same value appears
    multiple times in one or both arrays.
    
    This test also demonstrates the bug with repeated elements.
    """
    arr0 = [1, 1, 2]
    arr1 = [2, 1]
    
    # First 1 from arr0 matches 1 in arr1 (1 match)
    # Second 1 from arr0 matches 1 in arr1 (1 match)  
    # 2 from arr0 matches 2 in arr1 (1 match)
    # Total: 3 matches
    expected = 3
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected


def test_count_duplicates_no_common_elements():
    """
    Test that count_duplicates returns 0 when arrays have no common elements.
    """
    arr0 = [1, 2, 3]
    arr1 = [4, 5, 6]
    
    expected = 0
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected


def test_count_duplicates_all_same():
    """
    Test with arrays containing the same repeated value.
    """
    arr0 = [5, 5, 5]
    arr1 = [5, 5]
    
    # Each of 3 fives in arr0 matches each of 2 fives in arr1
    # 3 * 2 = 6 matches
    expected = 6
    
    result = DoubleForLoop.count_duplicates(arr0, arr1)
    assert result == expected
