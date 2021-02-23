# Both T and N are small, just loop the matrix row by row, column by column.


def parse_input():
    n = int(input())
    matrix = list()
    for _ in range(n):
        matrix.append(
            [int(e) for e in input().split()]
        )
    return n, matrix


def solve(n, matrix):
    k, r, c = (0, 0, 0)

    # trace
    for i in range(n):
        k += matrix[i][i]

    # row
    for row in matrix:
        if len(set(row)) < n:
            r += 1

    # column
    for col_id in range(n):
        col_elements = set()
        for row_id in range(n):
            col_elements.add(matrix[row_id][col_id])

        if len(col_elements) < n:
            c += 1

    return k, r, c


"""
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

"""

if __name__ == "__main__":
    num_of_test_cases = int(input())
    for test_id in range(1, num_of_test_cases + 1):
        result = solve(*parse_input())
        print("Case #{}: {} {} {}".format(test_id, *result))
