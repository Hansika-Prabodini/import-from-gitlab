"""
Test to demonstrate SQL injection vulnerability bug in query_album method.

This test would FAIL before the patch (when using f-string interpolation)
and PASS after the patch (when using parameterized queries).

The bug: query_album uses f-string interpolation which is vulnerable to SQL injection.
When a malicious input like "' OR '1'='1" is passed, it creates the query:
    SELECT * FROM Album WHERE Title = '' OR '1'='1'
This matches all albums (returns True), but should return False.

The fix: Use parameterized queries with placeholders instead of f-string interpolation.
"""

import pytest

from llm_benchmark.sql.query import SqlQuery


def test_sql_injection_vulnerability():
    """
    This test demonstrates the SQL injection bug.
    
    Before patch: The function uses f-string interpolation, so the input
    "' OR '1'='1" will be executed as SQL code, matching all albums and 
    returning True.
    
    After patch: The function uses parameterized queries, so the input is
    treated as a literal string value. No album has this exact title, so
    it returns False.
    """
    # Malicious input that attempts SQL injection
    malicious_input = "' OR '1'='1"
    
    result = SqlQuery.query_album(malicious_input)
    
    # Expected: False (no album has this literal title)
    # Before patch: True (SQL injection succeeds, matches all albums)
    # After patch: False (SQL injection is neutralized)
    assert result is False, (
        f"SQL injection vulnerability detected! "
        f"The input '{malicious_input}' should be treated as a literal string, "
        f"not as SQL code. Expected False but got {result}."
    )


def test_normal_album_query_still_works():
    """
    Verify that legitimate queries still work after the fix.
    """
    # Test with a known album from the chinook database
    result = SqlQuery.query_album("Presence")
    assert result is True, "Legitimate album query should return True"
    
    # Test with a non-existent album
    result = SqlQuery.query_album("NonExistentAlbum12345")
    assert result is False, "Non-existent album should return False"


def test_sql_injection_union_attack():
    """
    Test another common SQL injection technique (UNION-based).
    """
    malicious_input = "' UNION SELECT * FROM Track --"
    result = SqlQuery.query_album(malicious_input)
    
    # Should return False - no album has this literal title
    assert result is False, "UNION-based SQL injection should be neutralized"


def test_sql_injection_stacked_query():
    """
    Test stacked query SQL injection attempt.
    """
    malicious_input = "'; DROP TABLE Album; --"
    result = SqlQuery.query_album(malicious_input)
    
    # Should return False and not execute the DROP
    assert result is False, "Stacked query SQL injection should be neutralized"
    
    # Verify table still exists
    result_after = SqlQuery.query_album("Presence")
    assert result_after is True, "Album table should still exist"
