from typing import List

import pytest

from llm_benchmark.generator.gen_list import GenList


@pytest.mark.parametrize(
    "n, m",
    [
        (0, 10),
        (1, 10),
        (5, 10),
        (10, 10),
        (100, 50),
    ],
)
def test_random_list_length(n: int, m: int) -> None:
    """Test that random_list generates the correct number of elements"""
    result = GenList.random_list(n, m)
    assert len(result) == n


@pytest.mark.parametrize(
    "n, m",
    [
        (5, 10),
        (10, 5),
        (20, 100),
    ],
)
def test_random_list_range(n: int, m: int) -> None:
    """Test that random_list generates values in the correct range [0, m]"""
    result = GenList.random_list(n, m)
    for value in result:
        assert 0 <= value <= m
        assert isinstance(value, int)


def test_random_list_type() -> None:
    """Test that random_list returns a list of integers"""
    result = GenList.random_list(10, 20)
    assert isinstance(result, list)
    for value in result:
        assert isinstance(value, int)


def test_benchmark_random_list(benchmark) -> None:
    """Benchmark random_list generation"""
    benchmark(GenList.random_list, 100, 50)


@pytest.mark.parametrize(
    "n, m",
    [
        (1, 10),
        (3, 10),
        (5, 10),
        (10, 20),
    ],
)
def test_random_matrix_dimensions(n: int, m: int) -> None:
    """Test that random_matrix generates correct dimensions"""
    result = GenList.random_matrix(n, m)
    assert len(result) == n
    for row in result:
        assert len(row) == n


@pytest.mark.parametrize(
    "n, m",
    [
        (3, 10),
        (5, 20),
    ],
)
def test_random_matrix_range(n: int, m: int) -> None:
    """Test that random_matrix generates values in the correct range [0, m]"""
    result = GenList.random_matrix(n, m)
    for row in result:
        for value in row:
            assert 0 <= value <= m
            assert isinstance(value, int)


def test_random_matrix_type() -> None:
    """Test that random_matrix returns a list of lists of integers"""
    result = GenList.random_matrix(5, 10)
    assert isinstance(result, list)
    for row in result:
        assert isinstance(row, list)
        for value in row:
            assert isinstance(value, int)


def test_benchmark_random_matrix(benchmark) -> None:
    """Benchmark random_matrix generation"""
    benchmark(GenList.random_matrix, 10, 50)
