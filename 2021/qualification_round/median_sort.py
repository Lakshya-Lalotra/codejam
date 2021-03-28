import logging
from typing import List

logging.basicConfig(filename="example.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_median(i, j, k) -> int:
    print(i + 1, j + 1, k + 1)
    med = int(input()) - 1
    if med == -2:
        raise ValueError
    else:
        return med


def get_proper_location(x_i: int, arr: List[int]) -> int:
    # 3-ary search inside array
    left_end_ptr, left_ptr, right_ptr, right_end_ptr = (
        0,
        (len(arr) - 1) // 3,
        2 * (len(arr) - 1) // 3,
        len(arr) - 1,
    )

    while (right_end_ptr - left_end_ptr) > 1:
        x_left, x_right = arr[left_ptr], arr[right_ptr]
        median = get_median(x_left, x_i, x_right)

        if median == x_right:
            left_end_ptr = right_ptr
        elif median not in [x_left, x_right]:  # mid
            left_end_ptr = left_ptr
            right_end_ptr = right_ptr
        else:
            right_end_ptr = left_ptr

        left_ptr = left_end_ptr + (right_end_ptr - left_end_ptr) // 3
        right_ptr = left_end_ptr + 2 * (right_end_ptr - left_end_ptr) // 3

    if (right_end_ptr - left_end_ptr) == 0:
        return right_end_ptr

    if (right_end_ptr - left_end_ptr) == 1:
        x_left_end, x_right_end = arr[left_end_ptr], arr[right_end_ptr]
        if (left_end_ptr == 0) or (right_end_ptr == len(arr) - 1):
            median = get_median(x_left_end, x_i, x_right_end)

            if median == x_right_end:
                return right_end_ptr + 1
            elif median == x_left_end:
                return left_end_ptr
            else:
                return right_end_ptr
        else:
            return right_end_ptr


def solve(n: int, q: int):
    # init
    median = get_median(0, 1, 2)
    non_median_candidates = {0, 1, 2} - {median}
    arr = list(non_median_candidates)
    arr.insert(1, median)

    # locate value one by one
    for i in range(3, n):
        pos = get_proper_location(i, arr)
        arr.insert(pos, i)

    return " ".join(str(val + 1) for val in arr)


if __name__ == "__main__":
    num_of_test_cases, num_of_elements, num_of_queries = [int(val) for val in input().split()]
    for test_id in range(1, num_of_test_cases + 1):
        ret = solve(num_of_elements, num_of_queries)
        # test
        print(ret)
        verdict = int(input())
        if verdict == 1:
            continue
        else:
            raise ValueError
