"""
Chapter 2 Katas — The Many and the One

Lists, tuples, sets, and dictionaries.

HOW TO RUN THESE KATAS:
    From your terminal, navigate to the katas/ folder:

        cd path/to/Python-From-The-Void/katas
        pytest chapter_02_katas.py -v

    A test marked PASSED means your implementation is correct.
    A test marked FAILED means your function needs work.

YOUR MISSION:
    Implement each function below so that all 7 tests pass.
    Do not modify the test functions — only implement the functions above them.
"""

import pytest


# ─────────────────────────────────────────────
# KATA 1 — The Filter
# ─────────────────────────────────────────────

def get_even_numbers(numbers: list) -> list:
    """
    Return a new list containing only the even numbers from the input list.
    Use a list comprehension.

    Example:
        get_even_numbers([1, 2, 3, 4, 5, 6]) → [2, 4, 6]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5, 6],   [2, 4, 6]),
    ([1, 3, 5],            []),
    ([2, 4, 6],            [2, 4, 6]),
    ([],                   []),
    ([0, -2, 7, 10],       [0, -2, 10]),
])
def test_get_even_numbers(numbers, expected):
    assert get_even_numbers(numbers) == expected


# ─────────────────────────────────────────────
# KATA 2 — The Deduplifier
# ─────────────────────────────────────────────

def remove_duplicates(items: list) -> list:
    """
    Return a list with duplicates removed, preserving original order.

    Example:
        remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5]) → [3, 1, 4, 5, 9, 2, 6]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("items, expected", [
    ([3, 1, 4, 1, 5, 9, 2, 6, 5],        [3, 1, 4, 5, 9, 2, 6]),
    (["a", "b", "a", "c"],               ["a", "b", "c"]),
    ([1, 2, 3],                          [1, 2, 3]),
    ([],                                 []),
    ([7, 7, 7, 7],                       [7]),
])
def test_remove_duplicates(items, expected):
    assert remove_duplicates(items) == expected


# ─────────────────────────────────────────────
# KATA 3 — The Roster
# ─────────────────────────────────────────────

def build_player_profile(name: str, position: str, batting_avg: float) -> dict:
    """
    Build and return a player profile dictionary with keys:
    "name", "position", "batting_avg", and "grade".

    Grade rules:
        batting_avg >= 0.300  → "elite"
        batting_avg >= 0.250  → "solid"
        otherwise             → "developing"

    Example:
        build_player_profile("Cosmos", "pitcher", 0.342)
        → {"name": "Cosmos", "position": "pitcher", "batting_avg": 0.342, "grade": "elite"}
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("name, position, avg, expected_grade", [
    ("Cosmos", "pitcher",   0.342, "elite"),
    ("Miguel", "catcher",   0.275, "solid"),
    ("Luis",   "shortstop", 0.198, "developing"),
    ("Ana",    "outfield",  0.300, "elite"),
    ("Pedro",  "infield",   0.249, "developing"),
])
def test_build_player_profile(name, position, avg, expected_grade):
    profile = build_player_profile(name, position, avg)
    assert profile["name"] == name
    assert profile["position"] == position
    assert profile["batting_avg"] == avg
    assert profile["grade"] == expected_grade


# ─────────────────────────────────────────────
# KATA 4 — The Intersection
# ─────────────────────────────────────────────

def find_common_elements(list_a: list, list_b: list) -> list:
    """
    Return a sorted list of elements that appear in BOTH lists.
    No duplicates in the result.

    Use set operations.

    Example:
        find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]) → [3, 4]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3, 4],    [3, 4, 5, 6],       [3, 4]),
    (["a", "b", "c"], ["b", "c", "d"],    ["b", "c"]),
    ([1, 2, 3],       [4, 5, 6],          []),
    ([1, 1, 2, 2],    [2, 2, 3, 3],       [2]),
    ([],              [1, 2, 3],          []),
])
def test_find_common_elements(a, b, expected):
    assert find_common_elements(a, b) == expected


# ─────────────────────────────────────────────
# KATA 5 — The Inverter
# ─────────────────────────────────────────────

def invert_dictionary(original: dict) -> dict:
    """
    Return a new dictionary where keys and values are swapped.
    Assumes all values in the original are unique and hashable.

    Example:
        invert_dictionary({"a": 1, "b": 2, "c": 3}) → {1: "a", 2: "b", 3: "c"}
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("original, expected", [
    ({"a": 1, "b": 2, "c": 3},          {1: "a", 2: "b", 3: "c"}),
    ({"name": "cosmos", "age": 25},     {"cosmos": "name", 25: "age"}),
    ({},                                {}),
    ({"only": "one"},                   {"one": "only"}),
])
def test_invert_dictionary(original, expected):
    assert invert_dictionary(original) == expected


# ─────────────────────────────────────────────
# KATA 6 — The Sorter
# ─────────────────────────────────────────────

def sort_players_by_average(players: list) -> list:
    """
    Given a list of player dicts (each with "name" and "batting_avg"),
    return the list sorted by "batting_avg" in DESCENDING order (best first).

    Example:
        players = [
            {"name": "Luis", "batting_avg": 0.198},
            {"name": "Cosmos", "batting_avg": 0.342},
        ]
        sort_players_by_average(players)
        → [{"name": "Cosmos", ...}, {"name": "Luis", ...}]
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("players, expected_order", [
    (
        [{"name": "Luis", "batting_avg": 0.198},
         {"name": "Cosmos", "batting_avg": 0.342},
         {"name": "Miguel", "batting_avg": 0.275}],
        ["Cosmos", "Miguel", "Luis"]
    ),
    (
        [{"name": "A", "batting_avg": 0.1},
         {"name": "B", "batting_avg": 0.3}],
        ["B", "A"]
    ),
    (
        [{"name": "Solo", "batting_avg": 0.5}],
        ["Solo"]
    ),
])
def test_sort_players_by_average(players, expected_order):
    sorted_players = sort_players_by_average(players)
    assert [p["name"] for p in sorted_players] == expected_order


# ─────────────────────────────────────────────
# KATA 7 — The Unpacker
# ─────────────────────────────────────────────

def unpack_coordinates(points: list) -> tuple:
    """
    Given a list of (x, y) tuples, return a tuple of two lists:
    the first containing all x values, the second all y values.

    Use tuple unpacking.

    Example:
        unpack_coordinates([(1, 2), (3, 4), (5, 6)])
        → ([1, 3, 5], [2, 4, 6])
    """
    # YOUR CODE HERE
    pass


@pytest.mark.parametrize("points, expected", [
    ([(1, 2), (3, 4), (5, 6)],    ([1, 3, 5], [2, 4, 6])),
    ([(0, 0), (1, 1)],             ([0, 1], [0, 1])),
    ([(10, -10)],                  ([10], [-10])),
    ([],                           ([], [])),
])
def test_unpack_coordinates(points, expected):
    xs, ys = unpack_coordinates(points)
    assert xs == expected[0]
    assert ys == expected[1]
