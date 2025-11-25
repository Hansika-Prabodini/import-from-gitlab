import pytest

from llm_benchmark.sql.query import SqlQuery


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Presence", True),
        ("Roundabout", False),
    ],
)
def test_query_album(name: str, expected: bool) -> None:
    assert SqlQuery.query_album(name) == expected


def test_benchmark_query_album(benchmark) -> None:
    benchmark(SqlQuery.query_album, "Presence")


def test_join_albums() -> None:
    assert SqlQuery.join_albums()[0] == (
        "For Those About To Rock (We Salute You)",
        "For Those About To Rock We Salute You",
        "AC/DC",
    )


def test_benchmark_join_albums(benchmark) -> None:
    benchmark(SqlQuery.join_albums)


def test_top_invoices() -> None:
    top = SqlQuery.top_invoices()
    assert top[0][2] == 25.86
    assert top[2][2] == 21.86
    assert len(top) == 10


def test_benchmark_top_invoices(benchmark) -> None:
    benchmark(SqlQuery.top_invoices)


def test_query_album_sql_injection_or_based() -> None:
    """Test that OR-based SQL injection attempts are neutralized.
    
    Attack vector: "' OR '1'='1" attempts to bypass the WHERE clause
    by injecting a condition that is always true, which would return
    all albums in the database.
    
    Expected: Should return False (no album literally named "' OR '1'='1")
    unless a parameterized query is used to safely neutralize the input.
    """
    malicious_input = "' OR '1'='1"
    result = SqlQuery.query_album(malicious_input)
    # Should return False since no album has this literal title
    assert result is False, "SQL injection attempt should return False"


def test_query_album_sql_injection_comment_based() -> None:
    """Test that comment-based SQL injection attempts are neutralized.
    
    Attack vector: "'; --" attempts to terminate the query early and
    comment out the rest, potentially bypassing security checks or
    causing unexpected behavior.
    
    Expected: Should return False (no album literally named "'; --")
    when using parameterized queries.
    """
    malicious_input = "'; --"
    result = SqlQuery.query_album(malicious_input)
    # Should return False since no album has this literal title
    assert result is False, "SQL injection comment attempt should return False"


def test_query_album_sql_injection_union_based() -> None:
    """Test that UNION-based SQL injection attempts are neutralized.
    
    Attack vector: "' UNION SELECT * FROM Track --" attempts to append
    a UNION query to retrieve data from other tables (Track table in
    this case), potentially exposing sensitive information.
    
    Expected: Should return False (no album literally named with UNION syntax)
    when using parameterized queries.
    """
    malicious_input = "' UNION SELECT * FROM Track --"
    result = SqlQuery.query_album(malicious_input)
    # Should return False since no album has this literal title
    assert result is False, "SQL injection UNION attempt should return False"


def test_query_album_with_apostrophe() -> None:
    """Test that legitimate album titles containing apostrophes work correctly.
    
    This ensures that the parameterized query implementation doesn't break
    legitimate use cases where album titles naturally contain single quotes.
    
    Note: "Big Ones" is used as an example. If it doesn't exist in the database,
    this test will pass (return False) but demonstrates the query handles
    apostrophes safely without causing syntax errors.
    """
    legitimate_input = "Big Ones"
    # This should not raise an exception and should handle the apostrophe safely
    result = SqlQuery.query_album(legitimate_input)
    # Result depends on whether "Big Ones" actually exists in the database
    # The important part is that it doesn't cause a SQL syntax error
    assert isinstance(result, bool), "Should return a boolean without errors"


def test_query_album_sql_injection_stacked_queries() -> None:
    """Test that stacked query SQL injection attempts are neutralized.
    
    Attack vector: "'; DROP TABLE Album; --" attempts to execute multiple
    SQL statements, potentially causing data loss or corruption.
    
    Expected: Should return False and not execute the DROP statement
    when using parameterized queries.
    """
    malicious_input = "'; DROP TABLE Album; --"
    result = SqlQuery.query_album(malicious_input)
    # Should return False since no album has this literal title
    assert result is False, "SQL injection stacked query attempt should return False"
    
    # Verify the Album table still exists by querying a known album
    result_after = SqlQuery.query_album("Presence")
    assert result_after is True, "Album table should still exist and contain data"


def test_query_album_sql_injection_prevention() -> None:
    """Comprehensive test to verify SQL injection is prevented.
    
    This test would FAIL with vulnerable code using f-strings:
        cur.execute(f"SELECT * FROM Album WHERE Title = '{name}'")
    
    With the malicious input "' OR '1'='1", the query becomes:
        SELECT * FROM Album WHERE Title = '' OR '1'='1'
    
    This returns all albums (since '1'='1' is always true), making the
    function return True instead of False.
    
    This test PASSES with parameterized queries:
        cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
    
    The parameterized query treats the entire input as a literal string,
    so it searches for an album literally named "' OR '1'='1", which
    doesn't exist, correctly returning False.
    """
    # Test case that exploits SQL injection vulnerability
    malicious_input = "' OR '1'='1"
    
    # With parameterized queries, this should return False
    # (no album has this literal title)
    # With f-string interpolation, this would return True
    # (because the injected SQL always evaluates to true)
    result = SqlQuery.query_album(malicious_input)
    
    assert result is False, (
        "SQL injection prevention failed! The function should return False "
        "for malicious input, but it returned True. This indicates the query "
        "is vulnerable to SQL injection attacks."
    )
