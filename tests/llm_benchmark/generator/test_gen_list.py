import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_bounds():
    """Test that random_list generates values in the correct range [0, m)
    
    According to the docstring, m should be exclusive (maximum value exclusive).
    This test verifies that generated values are always < m, never == m.
    """
    m = 5  # Maximum value (should be exclusive)
    n = 1000  # Generate many values to increase confidence
    
    # Generate a large list to test the bounds
    result = GenList.random_list(n, m)
    
    # All values should be in range [0, m)
    # None of the values should equal m (since m is exclusive)
    assert all(0 <= val < m for val in result), \
        f"All values should be in range [0, {m}), but got values: {set(result)}"
    
    # Specifically check that no value equals m
    assert m not in result, \
        f"Value {m} should not appear (m is exclusive), but found in list"


def test_random_list_edge_cases():
    """Test edge cases for random_list"""
    # Test with m=1 (should only generate 0)
    result = GenList.random_list(100, 1)
    assert all(val == 0 for val in result), "With m=1, only 0 should be generated"
    
    # Test with m=2 (should only generate 0 or 1, never 2)
    result = GenList.random_list(100, 2)
    assert all(val in [0, 1] for val in result), "With m=2, only 0 or 1 should be generated"
    assert 2 not in result, "Value 2 should not appear when m=2"


def test_random_list_length():
    """Test that random_list generates the correct number of elements"""
    n = 10
    m = 5
    result = GenList.random_list(n, m)
    assert len(result) == n, f"Expected list of length {n}, got {len(result)}"


def test_random_matrix_bounds():
    """Test that random_matrix generates values in the correct range"""
    n = 5
    m = 3
    result = GenList.random_matrix(n, m)
    
    # Check matrix dimensions
    assert len(result) == n, f"Expected {n} rows, got {len(result)}"
    
    # Check all values are in range [0, m)
    for row in result:
        assert all(0 <= val < m for val in row), \
            f"All values should be in range [0, {m}), but got: {set(val for row in result for val in row)}"


def test_benchmark_random_list(benchmark):
    """Benchmark random_list generation"""
    benchmark(GenList.random_list, 100, 10)


def test_benchmark_random_matrix(benchmark):
    """Benchmark random_matrix generation"""
    benchmark(GenList.random_matrix, 10, 10)
