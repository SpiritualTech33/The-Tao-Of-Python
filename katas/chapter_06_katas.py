"""
Chapter 6 Katas — Truth Put to the Test

pytest, assert, parametrize, fixtures.
These katas test your ability to WRITE TESTS — not just implement functions.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/The-Tao-Of-Python/katas
        pytest chapter_06_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your tests or functions need work.

YOUR MISSION:
    Some katas ask you to implement functions.
    Others ask you to write the TESTS themselves.
    Read each kata carefully.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — Implement and Test: The Multiplier
# ─────────────────────────────────────────────

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("a, b, expected", [
    # Add at least 5 test cases here — cover positives, negatives, zero, floats
    # YOUR TEST CASES HERE
    # Example row: (2.0, 3.0, 6.0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected)


# ─────────────────────────────────────────────
# KATA 2 — Fixture Practice: The Stack
# ─────────────────────────────────────────────

class Stack:
    """A simple LIFO stack."""

    def __init__(self):
        self._items = []

    def push(self, item) -> None:
        """Add item to the top."""
        self._items.append(item)

    def pop(self):
        """Remove and return top item. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return top item without removing it. Raise IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack has no items."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return number of items."""
        return len(self._items)


@pytest.fixture
def empty_stack():
    """Return a fresh empty Stack."""
    # YOUR CODE HERE — return a Stack instance
    pass


@pytest.fixture
def populated_stack():
    """Return a Stack with items [1, 2, 3] already pushed (3 is on top)."""
    # YOUR CODE HERE — create a Stack, push 1, 2, 3, and return it
    pass


def test_stack_is_empty_when_new(empty_stack):
    assert empty_stack.is_empty() is True


def test_stack_push_increases_size(empty_stack):
    empty_stack.push(42)
    assert empty_stack.size() == 1


def test_stack_pop_returns_last_pushed(populated_stack):
    assert populated_stack.pop() == 3


def test_stack_pop_from_empty_raises(empty_stack):
    with pytest.raises(IndexError):
        empty_stack.pop()


def test_stack_peek_does_not_remove(populated_stack):
    top = populated_stack.peek()
    assert top == 3
    assert populated_stack.size() == 3  # size unchanged


# ─────────────────────────────────────────────
# KATA 3 — Write the Tests: The Palindrome Checker
# ─────────────────────────────────────────────

def is_palindrome(text: str) -> bool:
    """
    Return True if text (ignoring case and spaces) is a palindrome.

    Examples:
        is_palindrome("racecar") → True
        is_palindrome("Python")  → False
    """
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]


@pytest.mark.parametrize("text, expected", [
    # Write at least 6 test cases here.
    # Include: obvious palindrome, obvious non-palindrome,
    # mixed case, sentence palindrome, single char, empty string.
    # YOUR TEST CASES HERE
    # Example row: ("racecar", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected


# ─────────────────────────────────────────────
# KATA 4 — Implement and Test: The Temperature Converter
# ─────────────────────────────────────────────

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C * 9/5) + 32

    Example:
        celsius_to_fahrenheit(0)   → 32.0
        celsius_to_fahrenheit(100) → 212.0
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("celsius, expected_fahrenheit", [
    # Write at least 5 test cases here.
    # Include: freezing, boiling, body temperature, below zero, room temperature.
    # YOUR TEST CASES HERE
])
def test_celsius_to_fahrenheit(celsius, expected_fahrenheit):
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected_fahrenheit, abs=0.01)


# ─────────────────────────────────────────────
# KATA 5 — Test Edge Cases: The Divider
# ─────────────────────────────────────────────

def divide(a: float, b: float) -> float:
    """
    Return a / b.
    Raise ZeroDivisionError if b is 0.
    Raise TypeError if a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a / b


@pytest.mark.parametrize("a, b, expected", [
    # Write 4 normal cases
    # YOUR TEST CASES HERE
])
def test_divide_normal(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    # Write a test that verifies ZeroDivisionError is raised when b=0
    # YOUR CODE HERE
    pass


def test_divide_type_error():
    # Write a test that verifies TypeError is raised for non-numeric input
    # YOUR CODE HERE
    pass


# ─────────────────────────────────────────────
# KATA 6 — Fixture with Scope: The Logger
# ─────────────────────────────────────────────

class SimpleLogger:
    """Collects log messages in memory."""

    def __init__(self):
        self._messages = []

    def log(self, message: str) -> None:
        self._messages.append(message)

    def get_messages(self) -> list:
        return list(self._messages)

    def clear(self) -> None:
        self._messages.clear()

    def count(self) -> int:
        return len(self._messages)


@pytest.fixture
def logger():
    """
    Create and return a fresh SimpleLogger instance.
    YOUR CODE HERE — just return SimpleLogger()
    """
    # YOUR CODE HERE
    pass


def test_logger_starts_empty(logger):
    assert logger.count() == 0


def test_logger_records_messages(logger):
    logger.log("first message")
    logger.log("second message")
    assert logger.count() == 2
    assert "first message" in logger.get_messages()


def test_logger_clear(logger):
    logger.log("message")
    logger.clear()
    assert logger.count() == 0


@pytest.mark.parametrize("messages", [
    ["hello"],
    ["a", "b", "c"],
    ["zen", "tao", "void", "cosmos"],
])
def test_logger_parametrized(logger, messages):
    for msg in messages:
        logger.log(msg)
    assert logger.count() == len(messages)
    for msg in messages:
        assert msg in logger.get_messages()


# ─────────────────────────────────────────────
# KATA 7 — Integration: The Full Test Suite
# ─────────────────────────────────────────────

def calculate_team_average(players: list) -> float:
    """
    Given a list of player dicts (each with "hits" and "at_bats"),
    return the team's collective batting average:
        total_hits / total_at_bats

    Return 0.0 if total_at_bats is 0.
    Raise TypeError if players is not a list.
    Raise ValueError if the list is empty.
    """
    # YOUR CODE HERE
    pass


@pytest.fixture
def sample_team():
    """Return a sample team of 3 players."""
    return [
        {"name": "Cosmos", "hits": 34, "at_bats": 100},
        {"name": "Miguel", "hits": 27, "at_bats": 90},
        {"name": "Luis",   "hits": 15, "at_bats": 80},
    ]


def test_team_average_calculation(sample_team):
    # total_hits = 34 + 27 + 15 = 76
    # total_at_bats = 100 + 90 + 80 = 270
    # expected = 76 / 270 ≈ 0.2815
    result = calculate_team_average(sample_team)
    assert result == pytest.approx(76 / 270, abs=1e-4)


def test_team_average_empty_list():
    with pytest.raises(ValueError):
        calculate_team_average([])


def test_team_average_type_error():
    with pytest.raises(TypeError):
        calculate_team_average("not a list")


@pytest.mark.parametrize("players, expected", [
    ([{"hits": 1, "at_bats": 4}],                              0.25),
    ([{"hits": 0, "at_bats": 10}],                             0.0),
    ([{"hits": 3, "at_bats": 10}, {"hits": 7, "at_bats": 10}], 0.5),
])
def test_team_average_parametrized(players, expected):
    assert calculate_team_average(players) == pytest.approx(expected, abs=1e-4)
