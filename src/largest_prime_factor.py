import math


def solve(n):
    """ return greatest factor of n that is also prime """

    factor = -1

    # iterate the number of 2s that divide n
    while n % 2 == 0:
        factor = 2
        n >>= 1	 # equivalent to n /= 2

    # value of n can only be odd now; so we skip evens
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factor = i
            n = n / i

    # special condition
    if n > 2:
        factor = n

    return int(factor)


if __name__ == "__main__":
    import sys

    maximum = 600851475143

    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])

    print(solve(maximum))
