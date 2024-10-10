def ppolsol(l):

    def prime(n):

        def isprime(m):
            for _ in range(2, floor(sqrt(m)) + 1):
                if m % _ == 0:
                    return False
            return True

        a = 0
        c = 2
        while True:
            if isprime(c):
                a += 1
            if a == n:
                return c
            c += 1

    a = 0
    for _ in range(len(l)):
        if _ == 0:
            a -= prime(l[0] + 1)
        else:
            a += prime(l[_] + 1)*x**_
    return [*filter(lambda a:a.is_positive, [N(_) for _ in solve(a)])][0]

def get_bit(num):
    return ("00000000" + bin(int(str(num).split(".")[1]))[2:])[-8:]