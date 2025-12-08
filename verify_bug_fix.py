#!/usr/bin/env python3
"""
Verification script to demonstrate the bug fix in GenList.random_list

BEFORE THE FIX:
- random_list(n, m) used randint(0, m), which includes m as a possible value
- This violated the docstring which stated m is exclusive
- With m=5, values could be 0, 1, 2, 3, 4, or 5 (WRONG!)

AFTER THE FIX:
- random_list(n, m) uses randint(0, m-1), which excludes m
- This matches the docstring specification
- With m=5, values are only 0, 1, 2, 3, or 4 (CORRECT!)
"""

from llm_benchmark.generator.gen_list import GenList

def verify_fix():
    print("=" * 60)
    print("Verifying Bug Fix in GenList.random_list")
    print("=" * 60)
    print()
    
    # Test with a small value of m to make the bug obvious
    m = 5
    n = 1000
    
    print(f"Generating {n} random integers with m={m} (exclusive)")
    print(f"Expected range: [0, {m}) = {{0, 1, 2, 3, 4}}")
    print()
    
    result = GenList.random_list(n, m)
    unique_values = set(result)
    
    print(f"Unique values generated: {sorted(unique_values)}")
    print()
    
    # Check if m appears in the result (it shouldn't!)
    if m in result:
        print(f"❌ BUG FOUND: Value {m} appears in result (should be exclusive)!")
        print(f"   This violates the docstring specification.")
        return False
    else:
        print(f"✓ CORRECT: Value {m} does not appear in result (as expected)")
    
    # Check all values are in valid range
    if all(0 <= val < m for val in result):
        print(f"✓ CORRECT: All values are in range [0, {m})")
    else:
        invalid = [val for val in result if val < 0 or val >= m]
        print(f"❌ BUG: Found invalid values: {invalid}")
        return False
    
    print()
    print("=" * 60)
    print("✓ All checks passed! Bug is fixed.")
    print("=" * 60)
    return True

if __name__ == "__main__":
    verify_fix()
