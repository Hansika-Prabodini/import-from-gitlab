#!/usr/bin/env python3
"""
Demonstration of the bug and its fix.

This script shows what would happen with the old buggy code vs the fixed code.
"""

from random import randint

def random_list_buggy(n: int, m: int):
    """Original buggy implementation"""
    return [randint(0, m) for _ in range(n)]

def random_list_fixed(n: int, m: int):
    """Fixed implementation"""
    return [randint(0, m - 1) for _ in range(n)]

print("Bug Demonstration: random_list function")
print("=" * 70)
print("\nDocumentation states: m is 'Maximum value of integers (exclusive)'")
print("With m=5, valid values should be: {0, 1, 2, 3, 4}")
print()

# Test with m=5
m = 5
n = 10000

print(f"Generating {n} random values with m={m}...\n")

# Buggy version
buggy_values = random_list_buggy(n, m)
buggy_unique = set(buggy_values)
buggy_has_m = m in buggy_values
buggy_max = max(buggy_values)

print("BUGGY VERSION (using randint(0, m)):")
print(f"  Unique values found: {sorted(buggy_unique)}")
print(f"  Contains {m}? {buggy_has_m}")
print(f"  Maximum value: {buggy_max}")
if buggy_has_m:
    print(f"  ❌ BUG: Value {m} was generated but should be exclusive!")
else:
    print(f"  Note: {m} wasn't generated this run, but it CAN be generated")

print()

# Fixed version
fixed_values = random_list_fixed(n, m)
fixed_unique = set(fixed_values)
fixed_has_m = m in fixed_values
fixed_max = max(fixed_values)

print("FIXED VERSION (using randint(0, m-1)):")
print(f"  Unique values found: {sorted(fixed_unique)}")
print(f"  Contains {m}? {fixed_has_m}")
print(f"  Maximum value: {fixed_max}")
if not fixed_has_m:
    print(f"  ✅ CORRECT: Value {m} is never generated (exclusive)")

print()
print("=" * 70)

# Edge case: m=1
print("\nEdge Case: m=1")
print("With m=1 (exclusive), only value 0 should be generated")
print()

buggy_edge = random_list_buggy(100, 1)
fixed_edge = random_list_fixed(100, 1)

print(f"BUGGY VERSION unique values: {sorted(set(buggy_edge))}")
if 1 in buggy_edge:
    print("  ❌ BUG: Value 1 was generated but m=1 is exclusive!")

print(f"FIXED VERSION unique values: {sorted(set(fixed_edge))}")
if set(fixed_edge) == {0}:
    print("  ✅ CORRECT: Only 0 was generated")

print()
print("=" * 70)
print("\nConclusion:")
print("The bug is in using randint(0, m) which includes m.")
print("The fix is to use randint(0, m-1) which excludes m.")
