#!/usr/bin/env python3
"""Verification script for strings module input validation."""

from src.llm_benchmark.strings.strops import StrOps

def test_str_reverse():
    """Test str_reverse with various inputs."""
    print("Testing str_reverse...")
    
    # Valid string inputs
    assert StrOps.str_reverse("hello") == "olleh", "Failed: normal string"
    assert StrOps.str_reverse("python") == "nohtyp", "Failed: another string"
    assert StrOps.str_reverse("a") == "a", "Failed: single character"
    
    # Empty string (should work)
    assert StrOps.str_reverse("") == "", "Failed: empty string"
    
    # Type errors (should raise TypeError)
    try:
        StrOps.str_reverse(123)
        assert False, "Should have raised TypeError for int"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for int: {e}")
    
    try:
        StrOps.str_reverse(None)
        assert False, "Should have raised TypeError for None"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for None: {e}")
    
    try:
        StrOps.str_reverse([1, 2, 3])
        assert False, "Should have raised TypeError for list"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for list: {e}")
    
    print("  ✓ All str_reverse tests passed!\n")

def test_palindrome():
    """Test palindrome with various inputs."""
    print("Testing palindrome...")
    
    # Valid string inputs
    assert StrOps.palindrome("racecar") == True, "Failed: palindrome 'racecar'"
    assert StrOps.palindrome("hello") == False, "Failed: non-palindrome 'hello'"
    assert StrOps.palindrome("madam") == True, "Failed: palindrome 'madam'"
    assert StrOps.palindrome("a") == True, "Failed: single character"
    
    # Empty string (should return True)
    assert StrOps.palindrome("") == True, "Failed: empty string"
    
    # Type errors (should raise TypeError)
    try:
        StrOps.palindrome(123)
        assert False, "Should have raised TypeError for int"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for int: {e}")
    
    try:
        StrOps.palindrome(None)
        assert False, "Should have raised TypeError for None"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for None: {e}")
    
    try:
        StrOps.palindrome(['a', 'b', 'a'])
        assert False, "Should have raised TypeError for list"
    except TypeError as e:
        assert "must be a string" in str(e), f"Wrong error message: {e}"
        print(f"  ✓ TypeError for list: {e}")
    
    print("  ✓ All palindrome tests passed!\n")

if __name__ == "__main__":
    print("="*60)
    print("String Module Input Validation Verification")
    print("="*60 + "\n")
    
    test_str_reverse()
    test_palindrome()
    
    print("="*60)
    print("✓ All validation tests passed successfully!")
    print("="*60)
