def solve(n):
    """ sum multiples of three or five below a maximum """
    
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i

    return sum

if __name__ == "__main__":
    import sys
    max = 1000

    if len(sys.argv) > 1:
        max = int(sys.argv[1])

    print(solve(max))