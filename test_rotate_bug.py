"""
Demonstration of the rotate_list bug and fix.

BUG: The original rotate_list function crashes with IndexError when n >= len(v)
FIX: Use modulo to wrap n to valid range: n = n % len(v)
"""

from src.llm_benchmark.datastructures.dslist import DsList


def test_original_bug():
    """This test demonstrates the bug that would occur with the original code."""
    print("Testing rotate_list with edge cases...")
    
    # Test case 1: n > len(v) - This would cause IndexError in original code
    print("\nTest 1: Rotate [1, 2, 3] by 5 positions")
    result = DsList.rotate_list([1, 2, 3], 5)
    expected = [3, 1, 2]  # 5 % 3 = 2, so same as rotating by 2
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ PASS")
    
    # Test case 2: n == len(v) - Full rotation should return original
    print("\nTest 2: Rotate [1, 2, 3, 4, 5] by 5 positions (full rotation)")
    result = DsList.rotate_list([1, 2, 3, 4, 5], 5)
    expected = [1, 2, 3, 4, 5]
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ PASS")
    
    # Test case 3: n >> len(v) - Large rotation
    print("\nTest 3: Rotate [1, 2, 3] by 10 positions")
    result = DsList.rotate_list([1, 2, 3], 10)
    expected = [2, 3, 1]  # 10 % 3 = 1, so same as rotating by 1
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ PASS")
    
    # Test case 4: Empty list
    print("\nTest 4: Rotate empty list [] by 5 positions")
    result = DsList.rotate_list([], 5)
    expected = []
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ PASS")
    
    # Test case 5: Normal case (for comparison)
    print("\nTest 5: Rotate [1, 2, 3, 4, 5] by 2 positions (normal case)")
    result = DsList.rotate_list([1, 2, 3, 4, 5], 2)
    expected = [3, 4, 5, 1, 2]
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ PASS")
    
    print("\n" + "="*50)
    print("All tests PASSED! The bug has been fixed.")
    print("="*50)


if __name__ == "__main__":
    test_original_bug()
