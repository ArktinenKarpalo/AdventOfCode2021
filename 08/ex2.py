import sys
import itertools
input = sys.stdin.read().strip().split("\n")
fl2 = {
    0b1110111: 0,
    0b0010010: 1,
    0b1011101: 2,
    0b1011011: 3,
    0b0111010: 4,
    0b1101011: 5,
    0b1101111: 6,
    0b1010010: 7,
    0b1111111: 8,
    0b1111011: 9
}

ans = 0
for x in input:
    input1, input2 = map(str.split, x.split("|"))
    for perm in itertools.permutations([1<<x for x in range(7)]):
        cont = True
        for num in input1+input2:
            msk = 0
            for lt in (ord(x)-ord('a') for x in num):
                msk |= perm[lt]
            if msk not in fl2:
                cont = False
        if not cont:
            continue
        nf = 0
        for num in input2:
            msk = 0
            for lt in (ord(x)-ord('a') for x in num):
                msk |= perm[lt]
            nf *= 10
            nf += fl2[msk]
        ans += nf
        break
print(ans)

