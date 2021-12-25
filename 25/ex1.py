import sys
input = sys.stdin.read().strip().split("\n")
sc = {}
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != '.':
            sc[(j,i)] = input[i][j]
for stp in range(1,10000000):
    mv = False
    sc2 = {}
    for lc,t in sc.items():
        if t == '>':
            nlc = ((lc[0]+1)%len(input[0]), lc[1])
            if nlc in sc:
                nlc = lc
            else:
                mv = True
            sc2[nlc] = t
    for lc,t in sc.items():
        if t == 'v':
            nlc = (lc[0], (lc[1]+1)%len(input))
            if nlc in sc2 or (nlc in sc and sc[nlc] == 'v'):
                nlc = lc
            else:
                mv = True
            sc2[nlc] = t
    sc = sc2

    if not mv:
        print(stp)
        exit(0)
