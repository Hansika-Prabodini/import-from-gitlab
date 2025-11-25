# Authentication Module

This module provides simple authentication utilities for benchmarking authentication-related code generation and operations.

## Features

### Password Hashing and Verification
- **hash_password(password, salt=None)**: Hash a password using SHA-256 with salt
- **verify_password(password, hashed, salt)**: Verify a password against a stored hash

### Token Generation
- **generate_token(length=32)**: Generate secure random tokens for session management

### Username Validation
- **validate_username(username, min_length=3, max_length=20)**: Validate username format
  - Checks length constraints
  - Ensures alphanumeric characters and underscores only

### Password Strength Checking
- **check_password_strength(password)**: Verify password meets security requirements
  - Minimum 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit

### User Management
- **create_user(username, password)**: Create a new user with validated credentials
- **authenticate_user(username, password, stored_hash, stored_salt)**: Authenticate user credentials

## Usage Examples

```python
from llm_benchmark.auth.simple_auth import SimpleAuth

# Hash a password
hashed, salt = SimpleAuth.hash_password("MySecurePass123")
print(f"Hash: {hashed}")
print(f"Salt: {salt}")

# Verify a password
is_valid = SimpleAuth.verify_password("MySecurePass123", hashed, salt)
print(f"Password valid: {is_valid}")  # True

# Generate a session token
token = SimpleAuth.generate_token()
print(f"Token: {token}")

# Validate username
is_valid = SimpleAuth.validate_username("john_doe")
print(f"Username valid: {is_valid}")  # True

# Check password strength
is_strong = SimpleAuth.check_password_strength("Weak")
print(f"Password strong: {is_strong}")  # False

is_strong = SimpleAuth.check_password_strength("SecurePass123")
print(f"Password strong: {is_strong}")  # True

# Create a user
user = SimpleAuth.create_user("john_doe", "SecurePass123")
print(user)
# Output: {'username': 'john_doe', 'password_hash': '...', 'salt': '...', 'token': '...'}

# Authenticate a user
authenticated = SimpleAuth.authenticate_user(
    "john_doe",
    "SecurePass123",
    user['password_hash'],
    user['salt']
)
print(f"Authenticated: {authenticated}")  # True
```

## Implementation Details

### Hashing Algorithm
- Uses SHA-256 for password hashing
- Implements salting to prevent rainbow table attacks
- Salt is randomly generated using `secrets.token_hex()`

### Token Generation
- Uses cryptographically secure random generation via `secrets.token_hex()`
- Default token length is 32 bytes (64 hex characters)

### Security Considerations
This is a **simple** implementation for benchmarking purposes. For production use:
- Consider using more robust hashing algorithms like bcrypt, argon2, or scrypt
- Implement rate limiting for authentication attempts
- Add additional security measures like account lockout
- Use HTTPS for transmission of credentials
- Implement proper session management

## Benchmarking Use Cases

This module is designed to benchmark:
- Password hashing performance
- String validation operations
- Regular expression matching
- Cryptographic operations
- Dictionary/object creation and manipulation
