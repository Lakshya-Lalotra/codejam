"""
T, N are small, just solve it by brute force
"""

from typing import Tuple

INFINITY = 99999999


def parse_input() -> Tuple[int, int, str]:
    x, y, string = input().split()
    return int(x), int(y), string


def solve_with_non_negative_x_y(x: int, y: int, string: str) -> int:
    # observation: no matter how we fill '?'
    # pair of combining heading and trailing char must appear anyway
    string = string.replace("?", "")
    cost = 0
    cost_mapping = {
        "CC": 0,
        "JJ": 0,
        "CJ": x,
        "JC": y,
    }
    for i in range(len(string) - 1):
        cost += cost_mapping[string[i: i + 2]]

    return cost


def solve_with_general_x_y(x: int, y: int, string: str) -> int:
    cost_lookup = dict()
    first_char = string[0]
    if first_char == "C":
        cost_lookup.update({
            (0, "C"): 0,
            (0, "J"): INFINITY,
        })
    elif first_char == "J":
        cost_lookup.update({
            (0, "C"): INFINITY,
            (0, "J"): 0,
        })
    else:  # "?"
        cost_lookup.update({
            (0, "C"): 0,
            (0, "J"): 0,
        })

    for i in range(1, len(string)):
        previous_char, char = string[i - 1], string[i]
        if char == "C":
            cost_lookup.update({
                (i, "C"): min(
                    cost_lookup[(i - 1), "C"] + 0,
                    cost_lookup[(i - 1), "J"] + y,
                ),
                (i, "J"): INFINITY,
            })
        elif char == "J":
            cost_lookup.update({
                (i, "J"): min(
                    cost_lookup[(i - 1), "C"] + x,
                    cost_lookup[(i - 1), "J"] + 0,
                ),
                (i, "C"): INFINITY,
            })
        else:  # "?"
            cost_lookup.update({
                (i, "C"): min(
                    cost_lookup[(i - 1), "C"] + 0,
                    cost_lookup[(i - 1), "J"] + y,
                ),
                (i, "J"): min(
                    cost_lookup[(i - 1), "C"] + x,
                    cost_lookup[(i - 1), "J"] + 0,
                ),
            })

    final_pos = len(string) - 1
    return min(cost_lookup[(final_pos, "C")], cost_lookup[(final_pos, "J")])


def solve(x: int, y: int, string: str) -> int:
    return solve_with_general_x_y(x, y, string)


"""
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 5 ??J???

1
2 -5 ??JJ??

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {}".format(test_id, result))
