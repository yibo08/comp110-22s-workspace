"""EX06 - Dictionary Functions."""
__author__ = "730526118"


def invert(input_dic: dict[str, str]) -> dict[str, str]:
    """Return a dict[str, str] that inverts the key and value of input dict."""
    output_dic: dict[str, str] = {}
    for key in input_dic:
        for key_check in input_dic:
            if input_dic[key] == input_dic[key_check] and key_check != key:
                raise KeyError
        output_dic[input_dic[key]] = key
    return output_dic


def count(ls: list[str]) -> dict[str, int]:
    """Count the number of occurrences of each different element in the given list."""
    result: dict[str, int] = {}
    for item in ls:
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1
    return result


def favorite_color(dic: dict[str, str]) -> str:
    """Returns the color that occurs most often."""
    color_ls: list[str] = list()
    for key in dic:
        color_ls.append(dic[key])
    number_color: dict[str, int] = count(color_ls)
    number: list[int] = list()
    for keys in number_color:
        number.append(number_color[keys])
    maxnum: int = max(number)
    for ky in number_color:
        if number_color[ky] == maxnum:
            return ky
    return ""