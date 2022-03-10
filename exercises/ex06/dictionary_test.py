"""Test the funtions of EX06."""
__author__ = "730526118"


from dictionary import invert, count, favorite_color
import pytest


def test_invert_normal1() -> None:
    """Test the function invert in a normal use case."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_normal2() -> None:
    """Test invert on anthor use case."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_edge() -> None:
    """Test the edge case on function invert."""
    assert invert({}) == {}


with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_count_normal1() -> None:
    """Test count in a normal use case."""
    suppose: dict[str, int] = {"asd": 3, "123e": 2, "13": 1}
    assert count(["asd", "asd", "asd", "123e", "13", "123e"]) == suppose


def test_count_normal2() -> None:
    """Test count in the normal case 2."""
    assert count(["100", "1"]) == {"100": 1, "1": 1}


def test_count_edge() -> None:
    """Tese count in the edge case."""
    assert count([]) == {}


def test_favorite_color() -> None:
    """Test fn favorite color in normal case."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color2() -> None:
    """Test fn favorite color in normal case2."""
    assert favorite_color({"Marc": "yellow", "Ezri": "green", "Kris": "blue"}) == "yellow"


def test_favorite_edge() -> None:
    """Test fn favorite color in edge case."""
    assert favorite_color({"Marc": "", "Ezri": "", "Kris": ""}) == ""