from collections import deque
from typing import List


def parse_input():
    n = int(input())
    patterns = [input() for _ in range(n)]
    return n, patterns


class ImpossibleError(BaseException):
    pass


def split_pattern(pattern: str) -> List[str]:
    sub_patterns = pattern.split("*")
    first = sub_patterns[0]
    last = sub_patterns[-1]
    mid = "".join(sub_patterns[1:-1])
    return [first, mid, last]


def find_string(target_patterns: List[str]) -> str:
    # ignore empty pattern because it matches with any string
    target_patterns = [p for p in target_patterns if p != ""]

    if len(target_patterns) == 0:
        return ""

    longest_pattern = max(target_patterns, key=len)
    for pattern in target_patterns:
        if longest_pattern[:len(pattern)] != pattern:
            raise ImpossibleError()

    return longest_pattern


def solve(n: int, patterns: List[str]):
    # count max number of stars
    max_stars = 0
    for pattern in patterns:
        max_stars = max(max_stars, pattern.count("*"))

    # split patterns
    first_patterns = list()
    mid_patterns = list()
    last_patterns = list()
    for pattern in patterns:
        f, m, l = split_pattern(pattern)
        first_patterns.append(f)
        mid_patterns.append(m)
        last_patterns.append(l)

    # process "XXXX*" patterns
    first_string = find_string(first_patterns)

    # process "*XXXXX*" patterns
    mid_string = "".join(mid_patterns)

    # process "*XXXXX" patterns
    last_string = find_string(
        [p[::-1] for p in last_patterns]
    )[::-1]

    return "".join([first_string, mid_string, last_string])


"""
2
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ

"""

"""
3
4
H*O
HELLO*
*HELLO
HE*
2
CO*DE
J*AM
2
CODE*
*JAM

"""

"""
3
2
A*C*E
*B*D*
2
A*C*E
*B*D
2
**Q**
*A*

"""


if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        try:
            result = solve(*parse_input())
        except ImpossibleError:
            result = "*"
        print("Case #{}: {}".format(test_id, result))

