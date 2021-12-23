import sys
import re
input = sys.stdin.read().strip().split("\n")
sm = 0
cbd = []
for x in input:
    rs = re.match("(.*) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)", x).groups()
    rs = [rs[0]]+[int(x) for x in rs[1:]]
    cbd.append(rs)
def on(p, cb):
    if cb[1] <= p[0] and p[0] <= cb[2] and cb[3] <= p[1] and p[1] <= cb[4] and cb[5] <= p[2] and p[2] <= cb[6]:
            return True
    return False
for i in range(-50, 51):
    for j in range(-50, 51):
        for k in range(-50, 51):
            st = "off"
            for x in cbd:
                if x[0] != st and on((i,j,k), x):
                    st = x[0]
            if st == "on":
                sm += 1

print(sm)
