import hashlib
import secrets
import re
from typing import Tuple


class SimpleAuth:
    """Simple authentication utilities for benchmarking"""

    @staticmethod
    def hash_password(password: str, salt: str = None) -> Tuple[str, str]:
        """Hash a password using SHA-256 with salt
        
        Args:
            password (str): Plain text password to hash
            salt (str, optional): Salt for hashing. If None, generates a new salt
            
        Returns:
            Tuple[str, str]: Tuple of (hashed_password, salt)
        """
        if salt is None:
            salt = secrets.token_hex(16)
        
        # Combine password and salt
        salted_password = password + salt
        
        # Hash using SHA-256
        hashed = hashlib.sha256(salted_password.encode()).hexdigest()
        
        return hashed, salt

    @staticmethod
    def verify_password(password: str, hashed: str, salt: str) -> bool:
        """Verify a password against a hash
        
        Args:
            password (str): Plain text password to verify
            hashed (str): Hashed password to compare against
            salt (str): Salt used in original hashing
            
        Returns:
            bool: True if password matches, False otherwise
        """
        # Hash the provided password with the same salt
        new_hash, _ = SimpleAuth.hash_password(password, salt)
        
        # Compare hashes
        return new_hash == hashed

    @staticmethod
    def generate_token(length: int = 32) -> str:
        """Generate a random token for session management
        
        Args:
            length (int): Length of token in bytes (default: 32)
            
        Returns:
            str: Hexadecimal token string
        """
        return secrets.token_hex(length)

    @staticmethod
    def validate_username(username: str, min_length: int = 3, max_length: int = 20) -> bool:
        """Validate username format
        
        Args:
            username (str): Username to validate
            min_length (int): Minimum username length (default: 3)
            max_length (int): Maximum username length (default: 20)
            
        Returns:
            bool: True if username is valid, False otherwise
        """
        if not username:
            return False
        
        if len(username) < min_length or len(username) > max_length:
            return False
        
        # Username should only contain alphanumeric characters and underscores
        pattern = r'^[a-zA-Z0-9_]+$'
        return bool(re.match(pattern, username))

    @staticmethod
    def check_password_strength(password: str) -> bool:
        """Check if password meets basic strength requirements
        
        Requirements:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
        
        Args:
            password (str): Password to check
            
        Returns:
            bool: True if password meets requirements, False otherwise
        """
        if len(password) < 8:
            return False
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        return has_upper and has_lower and has_digit

    @staticmethod
    def create_user(username: str, password: str) -> dict:
        """Create a user with hashed password
        
        Args:
            username (str): Username for the new user
            password (str): Plain text password
            
        Returns:
            dict: User dictionary with username, hashed password, and salt,
                  or error message if validation fails
        """
        if not SimpleAuth.validate_username(username):
            return {"error": "Invalid username"}
        
        if not SimpleAuth.check_password_strength(password):
            return {"error": "Password does not meet strength requirements"}
        
        hashed, salt = SimpleAuth.hash_password(password)
        
        return {
            "username": username,
            "password_hash": hashed,
            "salt": salt,
            "token": SimpleAuth.generate_token()
        }

    @staticmethod
    def authenticate_user(username: str, password: str, stored_hash: str, stored_salt: str) -> bool:
        """Authenticate a user with username and password
        
        Args:
            username (str): Username attempting to authenticate
            password (str): Plain text password to verify
            stored_hash (str): Stored password hash
            stored_salt (str): Stored salt
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        if not SimpleAuth.validate_username(username):
            return False
        
        return SimpleAuth.verify_password(password, stored_hash, stored_salt)
