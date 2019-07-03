def fibonacci():
    """ yield fibonacci sequence to use as iterator """
    c, n = 0, 1
    while True:
        yield c
        c, n = n, c + n


def solve(n):
    """ sum even fibonacci numbers below a maximum """

    solution = 0
    for f in fibonacci():
        if f > n:
            break
        if f % 2 == 0:
            solution += f

    return solution


if __name__ == "__main__":
    import sys

    maximum = 4000000

    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    print(solve(maximum))
