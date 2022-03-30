"""Dictionary related utility functions."""

__author__ = "730526118"

# Define your functions below


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        n_values: list[str] = []
        table_ls: list[str] = table[column]
        if number >= len(table_ls):
            result[column] = table_ls
        else:
            i = 0
            while i < number:
                item = table_ls[i]
                n_values.append(item)
                i += 1
            result[column] = n_values
    return result


def select(table: dict[str, list[str]], copy_column: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset."""
    result: dict[str, list[str]] = {}
    for column in copy_column:
        result[column] = table[column]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concat two column-based tables into one."""
    result: dict[str, list[str]] = {}
    for column in table_1:
        result[column] = table_1[column]
    for column in table_2:
        if column in result:
            for items in table_2[column]:
                result[column].append(items)
        else:
            result[column] = table_2[column]
    return result


def count(ls: list[str]) -> dict[str, int]:
    """Count the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in ls:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result