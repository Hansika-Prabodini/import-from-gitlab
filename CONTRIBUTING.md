# Contributing to llm-benchmarking-py

Thank you for your interest in contributing to llm-benchmarking-py! This document provides guidelines and instructions for contributing to this project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Project Structure](#project-structure)
- [Adding New Benchmarks](#adding-new-benchmarks)
- [Reporting Issues](#reporting-issues)

## 📜 Code of Conduct

This project follows a standard code of conduct. By participating, you agree to:
- Be respectful and inclusive
- Accept constructive criticism
- Focus on what's best for the project
- Show empathy towards other contributors

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Poetry (package manager)
- Git
- A GitHub account

### First Time Setup

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/llm-benchmarking-py.git
   cd llm-benchmarking-py
   ```

3. **Add upstream remote:**
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/llm-benchmarking-py.git
   ```

4. **Install dependencies:**
   ```bash
   poetry install
   ```

5. **Verify installation:**
   ```bash
   poetry run pytest tests/
   poetry run main
   ```

## 🛠️ Development Setup

### Virtual Environment

Poetry automatically manages virtual environments:

```bash
# Activate the virtual environment
poetry shell

# Or run commands without activating
poetry run pytest tests/
```

### Development Tools

The project uses several development tools:

- **pytest**: Testing framework
- **pytest-benchmark**: Performance benchmarking
- **black**: Code formatting (line length: 88)
- **isort**: Import sorting

Install additional development tools:

```bash
# Already included in dev dependencies
poetry install

# Optional: Add pre-commit hooks
pip install pre-commit
pre-commit install
```

### IDE Setup

**VS Code recommended settings** (`.vscode/settings.json`):
```json
{
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "editor.formatOnSave": true,
  "python.sortImports.args": ["--profile", "black"]
}
```

**PyCharm settings:**
- Enable Black formatter: `Settings > Tools > Black`
- Set line length to 88
- Enable isort: `Settings > Tools > isort`

## 🤝 How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes** - Fix issues in existing code
2. **New Benchmarks** - Add new benchmark functions
3. **Performance Improvements** - Optimize existing implementations
4. **Documentation** - Improve docs, add examples
5. **Tests** - Add or improve test coverage
6. **Bug Reports** - Report issues you've found
7. **Feature Requests** - Suggest new features

### Contribution Workflow

1. **Find or create an issue** describing what you'll work on
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-123
   ```

3. **Make your changes** following our coding standards
4. **Write/update tests** for your changes
5. **Run the test suite:**
   ```bash
   poetry run pytest tests/
   ```

6. **Format your code:**
   ```bash
   poetry run black src/ tests/
   poetry run isort src/ tests/
   ```

7. **Commit your changes:**
   ```bash
   git add .
   git commit -m "feat: add new sorting benchmark"
   ```

8. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request** on GitHub

## 📝 Coding Standards

### Code Style

- **Formatter**: Black (line length: 88)
- **Import sorting**: isort with Black profile
- **Naming conventions**:
  - Classes: `PascalCase`
  - Functions/methods: `snake_case`
  - Constants: `UPPER_SNAKE_CASE`
  - Private methods: `_leading_underscore`

### Type Hints

All functions must include type hints:

```python
def sum_range(n: int) -> int:
    """Sum numbers from 0 to n.
    
    Args:
        n (int): Upper bound (exclusive)
    
    Returns:
        int: Sum of numbers
    """
    return sum(range(n))
```

### Docstrings

Use Google-style docstrings for all public functions:

```python
def function_name(param1: int, param2: str) -> bool:
    """Brief description of function.
    
    More detailed description if needed. Explain what the function
    does, not how it does it.
    
    Args:
        param1 (int): Description of param1
        param2 (str): Description of param2
    
    Returns:
        bool: Description of return value
    
    Raises:
        ValueError: When param1 is negative
    
    Examples:
        >>> function_name(5, "test")
        True
    """
    pass
```

### Static Methods

Use static methods for stateless operations:

```python
class MyBenchmark:
    @staticmethod
    def my_function(n: int) -> int:
        """Function docstring."""
        return n * 2
```

### Code Organization

- One class per file (generally)
- Related functions grouped in same class
- Keep functions focused and single-purpose
- Avoid global state

## ✅ Testing Requirements

### Test Coverage

All new code must include tests:

1. **Unit tests** for correctness
2. **Benchmark tests** for performance measurement
3. **Edge cases** (empty inputs, zero, negative numbers)

### Writing Tests

#### Unit Test Example

```python
import pytest
from llm_benchmark.module.file import MyClass

@pytest.mark.parametrize(
    "input_val, expected",
    [
        (0, 0),
        (1, 1),
        (5, 25),
        (-1, 1),
    ],
)
def test_my_function(input_val: int, expected: int) -> None:
    """Test my_function with various inputs."""
    result = MyClass.my_function(input_val)
    assert result == expected
```

#### Benchmark Test Example

```python
def test_benchmark_my_function(benchmark) -> None:
    """Benchmark my_function performance."""
    result = benchmark(MyClass.my_function, 1000)
    assert result > 0  # Optional: validate result
```

### Running Tests

```bash
# Run all tests
poetry run pytest tests/

# Run specific module
poetry run pytest tests/llm_benchmark/algorithms/

# Run with coverage
poetry run pytest --cov=src/llm_benchmark tests/

# Run only benchmarks
poetry run pytest --benchmark-only tests/

# Skip benchmarks
poetry run pytest --benchmark-skip tests/

# Verbose output
poetry run pytest -v tests/
```

### Test Requirements for PR

Before submitting a PR:
- ✅ All tests pass
- ✅ New code has ≥90% test coverage
- ✅ Benchmarks run without errors
- ✅ No regression in performance

## 🔄 Pull Request Process

### Before Submitting

1. **Update your branch:**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run the full test suite:**
   ```bash
   poetry run pytest tests/
   ```

3. **Format code:**
   ```bash
   poetry run black src/ tests/
   poetry run isort src/ tests/
   ```

4. **Check for issues:**
   ```bash
   # If using flake8
   poetry run flake8 src/ tests/
   ```

### PR Title Format

Use conventional commit format:

- `feat: add new benchmark for string algorithms`
- `fix: correct sum_primes edge case handling`
- `docs: update README with new examples`
- `test: add tests for sorting functions`
- `perf: optimize prime checking algorithm`
- `refactor: reorganize control flow module`
- `style: format code with black`
- `chore: update dependencies`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation update
- [ ] Test addition/improvement

## Checklist
- [ ] Tests pass locally
- [ ] Code formatted with black/isort
- [ ] New tests added for changes
- [ ] Documentation updated
- [ ] No breaking changes

## Related Issues
Closes #123

## Performance Impact
(If applicable) Describe performance changes

## Screenshots/Examples
(If applicable) Add examples of new functionality
```

### Review Process

1. **Automated checks** must pass (if CI is configured)
2. **At least one maintainer** must approve
3. **All comments** must be addressed
4. **Conflicts** must be resolved

### After Merge

1. Delete your feature branch
2. Update your local repository:
   ```bash
   git checkout main
   git pull upstream main
   ```

## 📂 Project Structure

Understanding the project structure helps you know where to add code:

```
src/llm_benchmark/
├── algorithms/       # Add algorithm-related benchmarks here
├── control/          # Add control flow benchmarks here
├── datastructures/   # Add data structure benchmarks here
├── generator/        # Add data generation utilities here
├── sql/             # Add SQL benchmarks here
└── strings/         # Add string manipulation benchmarks here

tests/llm_benchmark/  # Mirror structure of src/
```

### Module Guidelines

Each module should:
- Have a clear, focused purpose
- Contain a static class with related methods
- Include a `README.md` explaining the module
- Have comprehensive tests

## ➕ Adding New Benchmarks

### Step-by-Step Guide

1. **Choose the appropriate module** or create a new one
2. **Add the function** to the module's class:

   ```python
   # src/llm_benchmark/algorithms/math_ops.py
   class MathOps:
       @staticmethod
       def fibonacci(n: int) -> int:
           """Calculate nth Fibonacci number.
           
           Args:
               n (int): Position in sequence
           
           Returns:
               int: Fibonacci number at position n
           """
           if n <= 1:
               return n
           return MathOps.fibonacci(n - 1) + MathOps.fibonacci(n - 2)
   ```

3. **Add unit tests:**

   ```python
   # tests/llm_benchmark/algorithms/test_math_ops.py
   import pytest
   from llm_benchmark.algorithms.math_ops import MathOps
   
   @pytest.mark.parametrize(
       "n, expected",
       [
           (0, 0),
           (1, 1),
           (5, 5),
           (10, 55),
       ],
   )
   def test_fibonacci(n: int, expected: int) -> None:
       assert MathOps.fibonacci(n) == expected
   ```

4. **Add benchmark tests:**

   ```python
   def test_benchmark_fibonacci(benchmark) -> None:
       result = benchmark(MathOps.fibonacci, 10)
       assert result == 55
   ```

5. **Update documentation:**
   - Add to module's README.md
   - Add example to main README.md
   - Update ARCHITECTURE.md if needed

6. **Update main.py demo** (optional):

   ```python
   def demo_fibonacci():
       print("Fibonacci Demo")
       print("--------------")
       print(f"fibonacci(10): {MathOps.fibonacci(10)}")
   ```

### Benchmark Best Practices

- **Input sizes**: Test with realistic data sizes
- **Multiple cases**: Test best/average/worst cases
- **Comparison**: Include inefficient version for comparison
- **Documentation**: Explain complexity (O-notation)
- **No side effects**: Keep functions pure when possible

## 🐛 Reporting Issues

### Bug Reports

Include:
- **Description**: Clear description of the bug
- **Steps to reproduce**: Exact steps to trigger the bug
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Environment**: Python version, OS, Poetry version
- **Code samples**: Minimal code to reproduce

### Feature Requests

Include:
- **Use case**: Why is this feature needed?
- **Proposed solution**: How would it work?
- **Alternatives**: What alternatives have you considered?
- **Examples**: Code examples of usage

### Issue Template

```markdown
## Description
Clear description of issue/feature

## Type
- [ ] Bug report
- [ ] Feature request
- [ ] Documentation improvement
- [ ] Performance issue

## Environment (for bugs)
- Python version: 3.x.x
- Poetry version: 1.x.x
- OS: [e.g., Ubuntu 22.04]

## Steps to Reproduce (for bugs)
1. Step 1
2. Step 2
3. ...

## Expected Behavior


## Actual Behavior


## Additional Context
```

## 📞 Getting Help

- **Documentation**: Check README.md and ARCHITECTURE.md
- **Issues**: Search existing issues for similar problems
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Email maintainers (see README.md)

## 🎓 Learning Resources

New to contributing? Check out:
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [pytest Documentation](https://docs.pytest.org/)
- [Git Branching](https://learngitbranching.js.org/)

## 📊 Recognition

Contributors are recognized in:
- Git commit history
- Release notes (CHANGES.md)
- Project README.md

Thank you for contributing to llm-benchmarking-py! 🎉

---

**Questions?** Open an issue or reach out to the maintainers.

**Last Updated:** 2024
