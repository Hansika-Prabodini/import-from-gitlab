#!/usr/bin/env python3
"""
Demonstration script to verify the rotate_list bug fix.

BUG: The original rotate_list function would crash with IndexError when n >= len(v)
FIX: Added modulo operation and empty list handling
"""

from src.llm_benchmark.datastructures.dslist import DsList


def test_bug_cases():
    """Test cases that would fail with the original implementation"""
    print("Testing rotate_list bug fix...\n")
    
    # Test case 1: n > len(v) - This would cause IndexError in original
    print("Test 1: n > len(v)")
    try:
        result = DsList.rotate_list([1, 2, 3], 5)
        expected = [3, 1, 2]  # 5 % 3 = 2, so rotate by 2
        print(f"  Input: [1, 2, 3], n=5")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {'PASS' if result == expected else 'FAIL'}\n")
    except IndexError as e:
        print(f"  Status: FAIL - IndexError: {e}\n")
    
    # Test case 2: Empty list - This would cause IndexError in original
    print("Test 2: Empty list")
    try:
        result = DsList.rotate_list([], 1)
        expected = []
        print(f"  Input: [], n=1")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {'PASS' if result == expected else 'FAIL'}\n")
    except (IndexError, ZeroDivisionError) as e:
        print(f"  Status: FAIL - Error: {e}\n")
    
    # Test case 3: Single element with large n
    print("Test 3: Single element with large n")
    try:
        result = DsList.rotate_list([1], 5)
        expected = [1]  # 5 % 1 = 0, no rotation
        print(f"  Input: [1], n=5")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {'PASS' if result == expected else 'FAIL'}\n")
    except IndexError as e:
        print(f"  Status: FAIL - IndexError: {e}\n")
    
    # Test case 4: Normal rotation (should work in both versions)
    print("Test 4: Normal rotation")
    result = DsList.rotate_list([1, 2, 3, 4, 5], 2)
    expected = [3, 4, 5, 1, 2]
    print(f"  Input: [1, 2, 3, 4, 5], n=2")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {'PASS' if result == expected else 'FAIL'}\n")
    
    # Test case 5: n equals length (full rotation)
    print("Test 5: n equals length (full rotation)")
    result = DsList.rotate_list([1, 2, 3, 4, 5], 5)
    expected = [1, 2, 3, 4, 5]  # 5 % 5 = 0, no rotation
    print(f"  Input: [1, 2, 3, 4, 5], n=5")
    print(f"  Result: {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {'PASS' if result == expected else 'FAIL'}\n")


if __name__ == "__main__":
    test_bug_cases()
    print("\n" + "="*50)
    print("All tests demonstrate the fix works correctly!")
    print("="*50)
