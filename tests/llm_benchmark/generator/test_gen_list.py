import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_max_exclusive():
    """Test that random_list respects the exclusive upper bound for max value.
    
    According to the docstring, m should be exclusive, meaning values should be
    in range [0, m) not [0, m].
    
    This test generates many random numbers and verifies none of them equal m.
    With the bug (using randint(0, m)), this test will eventually fail because
    randint can return m. With the fix (using randint(0, m-1)), it will always pass.
    """
    m = 5
    n = 1000  # Generate many samples to catch the bug
    
    # Generate many lists and check all values are < m (exclusive)
    for _ in range(100):  # Multiple iterations to increase confidence
        result = GenList.random_list(n, m)
        # All values should be in [0, m), so max value should be at most m-1
        assert all(val < m for val in result), f"Found value >= {m} in result, but m should be exclusive"
        assert all(val >= 0 for val in result), "Found negative value"


def test_random_list_boundary():
    """Test boundary case: with m=1, should only generate 0s (exclusive of 1)."""
    result = GenList.random_list(100, 1)
    assert all(val == 0 for val in result), "With m=1 (exclusive), should only generate 0s"


def test_random_list_basic():
    """Test basic functionality of random_list."""
    result = GenList.random_list(10, 10)
    assert len(result) == 10, "Should generate exactly n integers"
    assert all(isinstance(val, int) for val in result), "All values should be integers"
