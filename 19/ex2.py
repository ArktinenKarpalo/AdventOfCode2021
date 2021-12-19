import sys
import copy
import itertools
input = list(map(lambda x: [list(map(int, y.split(","))) for y in x.split("\n")[1:]], sys.stdin.read().strip().split("\n\n")))
ans = set()
def roll(v):
	return (v[0],v[2],-v[1])
def turn(v):
	return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):
            v = roll(v)
            yield(v)
            for i in range(3):
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))

QAQ = list(sequence((1,2,3)))

locs = []
def ok(bc1, bcc2):
    for ori in QAQ:
        bc2 = set()
        for x in range(3):
            abs(ori[x])-1
        for i in range(len(bcc2)):
            bc2.add(tuple(bcc2[i][abs(ori[x])-1]*(ori[x]/abs(ori[x])) for x in range(3)))
        for lel in bc1:
            for k in bc2:
                ofs = [0, 0, 0]
                for q in range(3):
                    ofs[q] = k[q]-lel[q]
                ob = 0
                for i in bc1:
                    q = (i[0]+ofs[0], i[1]+ofs[1], i[2]+ofs[2])
                    if q not in bc2:
                        continue
                    ob += 1
                if ob >= 12:
                    locs.append(ofs)
                    return [[x[xx]-ofs[xx] for xx in range(3)] for x in bc2]
    return None
mg = {}
def hak(i):
    for j in range(len(input)):
        if j in mg:
            continue
        res = ok(input[i], input[j])
        if res is not None:
            print(f"OK {i} {j}")
            for x in res:
                ans.add(tuple(x))
            mg[j] = res
            input[j] = res
            hak(j)
init = 0
for x in input[init]:
    ans.add(tuple(x))
mg[init] = [[0,1,2], [1,1,1]]
hak(init)
print(mg)
print(len(ans))
ans2 = 0
for i in locs:
    for j in locs:
        ans2 = max(ans2, sum(abs(i[x]-j[x]) for x in range(3)))
print(ans2)
