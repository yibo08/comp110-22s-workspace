"""EX05 - `list` Utility Functions."""
__author__ = "730526118"


def only_evens(ls_even: list[int]) -> list[int]:
    """Return a list containing only the elements of the input list that were even."""
    even_numbers: list[int] = list()
    for i in ls_even:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


def sub(ls_sub: list[int], start_i: int, end_i: int) -> list[int]:
    """Generate a subset of given list of ints with an start index and an end index(not inclusive)."""
    subset: list[int] = list()
    if start_i < 0:
        start_i = 0
    if end_i > len(ls_sub):
        end_i = len(ls_sub)
    if len(ls_sub) == 0 or start_i > len(ls_sub) or end_i <= 0:
        return subset
    while start_i < end_i:
        subset.append(ls_sub[start_i])
        start_i += 1
    return subset


def concat(frs_list: list[int], sec_list: list[int]) -> list[int]:
    """Generate a new list which contains all of the elements of the first list followed by all of the elements of the second list."""
    added_list: list[int] = frs_list
    for i in sec_list:
        added_list.append(i)
    return added_list
