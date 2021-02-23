# Both T and S are small, just do it with brute force


def parse_input():
    return input()


def solve(string: str):
    mapping = {
        "0": "0",
        "1": "(1)",
        "2": "((2))",
        "3": "(((3)))",
        "4": "((((4))))",
        "5": "(((((5)))))",
        "6": "((((((6))))))",
        "7": "(((((((7)))))))",
        "8": "((((((((8))))))))",
        "9": "(((((((((9)))))))))",
    }
    for k, v in mapping.items():
        string = string.replace(k, v)

    # then remove unnecessary parenthesis
    for _ in range(9):
        string = string.replace(")(", "")

    return string



"""
4
0000
101
111000
1

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(parse_input())
        print("Case #{}: {}".format(test_id, result))
