# Metrics & KPIs Quick Reference

## 🚀 Quick Start

### View All Metrics
```bash
poetry run python metrics_summary.py
```

### Run Tests Only
```bash
poetry run pytest --benchmark-skip tests/
```

### Run Benchmarks Only
```bash
poetry run pytest --benchmark-only tests/
```

### Run with Coverage
```bash
poetry run pytest --cov=src --cov-report=term-missing --benchmark-skip tests/
```

---

## 📊 Key Metrics Tracked

### 1. Performance Metrics ⚡
- **What**: Execution time, operations per second, complexity
- **Why**: Evaluate efficiency of code generation
- **Where**: `pytest --benchmark-only`
- **Target**: Consistent performance, optimal complexity

### 2. Correctness Metrics ✅
- **What**: Test pass/fail rates, edge case handling
- **Why**: Ensure generated code works correctly
- **Where**: `pytest --benchmark-skip`
- **Target**: 100% test pass rate

### 3. Coverage Metrics 🎯
- **What**: Line and branch coverage of source code
- **Why**: Identify untested code paths
- **Where**: `pytest --cov`
- **Target**: 90%+ coverage

### 4. Security Metrics 🔐
- **What**: SQL injection tests, password validation
- **Why**: Ensure secure code generation
- **Where**: SQL and Auth module tests
- **Target**: All security tests passing

---

## 📈 Metrics by Module

| Module | Functions | Tests | Benchmarks | Coverage |
|--------|-----------|-------|------------|----------|
| **Algorithms** | 6 | ✅ | ✅ | High |
| **Control** | 8 | ✅ | ✅ | High |
| **Data Structures** | 6 | ✅ | ✅ | High |
| **SQL** | 3 | ✅ | ✅ | High |
| **Auth** | 7 | ✅ | ✅ | High |
| **Strings** | 2 | ✅ | ✅ | High |
| **Generators** | 2 | - | - | - |

---

## 🎯 Business KPIs

### Primary KPIs
1. **Code Generation Quality** → Test pass rate
2. **Performance Efficiency** → Benchmark results
3. **Test Coverage** → Coverage percentage
4. **Security Compliance** → Security test pass rate

### Secondary KPIs
1. **Module Coverage** → Modules with tests / Total modules
2. **Optimization Impact** → Speedup metrics (Original vs Optimized)
3. **Edge Case Handling** → Parametrized test coverage
4. **Documentation Quality** → README completeness

---

## 🔍 Common Commands

### Test Specific Module
```bash
# Algorithms
poetry run pytest tests/llm_benchmark/algorithms/

# Control Flow
poetry run pytest tests/llm_benchmark/control/

# Data Structures
poetry run pytest tests/llm_benchmark/datastructures/

# SQL
poetry run pytest tests/llm_benchmark/sql/

# Authentication
poetry run pytest tests/llm_benchmark/auth/

# Strings
poetry run pytest tests/llm_benchmark/strings/
```

### Benchmark Specific Module
```bash
poetry run pytest --benchmark-only tests/llm_benchmark/algorithms/
```

### Coverage for Specific Module
```bash
poetry run pytest --cov=src/llm_benchmark/algorithms --cov-report=term-missing tests/llm_benchmark/algorithms/
```

### Generate HTML Coverage Report
```bash
poetry run pytest --cov=src --cov-report=html --benchmark-skip tests/
open htmlcov/index.html  # View in browser
```

---

## 📋 Interpreting Results

### Test Results
```
===== test session starts =====
collected 150 items

tests/... PASSED [100%]
===== 150 passed in 2.50s =====
```
- **150 passed**: All tests successful ✅
- **X failed**: Some tests failed ❌ (needs fixing)

### Benchmark Results
```
Name                          Min      Max      Mean    Median     OPS
test_benchmark_is_prime     5.1us    8.2us    5.5us    5.4us   181.8k
```
- **Min/Max**: Fastest/slowest execution
- **Mean**: Average execution time
- **Median**: Middle value (less affected by outliers)
- **OPS**: Operations per second (higher is better)

### Coverage Results
```
src/llm_benchmark/algorithms/primes.py    85%   Missing: 45-50, 78
TOTAL                                      92%
```
- **85%**: 85% of lines covered by tests
- **Missing**: Line numbers not covered
- **Target**: Aim for 90%+ coverage

### Health Score
```
Overall Health Score: 95/100 (95.0%)
Status: 🌟 EXCELLENT - Project is in great shape!
```
- **90-100%**: Excellent ✅
- **75-89%**: Good ⚠️
- **60-74%**: Fair ⚠️
- **<60%**: Poor ❌

---

## ⚠️ Warning Signs

### Red Flags
- ❌ Tests failing
- ❌ Coverage below 80%
- ❌ Security tests failing
- ❌ Modules without tests
- ❌ Benchmarks showing performance regression

### Action Required
1. **Failing tests** → Debug and fix immediately
2. **Low coverage** → Add missing test cases
3. **Security failures** → Review and patch vulnerabilities
4. **Untested modules** → Create test files
5. **Performance regression** → Profile and optimize

---

## 📚 Additional Resources

- **Detailed Analysis**: [METRICS_ANALYSIS.md](METRICS_ANALYSIS.md)
- **Test Documentation**: [tests/README.md](tests/README.md)
- **Optimization Report**: [OPTIMIZATION.md](OPTIMIZATION.md)
- **Change Log**: [CHANGES.md](CHANGES.md)

---

## 🎓 Best Practices

### Writing Tests
1. **Parametrize**: Use `@pytest.mark.parametrize` for multiple cases
2. **Edge Cases**: Test boundary conditions (empty, zero, negative)
3. **Benchmarks**: Add benchmark tests for performance tracking
4. **Clear Names**: Use descriptive test function names

### Running Metrics
1. **Before Commit**: Run tests and coverage
2. **Before PR**: Run full metrics summary
3. **Weekly**: Review benchmark trends
4. **Monthly**: Analyze coverage gaps

### Maintaining Quality
1. **Keep tests updated** with code changes
2. **Add tests for bug fixes**
3. **Benchmark new optimizations**
4. **Document metric changes**

---

**Last Updated**: 2024  
**Maintained By**: Project Team  
**Questions?**: See METRICS_ANALYSIS.md for detailed information
