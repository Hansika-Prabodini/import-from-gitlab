import pytest
from llm_benchmark.generator.gen_list import GenList


class TestRandomList:
    """Tests for random_list function"""
    
    def test_random_list_length(self):
        """Test that random_list generates correct number of elements"""
        result = GenList.random_list(10, 5)
        assert len(result) == 10
    
    def test_random_list_empty(self):
        """Test that random_list handles zero length"""
        result = GenList.random_list(0, 10)
        assert len(result) == 0
    
    def test_random_list_values_in_range(self):
        """Test that generated values are within expected range"""
        # Note: randint(0, m) is inclusive, so values should be in [0, m]
        result = GenList.random_list(100, 10)
        for val in result:
            assert 0 <= val <= 10


class TestRandomMatrix:
    """Tests for random_matrix function - testing the bug fix"""
    
    def test_random_matrix_dimensions(self):
        """Test that random_matrix creates n×m matrix (not n×n)
        
        This test will FAIL before the bug fix and PASS after.
        The bug is that the function creates n×n matrices instead of n×m.
        """
        # Test case 1: 3 rows, 5 columns
        result = GenList.random_matrix(3, 5)
        assert len(result) == 3, "Should have 3 rows"
        for row in result:
            assert len(row) == 5, f"Each row should have 5 columns, but got {len(row)}"
    
    def test_random_matrix_square(self):
        """Test square matrix (n=m) still works correctly"""
        result = GenList.random_matrix(4, 4)
        assert len(result) == 4
        for row in result:
            assert len(row) == 4
    
    def test_random_matrix_rectangular_various_sizes(self):
        """Test various rectangular matrix sizes"""
        test_cases = [
            (2, 5),   # 2×5 matrix
            (5, 2),   # 5×2 matrix
            (1, 10),  # 1×10 matrix (single row)
            (10, 1),  # 10×1 matrix (single column)
        ]
        
        for rows, cols in test_cases:
            result = GenList.random_matrix(rows, cols)
            assert len(result) == rows, f"Expected {rows} rows, got {len(result)}"
            for i, row in enumerate(result):
                assert len(row) == cols, f"Expected {cols} columns in row {i}, got {len(row)}"
    
    def test_random_matrix_empty(self):
        """Test edge case with zero rows"""
        result = GenList.random_matrix(0, 5)
        assert len(result) == 0
    
    def test_random_matrix_values_in_range(self):
        """Test that generated values are within expected range"""
        result = GenList.random_matrix(5, 5)
        for row in result:
            for val in row:
                assert 0 <= val <= 5


def test_benchmark_random_list(benchmark):
    """Benchmark test for random_list"""
    benchmark(GenList.random_list, 100, 50)


def test_benchmark_random_matrix(benchmark):
    """Benchmark test for random_matrix"""
    benchmark(GenList.random_matrix, 10, 10)
