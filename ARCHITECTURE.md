# Architecture Documentation

## Overview

`llm-benchmarking-py` is a modular Python library designed to benchmark LLM code generation capabilities across multiple computational domains. This document provides comprehensive architectural views of the system using Mermaid diagrams.

## Table of Contents

- [High-Level Architecture](#high-level-architecture)
- [Module Structure](#module-structure)
- [Component Diagram](#component-diagram)
- [Data Flow](#data-flow)
- [Class Relationships](#class-relationships)
- [Test Architecture](#test-architecture)
- [Deployment View](#deployment-view)
- [Design Patterns](#design-patterns)
- [Performance Considerations](#performance-considerations)

## High-Level Architecture

```mermaid
graph TB
    subgraph "User Layer"
        CLI[Command Line Interface]
        API[Python API]
        Demo[Demo Script main.py]
    end
    
    subgraph "Core Package: llm_benchmark"
        ALG[Algorithms Module]
        CTL[Control Module]
        DS[Data Structures Module]
        STR[Strings Module]
        SQL[SQL Module]
        GEN[Generator Module]
    end
    
    subgraph "Test Layer"
        UNIT[Unit Tests]
        BENCH[Benchmark Tests]
        MICRO[Micro-Benchmarks]
    end
    
    subgraph "External Resources"
        DB[(Chinook Database)]
        DATA[Test Data]
    end
    
    CLI --> ALG
    CLI --> CTL
    CLI --> DS
    API --> ALG
    API --> CTL
    API --> DS
    Demo --> ALG
    Demo --> CTL
    Demo --> DS
    Demo --> STR
    Demo --> SQL
    Demo --> GEN
    
    SQL --> DB
    GEN --> DATA
    
    UNIT --> ALG
    UNIT --> CTL
    UNIT --> DS
    UNIT --> STR
    UNIT --> SQL
    BENCH --> ALG
    BENCH --> CTL
    BENCH --> DS
    MICRO --> ALG
    
    style CLI fill:#e1f5ff
    style API fill:#e1f5ff
    style Demo fill:#e1f5ff
    style ALG fill:#fff4e6
    style CTL fill:#fff4e6
    style DS fill:#fff4e6
    style STR fill:#fff4e6
    style SQL fill:#fff4e6
    style GEN fill:#fff4e6
    style UNIT fill:#f3e5f5
    style BENCH fill:#f3e5f5
    style MICRO fill:#f3e5f5
```

## Module Structure

```mermaid
graph LR
    subgraph "src/llm_benchmark"
        subgraph "algorithms/"
            PRIMES[primes.py<br/>Primes class]
            SORT[sort.py<br/>Sort class]
        end
        
        subgraph "control/"
            SINGLE[single.py<br/>SingleForLoop class]
            DOUBLE[double.py<br/>DoubleForLoop class]
        end
        
        subgraph "datastructures/"
            DSLIST[dslist.py<br/>DsList class]
        end
        
        subgraph "strings/"
            STROPS[strops.py<br/>StrOps class]
        end
        
        subgraph "sql/"
            QUERY[query.py<br/>SqlQuery class]
        end
        
        subgraph "generator/"
            GENLIST[gen_list.py<br/>GenList class]
        end
    end
    
    style PRIMES fill:#ffccbc
    style SORT fill:#ffccbc
    style SINGLE fill:#c8e6c9
    style DOUBLE fill:#c8e6c9
    style DSLIST fill:#bbdefb
    style STROPS fill:#f8bbd0
    style QUERY fill:#d1c4e9
    style GENLIST fill:#fff9c4
```

## Component Diagram

```mermaid
graph TD
    subgraph "Algorithms Domain"
        A1[Prime Number Operations]
        A2[Sorting Algorithms]
        A3[Factorization]
    end
    
    subgraph "Control Flow Domain"
        C1[Single Loop Operations]
        C2[Nested Loop Operations]
        C3[Range & Accumulation]
    end
    
    subgraph "Data Structure Domain"
        D1[List Manipulation]
        D2[Searching & Sorting]
        D3[Rotation & Merging]
    end
    
    subgraph "String Domain"
        S1[String Reversal]
        S2[Palindrome Detection]
    end
    
    subgraph "Database Domain"
        Q1[Album Queries]
        Q2[Table Joins]
        Q3[Aggregations]
    end
    
    subgraph "Utility Domain"
        G1[Random Data Generation]
        G2[Matrix Generation]
    end
    
    A1 --> |uses| G1
    A2 --> |uses| G1
    C2 --> |uses| G1
    C2 --> |uses| G2
    D1 --> |uses| G1
    Q1 --> |queries| DB[(Database)]
    Q2 --> |queries| DB
    Q3 --> |queries| DB
    
    style A1 fill:#ffccbc
    style A2 fill:#ffccbc
    style A3 fill:#ffccbc
    style C1 fill:#c8e6c9
    style C2 fill:#c8e6c9
    style C3 fill:#c8e6c9
    style D1 fill:#bbdefb
    style D2 fill:#bbdefb
    style D3 fill:#bbdefb
    style S1 fill:#f8bbd0
    style S2 fill:#f8bbd0
    style Q1 fill:#d1c4e9
    style Q2 fill:#d1c4e9
    style Q3 fill:#d1c4e9
    style G1 fill:#fff9c4
    style G2 fill:#fff9c4
```

## Data Flow

### Typical Benchmark Workflow

```mermaid
sequenceDiagram
    participant User
    participant Main
    participant Module
    participant TestData
    participant Benchmark
    
    User->>Main: Run demo/test
    Main->>TestData: Generate input data
    TestData-->>Main: Return test data
    Main->>Module: Call benchmark function
    Module->>Module: Execute algorithm
    Module-->>Main: Return result
    Main->>Benchmark: Measure performance
    Benchmark-->>Main: Return metrics
    Main-->>User: Display results
```

### SQL Query Flow

```mermaid
sequenceDiagram
    participant Client
    participant SqlQuery
    participant SQLite
    participant ChinookDB
    
    Client->>SqlQuery: query_album("Presence")
    SqlQuery->>SQLite: Connect to DB
    SQLite->>ChinookDB: Open chinook.db
    ChinookDB-->>SQLite: Connection established
    SqlQuery->>SQLite: Execute SELECT query
    SQLite->>ChinookDB: Query Album table
    ChinookDB-->>SQLite: Return rows
    SQLite-->>SqlQuery: fetchall()
    SqlQuery->>SqlQuery: Process results
    SqlQuery-->>Client: Return boolean
```

### Test Execution Flow

```mermaid
flowchart TD
    START([Test Execution])
    DISCOVER[Pytest Discovery]
    COLLECT[Collect Test Cases]
    UNIT{Unit Test?}
    BENCH{Benchmark?}
    RUN_UNIT[Run Test Function]
    RUN_BENCH[Run Benchmark Iterations]
    ASSERT[Check Assertions]
    MEASURE[Measure Performance]
    PASS{Pass?}
    REPORT[Generate Report]
    END([Complete])
    
    START --> DISCOVER
    DISCOVER --> COLLECT
    COLLECT --> UNIT
    UNIT -->|Yes| RUN_UNIT
    UNIT -->|No| BENCH
    RUN_UNIT --> ASSERT
    ASSERT --> PASS
    BENCH -->|Yes| RUN_BENCH
    RUN_BENCH --> MEASURE
    MEASURE --> PASS
    PASS -->|Yes| REPORT
    PASS -->|No| REPORT
    REPORT --> END
    
    style START fill:#c8e6c9
    style END fill:#c8e6c9
    style PASS fill:#fff9c4
    style RUN_UNIT fill:#bbdefb
    style RUN_BENCH fill:#ffccbc
```

## Class Relationships

```mermaid
classDiagram
    class Primes {
        <<static>>
        +is_prime(n: int) bool
        +is_prime_ineff(n: int) bool
        +sum_primes(n: int) int
        +prime_factors(n: int) List~int~
    }
    
    class Sort {
        <<static>>
        +sort_list(v: List) void
        +dutch_flag_partition(v: List, pivot: int) void
        +max_n(v: List, n: int) List
    }
    
    class SingleForLoop {
        <<static>>
        +sum_range(n: int) int
        +max_list(v: List) int
        +sum_modulus(n: int, m: int) int
    }
    
    class DoubleForLoop {
        <<static>>
        +sum_square(n: int) int
        +sum_triangle(n: int) int
        +count_pairs(v: List) int
        +count_duplicates(v1: List, v2: List) int
        +sum_matrix(m: List~List~) int
    }
    
    class DsList {
        <<static>>
        +modify_list(v: List) List
        +search_list(v: List, n: int) List~int~
        +sort_list(v: List) List
        +reverse_list(v: List) List
        +rotate_list(v: List, n: int) List
        +merge_lists(v1: List, v2: List) List
    }
    
    class StrOps {
        <<static>>
        +str_reverse(s: str) str
        +palindrome(s: str) bool
    }
    
    class SqlQuery {
        <<static>>
        +query_album(name: str) bool
        +join_albums() list
        +top_invoices() list
    }
    
    class GenList {
        <<static>>
        +random_list(size: int, max: int) List~int~
        +random_matrix(rows: int, cols: int, max: int) List~List~
    }
    
    note for Primes "O(√n) optimized prime checking\nSieve of Eratosthenes for sum_primes"
    note for Sort "In-place sorting algorithms\nDutch flag partitioning"
    note for DoubleForLoop "Nested loop patterns\nO(n²) complexity operations"
    note for SqlQuery "Uses SQLite with Chinook DB\nDemonstrates SQL operations"
```

## Test Architecture

```mermaid
graph TB
    subgraph "Test Organization"
        subgraph "tests/llm_benchmark/"
            T_ALG[algorithms/test_primes.py]
            T_SORT[algorithms/test_sort.py]
            T_SINGLE[control/test_single.py]
            T_DOUBLE[control/test_double.py]
            T_DS[datastructures/test_dslist.py]
            T_SQL[sql/test_query.py]
            T_STR[strings/test_strops.py]
        end
        
        subgraph "Test Types"
            PARAM[Parametrized Tests]
            UNIT[Unit Tests]
            BENCH_T[Benchmark Tests]
        end
        
        subgraph "Fixtures"
            SAMPLE[Sample Data]
            BENCH_FIX[Benchmark Fixture]
        end
    end
    
    T_ALG --> PARAM
    T_ALG --> UNIT
    T_ALG --> BENCH_T
    T_SORT --> PARAM
    T_SINGLE --> PARAM
    T_DOUBLE --> PARAM
    T_DS --> PARAM
    T_SQL --> UNIT
    T_STR --> PARAM
    
    PARAM --> SAMPLE
    BENCH_T --> BENCH_FIX
    
    style T_ALG fill:#ffccbc
    style T_SORT fill:#ffccbc
    style T_SINGLE fill:#c8e6c9
    style T_DOUBLE fill:#c8e6c9
    style T_DS fill:#bbdefb
    style T_SQL fill:#d1c4e9
    style T_STR fill:#f8bbd0
    style PARAM fill:#fff9c4
    style UNIT fill:#fff9c4
    style BENCH_T fill:#fff9c4
```

### Test Coverage Map

```mermaid
mindmap
    root((Test Coverage))
        Algorithms
            Prime Detection
                Edge cases 0,1,2
                Large primes
                Composite numbers
            Prime Summation
                Empty range
                Small ranges
                Large ranges
            Sorting
                Empty lists
                Single element
                Already sorted
                Reverse sorted
        Control Flow
            Single Loops
                Zero range
                Negative numbers
                Large ranges
            Double Loops
                Empty matrices
                Single row/col
                Square matrices
        Data Structures
            List Operations
                Empty lists
                Single element
                Duplicates
                Large lists
        SQL
            Query Operations
                Existing records
                Missing records
                Complex joins
        Strings
            String Ops
                Empty strings
                Palindromes
                Single chars
```

## Deployment View

```mermaid
flowchart TB
    subgraph "Development Environment"
        DEV[Developer Machine]
        POETRY[Poetry Env]
        GIT[Git Repository]
    end
    
    subgraph "Build & Package"
        BUILD[poetry build]
        WHEEL[.whl Package]
        SDIST[.tar.gz Source]
    end
    
    subgraph "Distribution"
        PYPI[PyPI Repository]
        PRIVATE[Private Registry]
        GIT_INSTALL[Git Install]
    end
    
    subgraph "Production Usage"
        PROD_APP[Application]
        VENV[Virtual Env]
        LIB[llm_benchmark]
    end
    
    DEV --> POETRY
    POETRY --> GIT
    GIT --> BUILD
    BUILD --> WHEEL
    BUILD --> SDIST
    WHEEL --> PYPI
    WHEEL --> PRIVATE
    SDIST --> PYPI
    GIT --> GIT_INSTALL
    
    PYPI --> PROD_APP
    PRIVATE --> PROD_APP
    GIT_INSTALL --> PROD_APP
    PROD_APP --> VENV
    VENV --> LIB
    
    style DEV fill:#e1f5ff
    style BUILD fill:#fff4e6
    style PYPI fill:#c8e6c9
    style PROD_APP fill:#bbdefb
```

## Design Patterns

### Static Method Pattern

```mermaid
classDiagram
    class BenchmarkClass {
        <<static methods only>>
        +operation1() result
        +operation2() result
        +operation3() result
    }
    
    note for BenchmarkClass "All methods are static\nNo instance state\nPure functions (mostly)\nEasy to test and benchmark"
```

**Rationale:**
- No need for instance state
- Functions are stateless and pure
- Easy to call from tests and benchmarks
- Simple API: `ClassName.method(args)`

### Module Organization Pattern

```mermaid
graph TD
    MODULE[Module Directory]
    README[README.md - Documentation]
    INIT[__init__.py - Exports]
    IMPL[implementation.py - Class]
    
    MODULE --> README
    MODULE --> INIT
    MODULE --> IMPL
    
    style MODULE fill:#bbdefb
    style README fill:#fff9c4
    style INIT fill:#c8e6c9
    style IMPL fill:#ffccbc
```

**Structure:**
- Each module has its own directory
- README.md documents the module
- `__init__.py` exports public classes
- Implementation files contain logic

### Test Mirroring Pattern

```mermaid
graph LR
    subgraph "Source Structure"
        S1[src/llm_benchmark/algorithms/primes.py]
        S2[src/llm_benchmark/control/single.py]
        S3[src/llm_benchmark/datastructures/dslist.py]
    end
    
    subgraph "Test Structure"
        T1[tests/llm_benchmark/algorithms/test_primes.py]
        T2[tests/llm_benchmark/control/test_single.py]
        T3[tests/llm_benchmark/datastructures/test_dslist.py]
    end
    
    S1 -.mirrors.-> T1
    S2 -.mirrors.-> T2
    S3 -.mirrors.-> T3
```

## Performance Considerations

### Complexity Overview

```mermaid
graph TD
    subgraph "Time Complexity Classes"
        O1["O(1) - Constant"]
        OLOGN["O(log n) - Logarithmic"]
        ON["O(n) - Linear"]
        ONLOGN["O(n log n) - Linearithmic"]
        ON2["O(n²) - Quadratic"]
        OSQRTN["O(√n) - Square Root"]
        ONLOGLGN["O(n log log n) - Sieve"]
    end
    
    subgraph "Implemented Operations"
        PRIME_CHECK["Primes.is_prime<br/>O(√n)"]
        PRIME_SUM["Primes.sum_primes<br/>O(n log log n)"]
        BUBBLE_SORT["Sort.sort_list<br/>O(n²)"]
        SUM_RANGE["SingleForLoop.sum_range<br/>O(n)"]
        SUM_MATRIX["DoubleForLoop.sum_matrix<br/>O(n²)"]
        SEARCH_LIST["DsList.search_list<br/>O(n)"]
    end
    
    OSQRTN --> PRIME_CHECK
    ONLOGLGN --> PRIME_SUM
    ON2 --> BUBBLE_SORT
    ON --> SUM_RANGE
    ON2 --> SUM_MATRIX
    ON --> SEARCH_LIST
    
    style O1 fill:#c8e6c9
    style OLOGN fill:#c8e6c9
    style ON fill:#fff9c4
    style ONLOGN fill:#fff9c4
    style ON2 fill:#ffccbc
    style OSQRTN fill:#c8e6c9
    style ONLOGLGN fill:#c8e6c9
```

### Optimization Journey

```mermaid
journey
    title Prime Functions Optimization Journey
    section Original Implementation
        is_prime O(n): 2: Slow
        sum_primes O(n²): 1: Very Slow
    section Analysis Phase
        Identify bottleneck: 3: Analysis
        Measure performance: 4: Benchmarking
        Research algorithms: 5: Research
    section Optimization
        Implement O(√n) is_prime: 4: Good
        Implement Sieve: 5: Excellent
        Verify correctness: 5: Testing
    section Validation
        Run benchmarks: 5: Fast
        Measure speedup: 5: 10-100x faster
        Document changes: 4: Complete
```

## Performance Hotspots

```mermaid
pie title "Benchmark Execution Time Distribution (Sample)"
    "Primes.sum_primes" : 35
    "DoubleForLoop.sum_matrix" : 20
    "Sort.sort_list" : 18
    "DsList operations" : 12
    "SQL queries" : 10
    "Other operations" : 5
```

## Design Decisions

### Key Architectural Decisions

| Decision | Rationale | Trade-offs |
|----------|-----------|------------|
| Static methods only | No need for state, simpler API | Less flexibility for inheritance |
| Separate modules | Clear separation of concerns | More files to manage |
| Type hints required | Better IDE support, documentation | Slight verbose overhead |
| Poetry for dependencies | Modern, reproducible builds | Learning curve for new users |
| Pytest for testing | Industry standard, excellent plugins | Additional dependency |
| In-place vs. copy | Some methods modify, some return new | Must document behavior clearly |

### Why These Choices?

```mermaid
graph TD
    REQ[Requirements]
    REQ --> R1[Benchmark LLM code generation]
    REQ --> R2[Measure performance]
    REQ --> R3[Easy to use API]
    REQ --> R4[Extensible design]
    
    R1 --> D1[Diverse problem domains]
    R2 --> D2[pytest-benchmark integration]
    R3 --> D3[Static methods, no state]
    R4 --> D4[Modular organization]
    
    D1 --> SOL[Multiple modules<br/>Clear separation]
    D2 --> SOL
    D3 --> SOL
    D4 --> SOL
    
    style REQ fill:#e1f5ff
    style SOL fill:#c8e6c9
```

## Module Dependencies

```mermaid
graph TD
    subgraph "External Dependencies"
        SQLITE[sqlite3<br/>built-in]
        TYPING[typing<br/>built-in]
        MATH[math<br/>built-in]
    end
    
    subgraph "Dev Dependencies"
        PYTEST[pytest]
        PYBENCH[pytest-benchmark]
        BLACK[black]
        ISORT[isort]
    end
    
    subgraph "Core Modules"
        ALG[algorithms]
        CTL[control]
        DS[datastructures]
        STR[strings]
        SQL_M[sql]
        GEN[generator]
    end
    
    SQL_M --> SQLITE
    ALG --> MATH
    ALG --> TYPING
    CTL --> TYPING
    DS --> TYPING
    
    PYTEST --> ALG
    PYTEST --> CTL
    PYTEST --> DS
    PYTEST --> STR
    PYTEST --> SQL_M
    PYBENCH --> PYTEST
    
    style SQLITE fill:#c8e6c9
    style TYPING fill:#c8e6c9
    style MATH fill:#c8e6c9
    style PYTEST fill:#bbdefb
    style PYBENCH fill:#bbdefb
```

## Future Architecture Considerations

```mermaid
mindmap
    root((Future Enhancements))
        Extensibility
            Plugin system
            Custom benchmarks
            External modules
        Performance
            Parallel execution
            Caching layer
            JIT compilation
        Features
            More algorithms
            Network operations
            File I/O benchmarks
            Async operations
        Integration
            CI/CD pipelines
            Cloud benchmarking
            Result storage
            Comparison tools
        Documentation
            Interactive examples
            Video tutorials
            API docs generation
```

## Conclusion

The architecture of `llm-benchmarking-py` is designed for:
- **Simplicity**: Easy to understand and use
- **Modularity**: Clear separation of concerns
- **Testability**: Comprehensive test coverage
- **Performance**: Optimized implementations where it matters
- **Extensibility**: Easy to add new benchmarks

The use of static methods, modular organization, and comprehensive testing makes the library both a useful tool and a good reference implementation for benchmarking systems.

---

**Document Version:** 1.0  
**Last Updated:** 2024  
**Maintainers:** See [CONTRIBUTING.md](CONTRIBUTING.md)

For implementation details, see the source code. For contributing, see [CONTRIBUTING.md](CONTRIBUTING.md).
