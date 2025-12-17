import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that the maximum value m is exclusive (not included in the generated values).
    
    This test will fail with the current bug where randint(0, m) is used (inclusive),
    and pass after the fix where randint(0, m-1) is used (exclusive of m).
    """
    # Generate many random numbers to get statistical confidence
    # that if m could be generated, it would appear at least once
    m = 10
    n = 1000  # Generate 1000 numbers
    
    result = GenList.random_list(n, m)
    
    # Assert that no value equals m (since m should be exclusive)
    assert all(val < m for val in result), f"Found value >= {m} in result, but m should be exclusive"
    
    # Also verify that values are >= 0
    assert all(val >= 0 for val in result), "Found negative value in result"


def test_random_list_reaches_m_minus_1():
    """Test that the maximum value that can be generated is m-1.
    
    This ensures the range is [0, m) not [0, m-k) for some k > 1.
    """
    # Generate many random numbers with a small range to increase probability
    # of hitting the maximum value
    m = 3  # Range should be [0, 1, 2]
    n = 500  # Generate enough numbers
    
    all_results = set()
    # Run multiple times to ensure we hit all values
    for _ in range(10):
        result = GenList.random_list(n, m)
        all_results.update(result)
    
    # Should contain 0, 1, 2 but not 3
    assert 0 in all_results, "Value 0 should be possible"
    assert 1 in all_results, "Value 1 should be possible"
    assert 2 in all_results, "Value 2 (m-1) should be possible"
    assert m not in all_results, f"Value {m} should not be possible (m is exclusive)"


def test_random_list_length():
    """Test that random_list generates the correct number of elements."""
    assert len(GenList.random_list(10, 100)) == 10
    assert len(GenList.random_list(5, 10)) == 5
    assert len(GenList.random_list(1, 5)) == 1
    assert len(GenList.random_list(0, 10)) == 0


def test_random_matrix_dimensions():
    """Test that random_matrix generates square matrices with correct dimensions."""
    # Test 3x3 matrix
    matrix = GenList.random_matrix(3, 10)
    assert len(matrix) == 3, "Should have 3 rows"
    assert all(len(row) == 3 for row in matrix), "Each row should have 3 elements"
    
    # Test 2x2 matrix
    matrix = GenList.random_matrix(2, 5)
    assert len(matrix) == 2, "Should have 2 rows"
    assert all(len(row) == 2 for row in matrix), "Each row should have 2 elements"


def test_random_matrix_values_in_range():
    """Test that random_matrix generates values in the correct range [0, m)."""
    m = 10
    matrix = GenList.random_matrix(5, m)
    
    # Flatten matrix to check all values
    all_values = [val for row in matrix for val in row]
    
    # All values should be < m (exclusive) and >= 0
    assert all(val < m for val in all_values), f"Found value >= {m}, but m should be exclusive"
    assert all(val >= 0 for val in all_values), "Found negative value"
