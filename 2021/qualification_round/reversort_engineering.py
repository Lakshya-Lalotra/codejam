"""
T, N are small, just solve it by brute force
"""

from typing import List, Tuple


def parse_input() -> Tuple:
    n, c = [int(v) for v in input().split()]
    return n, c


def cost_break_down(n: int, c: int) -> List[int]:
    min_cost = n - 1
    max_cost = (n * (n + 1) / 2) - 1
    if (c < min_cost) or (c > max_cost):
        return list()

    sub_arr_size = n
    cost = c
    costs = list()
    while cost > 0:
        # choose value as aggressive as possible
        val = min(sub_arr_size, cost - (sub_arr_size - 2))
        cost -= val
        sub_arr_size -= 1
        costs.append(val)

    assert len(costs) == n - 1
    return costs


def solve(n: int, c: int) -> str:
    costs = cost_break_down(n, c)
    if len(costs) == 0:
        return "IMPOSSIBLE"

    array = [i + 1 for i in range(n)]
    start_ptr = n - 2
    while len(costs) > 0:
        step_cost = costs.pop()
        array[start_ptr: start_ptr + step_cost] = array[start_ptr: start_ptr + step_cost][::-1]
        start_ptr -= 1

    return " ".join(str(val + 1) for val in array)


"""
5
4 6
2 1
7 12
7 2
2 1000

1
100 4505

"""


if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {}".format(test_id, result))
