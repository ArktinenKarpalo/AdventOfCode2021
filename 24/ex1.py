import sys
import math
input = list(map(str.split, sys.stdin.read().strip().split("\n")))
for i in input:
    if len(i) == 3:
        try:
            i[2] = int(i[2])
        except:
            pass
lol = []
lk = 0
for i in input:
    if i[1] == 'z' and i[0] == 'div':
        lk += 5
    lol.append(lk)
lol.append(lk)
lol = lol[::-1]
vs = set()
def st(vr, nm, pt):
    if pt == len(input):
        if vr["z"] == 0:
            print(nm)
            exit(0)
        return
    if input[pt][0] == "inp":
        if vr["z"]>0:
            if (vr["z"] >> lol[pt]) > 1:
                return
        elif vr["z"] < 0:
            return
        for i in range(9, 0, -1):
            vr2 = dict(vr)
            vr2[input[pt][1]] = i
            st(vr2, nm*10+i,pt+1)
    elif input[pt][0] == "add":
        vr2 = dict(vr)
        opr2 = int(input[pt][2]) if isinstance(input[pt][2], int) else vr2[input[pt][2]]
        vr2[input[pt][1]] = vr2[input[pt][1]]+opr2
        st(vr2, nm,pt+1)
    elif input[pt][0] == "mul":
        vr2 = dict(vr)
        opr2 = int(input[pt][2]) if isinstance(input[pt][2], int) else vr2[input[pt][2]]
        vr2[input[pt][1]] = vr2[input[pt][1]]*opr2
        st(vr2, nm,pt+1)
    elif input[pt][0] == "div":
        vr2 = dict(vr)
        opr2 = int(input[pt][2]) if isinstance(input[pt][2], int) else vr2[input[pt][2]]
        assert opr2 != 0
        vr2[input[pt][1]] = int(vr2[input[pt][1]]/opr2)
        if (tuple(vr2.values()), pt) in vs:
            return
        vs.add((tuple(vr2.values()), pt))
        st(vr2, nm,pt+1)
    elif input[pt][0] == "mod":
        vr2 = dict(vr)
        opr2 = int(input[pt][2]) if isinstance(input[pt][2], int) else vr2[input[pt][2]]
        assert opr2 > 0
        assert vr2[input[pt][1]] >= 0
        vr2[input[pt][1]] = vr2[input[pt][1]]%opr2
        if (tuple(vr2.values()), pt) in vs:
            return
        vs.add((tuple(vr2.values()), pt))
        st(vr2, nm,pt+1)
    elif input[pt][0] == "eql":
        vr2 = dict(vr)
        opr2 = int(input[pt][2]) if isinstance(input[pt][2], int) else vr2[input[pt][2]]
        if vr2[input[pt][1]] == opr2:
            vr2[input[pt][1]] = 1
        else:
            vr2[input[pt][1]] = 0
        st(vr2, nm,pt+1)

st({"x": 0, "y": 0, "z": 0, "w": 0}, 0, 0)
print(ans)
