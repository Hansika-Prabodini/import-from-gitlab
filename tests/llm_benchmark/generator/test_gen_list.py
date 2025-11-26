import pytest
from llm_benchmark.generator.gen_list import GenList


def test_random_list_length():
    """Test that random_list generates correct number of elements"""
    n = 10
    m = 5
    result = GenList.random_list(n, m)
    assert len(result) == n, f"Expected {n} elements, got {len(result)}"


def test_random_matrix_dimensions():
    """Test that random_matrix generates correct dimensions (n rows x m columns)"""
    n = 3  # Number of rows
    m = 5  # Number of columns
    
    matrix = GenList.random_matrix(n, m)
    
    # Check number of rows
    assert len(matrix) == n, f"Expected {n} rows, got {len(matrix)}"
    
    # Check number of columns in each row
    for i, row in enumerate(matrix):
        assert len(row) == m, f"Row {i}: Expected {m} columns, got {len(row)}"


def test_random_matrix_square():
    """Test that random_matrix works for square matrices"""
    n = 4
    m = 4
    
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n
    for row in matrix:
        assert len(row) == m


def test_random_matrix_rectangular():
    """Test that random_matrix works for rectangular matrices (more columns than rows)"""
    n = 2  # rows
    m = 7  # columns
    
    matrix = GenList.random_matrix(n, m)
    
    assert len(matrix) == n
    for row in matrix:
        assert len(row) == m
