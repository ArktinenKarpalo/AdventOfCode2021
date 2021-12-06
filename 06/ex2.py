import sys
import collections
input = list(map(int, sys.stdin.read().split(",")))

fish = collections.defaultdict(int)
for x in input:
    fish[x] += 1
for _ in range(256):
    fish2 = collections.defaultdict(int)
    for x, cnt in fish.items():
        if x == 0:
            fish2[6] += cnt
            fish2[8] += cnt
        else:
            fish2[x-1] += cnt
    fish = fish2
print(sum(fish.values()))
