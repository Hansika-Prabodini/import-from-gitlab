# Tests Directory

This directory contains unit tests and performance benchmarks for the llm-benchmarking-py project. Tests are organized by module and use pytest with pytest-benchmark for performance measurements.

## Directory Structure

```
tests/
├── __init__.py
└── llm_benchmark/
    ├── __init__.py
    ├── algorithms/
    │   ├── __init__.py
    │   └── test_primes.py
    ├── control/
    │   ├── __init__.py
    │   ├── test_double.py
    │   └── test_single.py
    ├── datastructures/
    │   ├── __init__.py
    │   └── test_dslist.py
    ├── sql/
    │   ├── __init__.py
    │   └── test_query.py
    └── strings/
        └── __init__.py
```

## Test Framework

**Framework:** pytest  
**Benchmarking:** pytest-benchmark  
**Python Version:** 3.8+

## Running Tests

### Run All Tests (Skip Benchmarks)

Execute all unit tests without performance benchmarking:

```bash
poetry run pytest --benchmark-skip tests/
```

This runs tests quickly, verifying correctness without measuring performance.

### Run All Benchmarks (Skip Tests)

Execute only performance benchmarks:

```bash
poetry run pytest --benchmark-only tests/
```

This measures execution time and provides performance statistics.

### Run Both Tests and Benchmarks

Execute everything (tests + benchmarks):

```bash
poetry run pytest tests/
```

### Run Specific Module Tests

Test only a specific module:

```bash
# Test algorithms module
poetry run pytest tests/llm_benchmark/algorithms/

# Test control flow module
poetry run pytest tests/llm_benchmark/control/

# Test data structures module
poetry run pytest tests/llm_benchmark/datastructures/

# Test SQL module
poetry run pytest tests/llm_benchmark/sql/
```

### Run Specific Test File

```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py
```

### Run Specific Test Function

```bash
poetry run pytest tests/llm_benchmark/algorithms/test_primes.py::test_is_prime
```

### Verbose Output

Add `-v` or `-vv` for more detailed output:

```bash
poetry run pytest -v tests/
poetry run pytest -vv tests/
```

## Test Types

### Unit Tests

Verify correctness of implementations using parametrized test cases.

**Example from test_primes.py:**
```python
@pytest.mark.parametrize(
    "n, is_prime",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (17, True),
    ],
)
def test_is_prime(n: int, is_prime: bool) -> None:
    assert Primes.is_prime(n) == is_prime
```

### Benchmark Tests

Measure performance using pytest-benchmark.

**Example:**
```python
def test_benchmark_is_prime(benchmark) -> None:
    benchmark(Primes.is_prime, 17)
```

The `benchmark` fixture automatically:
- Runs the function multiple times
- Measures execution time
- Calculates statistics (min, max, mean, median, stddev)
- Provides comparison data

## Test Coverage by Module

### Algorithms (`algorithms/`)
- **test_primes.py**: Tests for prime number operations
  - `test_is_prime`: Validates prime detection
  - `test_sum_primes`: Validates prime summation
  - `test_prime_factors`: Validates prime factorization
  - Benchmarks for each function

### Control Flow (`control/`)
- **test_single.py**: Tests for single-loop operations
  - Range summation
  - List maximum finding
  - Modulus summation
- **test_double.py**: Tests for nested-loop operations
  - Sum of squares
  - Triangular sums
  - Pair counting
  - Duplicate detection
  - Matrix summation

### Data Structures (`datastructures/`)
- **test_dslist.py**: Tests for list operations
  - List modification
  - List searching
  - List sorting
  - List reversal
  - List rotation
  - List merging

### SQL (`sql/`)
- **test_query.py**: Tests for database queries
  - Album existence checking
  - Multi-table joins
  - Top invoice queries

### Strings (`strings/`)
- **test_strops.py**: Tests for string operations
  - String reversal
  - Palindrome detection
  - Edge cases with unicode and special characters

## Benchmark Output

When running benchmarks, you'll see output like:

```
----------------------------------------------------- benchmark: 3 tests -----------------------------------------------------
Name (time in us)                  Min       Max      Mean    StdDev    Median     IQR  Outliers     OPS  Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------
test_benchmark_is_prime          5.100     8.200    5.500    0.400     5.400    0.300     15;10  181.8k     100       100
test_benchmark_sum_primes      125.300   150.600  132.800    5.200   131.900    4.500      8;5    7.5k      50       100
test_benchmark_prime_factors    15.600    22.100   17.200    1.100    16.900    0.800     12;8   58.1k      75       100
---------------------------------------------------------------------------------------------------------------------------
```

**Key Metrics:**
- **Min/Max**: Fastest and slowest execution times
- **Mean**: Average execution time
- **Median**: Middle value (less affected by outliers)
- **StdDev**: Standard deviation (consistency)
- **OPS**: Operations per second
- **Rounds**: Number of test rounds
- **Iterations**: Iterations per round

## Writing New Tests

### Basic Test

```python
def test_new_function():
    result = YourClass.your_function(input_data)
    assert result == expected_output
```

### Parametrized Test

```python
@pytest.mark.parametrize(
    "input_val, expected",
    [
        (1, "one"),
        (2, "two"),
        (3, "three"),
    ],
)
def test_parametrized(input_val, expected):
    result = convert_number(input_val)
    assert result == expected
```

### Benchmark Test

```python
def test_benchmark_function(benchmark):
    # Pass function and arguments to benchmark
    result = benchmark(your_function, arg1, arg2)
    # Optional: assert on result
    assert result == expected_value
```

## Best Practices

1. **Organize by Module**: Keep tests in parallel directory structure with source code
2. **Use Parametrize**: Test multiple cases efficiently with `@pytest.mark.parametrize`
3. **Separate Concerns**: Keep unit tests and benchmarks separate (can run independently)
4. **Clear Names**: Use descriptive test function names (`test_is_prime_with_zero`)
5. **Edge Cases**: Test boundary conditions (empty lists, zero, negative numbers)
6. **Benchmark Realistic Data**: Use representative input sizes for benchmarking

## Continuous Integration

These tests can be integrated into CI/CD pipelines:

```yaml
# Example GitHub Actions workflow
- name: Run Tests
  run: poetry run pytest --benchmark-skip tests/

- name: Run Benchmarks
  run: poetry run pytest --benchmark-only tests/
```

## Performance Regression Testing

pytest-benchmark can save baseline results and compare against them:

```bash
# Save baseline
poetry run pytest --benchmark-only --benchmark-save=baseline tests/

# Compare against baseline
poetry run pytest --benchmark-only --benchmark-compare=baseline tests/
```

## Troubleshooting

### Import Errors

If you get import errors, ensure the package is installed:
```bash
poetry install
```

### Database Errors (SQL tests)

Ensure the Chinook database exists:
```bash
ls data/chinook.db
```

### Benchmark Not Running

Check that pytest-benchmark is installed:
```bash
poetry show pytest-benchmark
```

## Contributing Tests

When adding new features:
1. Create corresponding test file in parallel directory structure
2. Include both correctness tests (unit tests) and performance tests (benchmarks)
3. Use parametrized tests for comprehensive coverage
4. Document expected behavior in test docstrings
5. Run all tests before submitting: `poetry run pytest tests/`

## Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-benchmark Documentation](https://pytest-benchmark.readthedocs.io/)
- [Python unittest Documentation](https://docs.python.org/3/library/unittest.html)
