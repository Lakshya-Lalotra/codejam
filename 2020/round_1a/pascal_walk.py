import math
from typing import Tuple, Optional


def parse_input():
    return int(input())


NCR = dict()


def get_ncr(n, r):
    if r == 1 or r == n:
        return 1

    if (n, r) not in NCR:
        ret = get_ncr(n - 1, r - 1) + get_ncr(n - 1, r)
        NCR.update({(n, r): ret})

    return NCR[(n, r)]


class OrderedSet:
    def __init__(self):
        self.elements = set()
        self.order = list()

    def __contains__(self, item):
        return item in self.elements

    def append(self, item):
        self.elements.add(item)
        self.order.append(item)

    def pop(self):
        ret = self.order.pop()
        self.elements.discard(ret)
        return ret

    def __getitem__(self, item):
        return self.order[item]


def is_valid_pos(pos: Tuple[int, int]):
    n, r = pos
    return 1 <= r <= n


def find_valid_neighbours(current_pos: Tuple[int, int], walked_path: OrderedSet):
    n, r = current_pos
    neighbour_candidates = [
        (n - 1, r - 1), (n - 1, r),
        (n, r - 1), (n, r + 1),
        (n + 1, r), (n + 1, r + 1),
    ]
    neighbours = list()
    for neighbour in neighbour_candidates:
        # valid & not travelled
        if is_valid_pos(neighbour) and neighbour not in walked_path:
            neighbours.append(neighbour)

    # sorting is important!
    # it reduces number of wrong path finding due to current_sum << target_sum
    # TLE will be raised if we don't sort the neighbours
    return sorted(neighbours, key=lambda pos: get_ncr(*pos), reverse=True)


def dfs(current_sum: int, current_path: OrderedSet, target_sum: int, ttl: int) -> Optional[OrderedSet]:
    if ttl == 0:
        return None

    if current_sum > target_sum:
        return None

    if current_sum == target_sum:
        return current_path

    # still finding
    current_pos = current_path[-1]
    for neighbour in find_valid_neighbours(current_pos, current_path):
        current_path.append(neighbour)
        ret = dfs(
            current_sum + get_ncr(*neighbour),
            current_path,
            target_sum,
            ttl - 1
        )
        if ret is None:
            # remove newly added neighbour if no solution is found
            current_path.pop()
        else:
            return current_path
    else:
        return None


def solve(n: int):
    path = OrderedSet()
    path.append((1, 1))
    current_sum = 1
    ans = dfs(
        current_sum,
        path,
        n,
        500,
    )
    return ans


"""
3
1
4
19

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        answer = solve(parse_input())
        print("Case #{}:".format(test_id))
        s = 0
        for pos_i, pos_j in answer.order:
            s += get_ncr(pos_i, pos_j)
            print(pos_i, pos_j)
