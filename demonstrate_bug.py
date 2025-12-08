#!/usr/bin/env python3
"""
This script demonstrates the bug that existed before the fix.

To see the bug, you would need to revert the fix in gen_list.py:
Change line 17 from:
    return [randint(0, m - 1) for _ in range(n)]
Back to:
    return [randint(0, m) for _ in range(n)]

Then run this script to see the bug in action.
"""

from random import randint

def buggy_random_list(n: int, m: int):
    """The BUGGY version - includes m"""
    return [randint(0, m) for _ in range(n)]

def fixed_random_list(n: int, m: int):
    """The FIXED version - excludes m"""
    return [randint(0, m - 1) for _ in range(n)]

def main():
    print("Demonstrating the bug in random_list\n")
    print("=" * 70)
    
    m = 5
    n = 10000  # Large sample to ensure we hit the bug
    
    print(f"\nGenerating {n} random integers with m={m}")
    print(f"According to docstring: m is EXCLUSIVE, so valid range is [0, {m})")
    print(f"Expected values: {{0, 1, 2, 3, 4}}")
    print(f"Invalid value that shouldn't appear: {m}")
    print()
    
    # Test buggy version
    print("-" * 70)
    print("BUGGY VERSION (using randint(0, m)):")
    print("-" * 70)
    buggy_result = buggy_random_list(n, m)
    buggy_values = sorted(set(buggy_result))
    buggy_count_m = buggy_result.count(m)
    
    print(f"Unique values generated: {buggy_values}")
    print(f"Times {m} appeared: {buggy_count_m}")
    
    if m in buggy_result:
        print(f"❌ BUG: Value {m} appeared {buggy_count_m} times, but m should be exclusive!")
    else:
        print(f"⚠️  By chance, {m} didn't appear this time (try running again)")
    
    # Test fixed version
    print()
    print("-" * 70)
    print("FIXED VERSION (using randint(0, m-1)):")
    print("-" * 70)
    fixed_result = fixed_random_list(n, m)
    fixed_values = sorted(set(fixed_result))
    fixed_count_m = fixed_result.count(m)
    
    print(f"Unique values generated: {fixed_values}")
    print(f"Times {m} appeared: {fixed_count_m}")
    
    if m not in fixed_result:
        print(f"✓ CORRECT: Value {m} never appeared (m is exclusive as documented)")
    else:
        print(f"❌ ERROR: This shouldn't happen with the fix!")
    
    print()
    print("=" * 70)
    print("\nSummary:")
    print(f"- Buggy version can generate {m}, violating the 'exclusive' specification")
    print(f"- Fixed version never generates {m}, respecting the documentation")
    print(f"- The bug was fixed by changing randint(0, m) to randint(0, m-1)")

if __name__ == "__main__":
    main()
