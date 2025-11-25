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


def test_query_album_sql_injection_safety() -> None:
    """Test that the query_album function is safe from SQL injection.
    
    This test ensures that single quotes in album names are properly escaped
    and don't break the SQL query or allow injection attacks.
    """
    # Test with a single quote in the name (common in album titles)
    # This should return False (album doesn't exist) without causing an error
    result = SqlQuery.query_album("Test' OR '1'='1")
    assert result is False
    
    # Test with another injection attempt
    result = SqlQuery.query_album("'; DROP TABLE Album; --")
    assert result is False
    
    # Test normal string with apostrophe (like "Greatest Hits '92")
    # Should work without crashing
    result = SqlQuery.query_album("Greatest Hits '92")
    assert result is False  # Assuming this album doesn't exist in test DB


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
