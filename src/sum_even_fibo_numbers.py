def fibonacci():
    """ yield fibonacci sequence to use as iterator """
    c,n = 0,1
    while True:
        yield c
        c, n = n, c + n

def solve(max):
    """ sum even fibonacci numbers below a maximum """

    sum = 0    
    for n in fibonacci():
        if n > max:
            break
        if n % 2 == 0:
            sum += n
    
    return sum

if __name__ == "__main__":
    import sys
    max = 4000000

    if len(sys.argv) > 1:
        max = int(sys.argv[1])

    print(solve(max))