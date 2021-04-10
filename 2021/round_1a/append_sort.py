from typing import List, Tuple


def parse_input() -> Tuple[int, List[str]]:
    n = int(input())
    xs = [x for x in input().split()]
    return n, xs


def is_strictly_increasing(previous: str, current: str) -> bool:
    # strictly increasing order
    return int(previous) < int(current)


def add_one(s: str) -> str:
    i = int(s) + 1
    target = str(i).zfill(len(s))

    # advanced?
    if len(s) == len(target):
        return target
    else:
        return "OVERFLOW"


def append(previous: str, current: str) -> Tuple[str, int]:
    previous_len = len(previous)
    current_len = len(current)

    if previous_len == current_len:  # append 1 trailing zero will work
        return current + "0", 1

    elif previous_len > current_len:
        is_prefix_bigger = None
        for i in range(current_len):
            if previous[i] == current[i]:
                continue
            elif previous[i] > current[i]:
                is_prefix_bigger = False
                break
            else:
                is_prefix_bigger = True
                break

        if is_prefix_bigger is True:
            num_of_zeros = previous_len - current_len
            return current + "0" * num_of_zeros, num_of_zeros
        elif is_prefix_bigger is False:
            num_of_zeros = previous_len - current_len + 1
            return current + "0" * num_of_zeros, num_of_zeros
        else:
            assert is_prefix_bigger is None
            trailing_str = add_one(previous[current_len:])
            if trailing_str == "OVERFLOW":
                added_char = previous_len - current_len + 1
                return current + "0" * added_char, added_char
            else:
                return current + trailing_str, len(trailing_str)

    else:
        # cannot reach this block
        raise AssertionError


def solve(n: int, xs: List[str]) -> int:
    total_append = 0
    new_xs = list()
    current = "0"
    for x in xs:
        if is_strictly_increasing(current, x):
            current = x
        else:
            new_x, len_of_appended_char = append(current, x)
            # print("current:", current, "x:", x, "new_x:", new_x)
            current = new_x
            total_append += len_of_appended_char
        new_xs.append(current)

    # print(new_xs)
    return total_append


"""
4
3
100 7 10
2
10 10
3
4 19 1
3
1 2 3

1
3
9999 99 9

1
12
9 9 9 9 9 9 9 9 9 9 9 9

3
2
12745 1294
2
12745 1264
6
12745 1274 1274 1274 1274 1275

1
0
7 6 4 5 8 8 8

1
0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {}".format(test_id, result))
