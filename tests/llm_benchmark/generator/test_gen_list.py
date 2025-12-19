import pytest

from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_value_exclusive():
    """Test that random_list respects m as exclusive upper bound.
    
    This test verifies that the maximum value m is never generated,
    as documented. With m=5, values should be in [0, 1, 2, 3, 4] only.
    """
    # Generate many random values to ensure m never appears
    for _ in range(100):
        random_values = GenList.random_list(100, 5)
        
        # Check that all values are less than m (m is exclusive)
        for value in random_values:
            assert value < 5, f"Value {value} should be less than m=5 (exclusive)"
            assert value >= 0, f"Value {value} should be >= 0"


def test_random_list_m_equals_1():
    """Test edge case where m=1 should only generate 0s.
    
    With m=1 (exclusive), the only valid value is 0.
    This test would fail if randint(0, m) is used (generating 0 or 1)
    but pass if randint(0, m-1) is used (generating only 0).
    """
    random_values = GenList.random_list(50, 1)
    
    # All values should be 0 when m=1 (exclusive)
    for value in random_values:
        assert value == 0, f"With m=1 (exclusive), only value 0 should be generated, got {value}"


def test_random_list_length():
    """Test that random_list generates the correct number of elements."""
    assert len(GenList.random_list(10, 100)) == 10
    assert len(GenList.random_list(0, 100)) == 0
    assert len(GenList.random_list(1, 100)) == 1


def test_random_list_values_in_range():
    """Test that all generated values are within the expected range [0, m)."""
    n, m = 50, 10
    random_values = GenList.random_list(n, m)
    
    assert len(random_values) == n
    for value in random_values:
        assert 0 <= value < m, f"Value {value} not in range [0, {m})"


def test_benchmark_random_list(benchmark):
    """Benchmark the random_list function."""
    benchmark(GenList.random_list, 100, 100)


def test_random_matrix_shape():
    """Test that random_matrix generates correct dimensions."""
    matrix = GenList.random_matrix(5, 10)
    
    assert len(matrix) == 5, "Matrix should have n rows"
    for row in matrix:
        assert len(row) == 5, "Each row should have n elements"


def test_benchmark_random_matrix(benchmark):
    """Benchmark the random_matrix function."""
    benchmark(GenList.random_matrix, 10, 10)
