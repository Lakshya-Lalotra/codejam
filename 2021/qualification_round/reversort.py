"""
T, N are small, just solve it by brute force
"""

from typing import List


def parse_input() -> List[int]:
    _ = int(input())
    arr = [int(v) for v in input().split()]
    return arr


def reversort(arr: List[int]) -> List[int]:
    return arr[::-1]


def get_min_loc(arr: List[int]) -> int:
    pos = 0
    min_so_far = 99999999
    for i in range(len(arr)):
        val = arr[i]
        if val < min_so_far:
            min_so_far = val
            pos = i

    return pos


def solve(arr: List[int]) -> int:
    work = 0

    for i in range(len(arr) - 1):
        j = get_min_loc(arr[i:]) + i
        work += (j - i + 1)
        arr[i:j + 1] = reversort(arr[i:j + 1])

    return work


"""
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1

1
7
7 6 2 3 4 5 1

1
100
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 84 83 82 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 65 63 61 59 57 55 53 51 49 47 45 43 41 39 37 35 33 31 29 27 25 23 21 19 17 15 13 11 9 7 5 3 1

"""


if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(parse_input())
        print("Case #{}: {}".format(test_id, result))
