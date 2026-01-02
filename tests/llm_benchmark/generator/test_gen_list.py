import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_matrix_dimensions():
    """Test that random_matrix creates a matrix with correct dimensions.
    
    This test checks that random_matrix(n, m) creates an n×m matrix
    (n rows, m columns) as specified in the docstring.
    
    Bug: The current implementation creates an n×n matrix instead of n×m.
    """
    # Test case 1: 3 rows, 5 columns
    matrix = GenList.random_matrix(3, 5)
    assert len(matrix) == 3, f"Expected 3 rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == 5, f"Expected 5 columns in row {i}, got {len(row)}"
    
    # Test case 2: 2 rows, 7 columns
    matrix = GenList.random_matrix(2, 7)
    assert len(matrix) == 2, f"Expected 2 rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == 7, f"Expected 7 columns in row {i}, got {len(row)}"
    
    # Test case 3: 5 rows, 2 columns (reverse of case 2)
    matrix = GenList.random_matrix(5, 2)
    assert len(matrix) == 5, f"Expected 5 rows, got {len(matrix)}"
    for i, row in enumerate(matrix):
        assert len(row) == 2, f"Expected 2 columns in row {i}, got {len(row)}"


def test_random_matrix_square():
    """Test that random_matrix still works correctly for square matrices."""
    # For square matrices (n == m), the bug wouldn't be apparent
    matrix = GenList.random_matrix(4, 4)
    assert len(matrix) == 4
    for row in matrix:
        assert len(row) == 4


def test_random_list_length():
    """Test that random_list generates correct number of elements."""
    lst = GenList.random_list(10, 100)
    assert len(lst) == 10
    # Verify all elements are within range [0, 100]
    for elem in lst:
        assert 0 <= elem <= 100
