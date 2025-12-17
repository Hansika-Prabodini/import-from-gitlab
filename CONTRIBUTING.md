# Contributing to llm-benchmarking-py

Thank you for your interest in contributing to llm-benchmarking-py! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Code Style Guidelines](#code-style-guidelines)
- [Adding New Benchmarks](#adding-new-benchmarks)
- [Testing](#testing)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Code Review Guidelines](#code-review-guidelines)

## Getting Started

### Prerequisites

Before contributing, ensure you have:
- Python 3.8 or higher installed
- Poetry for dependency management
- Git for version control
- A GitHub account

### Development Setup

1. **Fork the repository** on GitHub

2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/llm-benchmarking-py.git
   cd llm-benchmarking-py
   ```

3. **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```

4. **Activate the virtual environment:**
   ```bash
   poetry shell
   ```

5. **Verify installation by running tests:**
   ```bash
   poetry run pytest --benchmark-skip tests/
   ```

6. **Create a new branch for your feature:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Project Structure

Understanding the project layout will help you contribute effectively:

```
llm-benchmarking-py/
├── src/
│   └── llm_benchmark/          # Main package
│       ├── __init__.py
│       ├── algorithms/         # Algorithm implementations
│       │   ├── primes.py       # Prime number operations
│       │   └── sort.py         # Sorting algorithms
│       ├── auth/              # Authentication utilities
│       │   └── simple_auth.py  # Password hashing, tokens, validation
│       ├── control/            # Control flow benchmarks
│       │   ├── single.py       # Single-loop operations
│       │   └── double.py       # Nested-loop operations
│       ├── datastructures/     # Data structure operations
│       │   └── dslist.py       # List operations
│       ├── generator/          # Test data generators
│       │   └── gen_list.py     # Random data generation
│       ├── sql/               # SQL query benchmarks
│       │   └── query.py        # Database operations
│       └── strings/           # String operations
│           └── strops.py       # String manipulation
├── tests/                     # Test suite (mirrors src structure)
│   ├── README.md             # Testing documentation
│   └── llm_benchmark/        # Test modules
├── data/                     # Database files
│   └── chinook.db           # SQLite database for SQL tests
├── main.py                   # Demo/example script
├── benchmark_primes.py       # Micro-benchmark utility
├── pyproject.toml           # Poetry configuration
├── README.md                # Project documentation
├── CONTRIBUTING.md          # This file
├── CHANGES.md              # Changelog
└── OPTIMIZATION.md         # Optimization documentation
```

### Module Responsibilities

- **algorithms/**: Computational algorithms (primes, sorting)
- **auth/**: Security and authentication functions
- **control/**: Control flow patterns (loops, conditionals)
- **datastructures/**: Data structure operations
- **generator/**: Utilities for generating test data
- **sql/**: Database query operations
- **strings/**: String manipulation functions

Each module is self-contained with static methods organized in classes.

## Code Style Guidelines

### General Principles

1. **Follow PEP 8**: Use Python's official style guide
2. **Type hints**: Use type annotations for all function signatures
3. **Docstrings**: All public functions must have docstrings
4. **Static methods**: Use `@staticmethod` decorator for utility functions
5. **Class-based organization**: Group related functions in classes

### Code Formatting

We use **Black** and **isort** for consistent code formatting:

```bash
# Format code with Black (line length: 88)
poetry run black src/ tests/

# Sort imports with isort
poetry run isort src/ tests/

# Format everything at once
poetry run black src/ tests/ && poetry run isort src/ tests/
```

**Always format your code before committing!**

### Docstring Format

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """Brief description of what the function does.

    Longer description if needed. Explain the algorithm,
    time complexity, and any important details.

    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2

    Returns:
        bool: Description of return value

    Raises:
        ValueError: When invalid input is provided
    
    Example:
        >>> function_name(42, "test")
        True
    """
    pass
```

### Type Hints

Always use type hints for better code clarity:

```python
from typing import List, Dict, Optional, Tuple

def process_data(items: List[int], threshold: int = 10) -> Dict[str, int]:
    """Process data with type hints."""
    pass
```

## Adding New Benchmarks

### Creating a New Module

If you're adding a completely new category of benchmarks:

1. **Create module directory:**
   ```bash
   mkdir -p src/llm_benchmark/your_module
   touch src/llm_benchmark/your_module/__init__.py
   ```

2. **Create implementation file:**
   ```python
   # src/llm_benchmark/your_module/your_file.py
   
   class YourClass:
       """Description of what this class benchmarks."""
       
       @staticmethod
       def your_function(param: int) -> int:
           """Brief description.
           
           Args:
               param (int): Description
               
           Returns:
               int: Description
           """
           # Implementation here
           pass
   ```

3. **Create corresponding test file:**
   ```bash
   mkdir -p tests/llm_benchmark/your_module
   touch tests/llm_benchmark/your_module/__init__.py
   ```

4. **Write tests:**
   ```python
   # tests/llm_benchmark/your_module/test_your_file.py
   import pytest
   from llm_benchmark.your_module.your_file import YourClass
   
   @pytest.mark.parametrize(
       "input_val, expected",
       [
           (1, 1),
           (5, 25),
           (10, 100),
       ],
   )
   def test_your_function(input_val: int, expected: int) -> None:
       assert YourClass.your_function(input_val) == expected
   
   def test_benchmark_your_function(benchmark) -> None:
       benchmark(YourClass.your_function, 100)
   ```

### Adding Functions to Existing Modules

1. **Add your function to the appropriate class**
2. **Include comprehensive docstring**
3. **Add unit tests** in the corresponding test file
4. **Add benchmark test** using pytest-benchmark
5. **Update documentation** if needed

### Best Practices for Benchmarks

- **Deterministic results**: Functions should produce consistent outputs for the same inputs
- **No side effects**: Avoid modifying global state or external resources
- **Reasonable performance**: Functions should complete in milliseconds for typical inputs
- **Educational value**: Benchmarks should test common patterns or algorithms
- **Scalable inputs**: Design functions that can scale to different input sizes

## Testing

### Running Tests

```bash
# Run all tests without benchmarks (fast)
poetry run pytest --benchmark-skip tests/

# Run only benchmarks (slow)
poetry run pytest --benchmark-only tests/

# Run everything
poetry run pytest tests/

# Run specific module tests
poetry run pytest tests/llm_benchmark/algorithms/

# Run with verbose output
poetry run pytest -v tests/

# Run with coverage
poetry run pytest --cov=llm_benchmark tests/
```

### Writing Tests

Every new function should have:

1. **Unit tests** - Verify correctness with multiple test cases
2. **Edge case tests** - Test boundary conditions (empty, zero, negative, large values)
3. **Benchmark tests** - Measure performance using pytest-benchmark

Example test structure:

```python
import pytest
from llm_benchmark.module.file import ClassName

# Unit tests with parametrization
@pytest.mark.parametrize(
    "input_val, expected",
    [
        (0, result_0),
        (1, result_1),
        (100, result_100),
        (-1, result_negative),  # Edge case
    ],
)
def test_function_name(input_val, expected):
    """Test function correctness."""
    assert ClassName.function_name(input_val) == expected

# Benchmark test
def test_benchmark_function_name(benchmark):
    """Benchmark function performance."""
    result = benchmark(ClassName.function_name, typical_input)
    assert result == expected_result  # Optional correctness check
```

### Test Coverage Goals

- Aim for **>90% code coverage**
- All public methods must be tested
- Edge cases must be covered
- Performance regressions should be caught by benchmarks

## Documentation

### Updating Documentation

When adding features, update:

1. **Function docstrings** - Inline documentation
2. **README.md** - If adding new modules or major features
3. **CHANGES.md** - Document your changes
4. **Module README** (if applicable) - tests/README.md for test changes

### Documentation Standards

- Use clear, concise language
- Include code examples where helpful
- Explain time/space complexity for algorithms
- Document any trade-offs or limitations

## Pull Request Process

### Before Submitting

1. **Ensure all tests pass:**
   ```bash
   poetry run pytest tests/
   ```

2. **Format your code:**
   ```bash
   poetry run black src/ tests/
   poetry run isort src/ tests/
   ```

3. **Verify no lint errors:**
   ```bash
   poetry run black --check src/ tests/
   ```

4. **Update documentation** as needed

5. **Add/update tests** for your changes

### Submitting a Pull Request

1. **Commit your changes** with clear, descriptive commit messages:
   ```bash
   git add .
   git commit -m "Add feature: brief description"
   ```

2. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what changed and why
   - Reference any related issues
   - Screenshots/benchmarks if applicable

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation update
- [ ] Test improvements

## Checklist
- [ ] Tests pass locally
- [ ] Code is formatted (Black + isort)
- [ ] Docstrings added/updated
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No breaking changes (or documented if necessary)

## Performance Impact
(If applicable) Describe performance improvements or regressions

## Additional Notes
Any other context about the changes
```

## Code Review Guidelines

### For Contributors

- Be open to feedback and suggestions
- Respond to review comments promptly
- Make requested changes or explain why they might not be appropriate
- Keep discussions professional and constructive

### For Reviewers

- Be respectful and constructive
- Explain the reasoning behind suggested changes
- Approve when code meets standards
- Test the changes locally if possible

## Common Issues and Solutions

### Poetry Issues

```bash
# Reset poetry environment
poetry env remove python
poetry install

# Update dependencies
poetry update

# Show virtual environment path
poetry env info
```

### Test Failures

```bash
# Run specific test with verbose output
poetry run pytest -vv tests/path/to/test_file.py::test_function

# Run with print statements visible
poetry run pytest -s tests/

# Debug with pdb
poetry run pytest --pdb tests/
```

### Import Errors

Ensure you're running commands through Poetry to use the correct environment:
```bash
# ✅ Correct
poetry run python main.py
poetry run pytest tests/

# ❌ Incorrect (might use wrong Python/packages)
python main.py
pytest tests/
```

## Getting Help

- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Documentation**: Check README.md and inline docstrings

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Welcome newcomers and help them learn
- Maintain a positive and collaborative environment

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to llm-benchmarking-py!** Your efforts help make this project better for everyone.
