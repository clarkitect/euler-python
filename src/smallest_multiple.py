def evenly_divisible(num, divisors):
    for divisor in divisors:
        if num % divisor != 0:
            return False

    return True


def solve(min_divisor, max_divisor):
    num, divisors = 1, range(min_divisor, max_divisor + 1)

    while not evenly_divisible(num, divisors):
        num = num + 1

    return num


if __name__ == "__main__":
    import sys

    lower_bound, upper_bound = 1, 20

    if len(sys.argv) == 3:
        lower_bound, upper_bound = sys.argv[1], sys.argv[2]

    print(solve(lower_bound, upper_bound))
