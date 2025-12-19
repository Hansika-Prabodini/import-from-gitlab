"""
Demonstration test for SQL injection vulnerability in query_album.

This test will FAIL before the patch (returns True due to SQL injection)
and PASS after the patch (returns False, treating input as literal string).
"""
from llm_benchmark.sql.query import SqlQuery


def test_sql_injection_vulnerability():
    """
    Test that demonstrates the SQL injection bug.
    
    With the buggy implementation using f-strings:
        f"SELECT * FROM Album WHERE Title = '{name}'"
    
    When name = "' OR '1'='1", the query becomes:
        SELECT * FROM Album WHERE Title = '' OR '1'='1'
    
    This condition is always true ('1'='1'), so it returns all albums,
    making the function return True instead of False.
    
    After the patch using parameterized queries:
        cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
    
    The input is treated as a literal string, so it searches for an album
    literally named "' OR '1'='1", which doesn't exist, returning False.
    """
    malicious_input = "' OR '1'='1"
    result = SqlQuery.query_album(malicious_input)
    
    # Expected: False (no album with this literal name exists)
    # Buggy behavior: True (SQL injection makes WHERE clause always true)
    assert result is False, (
        f"SQL injection vulnerability detected! "
        f"Input \"' OR '1'='1\" returned {result} but should return False"
    )


if __name__ == "__main__":
    test_sql_injection_vulnerability()
    print("Test passed! SQL injection is properly handled.")
