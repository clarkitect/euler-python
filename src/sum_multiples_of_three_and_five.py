def solve(n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i

    print(sum)

if __name__ == "__main__":
    import sys
    max = int(sys.argv[1] or 1000)
    "solving for {max}".format(max=max)
    solve(max)