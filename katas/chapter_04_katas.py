"""
Chapter 4 Katas — When Action Learns to Repeat

Functions, docstrings, *args/**kwargs, scope.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/The-Tao-Of-Python/katas
        pytest chapter_04_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your function needs work.

YOUR MISSION:
    Implement each function below so that all 7 tests pass.
    Do not modify the test functions — only implement the functions above them.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — The Pure One
# ─────────────────────────────────────────────

def calculate_batting_average(hits: int, at_bats: int) -> float:
    """
    Calculate batting average as hits / at_bats.
    Return 0.0 if at_bats is 0.
    Round to 3 decimal places.

    Example:
        calculate_batting_average(34, 100) → 0.34
        calculate_batting_average(0, 50)   → 0.0
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("hits, at_bats, expected", [
    (34,  100,  0.34),
    (0,   50,   0.0),
    (3,   10,   0.3),
    (1,   3,    0.333),
    (0,   0,    0.0),
])
def test_calculate_batting_average(hits, at_bats, expected):
    assert calculate_batting_average(hits, at_bats) == pytest.approx(expected, abs=1e-3)


# ─────────────────────────────────────────────
# KATA 2 — The Flexible Adder
# ─────────────────────────────────────────────

def sum_all(*numbers: float) -> float:
    """
    Accept any number of positional arguments and return their sum.
    Return 0.0 if no arguments given.

    Example:
        sum_all(1, 2, 3)      → 6.0
        sum_all(10, 20, 30)   → 60.0
        sum_all()             → 0.0
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("numbers, expected", [
    ((1, 2, 3),          6.0),
    ((10, 20, 30, 40),   100.0),
    ((),                 0.0),
    ((-1, 1),            0.0),
    ((3.14, 2.0),        5.14),
])
def test_sum_all(numbers, expected):
    assert sum_all(*numbers) == pytest.approx(expected)


# ─────────────────────────────────────────────
# KATA 3 — The Profile Builder
# ─────────────────────────────────────────────

def create_profile(name: str, **attributes) -> dict:
    """
    Create a profile dictionary with a required "name" key
    and any additional keyword arguments as additional keys.

    Example:
        create_profile("Cosmos", age=25, position="pitcher")
        → {"name": "Cosmos", "age": 25, "position": "pitcher"}
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("name, kwargs, expected", [
    ("Cosmos", {"age": 25, "position": "pitcher"},
               {"name": "Cosmos", "age": 25, "position": "pitcher"}),
    ("Miguel", {},
               {"name": "Miguel"}),
    ("Ana",    {"country": "Mexico"},
               {"name": "Ana", "country": "Mexico"}),
])
def test_create_profile(name, kwargs, expected):
    assert create_profile(name, **kwargs) == expected


# ─────────────────────────────────────────────
# KATA 4 — The Classifier
# ─────────────────────────────────────────────

def classify_number(n: float) -> str:
    """
    Return the classification of a number:
        n > 0  → "positive"
        n < 0  → "negative"
        n == 0 → "zero"

    Example:
        classify_number(42)   → "positive"
        classify_number(-3)   → "negative"
        classify_number(0)    → "zero"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("n, expected", [
    (42,    "positive"),
    (-3,    "negative"),
    (0,     "zero"),
    (0.001, "positive"),
    (-0.001, "negative"),
])
def test_classify_number(n, expected):
    assert classify_number(n) == expected


# ─────────────────────────────────────────────
# KATA 5 — The Composer
# ─────────────────────────────────────────────

def apply_transformations(value: float, *funcs) -> float:
    """
    Apply a sequence of functions to a value, one after another.
    Each function in `funcs` takes a single float and returns a float.
    If no functions are given, return the value unchanged.

    Example:
        double = lambda x: x * 2
        add_ten = lambda x: x + 10
        apply_transformations(5, double, add_ten) → 20.0
        # 5 → double → 10 → add_ten → 20
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("value, funcs, expected", [
    (5.0,  (lambda x: x * 2, lambda x: x + 10),  20.0),
    (3.0,  (lambda x: x ** 2,),                   9.0),
    (10.0, (),                                     10.0),
    (2.0,  (lambda x: x + 1, lambda x: x * 3),    9.0),
])
def test_apply_transformations(value, funcs, expected):
    assert apply_transformations(value, *funcs) == pytest.approx(expected)


# ─────────────────────────────────────────────
# KATA 6 — The Memoizer (Scope & Closures)
# ─────────────────────────────────────────────

def make_counter(start: int = 0):
    """
    Return a function that, when called, increments and returns a count.
    The count starts at `start` and increases by 1 each call.
    Uses closure to maintain state.

    Example:
        counter = make_counter(0)
        counter()  → 1
        counter()  → 2
        counter()  → 3
    """
    # YOUR CODE HERE
    pass


def test_make_counter():
    counter = make_counter(0)
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3


def test_make_counter_custom_start():
    counter = make_counter(10)
    assert counter() == 11
    assert counter() == 12


def test_make_counter_independent():
    """Two counters should be independent."""
    counter_a = make_counter(0)
    counter_b = make_counter(0)
    counter_a()
    counter_a()
    assert counter_b() == 1   # counter_b is unaffected by counter_a


# ─────────────────────────────────────────────
# KATA 7 — The Pipeline
# ─────────────────────────────────────────────

def process_names(names: list, prefix: str = "", suffix: str = "") -> list:
    """
    Process a list of raw names:
    1. Strip each name
    2. Title-case each name
    3. Add `prefix` before and `suffix` after each name (if provided)

    Return the processed list.

    Example:
        process_names(["  cosmos  ", " miguel "], prefix="Sr. ")
        → ["Sr. Cosmos", "Sr. Miguel"]

        process_names(["zen"], suffix=" (active)")
        → ["Zen (active)"]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("names, prefix, suffix, expected", [
    (["  cosmos  ", " miguel "], "Sr. ", "",         ["Sr. Cosmos", "Sr. Miguel"]),
    (["zen"],                    "",     " (active)", ["Zen (active)"]),
    (["  tao  "],                "",     "",          ["Tao"]),
    (["a", "b", "c"],            "X-",  "-Y",         ["X-A-Y", "X-B-Y", "X-C-Y"]),
])
def test_process_names(names, prefix, suffix, expected):
    assert process_names(names, prefix, suffix) == expected
