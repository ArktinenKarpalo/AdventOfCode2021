pl1 = 4-1
pl2 = 10-1
sc1 = 0
sc2 = 0
die = 1
dr = 0
for _ in range(1000000):
    for _ in range(3):
        pl1 += die
        die %= 100
        die += 1
        dr += 1
    pl1 = pl1%10
    sc1 += pl1+1
    if sc1 >= 1000:
        print(sc2*dr)
        exit(0)
    for _ in range(3):
        pl2 += die
        die %= 100
        die += 1
        dr += 1
    pl2 = pl2%10
    sc2 += pl2+1
    if sc2 >= 1000:
        print(sc1*dr)
        exit(0)

