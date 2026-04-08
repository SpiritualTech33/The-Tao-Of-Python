"""
Chapter 1 Katas — The First Steps of the Programmer Monk

Variables, types, strings, operators.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/Python-From-The-Void/katas
        pytest chapter_01_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your function needs work.

YOUR MISSION:
    Implement each function below so that all 7 tests pass.
    Do not modify the test functions — only implement the functions above them.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — The Name
# ─────────────────────────────────────────────

def describe_variable(value) -> str:
    """
    Return a string describing the type and value of the given variable.

    Examples:
        describe_variable(42)        → "int: 42"
        describe_variable("cosmos")  → "str: cosmos"
        describe_variable(3.14)      → "float: 3.14"
        describe_variable(True)      → "bool: True"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("value, expected", [
    (42,       "int: 42"),
    ("cosmos", "str: cosmos"),
    (3.14,     "float: 3.14"),
    (True,     "bool: True"),
    (None,     "NoneType: None"),
])
def test_describe_variable(value, expected):
    assert describe_variable(value) == expected


# ─────────────────────────────────────────────
# KATA 2 — The Greeting
# ─────────────────────────────────────────────

def build_greeting(name: str, age: int) -> str:
    """
    Build a greeting string using an f-string.

    Example:
        build_greeting("cosmos", 25) → "Hello, Cosmos. You are 25 years old."
    Note: name should be title-cased in the output.
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("name, age, expected", [
    ("cosmos",  25, "Hello, Cosmos. You are 25 years old."),
    ("miguel",  30, "Hello, Miguel. You are 30 years old."),
    ("ana",      1, "Hello, Ana. You are 1 years old."),
])
def test_build_greeting(name, age, expected):
    assert build_greeting(name, age) == expected


# ─────────────────────────────────────────────
# KATA 3 — The Cleaner
# ─────────────────────────────────────────────

def clean_and_title(raw_name: str) -> str:
    """
    Strip whitespace from both ends of the string
    and return it in title case.

    Example:
        clean_and_title("  cosmos de la cruz  ") → "Cosmos De La Cruz"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("raw, expected", [
    ("  cosmos de la cruz  ", "Cosmos De La Cruz"),
    ("   python   ",          "Python"),
    ("\tthe tao\n",           "The Tao"),
    ("ZEN",                   "Zen"),
])
def test_clean_and_title(raw, expected):
    assert clean_and_title(raw) == expected


# ─────────────────────────────────────────────
# KATA 4 — The Slicer
# ─────────────────────────────────────────────

def get_initials(full_name: str) -> str:
    """
    Return the initials of a full name as uppercase letters separated by dots.

    Example:
        get_initials("cosmos de la cruz") → "C.D.L.C"
        get_initials("guido van rossum")  → "G.V.R"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("name, expected", [
    ("cosmos de la cruz", "C.D.L.C"),
    ("guido van rossum",  "G.V.R"),
    ("zen",               "Z"),
    ("the tao of python", "T.T.O.P"),
])
def test_get_initials(name, expected):
    assert get_initials(name) == expected


# ─────────────────────────────────────────────
# KATA 5 — The Calculator
# ─────────────────────────────────────────────

def compute(a: float, b: float, operator: str) -> float:
    """
    Perform a basic arithmetic operation based on the operator string.
    Supported operators: "+", "-", "*", "/"

    Returns float result.
    Raises ValueError if operator is not supported.
    Raises ZeroDivisionError if dividing by zero.

    Example:
        compute(10, 3, "+") → 13.0
        compute(10, 3, "/") → 3.3333...
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("a, b, op, expected", [
    (10.0, 3.0,  "+",  13.0),
    (10.0, 3.0,  "-",   7.0),
    (10.0, 3.0,  "*",  30.0),
    (10.0, 2.0,  "/",   5.0),
    (-4.0, 2.0,  "*",  -8.0),
])
def test_compute(a, b, op, expected):
    assert compute(a, b, op) == pytest.approx(expected)


def test_compute_invalid_operator():
    with pytest.raises(ValueError):
        compute(1, 2, "^")


def test_compute_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        compute(5, 0, "/")


# ─────────────────────────────────────────────
# KATA 6 — The Word Counter
# ─────────────────────────────────────────────

def count_words(sentence: str) -> int:
    """
    Count the number of words in a sentence.
    Words are separated by spaces. Strip first.

    Example:
        count_words("the tao of python") → 4
        count_words("  hello   world  ") → 2
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("sentence, expected", [
    ("the tao of python",   4),
    ("  hello   world  ",   2),
    ("one",                 1),
    ("",                    0),
    ("   ",                 0),
])
def test_count_words(sentence, expected):
    assert count_words(sentence) == expected


# ─────────────────────────────────────────────
# KATA 7 — The Palindrome
# ─────────────────────────────────────────────

def is_palindrome(word: str) -> bool:
    """
    Return True if the word is a palindrome (reads the same forwards and backwards).
    Ignore case. Ignore spaces.

    Example:
        is_palindrome("racecar") → True
        is_palindrome("Python")  → False
        is_palindrome("A man a plan a canal Panama") → True
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("word, expected", [
    ("racecar",                        True),
    ("Python",                         False),
    ("A man a plan a canal Panama",    True),
    ("Was it a car or a cat I saw",    True),
    ("cosmos",                         False),
    ("level",                          True),
])
def test_is_palindrome(word, expected):
    assert is_palindrome(word) == expected
