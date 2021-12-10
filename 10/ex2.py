import sys
input = sys.stdin.read().strip().split("\n")
ans = []
for line in input:
    stk = []
    corrupt = False
    for x in line:
        if x in [")", "]", "}", ">"]:
            if x == ")":
                if len(stk) > 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    corrupt = True
                    break
            if x == "]":
                if len(stk) > 0 and stk[-1] == '[':
                    stk.pop()
                else:
                    corrupt = True
                    break
            if x == "}":
                if len(stk) > 0 and stk[-1] == '{':
                    stk.pop()
                else:
                    corrupt = True
                    break
            if x == ">":
                if len(stk) > 0 and stk[-1] == '<':
                    stk.pop()
                else:
                    corrupt = True
                    break
        else:
            stk.append(x)
    if corrupt:
        continue
    score = 0
    for x in stk[::-1]:
        score *= 5
        if x == '(':
            score += 1
        elif x == '[':
            score += 2
        elif x == '{':
            score += 3
        elif x == '<':
            score += 4
    ans.append(score)
print(sorted(ans)[int(len(ans)/2)])
