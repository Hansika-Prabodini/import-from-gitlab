import pytest

from llm_benchmark.auth.simple_auth import SimpleAuth


# Test password hashing and verification
def test_hash_password():
    password = "TestPassword123"
    hashed, salt = SimpleAuth.hash_password(password)
    
    assert hashed is not None
    assert salt is not None
    assert len(hashed) == 64  # SHA-256 produces 64 hex characters
    assert len(salt) == 32  # 16 bytes = 32 hex characters


def test_hash_password_with_salt():
    password = "TestPassword123"
    custom_salt = "abc123def456"
    hashed, salt = SimpleAuth.hash_password(password, custom_salt)
    
    assert salt == custom_salt
    assert hashed is not None


def test_verify_password_correct():
    password = "TestPassword123"
    hashed, salt = SimpleAuth.hash_password(password)
    
    assert SimpleAuth.verify_password(password, hashed, salt) is True


def test_verify_password_incorrect():
    password = "TestPassword123"
    hashed, salt = SimpleAuth.hash_password(password)
    
    assert SimpleAuth.verify_password("WrongPassword", hashed, salt) is False


def test_benchmark_hash_password(benchmark):
    benchmark(SimpleAuth.hash_password, "TestPassword123")


def test_benchmark_verify_password(benchmark):
    password = "TestPassword123"
    hashed, salt = SimpleAuth.hash_password(password)
    benchmark(SimpleAuth.verify_password, password, hashed, salt)


# Test token generation
@pytest.mark.parametrize("length", [8, 16, 32, 64])
def test_generate_token(length: int):
    token = SimpleAuth.generate_token(length)
    
    assert token is not None
    assert len(token) == length * 2  # hex encoding doubles the length


def test_generate_token_uniqueness():
    token1 = SimpleAuth.generate_token()
    token2 = SimpleAuth.generate_token()
    
    assert token1 != token2


def test_benchmark_generate_token(benchmark):
    benchmark(SimpleAuth.generate_token, 32)


# Test username validation
@pytest.mark.parametrize(
    "username, expected",
    [
        ("john_doe", True),
        ("user123", True),
        ("JohnDoe", True),
        ("_underscore", True),
        ("ab", False),  # too short
        ("a" * 21, False),  # too long
        ("user@name", False),  # invalid character
        ("user name", False),  # space not allowed
        ("user-name", False),  # hyphen not allowed
        ("", False),  # empty string
    ],
)
def test_validate_username(username: str, expected: bool):
    assert SimpleAuth.validate_username(username) == expected


def test_benchmark_validate_username(benchmark):
    benchmark(SimpleAuth.validate_username, "john_doe")


# Test password strength checking
@pytest.mark.parametrize(
    "password, expected",
    [
        ("SecurePass123", True),
        ("Abcdefg1", True),
        ("MyP@ssw0rd", True),
        ("weak", False),  # too short
        ("WeakPassword", False),  # no digit
        ("weakpassword1", False),  # no uppercase
        ("WEAKPASSWORD1", False),  # no lowercase
        ("NoDigits", False),  # no digit
        ("12345678", False),  # no letters
    ],
)
def test_check_password_strength(password: str, expected: bool):
    assert SimpleAuth.check_password_strength(password) == expected


def test_benchmark_check_password_strength(benchmark):
    benchmark(SimpleAuth.check_password_strength, "SecurePass123")


# Test user creation
def test_create_user_valid():
    user = SimpleAuth.create_user("john_doe", "SecurePass123")
    
    assert "error" not in user
    assert user["username"] == "john_doe"
    assert "password_hash" in user
    assert "salt" in user
    assert "token" in user


def test_create_user_invalid_username():
    user = SimpleAuth.create_user("ab", "SecurePass123")
    
    assert "error" in user
    assert user["error"] == "Invalid username"


def test_create_user_weak_password():
    user = SimpleAuth.create_user("john_doe", "weak")
    
    assert "error" in user
    assert user["error"] == "Password does not meet strength requirements"


def test_benchmark_create_user(benchmark):
    benchmark(SimpleAuth.create_user, "john_doe", "SecurePass123")


# Test user authentication
def test_authenticate_user_correct():
    user = SimpleAuth.create_user("john_doe", "SecurePass123")
    
    authenticated = SimpleAuth.authenticate_user(
        "john_doe", "SecurePass123", user["password_hash"], user["salt"]
    )
    
    assert authenticated is True


def test_authenticate_user_wrong_password():
    user = SimpleAuth.create_user("john_doe", "SecurePass123")
    
    authenticated = SimpleAuth.authenticate_user(
        "john_doe", "WrongPassword", user["password_hash"], user["salt"]
    )
    
    assert authenticated is False


def test_authenticate_user_invalid_username():
    user = SimpleAuth.create_user("john_doe", "SecurePass123")
    
    authenticated = SimpleAuth.authenticate_user(
        "ab", "SecurePass123", user["password_hash"], user["salt"]
    )
    
    assert authenticated is False


def test_benchmark_authenticate_user(benchmark):
    user = SimpleAuth.create_user("john_doe", "SecurePass123")
    benchmark(
        SimpleAuth.authenticate_user,
        "john_doe",
        "SecurePass123",
        user["password_hash"],
        user["salt"],
    )
