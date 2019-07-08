import itertools
import math


def is_palindrome(pair):
    """ true if the number is a palindrome """

    num = pair[0] * pair[1]
    stringed = str(num)

    if len(stringed) % 2 != 0:
        return False

    half = int(len(stringed) / 2)
    front, back = stringed[:half], stringed[half:]

    return front == back[::-1]


def solve(n):
    candidates = list(itertools.product(range(n, 0, -1), range(n, 0, -1)))
    palindromes = filter(is_palindrome, candidates)

    largest_pair = sorted(palindromes, key=lambda p: p[0] * p[1], reverse=True)[0]

    return largest_pair[0] * largest_pair[1]


if __name__ == "__main__":
    import sys

    maximum = 999

    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    # prevent subtle breakage
    # assert is_palindrome(9999) is True
    # assert is_palindrome(1234) is False
    # assert is_palindrome(12345) is False

    print(solve(maximum))
