
def fibonacci():
    """ yield fibonacci sequence to use as iterator """
    c,n = 0,1
    while True:
        yield c
        c, n = n, c + n

if __name__ == "__main__":
    import sys
    max = 4000000

    if len(sys.argv) > 1:
        max = int(sys.argv[1])

    solve(max)