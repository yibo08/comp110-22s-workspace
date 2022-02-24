"""Test the functionality of ex05."""
__author__ = "730526118"

from utils import only_evens, sub, concat


def test_only_evens_edge() -> None:
    """To test only_evens func in the case containing huge number, negative number, and zero."""
    given: list[int] = [1, 212312312312, 129380471290856, 7777, 0, -100, 12341234221231231234]
    suppose: list[int] = [212312312312, 129380471290856, 0, -100, 12341234221231231234]
    assert only_evens(given) == suppose


def test_only_evens_emptyset_edge() -> None:
    """To test only_evens func with the input of an empty set."""
    suppose: list[int] = list()
    assert only_evens([]) == suppose


def test_only_evens_commonuse1() -> None:
    """To test only_evens func in common use cases."""
    given: list[int] = [1, 2, 10, 44, 98945, 54478]
    suppose: list[int] = [2, 10, 44, 54478]
    assert only_evens(given) == suppose


def test_only_evens_use2() -> None:
    """Test fn only_evens in common use case2."""
    assert only_evens([4, 4, 4, 1, 2, 3, 1, 5, 3]) == [4, 4, 4, 2]


def test_sub_use1() -> None:
    """Test the common use of func sub."""
    given = [10, 20, 30, 40]
    assert sub(given, 1, 3) == [20, 30]


def test_sub_use2() -> None:
    """Second test of the common use of sub."""
    given = [0, 12, 123, 2134, 321, 100, -123]
    assert sub(given, 0, 5) == [0, 12, 123, 2134, 321]


def test_sub_edge1() -> None:
    """Edge test of func sub with first index is negtive and the second one exceeds the len of list."""
    given = [0, 12, 123, 2134, 321, 100, -123]
    assert sub(given, -100, 1000) == [0, 12, 123, 2134, 321, 100, -123]


def test_sub_edge2() -> None:
    """Edge test of func sub. given a empty list."""
    assert sub([], -100, 10123) == []


def test_sub_edge3() -> None:
    """Edge test of func sub, first index is larger than the len of list."""
    assert sub([1], 10, -1) == []


def test_concat_use1() -> None:
    """Test the common use of func concat."""
    list_1 = [1, 2, 3]
    list_2 = [9, 9, 1112312341234]
    assert concat(list_1, list_2) == [1, 2, 3, 9, 9, 1112312341234]


def test_concat_use2() -> None:
    """Second test of the common use of func concat."""
    assert concat([1], [-0]) == [1, -0]


def test_concat_edge() -> None:
    """Edge test of concat, given two empty sets."""
    assert concat([], []) == []


def test_concat_edge2() -> None:
    """Second edge test of concat, second set is empty."""
    assert concat([114514], []) == [114514]
