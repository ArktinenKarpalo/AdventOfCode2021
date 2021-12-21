import collections
import itertools
pl1 = 4-1
pl2 = 10-1
sc1 = 0
sc2 = 0
die = 1
dr = 0
mp1 = collections.defaultdict(int)
mp1[(pl1, pl2, sc1, sc2)] = 1
pl1w = 0
pl2w = 0
while len(mp1) > 0:
    mp2 = collections.defaultdict(int)
    for x,v in mp1.items():
        for drr in itertools.product([1,2,3], repeat=3):
            if x[2]+((x[0]+sum(drr))%10)+1 >= 21:
                pl1w += v
            else:
                mp2[(((x[0]+sum(drr))%10), x[1], x[2]+((x[0]+sum(drr))%10)+1, x[3])] += v
    mp1 = mp2
    mp2 = collections.defaultdict(int)
    for x,v in mp1.items():
        for drr in itertools.product([1,2,3], repeat=3):
            if x[3]+((x[1]+sum(drr))%10)+1 >= 21:
                pl2w += v
            else:
                mp2[(x[0], (x[1]+sum(drr))%10, x[2], x[3]+((x[1]+sum(drr))%10)+1)] += v
    mp1 = mp2
print(max(pl1w, pl2w))
