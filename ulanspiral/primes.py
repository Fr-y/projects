def prim(szam):
    osztok = sum(szam % i == 0 for i in range(1, szam+1))
    return osztok == 2

def kiirprim():
    szam = int(input("Kérek egy pozitiv egész számot: "))
    for i in range(1, szam+1):
        if prim(i):
            print(i)

kiirprim()