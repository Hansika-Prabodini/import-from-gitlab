#!/usr/bin/env python3
"""Manual verification of the count_duplicates fix"""

from typing import List

def count_duplicates_buggy(arr0: List[int], arr1: List[int]) -> int:
    """Buggy version with i == j condition"""
    count = 0
    for i in range(len(arr0)):
        for j in range(len(arr1)):
            if i == j and arr0[i] == arr1[j]:
                count += 1
    return count

def count_duplicates_fixed(arr0: List[int], arr1: List[int]) -> int:
    """Fixed version without i == j condition"""
    count = 0
    for i in range(len(arr0)):
        for j in range(len(arr1)):
            if arr0[i] == arr1[j]:
                count += 1
    return count

# Test cases
test_cases = [
    ([0], [0]),
    ([1, 2, 3], [2, 3, 1]),
    ([1, 1, 1], [1, 2, 3]),
    ([1, 1, 2], [1, 2, 2]),
    ([1, 1, 2, 2], [1, 1, 2, 2]),
    ([1, 1], [1, 1]),  # New test case
]

print("Verification of count_duplicates fix")
print("=" * 60)

for arr0, arr1 in test_cases:
    buggy_result = count_duplicates_buggy(arr0, arr1)
    fixed_result = count_duplicates_fixed(arr0, arr1)
    
    print(f"\nInput: {arr0}, {arr1}")
    print(f"  Buggy implementation: {buggy_result}")
    print(f"  Fixed implementation: {fixed_result}")
    
    if buggy_result != fixed_result:
        print(f"  ✓ Different results (bug was present)")
    else:
        print(f"  = Same result")

print("\n" + "=" * 60)
print("\nExpected results for fixed implementation:")
print("([0], [0]): 1")
print("([1, 2, 3], [2, 3, 1]): 3")
print("([1, 1, 1], [1, 2, 3]): 3")
print("([1, 1, 2], [1, 2, 2]): 4")
print("([1, 1, 2, 2], [1, 1, 2, 2]): 8")
print("([1, 1], [1, 1]): 4")
