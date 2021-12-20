import sys
import collections
enc, input = sys.stdin.read().strip().split("\n\n")
input = input.split("\n")
pxl = set()
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '#':
            pxl.add((i,j))
def chk(k,it):
    idx = 0
    cn = 8
    for i in range(-1, 1+1):
        for j in range(-1, 1+1):
            if it%2 == 0:
                if (k[0]+i, k[1]+j) in pxl:
                    idx |= (1<<(cn))
            else:
                if not (k[0]+i, k[1]+j) in pxl:
                    idx |= (1<<(cn))
            cn-=1
    return enc[idx]
for it in range(50):
    pxl2 = set()
    for k in pxl:
        for i in range(-1, 1+1):
            for j in range(-1, 1+1):
                if it%2 == 0:
                    if chk((k[0]+i, k[1]+j),it) == '.':
                        pxl2.add((k[0]+i, k[1]+j))
                else:
                    if chk((k[0]+i, k[1]+j),it) == '#':
                        pxl2.add((k[0]+i, k[1]+j))
    pxl = pxl2
print(len(pxl))
