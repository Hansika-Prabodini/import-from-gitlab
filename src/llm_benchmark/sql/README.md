# SQL Module

This module provides SQL query operations for benchmarking LLM code generation capabilities with database interactions. It uses the Chinook sample database (SQLite) to test various SQL patterns including simple queries, joins, and aggregations.

## Database

**Database File:** `data/chinook.db`  
**Type:** SQLite  
**Schema:** Chinook sample database (music store)

### Key Tables
- **Album**: Album information (AlbumId, Title, ArtistId)
- **Artist**: Artist information (ArtistId, Name)
- **Track**: Track information (TrackId, Name, AlbumId, etc.)
- **Invoice**: Invoice data (InvoiceId, CustomerId, Total, etc.)
- **Customer**: Customer information (CustomerId, FirstName, LastName, etc.)

## Components

### SqlQuery (`query.py`)

Database query operations demonstrating various SQL patterns.

#### Methods

##### `query_album(name: str) -> bool`
Checks if an album with the given title exists in the database.

**Parameters:**
- `name` (str): The album title to search for

**Returns:**
- `bool`: True if the album exists, False otherwise

**Example:**
```python
from llm_benchmark.sql.query import SqlQuery

result = SqlQuery.query_album('Presence')
print(result)  # Output: True (Led Zeppelin album)

result = SqlQuery.query_album('Nonexistent Album')
print(result)  # Output: False
```

**SQL Pattern:**
```sql
SELECT * FROM Album WHERE Title = '{name}'
```

**Optimization Notes:**
- Current implementation selects all columns (`SELECT *`)
- Could be optimized to `SELECT COUNT(*)` or `SELECT 1`
- Uses string interpolation (vulnerable to SQL injection in production)

---

##### `join_albums() -> list`
Joins the Album, Artist, and Track tables to retrieve comprehensive music information.

**Parameters:**
- None

**Returns:**
- `list`: List of tuples containing (TrackName, AlbumName, ArtistName)

**Example:**
```python
from llm_benchmark.sql.query import SqlQuery

results = SqlQuery.join_albums()
print(results[0])  # Output: ('For Those About To Rock', 'For Those About To Rock We Salute You', 'AC/DC')
```

**SQL Pattern:**
```sql
SELECT 
    t.Name AS TrackName,
    (SELECT a2.Title FROM Album a2 WHERE a2.AlbumId = t.AlbumId) AS AlbumName,
    (SELECT ar.Name FROM Artist ar
     JOIN Album a3 ON a3.ArtistId = ar.ArtistId
     WHERE a3.AlbumId = t.AlbumId) AS ArtistName
FROM Track t
```

**Optimization Notes:**
- Current implementation uses correlated subqueries
- Could be optimized with explicit JOINs for better performance
- Demonstrates nested query patterns

---

##### `top_invoices() -> list`
Retrieves the top 10 invoices by total amount with customer information.

**Parameters:**
- None

**Returns:**
- `list`: List of tuples containing (InvoiceId, CustomerName, Total) for top 10 invoices

**Example:**
```python
from llm_benchmark.sql.query import SqlQuery

results = SqlQuery.top_invoices()
for invoice in results:
    print(f"Invoice {invoice[0]}: {invoice[1]} - ${invoice[2]}")
```

**SQL Pattern:**
```sql
SELECT 
    i.InvoiceId,
    c.FirstName || ' ' || c.LastName AS CustomerName,
    i.Total
FROM Invoice i
JOIN Customer c ON c.CustomerId = i.CustomerId
ORDER BY i.Total DESC
```

**Features:**
- Uses explicit JOIN for optimal performance
- String concatenation with `||` operator
- Returns top 10 via Python slicing `[:10]`

---

## Usage in Benchmarking

These SQL operations test:
- **Query Construction**: Building syntactically correct SQL queries
- **Join Patterns**: Using different types of joins (explicit vs. subqueries)
- **Filtering**: WHERE clause usage
- **Ordering**: ORDER BY implementation
- **Aggregation**: Working with result sets
- **String Manipulation**: SQL string operations

## SQL Patterns Tested

1. **Simple SELECT with WHERE**: Basic filtering
2. **Correlated Subqueries**: Nested queries with outer table references
3. **Explicit JOINs**: Proper join syntax
4. **String Concatenation**: Using `||` operator
5. **Ordering**: Sorting results with ORDER BY

## Performance Considerations

| Method | Pattern | Performance Notes |
|--------|---------|------------------|
| `query_album` | Simple SELECT | Fast with index on Title |
| `join_albums` | Correlated subqueries | Could be optimized with explicit JOINs |
| `top_invoices` | Explicit JOIN + ORDER BY | Efficient with proper indexing |

## Testing

Run tests specific to this module:

```bash
poetry run pytest tests/llm_benchmark/sql/
```

Run benchmarks:

```bash
poetry run pytest --benchmark-only tests/llm_benchmark/sql/
```

## Complete Demo

```python
from llm_benchmark.sql.query import SqlQuery

print("=== Album Search ===")
albums = ['Presence', 'Roundabout', 'Nonexistent']
for album in albums:
    exists = SqlQuery.query_album(album)
    print(f"'{album}': {exists}")

print("\n=== Album Joins (First 3) ===")
joins = SqlQuery.join_albums()
for i, row in enumerate(joins[:3], 1):
    print(f"{i}. Track: {row[0]}, Album: {row[1]}, Artist: {row[2]}")

print("\n=== Top 5 Invoices ===")
invoices = SqlQuery.top_invoices()
for invoice in invoices[:5]:
    print(f"Invoice #{invoice[0]}: {invoice[1]} - ${invoice[2]:.2f}")
```

**Sample Output:**
```
=== Album Search ===
'Presence': True
'Roundabout': False
'Nonexistent': False

=== Album Joins (First 3) ===
1. Track: For Those About To Rock, Album: For Those About..., Artist: AC/DC
2. Track: Put The Finger On You, Album: For Those About..., Artist: AC/DC
3. Track: Let's Get It Up, Album: For Those About..., Artist: AC/DC

=== Top 5 Invoices ===
Invoice #299: Helena Holý - $25.86
Invoice #334: Julia Barnett - $25.86
...
```

## Design Notes

- **Real Database**: Uses actual SQLite database (Chinook) for realistic testing
- **Context Managers**: Uses `with` statements for proper connection management
- **Multiple Patterns**: Demonstrates different SQL approaches (subqueries vs. joins)
- **Production Warnings**: Some patterns (like string interpolation) are for demonstration only

## Security Considerations

⚠️ **Warning**: The `query_album` method uses string interpolation for SQL queries, which is vulnerable to SQL injection. This is intentional for benchmarking purposes but should **never** be used in production code.

**Production-safe alternative:**
```python
cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
```

## Database Schema Overview

The Chinook database models a digital music store:

```
Artist (ArtistId, Name)
    ↓
Album (AlbumId, Title, ArtistId)
    ↓
Track (TrackId, Name, AlbumId, ...)
    ↓
InvoiceLine (InvoiceLineId, InvoiceId, TrackId, ...)
    ↓
Invoice (InvoiceId, CustomerId, Total, ...)
    ↓
Customer (CustomerId, FirstName, LastName, ...)
```

## Further Reading

- See `query.md` for additional optimization notes
- Chinook database documentation: [GitHub - lerocha/chinook-database](https://github.com/lerocha/chinook-database)
