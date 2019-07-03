import math


def prime_check(subject):
    """ test a subject for prime """
    if subject % 2 == 0 and subject > 2:
        return False

    return all(subject % i for i in range(3, int(math.sqrt(subject)) + 1, 2))


def solve(n):
    """ determine the Nth prime """

    found, num = 0, 1

    while found < n:
        num = num + 1
        if prime_check(num) and found < n:
            found = found + 1

    return num


if __name__ == "__main__":
    import sys

    upper_bound = 10001

    if not len(sys.argv) == 1:
        upper_bound = sys.argv[1]

    print(solve(upper_bound))
