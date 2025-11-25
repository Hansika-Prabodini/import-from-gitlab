# Strings Module

This module provides string manipulation operations for benchmarking LLM code generation capabilities with character-level string processing. It focuses on fundamental string operations commonly encountered in programming challenges.

## Components

### StrOps (`strops.py`)

String operations including reversal and palindrome detection.

#### Methods

##### `str_reverse(s: str) -> str`
Reverses a string character by character.

**Parameters:**
- `s` (str): The string to reverse

**Returns:**
- `str`: The reversed string

**Example:**
```python
from llm_benchmark.strings.strops import StrOps

result = StrOps.str_reverse("hello")
print(result)  # Output: "olleh"

result = StrOps.str_reverse("python")
print(result)  # Output: "nohtyp"

result = StrOps.str_reverse("a")
print(result)  # Output: "a"
```

**Algorithm:** Iterates through string backwards, building new string character by character.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

##### `palindrome(s: str) -> bool`
Checks if a string is a palindrome (reads the same forwards and backwards).

**Parameters:**
- `s` (str): The string to check

**Returns:**
- `bool`: True if the string is a palindrome, False otherwise

**Example:**
```python
from llm_benchmark.strings.strops import StrOps

result = StrOps.palindrome("racecar")
print(result)  # Output: True

result = StrOps.palindrome("hello")
print(result)  # Output: False

result = StrOps.palindrome("madam")
print(result)  # Output: True

result = StrOps.palindrome("a")
print(result)  # Output: True
```

**Algorithm:** Compares characters from both ends moving towards the center.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

**Note:** Case-sensitive comparison; "Racecar" would return False.

---

## Usage in Benchmarking

These string operations test:
- **Character Iteration**: Ability to iterate through strings
- **String Building**: Constructing new strings character by character
- **Index Manipulation**: Accessing characters at specific positions
- **Comparison Logic**: Implementing character-level comparisons
- **Algorithmic Thinking**: Efficient palindrome checking

## Performance Characteristics

| Method | Time Complexity | Space Complexity | Description |
|--------|----------------|------------------|-------------|
| `str_reverse` | O(n) | O(n) | Must create new string |
| `palindrome` | O(n) | O(1) | Only needs comparison |

## Common Patterns Tested

1. **String Reversal**: Classic operation in many languages
2. **Palindrome Detection**: Common interview question
3. **Index Arithmetic**: Working with string indices
4. **Character Access**: Using bracket notation for characters
5. **String Concatenation**: Building strings iteratively

## Edge Cases Handled

- Empty strings: `str_reverse("")` returns `""`
- Single character: `palindrome("a")` returns `True`
- Even-length palindromes: `"noon"` returns `True`
- Odd-length palindromes: `"radar"` returns `True`

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/strings/
```

Run benchmarks:

```bash
poetry run pytest --benchmark-only tests/llm_benchmark/strings/
```

## Complete Demo

```python
from llm_benchmark.strings.strops import StrOps

# Test string reversal
test_strings = ["hello", "python", "racecar", ""]

print("=== String Reversal ===")
for s in test_strings:
    reversed_s = StrOps.str_reverse(s)
    print(f"'{s}' -> '{reversed_s}'")

print("\n=== Palindrome Detection ===")
palindrome_tests = ["racecar", "hello", "madam", "noon", "python", "a", ""]

for s in palindrome_tests:
    is_palindrome = StrOps.palindrome(s)
    print(f"'{s}': {is_palindrome}")
```

**Output:**
```
=== String Reversal ===
'hello' -> 'olleh'
'python' -> 'nohtyp'
'racecar' -> 'racecar'
'' -> ''

=== Palindrome Detection ===
'racecar': True
'hello': False
'madam': True
'noon': True
'python': False
'a': True
'': True
```

## Design Notes

- **Explicit Iteration**: Uses manual loops instead of Python's string slicing (e.g., `s[::-1]`) to demonstrate algorithmic approach
- **Character-by-Character**: Builds strings one character at a time to show fundamental operations
- **Educational Focus**: Implementations prioritize clarity and demonstrating concepts over raw performance
- **No Built-ins**: Avoids high-level string methods to test LLM's ability to work with basic operations

## Potential Extensions

Future additions to this module could include:
- Case-insensitive palindrome checking
- String pattern matching
- Substring search
- Character frequency counting
- Anagram detection
- String compression/decompression

## Real-World Applications

These fundamental operations are building blocks for:
- Text processing pipelines
- Data validation (e.g., checking symmetric patterns)
- Password strength validation
- DNA sequence analysis
- Lexical analysis in compilers
