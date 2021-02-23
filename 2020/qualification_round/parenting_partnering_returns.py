from typing import List, Tuple


def parse_input():
    num_of_activities = int(input())
    activities = list()
    for _ in range(num_of_activities):
        activities.append(
            tuple(int(_) for _ in input().split())
        )
    return num_of_activities, activities


class Parent:
    def __init__(self):
        self.time_slots: List[Tuple[int, int]] = list()

    def is_available(self, slot: Tuple[int, int]) -> bool:
        # edge case: empty slots
        if len(self.time_slots) == 0:
            return True

        last_activity = self.time_slots[-1]
        # activity start after the last activity end
        return slot[0] >= last_activity[1]

    def assign(self, slot: Tuple[int, int]):
        self.time_slots.append(slot)


def solve(num_of_activities: int, activities: List[Tuple[int, int]]):
    # sort activities by START time
    enum_activities: List[Tuple[int, Tuple[int, int]]] = sorted(
        enumerate(activities),
        key=lambda t: t[1][0]
    )

    # assign tasks
    cameron = Parent()
    jamie = Parent()
    assignee = ['' for _ in range(num_of_activities)]
    for activity_id, activity in enum_activities:
        if cameron.is_available(activity):
            cameron.assign(activity)
            assignee[activity_id] = 'C'
        elif jamie.is_available(activity):
            jamie.assign(activity)
            assignee[activity_id] = 'J'
        else:
            return "IMPOSSIBLE"

    return ''.join(assignee)


"""
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {}".format(test_id, result))
