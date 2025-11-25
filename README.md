# llm-benchmarking-py

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)

A comprehensive collection of Python functions designed to benchmark LLM (Large Language Model) projects and code generation capabilities. This library provides a diverse set of computational tasks across multiple domains to evaluate performance, correctness, and efficiency of AI-generated code.

## 📋 Table of Contents

- [Purpose](#purpose)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Testing & Benchmarking](#testing--benchmarking)
- [Project Structure](#project-structure)
- [Architecture](#architecture)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Purpose

`llm-benchmarking-py` serves as a standardized test suite for evaluating:

- **Code Generation Quality**: Assess how well LLMs generate functional Python code
- **Algorithm Correctness**: Verify implementations across various computational domains
- **Performance Optimization**: Benchmark execution efficiency and identify bottlenecks
- **Code Complexity**: Test LLM capabilities with varying complexity levels (simple loops to complex algorithms)

This library is ideal for:
- AI/ML researchers evaluating code generation models
- Developers benchmarking optimization improvements
- Educators teaching algorithmic concepts
- QA teams validating code transformation tools

## ✨ Overview

This benchmarking suite tests various aspects of code generation and execution including:
- **Algorithm implementation** (prime numbers, sorting, factorization)
- **Control flow structures** (single/nested loops, conditionals)
- **Data structure operations** (lists, arrays, manipulation)
- **String manipulation** (reversal, palindrome detection)
- **SQL query execution** (database operations, joins, aggregations)
- **Data generation utilities** (random test data creation)

## Features

### 🔢 Algorithms (`llm_benchmark.algorithms`)
- **Primes**: Prime number detection, prime summation, and prime factorization
- **Sort**: Sorting algorithms, Dutch flag partition, and finding max N elements

### 🔄 Control Flow (`llm_benchmark.control`)
- **SingleForLoop**: Single-loop operations for range sums, list maximums, and modulus operations
- **DoubleForLoop**: Nested loop operations for matrix sums, pair counting, and duplicate detection

### 📊 Data Structures (`llm_benchmark.datastructures`)
- **DsList**: List manipulation including modify, search, sort, reverse, rotate, and merge operations

### 🔤 String Operations (`llm_benchmark.strings`)
- **StrOps**: String reversal and palindrome detection

### 🗄️ SQL Queries (`llm_benchmark.sql`)
- **SqlQuery**: Database operations including album queries, table joins, and invoice analysis using SQLite (Chinook database)

### 🎲 Generators (`llm_benchmark.generator`)
- **GenList**: Random list and matrix generation for testing purposes

## 🚀 Installation

### Prerequisites

- **Python**: 3.8 or higher ([Download Python](https://www.python.org/downloads/))
- **Poetry**: Python package manager ([Install Poetry](https://python-poetry.org/docs/#installation))

### Quick Install Poetry

```bash
# Linux, macOS, Windows (WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Or using pip
pip install poetry
```

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd llm-benchmarking-py
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```
   
   This will:
   - Create a virtual environment automatically
   - Install all required dependencies
   - Install development dependencies (pytest, black, isort)
   - Set up the project in editable mode

3. **Activate the virtual environment (optional):**
   ```bash
   poetry shell
   ```

### Alternative: Using pip (not recommended)

```bash
pip install -e .
```

## 🏃 Quick Start

### Running the Demo

Execute all benchmark functions with example data:

```bash
poetry run main
```

Or if you activated the Poetry shell:
```bash
main
```

This will run demonstrations of all available modules and display their outputs, including:
- Single and double loop operations
- SQL queries on the Chinook database
- Prime number calculations
- Sorting algorithms
- List manipulations
- String operations

### Build Instructions

#### Build Package

To build a distributable package:

```bash
poetry build
```

This creates both wheel (`.whl`) and source distribution (`.tar.gz`) files in the `dist/` directory.

#### Install Built Package

```bash
pip install dist/llm_benchmark-0.1.0-py3-none-any.whl
```

#### Publish to PyPI (for maintainers)

```bash
# Configure PyPI credentials
poetry config pypi-token.pypi <your-token>

# Publish
poetry publish
```

## 📖 Usage

### Import and Use Individual Modules

```python
from llm_benchmark.algorithms.primes import Primes
from llm_benchmark.algorithms.sort import Sort
from llm_benchmark.control.single import SingleForLoop
from llm_benchmark.control.double import DoubleForLoop
from llm_benchmark.datastructures.dslist import DsList
from llm_benchmark.strings.strops import StrOps
from llm_benchmark.sql.query import SqlQuery
from llm_benchmark.generator.gen_list import GenList

# ===== ALGORITHMS =====

# Check if a number is prime (optimized O(√n))
is_prime = Primes.is_prime(17)  # Returns: True

# Sum all primes up to n (Sieve of Eratosthenes)
prime_sum = Primes.sum_primes(100)  # Returns: 1060

# Get prime factors
factors = Primes.prime_factors(84)  # Returns: [2, 2, 3, 7]

# Sort a list (in-place bubble sort)
numbers = [5, 2, 8, 1, 9]
Sort.sort_list(numbers)  # numbers is now [1, 2, 5, 8, 9]

# Dutch flag partition
values = [3, 1, 4, 1, 5, 9, 2, 6]
Sort.dutch_flag_partition(values, 5)  # Partitions around pivot value 5

# Find N largest elements
max_elements = Sort.max_n([3, 1, 4, 1, 5, 9], 3)  # Returns: [9, 5, 4]

# ===== CONTROL FLOW =====

# Sum numbers from 0 to n
total = SingleForLoop.sum_range(10)  # Returns: 45

# Find maximum in list
max_val = SingleForLoop.max_list([1, 5, 3, 9, 2])  # Returns: 9

# Sum numbers divisible by m
modulo_sum = SingleForLoop.sum_modulus(100, 5)  # Returns: 950

# Sum of squares using nested loops
square_sum = DoubleForLoop.sum_square(5)  # Returns: 225

# Count unique pairs
pair_count = DoubleForLoop.count_pairs([1, 2, 2, 3, 3, 3])  # Returns: 3

# Sum 2D matrix elements
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_sum = DoubleForLoop.sum_matrix(matrix)  # Returns: 45

# ===== DATA STRUCTURES =====

# Modify list (add 1 to each element)
modified = DsList.modify_list([1, 2, 3, 4, 5])  # Returns: [2, 3, 4, 5, 6]

# Search for all indices of a value
indices = DsList.search_list([1, 2, 3, 2, 4], 2)  # Returns: [1, 3]

# Reverse a list
reversed_list = DsList.reverse_list([1, 2, 3, 4, 5])  # Returns: [5, 4, 3, 2, 1]

# Rotate list by n positions
rotated = DsList.rotate_list([1, 2, 3, 4, 5], 2)  # Returns: [4, 5, 1, 2, 3]

# Merge two lists
merged = DsList.merge_lists([1, 2, 3], [4, 5, 6])  # Returns: [1, 2, 3, 4, 5, 6]

# ===== STRING OPERATIONS =====

# Reverse a string
reversed_str = StrOps.str_reverse("hello")  # Returns: "olleh"

# Check if palindrome
is_palindrome = StrOps.palindrome("racecar")  # Returns: True
is_palindrome2 = StrOps.palindrome("hello")  # Returns: False

# ===== SQL QUERIES =====

# Check if album exists in database
exists = SqlQuery.query_album("Presence")  # Returns: True

# Join Album, Artist, and Track tables
joined_data = SqlQuery.join_albums()  # Returns list of tuples

# Get top 10 invoices
top_invoices = SqlQuery.top_invoices()  # Returns top 10 invoice records

# ===== DATA GENERATORS =====

# Generate random list
random_nums = GenList.random_list(10, 100)  # 10 random numbers 0-99

# Generate random matrix
random_matrix = GenList.random_matrix(5, 5, 100)  # 5x5 matrix with values 0-99
```

### Using as a Library in Your Project

Add to your `pyproject.toml`:
```toml
[tool.poetry.dependencies]
llm_benchmark = {path = "../llm-benchmarking-py", develop = true}
```

Or install from a git repository:
```bash
poetry add git+https://github.com/your-org/llm-benchmarking-py.git
```

## 🧪 Testing & Benchmarking

### Run Unit Tests

Execute all unit tests without benchmarking:

```bash
poetry run pytest --benchmark-skip tests/
```

**Expected output:**
```
======================== test session starts ========================
collected 42 items

tests/llm_benchmark/algorithms/test_primes.py ........     [ 19%]
tests/llm_benchmark/control/test_single.py .......        [ 35%]
tests/llm_benchmark/control/test_double.py ........       [ 54%]
tests/llm_benchmark/datastructures/test_dslist.py ...     [ 61%]
tests/llm_benchmark/sql/test_query.py ....                [100%]

======================== 42 passed in 0.45s =========================
```

### Run Performance Benchmarks

Execute performance benchmarks for all functions:

```bash
poetry run pytest --benchmark-only tests/
```

This will measure and compare the execution time of different implementations and provide detailed performance metrics.

**Sample benchmark output:**
```
--------------------------------------------- benchmark: 15 tests --------------------------------------------
Name (time in us)                     Min       Max      Mean    StdDev    Median     IQR  Outliers  OPS
-----------------------------------------------------------------------------------------------------------
test_benchmark_is_prime             2.100     5.400    2.300    0.200     2.200    0.100    15;10  434.8K
test_benchmark_sum_primes         110.200   145.600  118.400    6.100   117.300    5.200     8;5    8.4K
test_benchmark_sort_list            8.500    12.300    9.200    0.600     9.100    0.400    12;8  108.7K
-----------------------------------------------------------------------------------------------------------
```

### Run Custom Micro-Benchmark

For detailed optimization comparisons:

```bash
poetry run python benchmark_primes.py
```

This custom benchmark compares optimized vs. original implementations showing:
- Detailed timing for multiple input sizes
- Speedup calculations
- Complexity analysis
- Correctness verification

### Test Coverage

Generate a test coverage report:

```bash
poetry run pytest --cov=src/llm_benchmark --cov-report=html tests/
```

View the report by opening `htmlcov/index.html` in your browser.

### Continuous Testing

Watch mode for development:

```bash
poetry run pytest-watch tests/
```

Or use pytest's built-in watch (with pytest-xdist):

```bash
poetry add --dev pytest-xdist
poetry run pytest tests/ --looponfail
```

## Module Documentation

### Algorithms
- `Primes.is_prime(n)` - Check if a number is prime
- `Primes.is_prime_ineff(n)` - Inefficient prime check (for benchmarking)
- `Primes.sum_primes(n)` - Sum all primes from 0 to n
- `Primes.prime_factors(n)` - Get prime factorization
- `Sort.sort_list(v)` - Sort a list in-place
- `Sort.dutch_flag_partition(v, pivot)` - Partition list around pivot
- `Sort.max_n(v, n)` - Find the N largest elements

### Control Flow
- `SingleForLoop.sum_range(n)` - Sum numbers from 0 to n
- `SingleForLoop.max_list(v)` - Find maximum in list
- `SingleForLoop.sum_modulus(n, m)` - Sum numbers divisible by m
- `DoubleForLoop.sum_square(n)` - Sum of squares using nested loops
- `DoubleForLoop.sum_triangle(n)` - Triangular number sum
- `DoubleForLoop.count_pairs(v)` - Count unique pairs in list
- `DoubleForLoop.count_duplicates(v1, v2)` - Count duplicates between lists
- `DoubleForLoop.sum_matrix(m)` - Sum all matrix elements

### Data Structures
- `DsList.modify_list(v)` - Add 1 to each element
- `DsList.search_list(v, n)` - Find all indices of value
- `DsList.sort_list(v)` - Sort and return copy
- `DsList.reverse_list(v)` - Reverse and return copy
- `DsList.rotate_list(v, n)` - Rotate list by n positions
- `DsList.merge_lists(v1, v2)` - Merge two lists

### String Operations
- `StrOps.str_reverse(s)` - Reverse a string
- `StrOps.palindrome(s)` - Check if string is palindrome

### SQL Queries
- `SqlQuery.query_album(name)` - Check if album exists
- `SqlQuery.join_albums()` - Join Album, Artist, and Track tables
- `SqlQuery.top_invoices()` - Get top 10 invoices by total

## 📁 Project Structure

```
llm-benchmarking-py/
├── src/
│   └── llm_benchmark/           # Main package
│       ├── __init__.py
│       ├── algorithms/          # Algorithm implementations
│       │   ├── primes.py        # Prime number operations (O(√n) optimized)
│       │   └── sort.py          # Sorting algorithms
│       ├── control/             # Control flow operations
│       │   ├── single.py        # Single-loop operations
│       │   └── double.py        # Nested-loop operations
│       ├── datastructures/      # Data structure operations
│       │   └── dslist.py        # List manipulation functions
│       ├── generator/           # Test data generators
│       │   └── gen_list.py      # Random data generation
│       ├── sql/                 # SQL query operations
│       │   └── query.py         # Database queries (Chinook DB)
│       └── strings/             # String manipulation
│           └── strops.py        # String operations
├── tests/                       # Unit tests and benchmarks (mirrors src/)
│   ├── __init__.py
│   ├── README.md               # Test documentation
│   └── llm_benchmark/
│       ├── algorithms/
│       │   └── test_primes.py
│       ├── control/
│       │   ├── test_single.py
│       │   └── test_double.py
│       ├── datastructures/
│       │   └── test_dslist.py
│       ├── sql/
│       │   └── test_query.py
│       └── strings/
│           └── test_strops.py
├── data/
│   └── chinook.db              # SQLite database for SQL tests
├── main.py                     # Demo script (entry point)
├── benchmark_primes.py         # Custom micro-benchmark script
├── pyproject.toml              # Poetry configuration
├── poetry.lock                 # Locked dependencies
├── README.md                   # This file
├── ARCHITECTURE.md             # System architecture documentation
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGES.md                  # Change history
└── OPTIMIZATION.md             # Performance optimization report
```

### Module Organization

Each module follows a consistent pattern:
- **Static classes** with class methods for easy importing and usage
- **Type hints** for all function signatures
- **Docstrings** with Args and Returns documentation
- **Focused functionality** - each module handles one domain

## 🏗️ Architecture

The project follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────┐
│                      main.py (Entry Point)              │
└────────────────────────┬────────────────────────────────┘
                         │
            ┌────────────┴────────────┐
            │   llm_benchmark Package  │
            └────────────┬────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
   │Algorithm│     │ Control │     │   Data  │
   │ Module  │     │  Module │     │Structure│
   └─────────┘     └─────────┘     └─────────┘
        │                │                │
   ┌────▼────┐     ┌────▼────┐     ┌────▼────┐
   │ Strings │     │   SQL   │     │Generator│
   │ Module  │     │  Module │     │ Module  │
   └─────────┘     └─────────┘     └─────────┘
```

For detailed architecture diagrams and design decisions, see [ARCHITECTURE.md](ARCHITECTURE.md).

### Design Principles

- **Stateless Design**: All functions are static methods, no instance state
- **Pure Functions**: Most functions have no side effects (except SQL operations)
- **Minimal Dependencies**: Core library only requires Python 3.8+
- **Testability**: Every function has corresponding unit tests and benchmarks
- **Performance Focus**: Optimized implementations (e.g., O(√n) prime checking)

## 🛠️ Development

### Setting Up Development Environment

1. **Clone and install with dev dependencies:**
   ```bash
   git clone <repository-url>
   cd llm-benchmarking-py
   poetry install
   ```

2. **Activate virtual environment:**
   ```bash
   poetry shell
   ```

3. **Install pre-commit hooks (optional):**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

### Code Formatting

Format code with Black and isort:

```bash
# Format all source code
poetry run black src/ tests/

# Sort imports
poetry run isort src/ tests/

# Or do both at once
poetry run black src/ tests/ && poetry run isort src/ tests/
```

### Running Quality Checks

```bash
# Run all tests
poetry run pytest tests/

# Run with coverage
poetry run pytest --cov=src/llm_benchmark tests/

# Run type checking (if mypy is added)
poetry run mypy src/

# Run linting (if flake8 is added)
poetry run flake8 src/ tests/
```

### Adding New Benchmarks

See our [Contributing Guide](CONTRIBUTING.md) for detailed instructions on:
- Adding new benchmark functions
- Writing tests and benchmarks
- Code style guidelines
- Pull request process

## 📊 Performance Notes

Key optimizations implemented:
- **`Primes.is_prime`**: O(n) → O(√n) using sqrt optimization
- **`Primes.sum_primes`**: O(n²) → O(n log log n) using Sieve of Eratosthenes
- See [OPTIMIZATION.md](OPTIMIZATION.md) for detailed performance analysis

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to report bugs and request features
- Development setup instructions
- Code style and testing requirements
- Pull request submission process

**Quick Contribution Checklist:**
- ✅ All tests pass: `poetry run pytest tests/`
- ✅ Code is formatted: `poetry run black src/ tests/`
- ✅ Imports are sorted: `poetry run isort src/ tests/`
- ✅ New functions have tests and docstrings
- ✅ Documentation is updated

## 📄 License

See project repository for license information.

## 👥 Authors & Acknowledgments

**Main Author:** Matthew Truscott (matthew.truscott@turintech.ai)

**Contributors:** See [CONTRIBUTING.md](CONTRIBUTING.md) for how to become a contributor.

## 📚 Additional Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture and design diagrams
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [OPTIMIZATION.md](OPTIMIZATION.md) - Performance optimization report
- [CHANGES.md](CHANGES.md) - Change history and release notes
- [tests/README.md](tests/README.md) - Testing documentation

## 🔗 Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [pytest-benchmark](https://pytest-benchmark.readthedocs.io/)
- [Black Code Formatter](https://black.readthedocs.io/)
- [isort](https://pycqa.github.io/isort/)

---

**Last Updated:** 2024  
**Version:** 0.1.0  
**Status:** Active Development
