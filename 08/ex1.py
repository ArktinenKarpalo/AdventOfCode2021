import sys
input = sys.stdin.read().strip().split("\n")
ans = 0
for x in input:
    input1, input2 = map(str.split, x.split("|"))
    ans += sum(1 for x in input2 if len(x) in [2, 4, 3, 7])
print(ans)

