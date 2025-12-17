import pytest

from llm_benchmark.strings.strops import StrOps


# Test string reversal
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", ""),  # Empty string
        ("a", "a"),  # Single character
        ("ab", "ba"),  # Two characters
        ("hello", "olleh"),  # Simple word
        ("racecar", "racecar"),  # Palindrome
        ("Hello World!", "!dlroW olleH"),  # With spaces and punctuation
        ("12345", "54321"),  # Numbers
        ("a b c", "c b a"),  # Spaced characters
    ],
)
def test_str_reverse(input_str: str, expected: str) -> None:
    """Test string reversal with various inputs"""
    assert StrOps.str_reverse(input_str) == expected


def test_benchmark_str_reverse(benchmark) -> None:
    """Benchmark string reversal performance"""
    benchmark(StrOps.str_reverse, "The quick brown fox jumps over the lazy dog")


# Test palindrome detection
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("", True),  # Empty string is palindrome
        ("a", True),  # Single character
        ("aa", True),  # Two same characters
        ("ab", False),  # Two different characters
        ("racecar", True),  # Odd-length palindrome
        ("noon", True),  # Even-length palindrome
        ("hello", False),  # Not a palindrome
        ("A man a plan a canal Panama", False),  # Case-sensitive (not palindrome)
        ("amanaplanacanalpanama", True),  # Same but lowercase (palindrome)
        ("12321", True),  # Numeric palindrome
        ("12345", False),  # Not a palindrome
        ("abcba", True),  # Simple palindrome
        ("abccba", True),  # Even-length palindrome
        ("abcdba", False),  # Not a palindrome
    ],
)
def test_palindrome(input_str: str, expected: bool) -> None:
    """Test palindrome detection with various inputs"""
    assert StrOps.palindrome(input_str) == expected


def test_benchmark_palindrome(benchmark) -> None:
    """Benchmark palindrome checking performance"""
    benchmark(StrOps.palindrome, "amanaplanacanalpanama")


# Additional edge case tests
def test_str_reverse_special_characters():
    """Test string reversal with special characters"""
    assert StrOps.str_reverse("!@#$%^&*()") == ")(*&^%$#@!"


def test_str_reverse_unicode():
    """Test string reversal with unicode characters"""
    assert StrOps.str_reverse("café") == "éfac"
    assert StrOps.str_reverse("你好") == "好你"


def test_palindrome_special_characters():
    """Test palindrome detection with special characters"""
    assert StrOps.palindrome("!@@!") == True
    assert StrOps.palindrome("!@#!") == False


def test_palindrome_unicode():
    """Test palindrome detection with unicode characters"""
    assert StrOps.palindrome("你好你") == False
    assert StrOps.palindrome("你你") == True
