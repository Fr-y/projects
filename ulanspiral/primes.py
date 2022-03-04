def prim(szam):
    osztok = 0
    for i in range(1, szam+1):
        if szam % i == 0:
            osztok += 1
    if osztok == 2:
        return True
    else:
        return False

def kiirprim():
    szam = int(input("Kérek egy pozitiv egész számot: "))
    for i in range(1, szam+1):
        if prim(i):
            print(i)

kiirprim()