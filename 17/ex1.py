tx = [29, 73]
ty = [-248,-194]
def chek(vx, vy):
    x = 0
    y = 0
    mx = y
    while x <= tx[1] and y >= ty[0]:
        x += vx
        y += vy
        mx = max(y, mx)
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if x <= tx[1] and x >= tx[0] and y <= ty[1] and y >= ty[0]:
            return (True, mx)
    return (False, 0)
ans = 0
for i in range(1000):
    for j in range(1000):
        res = chek(i, j)
        if res[0]:
            ans = max(ans, res[1])
print(ans)
