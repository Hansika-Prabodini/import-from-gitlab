#!/usr/bin/env python3
"""
Verification script to demonstrate the bug fix in random_list function.

BUG: The original implementation used randint(0, m) which is inclusive of m,
     but the documentation states m should be exclusive.

FIX: Changed to randint(0, m - 1) to make m exclusive.
"""

from llm_benchmark.generator.gen_list import GenList

print("Testing the random_list bug fix...")
print("=" * 60)

# Test 1: Generate many values and check none equal m
print("\nTest 1: Verify m is never generated (m=5)")
m = 5
all_values = []
for _ in range(1000):
    values = GenList.random_list(100, m)
    all_values.extend(values)

max_value = max(all_values)
min_value = min(all_values)
has_m = m in all_values

print(f"Generated {len(all_values)} random values with m={m}")
print(f"Min value: {min_value}, Max value: {max_value}")
print(f"Does list contain m={m}? {has_m}")

if has_m:
    print("❌ FAIL: m was generated (bug present)")
else:
    print("✅ PASS: m was never generated (bug fixed)")

# Test 2: Edge case with m=1
print("\nTest 2: Edge case with m=1 (should only generate 0)")
values = GenList.random_list(100, 1)
unique_values = set(values)

print(f"Generated {len(values)} values with m=1")
print(f"Unique values: {unique_values}")

if unique_values == {0}:
    print("✅ PASS: Only 0 was generated (bug fixed)")
else:
    print(f"❌ FAIL: Values other than 0 were generated (bug present)")

# Test 3: Verify range [0, m)
print("\nTest 3: Verify all values are in range [0, m)")
m = 10
values = GenList.random_list(1000, m)
all_in_range = all(0 <= v < m for v in values)

print(f"Generated {len(values)} values with m={m}")
print(f"All values in range [0, {m})? {all_in_range}")

if all_in_range:
    print("✅ PASS: All values are in the correct range (bug fixed)")
else:
    print("❌ FAIL: Some values are out of range (bug present)")

print("\n" + "=" * 60)
print("Verification complete!")
