import numpy as np


def no_newlines(val):
    return val is not '\n'


def row_segment(a, r, c, s):
    return a[r][c:c + s]


def col_segment(a, r, c, s):
    return a[:, c][r:r + s]


def south(a, r, c, s):
    return col_segment(a, r, c, s)


def east(a, r, c, s):
    return row_segment(a, r, c, s)


def southeast(a, r, c, s):
    weak = []
    for i in range(0, s, 1):
        weak.append(a[r + i][c + i])

    return weak


def solve(s, m):
    """ find the largest product of a series length S within matrix M  """
    print('series of {s} within a matrix of size {x}x{y}'.format(s=s, x=len(m), y=len(m[0])))

    matrix = np.array(m, np.int32)

    prods = []

    for row in matrix:
        for col in row:
            prods.append(np.prod(south(matrix, row, col, s)))
            prods.append(np.prod(east(matrix, row, col, s)))
            prods.append(np.prod(southeast(matrix, row, col, s)))

    return sorted(prods)[::-1][0]


def test_matrix(m):
    # middle point: 2, 2
    row, col, sz = 2, 2, 3

    r_south = south(m, row, col, sz)
    r_east = east(m, row, col, sz)
    r_southeast = southeast(m, row, col, sz)

    assert np.prod(r_south) == np.prod([8, 5, 8])
    assert np.prod(r_east) == np.prod([8, 6, 1])
    assert np.prod(r_southeast) == np.prod([8, 4, 6])


if __name__ == "__main__":
    f = open('largest-product-in-a-series.txt', 'r')
    input_lists = []

    for ln in f.readlines():
        input_lists.append(list(filter(no_newlines, list(ln))))

    print('found {ln} lines with {ll} digits per line'.format(ln=len(input_lists), ll=len(input_lists[0])))
    digits = len(input_lists) * len(input_lists[0])
    print('total elements: {dg}'.format(dg=digits))

    # size four: 5832
    # size thirteen: unknown
    size = 4
    import sys

    if len(sys.argv) is 2:
        size = sys.argv[1]

    assert solve(4, input_lists) is 5832

    print(solve(size, input_lists))
