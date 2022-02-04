from math import sqrt



def method1():
    iteration = int(input()) +1
    print()

    # -- osszeg --
    o = 0

    for n in range(1, iteration):
        # -- tört --
        t = 1 / (n*n)
        o += t
    # -- pi --
    pi = sqrt(o * 6) 
    print(pi)

# Nilakantha's series 
def method2():
    iteration = int(input())

    pi = 3
    for n in range(1, iteration):
        # d = 4 / (pow(n, 3)- n)
        # d = 4 / ((n-1) * n * (n+1))
        d = 4 / ((2*n) * (2*n+1) * (2*n+2))

        if n % 2 == 0:
            pi -= d
        else:
            pi += d

    print(pi)




# -- hivas --
method1()
method2()