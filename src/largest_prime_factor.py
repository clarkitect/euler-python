import math

def solve(n):
    """ return greatest factor of n that is also prime """

    max = -1

    # iterate the number of 2s that divide n
    while n % 2 == 0:
        max = 2
        n >>= 1	 # equivalent to n /= 2

    # value of n can only be odd now; so we skip evens
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max = i
            n = n / i

    # special condition
    if n > 2:
        max = n

    return int(max)

if __name__ == "__main__":
    import sys
    max = 600851475143

    if len(sys.argv) > 1:
        max = int(sys.argv[1])

    print(solve(max))
