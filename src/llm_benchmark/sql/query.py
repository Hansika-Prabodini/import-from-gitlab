import sqlite3
from textwrap import dedent


class SqlQuery:
    @staticmethod
    def query_album(name: str) -> bool:
        """Check if an album exists

        Args:
            name (str): Name of the album

        Returns:
            bool: True if the album exists, False otherwise
        
        Security:
            Uses parameterized queries to prevent SQL injection attacks.
            User input is passed as a query parameter, never interpolated.
        """
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()
            # Use parameterized query with ? placeholder to prevent SQL injection
            cur.execute("SELECT * FROM Album WHERE Title = ?", (name,))
            return len(cur.fetchall()) > 0

    @staticmethod
    def join_albums() -> list:
        """Join the Album, Artist, and Track tables

        Returns:
            list:
        
        Security:
            Static query with no user input parameters - no SQL injection risk.
        """
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()
            # Static query with no parameters - secure by design
            cur.execute(
                dedent(
                    """\
                    SELECT 
                        t.Name AS TrackName, (
                            SELECT a2.Title 
                            FROM Album a2 
                            WHERE a2.AlbumId = t.AlbumId
                        ) AS AlbumName, 
                        (
                            SELECT ar.Name 
                            FROM Artist ar
                            JOIN Album a3 ON a3.ArtistId = ar.ArtistId
                            WHERE a3.AlbumId = t.AlbumId
                        ) AS ArtistName
                    FROM 
                        Track t
                    """
                )
            )
            return cur.fetchall()

    @staticmethod
    def top_invoices() -> list:
        """Get the top 10 invoices by total

        Returns:
            list: List of tuples
        
        Security:
            Static query with no user input parameters - no SQL injection risk.
        """
        with sqlite3.connect("data/chinook.db") as conn:
            cur = conn.cursor()
            # Static query with no parameters - secure by design
            cur.execute(
                dedent(
                    """\
                    SELECT 
                        i.InvoiceId, 
                        c.FirstName || ' ' || c.LastName AS CustomerName, 
                        i.Total
                    FROM 
                        Invoice i
                    JOIN Customer c ON c.CustomerId = i.CustomerId
                    ORDER BY i.Total DESC
                    """
                )
            )
            return cur.fetchall()[:10]
