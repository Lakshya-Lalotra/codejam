from typing import List, Tuple, Dict


def parse_input() -> Tuple[int, int, List[List[int]]]:
    r, c = [int(_) for _ in input().split()]
    skills = [
        [int(s) for s in input().split()]
        for _ in range(r)
    ]
    return r, c, skills


class Player:
    _players: Dict[Tuple[int, int], "Player"] = dict()

    def __init__(self, i: int, j: int, skill: int):
        self.loc = (i, j)
        self.skill = skill
        self.is_alive = True
        self.w = None
        self.a = None
        self.s = None
        self.d = None

        self._players[(i, j)] = self

    def is_eliminated(self) -> bool:
        neighbour_skills = [p.skill for p in [self.w, self.a, self.s, self.d] if p is not None]
        length = len(neighbour_skills)
        if length == 0:
            return False
        else:
            avg_level = sum(neighbour_skills) / length
            return self.skill < avg_level

    @classmethod
    def from_loc(cls, i: int, j: int) -> "Player":
        return cls._players.get((i, j), None)

    @classmethod
    def init_linkage(cls, r: int, c: int):
        for i in range(r):
            for j in range(c):
                player = cls.from_loc(i, j)
                player.w = cls.from_loc(i - 1, j)
                player.a = cls.from_loc(i, j - 1)
                player.s = cls.from_loc(i + 1, j)
                player.d = cls.from_loc(i, j + 1)

    @classmethod
    def current_interest_level(cls) -> int:
        interest_level = 0
        for player in cls._players.values():
            if player.is_alive:
                interest_level += player.skill
        return interest_level

    @classmethod
    def cleanup(cls):
        cls._players = dict()


# It works except a constant factor to get all tests passed.
# (Compared with optimized version, there is a constant difference `~1.3x`)
# I will leave it as it is, further optimization will decrease readability significantly.
def solve(r: int, c: int, skills: List[List[int]]):
    # init
    Player.cleanup()
    for i in range(r):
        for j in range(c):
            Player(i, j, skills[i][j])
    Player.init_linkage(r, c)
    interest_level = 0

    # start
    proceed_to_next_round = True
    affected_candidates = [Player.from_loc(i, j) for i in range(r) for j in range(c)]
    while proceed_to_next_round:
        interest_level += Player.current_interest_level()

        # check if player is eliminated
        affected_candidates_in_next_stage: Dict[Tuple[int, int], Player] = dict()
        eliminated_players: List[Player] = list()
        for player in affected_candidates:
            if player.is_eliminated():
                eliminated_players.append(player)

        # update eliminated players
        for player in eliminated_players:
            player.is_alive = 0
            # update its neighbour
            if player.w:
                player.w.s = player.s
                affected_candidates_in_next_stage.update({
                    player.w.loc: player.w
                })
            if player.s:
                player.s.w = player.w
                affected_candidates_in_next_stage.update({
                    player.s.loc: player.s
                })
            if player.a:
                player.a.d = player.d
                affected_candidates_in_next_stage.update({
                    player.a.loc: player.a
                })
            if player.d:
                player.d.a = player.a
                affected_candidates_in_next_stage.update({
                    player.d.loc: player.d
                })

        # loop condition
        proceed_to_next_round = len(eliminated_players) > 0
        affected_candidates = [p for p in affected_candidates_in_next_stage.values() if p.is_alive]

    return interest_level


def gen_large_input():
    import numpy as np
    arr = np.random.randint(0, 100, size=(1000, 1000))
    with open("../../large_input.txt", "w+") as f:
        f.write("1\n")
        f.write("1000 1000\n")
        for line in arr:
            f.write(" ".join(str(val) for val in line))
            f.write("\n")


"""
4
1 1
15
3 3
1 1 1
1 2 1
1 1 1
1 3
3 1 2
1 3
1 2 3

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {}".format(test_id, result))
