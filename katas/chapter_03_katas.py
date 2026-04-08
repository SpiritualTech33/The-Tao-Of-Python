"""
Chapter 3 Katas — The Word and the Path

String manipulation and control flow.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/Python-From-The-Void/katas
        pytest chapter_03_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your function needs work.

YOUR MISSION:
    Implement each function below so that all 7 tests pass.
    Do not modify the test functions — only implement the functions above them.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — The Censor
# ─────────────────────────────────────────────

def censor_word(sentence: str, word: str) -> str:
    """
    Replace every occurrence of `word` in `sentence` with asterisks
    of the same length. Case-insensitive match, but replacement uses
    asterisks equal to the original word length.

    Example:
        censor_word("I love Python", "Python") → "I love ******"
        censor_word("python is PYTHON", "python") → "****** is ******"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("sentence, word, expected", [
    ("I love Python",        "Python",  "I love ******"),
    ("python is PYTHON",     "python",  "****** is ******"),
    ("nothing to censor",    "xyz",     "nothing to censor"),
    ("zen zen zen",          "zen",     "*** *** ***"),
])
def test_censor_word(sentence, word, expected):
    assert censor_word(sentence, word) == expected


# ─────────────────────────────────────────────
# KATA 2 — The Grade
# ─────────────────────────────────────────────

def letter_grade(score: int) -> str:
    """
    Convert a numeric score (0-100) to a letter grade using conditionals.

    90-100 → "A"
    80-89  → "B"
    70-79  → "C"
    60-69  → "D"
    0-59   → "F"

    Raise ValueError for scores outside 0-100.
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("score, expected", [
    (100, "A"),
    (95,  "A"),
    (85,  "B"),
    (72,  "C"),
    (65,  "D"),
    (40,  "F"),
    (0,   "F"),
])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected


def test_letter_grade_invalid():
    with pytest.raises(ValueError):
        letter_grade(101)
    with pytest.raises(ValueError):
        letter_grade(-1)


# ─────────────────────────────────────────────
# KATA 3 — The Accumulator
# ─────────────────────────────────────────────

def sum_of_squares(n: int) -> int:
    """
    Return the sum of squares from 1 to n (inclusive) using a loop.

    sum_of_squares(4) = 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30

    Raise ValueError if n < 1.
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("n, expected", [
    (1,  1),
    (2,  5),
    (3,  14),
    (4,  30),
    (5,  55),
    (10, 385),
])
def test_sum_of_squares(n, expected):
    assert sum_of_squares(n) == expected


def test_sum_of_squares_invalid():
    with pytest.raises(ValueError):
        sum_of_squares(0)


# ─────────────────────────────────────────────
# KATA 4 — The Formatter
# ─────────────────────────────────────────────

def format_player_stats(name: str, hits: int, at_bats: int) -> str:
    """
    Return a formatted stats string for a player.
    Batting average = hits / at_bats (0.000 if at_bats is 0).
    Format: "Player: {Name} | H: {hits} | AB: {at_bats} | AVG: {avg:.3f}"

    Name should be title-cased.

    Example:
        format_player_stats("cosmos", 34, 100)
        → "Player: Cosmos | H: 34 | AB: 100 | AVG: 0.340"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("name, hits, ab, expected", [
    ("cosmos", 34, 100, "Player: Cosmos | H: 34 | AB: 100 | AVG: 0.340"),
    ("miguel", 0,  50,  "Player: Miguel | H: 0 | AB: 50 | AVG: 0.000"),
    ("ANA",    10, 0,   "Player: Ana | H: 10 | AB: 0 | AVG: 0.000"),
])
def test_format_player_stats(name, hits, ab, expected):
    assert format_player_stats(name, hits, ab) == expected


# ─────────────────────────────────────────────
# KATA 5 — The Fizzbuzz (Classic. Inevitable.)
# ─────────────────────────────────────────────

def fizzbuzz(n: int) -> list:
    """
    Return a list of strings for numbers 1 through n:
      - "FizzBuzz" if divisible by both 3 and 5
      - "Fizz"     if divisible by 3 only
      - "Buzz"     if divisible by 5 only
      - The number as a string otherwise

    Example:
        fizzbuzz(15) → ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz",
                        "11","Fizz","13","14","FizzBuzz"]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("n, expected_slice", [
    (5,  ["1", "2", "Fizz", "4", "Buzz"]),
    (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]),
    (1,  ["1"]),
])
def test_fizzbuzz(n, expected_slice):
    assert fizzbuzz(n) == expected_slice


# ─────────────────────────────────────────────
# KATA 6 — The Caesar Cipher
# ─────────────────────────────────────────────

def caesar_cipher(text: str, shift: int) -> str:
    """
    Encrypt text using a Caesar cipher — shift each letter by `shift` positions.
    Preserve case. Non-letter characters remain unchanged.
    Wrap around the alphabet (z + 1 = a).

    Example:
        caesar_cipher("Hello, World!", 3) → "Khoor, Zruog!"
        caesar_cipher("xyz", 3)           → "abc"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("text, shift, expected", [
    ("Hello, World!", 3,  "Khoor, Zruog!"),
    ("xyz",           3,  "abc"),
    ("ABC",           1,  "BCD"),
    ("Python",        0,  "Python"),
    ("Zen",           13, "Mra"),
])
def test_caesar_cipher(text, shift, expected):
    assert caesar_cipher(text, shift) == expected


# ─────────────────────────────────────────────
# KATA 7 — The Sentence Reverser
# ─────────────────────────────────────────────

def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.
    Strip leading/trailing whitespace first.
    Multiple spaces between words should become one.

    Example:
        reverse_words("the tao of python") → "python of tao the"
        reverse_words("  hello   world  ") → "world hello"
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("sentence, expected", [
    ("the tao of python",   "python of tao the"),
    ("  hello   world  ",   "world hello"),
    ("one",                 "one"),
    ("zen and flow",        "flow and zen"),
])
def test_reverse_words(sentence, expected):
    assert reverse_words(sentence) == expected
