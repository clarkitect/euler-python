def solve(largest_natural):
    naturals = range(1, largest_natural + 1)

    squares = map(lambda n: n ** 2, naturals)

    sum_of_squares = sum(squares)
    square_of_sum = sum(naturals) ** 2
    difference = int(square_of_sum - sum_of_squares)

    # print('{sq_su} - {su_sq} = {df}'.format(sq_su=square_of_sum, su_sq=sum_of_squares, df=difference))

    return difference


if __name__ == "__main__":
    import sys

    upper_bound = 100

    if not len(sys.argv) == 1:
        upper_bound = sys.argv[1]

    print(solve(upper_bound))
