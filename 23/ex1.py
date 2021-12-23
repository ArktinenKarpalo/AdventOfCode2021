import sys
import queue
input = sys.stdin.read().strip().split("\n")
input = [list(x) for x in input]

def ok(ip):
    for i in range(4):
        for j in range(2):
            if ip[2+j][3+i*2] != chr(ord("A")+i):
                return False
    return True
ans = 1e9

def ps(ip, i, j):
    q = queue.Queue()
    q.put(((i+1,j), 1))
    q.put(((i,j+1), 1))
    q.put(((i-1,j), 1))
    q.put(((i,j-1), 1))
    vis = set()
    while not q.empty():
        e, cst = q.get()
        i, j = e
        if e in vis or ip[i][j] != '.':
            continue
        yield((i,j), cst)
        vis.add(e)
        q.put(((i+1,j), cst+1))
        q.put(((i,j+1), cst+1))
        q.put(((i-1,j), cst+1))
        q.put(((i,j-1), cst+1))

def valid(ip, i, j, ch):
    if i > 1:
        if j == 3 and ch != 'A':
            return False
        if j == 5 and ch != 'B':
            return False
        if j == 7 and ch != 'C':
            return False
        if j == 9 and ch != 'D':
            return False
        ##
        i2 = i+1
        while True:
            if ip[i2][j] == '#':
                return True
            if j == 3 and ip[i2][j] != 'A':
                return False
            if j == 5 and ip[i2][j] != 'B':
                return False
            if j == 7 and ip[i2][j] != 'C':
                return False
            if j == 9 and ip[i2][j] != 'D':
                return False
            i2 += 1
        return True
    if j in [3, 5, 7, 9]:
        return False
    return True
def valid2(ip, i, j, ch):
    if i > 1:
        i2 = i
        while True:
            if ip[i2][j] == '#':
                return False
            if j == 3 and ip[i2][j] != 'A':
                return True
            if j == 5 and ip[i2][j] != 'B':
                return True
            if j == 7 and ip[i2][j] != 'C':
                return True
            if j == 9 and ip[i2][j] != 'D':
                return True
            i2 += 1
    return True

atm = {}
def hk(ip, cst):
    global atm
    global ans
    if ok(ip):
        if cst < ans:
            print(len(atm))
            print(f"{ans} -> {cst}")
            ans = cst
    st = []
    for i in ip:
        st.append("".join(i))
    st = "".join(st)
    if st in atm and atm[st] <= cst:
        return
    atm[st] = cst
    for i in range(len(input)):
        for j in range(len(input[i])):
            if ord("A") <= ord(ip[i][j]) and ord(ip[i][j]) <= ord("D"):
                if not valid2(ip, i, j, ip[i][j]):
                    continue
                for x in filter(lambda x: valid(ip, x[0][0], x[0][1], ip[i][j]), ps(ip, i, j)):
                    if x[0][0] == 1 and i == 1:
                       continue
                    nc = x[1]*pow(10, ord(ip[i][j])-ord("A"))
                    ip2 = []
                    for z in ip:
                        ip2.append(list(z))
                    ip2[x[0][0]][x[0][1]] = ip[i][j]
                    ip2[i][j] = "."
                    hk(ip2, cst+nc)




hk(input, 0)
print(ans)
