from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 10),
        (1, 10),
        (5, 10),
        (10, 100),
        (100, 1000),
    ],
)
def test_random_list_length(n: int, m: int) -> None:
    """Test that random_list generates a list of correct length"""
    result = GenList.random_list(n, m)
    assert len(result) == n


@pytest.mark.parametrize(
    "n, m",
    [
        (5, 10),
        (10, 100),
        (20, 50),
    ],
)
def test_random_list_values_in_range(n: int, m: int) -> None:
    """Test that all values in random_list are within the expected range [0, m]"""
    result = GenList.random_list(n, m)
    assert all(0 <= val <= m for val in result)


def test_random_list_type() -> None:
    """Test that random_list returns a list of integers"""
    result = GenList.random_list(10, 100)
    assert isinstance(result, list)
    assert all(isinstance(val, int) for val in result)


def test_benchmark_random_list(benchmark) -> None:
    """Benchmark random_list generation"""
    benchmark(GenList.random_list, 100, 1000)


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 10),
        (1, 10),
        (3, 20),
        (5, 100),
        (10, 50),
    ],
)
def test_random_matrix_dimensions(n: int, m: int) -> None:
    """Test that random_matrix generates a matrix of correct dimensions (n x n)"""
    result = GenList.random_matrix(n, m)
    assert len(result) == n
    for row in result:
        assert len(row) == n


@pytest.mark.parametrize(
    "n, m",
    [
        (3, 10),
        (5, 50),
        (10, 100),
    ],
)
def test_random_matrix_values_in_range(n: int, m: int) -> None:
    """Test that all values in random_matrix are within the expected range [0, m]"""
    result = GenList.random_matrix(n, m)
    for row in result:
        assert all(0 <= val <= m for val in row)


def test_random_matrix_type() -> None:
    """Test that random_matrix returns a list of lists of integers"""
    result = GenList.random_matrix(5, 100)
    assert isinstance(result, list)
    for row in result:
        assert isinstance(row, list)
        assert all(isinstance(val, int) for val in row)


def test_benchmark_random_matrix(benchmark) -> None:
    """Benchmark random_matrix generation"""
    benchmark(GenList.random_matrix, 10, 100)


def test_random_list_empty() -> None:
    """Test edge case: generating an empty list"""
    result = GenList.random_list(0, 10)
    assert result == []


def test_random_matrix_empty() -> None:
    """Test edge case: generating an empty matrix"""
    result = GenList.random_matrix(0, 10)
    assert result == []


def test_random_list_single_element() -> None:
    """Test edge case: generating a list with single element"""
    result = GenList.random_list(1, 10)
    assert len(result) == 1
    assert 0 <= result[0] <= 10


def test_random_matrix_single_element() -> None:
    """Test edge case: generating a 1x1 matrix"""
    result = GenList.random_matrix(1, 10)
    assert len(result) == 1
    assert len(result[0]) == 1
    assert 0 <= result[0][0] <= 10
