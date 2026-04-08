"""
Chapter 5 Katas — The Art of Falling Without Breaking

Error handling, exceptions, try/except, raise.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/Python-From-The-Void/katas
        pytest chapter_05_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your function needs work.

YOUR MISSION:
    Implement each function below so that all 7 tests pass.
    Do not modify the test functions — only implement the functions above them.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — The Safe Divider
# ─────────────────────────────────────────────

def safe_divide(numerator: float, denominator: float) -> float | None:
    """
    Divide numerator by denominator.
    Return None if denominator is zero.
    Raise TypeError if either argument is not a number.

    Example:
        safe_divide(10, 2)  → 5.0
        safe_divide(10, 0)  → None
        safe_divide("a", 2) → raises TypeError
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("num, den, expected", [
    (10.0, 2.0,   5.0),
    (9.0,  3.0,   3.0),
    (7.0,  2.0,   3.5),
    (0.0,  5.0,   0.0),
    (10.0, 0.0,   None),
])
def test_safe_divide(num, den, expected):
    assert safe_divide(num, den) == expected


def test_safe_divide_type_error():
    with pytest.raises(TypeError):
        safe_divide("ten", 2)


# ─────────────────────────────────────────────
# KATA 2 — The Safe Converter
# ─────────────────────────────────────────────

def safe_to_int(value, default: int = 0) -> int:
    """
    Convert `value` to int.
    If conversion fails, return `default` instead of raising an exception.

    Example:
        safe_to_int("42")       → 42
        safe_to_int("cosmos")   → 0
        safe_to_int(3.9)        → 3
        safe_to_int("xyz", -1)  → -1
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("value, default, expected", [
    ("42",     0,   42),
    ("cosmos", 0,   0),
    (3.9,      0,   3),
    ("xyz",   -1,  -1),
    (None,     5,   5),
])
def test_safe_to_int(value, default, expected):
    assert safe_to_int(value, default) == expected


# ─────────────────────────────────────────────
# KATA 3 — The Validator
# ─────────────────────────────────────────────

class InvalidAverageError(ValueError):
    """Raised when a batting average is outside the valid range [0.0, 1.0]."""
    pass


def validate_batting_average(average: float) -> float:
    """
    Return the average if it is valid (between 0.0 and 1.0 inclusive).
    Raise InvalidAverageError if out of range.
    Raise TypeError if not a float or int.

    Example:
        validate_batting_average(0.342)  → 0.342
        validate_batting_average(1.5)    → raises InvalidAverageError
        validate_batting_average("high") → raises TypeError
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("avg, expected", [
    (0.342,  0.342),
    (0.0,    0.0),
    (1.0,    1.0),
    (0.5,    0.5),
])
def test_validate_batting_average_valid(avg, expected):
    assert validate_batting_average(avg) == expected


@pytest.mark.parametrize("avg", [-0.1, 1.001, 2.0])
def test_validate_batting_average_invalid(avg):
    with pytest.raises(InvalidAverageError):
        validate_batting_average(avg)


def test_validate_batting_average_type_error():
    with pytest.raises(TypeError):
        validate_batting_average("high")


# ─────────────────────────────────────────────
# KATA 4 — The File Reader
# ─────────────────────────────────────────────

def read_first_line(filepath: str) -> str | None:
    """
    Open the file at `filepath` and return its first line (stripped).
    If the file does not exist, return None.
    If the file is empty, return an empty string "".

    Use EAFP style (try/except).

    Example:
        read_first_line("existing.txt") → "first line content"
        read_first_line("ghost.txt")    → None
    """
    # YOUR CODE HERE
    pass


def test_read_first_line_not_found():
    assert read_first_line("/nonexistent/path/file.txt") is None


def test_read_first_line_existing(tmp_path):
    """tmp_path is a pytest built-in fixture that creates a temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("hello cosmos\nsecond line\n")
    assert read_first_line(str(test_file)) == "hello cosmos"


def test_read_first_line_empty(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    assert read_first_line(str(empty_file)) == ""


# ─────────────────────────────────────────────
# KATA 5 — The Retry
# ─────────────────────────────────────────────

def retry(func, max_attempts: int = 3):
    """
    Call `func()` up to `max_attempts` times.
    If it succeeds (no exception), return the result.
    If it raises an exception every time, re-raise the last exception.

    Example:
        call_count = 0
        def flaky():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("not yet")
            return "success"

        retry(flaky, 3)  → "success"
    """
    # YOUR CODE HERE
    pass


def test_retry_succeeds_on_first_try():
    result = retry(lambda: "ok", max_attempts=3)
    assert result == "ok"


def test_retry_succeeds_on_third_try():
    call_count = {"n": 0}

    def flaky():
        call_count["n"] += 1
        if call_count["n"] < 3:
            raise ValueError("not yet")
        return "success"

    assert retry(flaky, max_attempts=3) == "success"
    assert call_count["n"] == 3


def test_retry_raises_after_max_attempts():
    def always_fails():
        raise RuntimeError("always fails")

    with pytest.raises(RuntimeError):
        retry(always_fails, max_attempts=3)


# ─────────────────────────────────────────────
# KATA 6 — The Context Manager
# ─────────────────────────────────────────────

def count_lines_in_file(filepath: str) -> int:
    """
    Count and return the number of lines in a file.
    Return 0 if the file does not exist.
    Use a `with` statement to open the file.

    Example:
        count_lines_in_file("three_lines.txt") → 3
        count_lines_in_file("ghost.txt")       → 0
    """
    # YOUR CODE HERE
    pass


def test_count_lines_not_found():
    assert count_lines_in_file("/no/such/file.txt") == 0


def test_count_lines_existing(tmp_path):
    test_file = tmp_path / "lines.txt"
    test_file.write_text("line one\nline two\nline three\n")
    assert count_lines_in_file(str(test_file)) == 3


def test_count_lines_empty(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("")
    assert count_lines_in_file(str(empty_file)) == 0


# ─────────────────────────────────────────────
# KATA 7 — The Multi-Guard
# ─────────────────────────────────────────────

def parse_player_data(data: dict) -> dict:
    """
    Parse and validate a player data dictionary.
    Expected keys: "name" (str), "hits" (int >= 0), "at_bats" (int >= 0).

    Return a dict with:
        "name": cleaned (stripped, title-cased)
        "hits": int
        "at_bats": int
        "batting_avg": float (hits / at_bats, 0.0 if at_bats is 0)

    Raise KeyError if any required key is missing.
    Raise TypeError if "hits" or "at_bats" are not integers.
    Raise ValueError if "hits" or "at_bats" are negative,
                      or if "hits" > "at_bats".
    """
    # YOUR CODE HERE
    pass


def test_parse_player_data_valid():
    result = parse_player_data({"name": " cosmos ", "hits": 34, "at_bats": 100})
    assert result["name"] == "Cosmos"
    assert result["hits"] == 34
    assert result["at_bats"] == 100
    assert result["batting_avg"] == pytest.approx(0.34)


def test_parse_player_data_missing_key():
    with pytest.raises(KeyError):
        parse_player_data({"name": "Cosmos", "hits": 5})


def test_parse_player_data_type_error():
    with pytest.raises(TypeError):
        parse_player_data({"name": "Cosmos", "hits": "34", "at_bats": 100})


def test_parse_player_data_value_error_negative():
    with pytest.raises(ValueError):
        parse_player_data({"name": "Cosmos", "hits": -1, "at_bats": 100})


def test_parse_player_data_value_error_hits_exceed():
    with pytest.raises(ValueError):
        parse_player_data({"name": "Cosmos", "hits": 101, "at_bats": 100})
