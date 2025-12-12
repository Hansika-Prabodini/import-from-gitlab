from typing import List

import pytest

from llm_benchmark.datastructures.dslist import DsList


@pytest.mark.parametrize(
    "v, n, ref",
    [
        # Basic rotations
        ([1, 2, 3, 4, 5], 0, [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [2, 3, 4, 5, 1]),
        ([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # Full rotation
        # Bug case: n > len(v)
        ([1, 2, 3, 4, 5], 7, [3, 4, 5, 1, 2]),  # Same as rotating by 2
        ([1, 2, 3, 4, 5], 10, [1, 2, 3, 4, 5]),  # Same as rotating by 0
        # Negative rotation (right rotation)
        ([1, 2, 3, 4, 5], -1, [5, 1, 2, 3, 4]),  # Rotate right by 1
        ([1, 2, 3, 4, 5], -2, [4, 5, 1, 2, 3]),  # Rotate right by 2
    ],
)
def test_rotate_list(v: List[int], n: int, ref: List[int]) -> None:
    """Test rotate_list with various rotation amounts including edge cases"""
    assert DsList.rotate_list(v, n) == ref


def test_benchmark_rotate_list(benchmark) -> None:
    benchmark(DsList.rotate_list, [1, 2, 3, 4, 5], 2)
