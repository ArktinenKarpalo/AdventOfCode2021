import sys
input = sys.stdin.read().strip().split("\n")
ans = 0
for line in input:
    stk = []
    for x in line:
        if x in [")", "]", "}", ">"]:
            if x == ")":
                if len(stk) > 0 and stk[-1] == '(':
                    stk.pop()
                else:
                    ans += 3
                    break
            if x == "]":
                if len(stk) > 0 and stk[-1] == '[':
                    stk.pop()
                else:
                    ans += 57
                    break
            if x == "}":
                if len(stk) > 0 and stk[-1] == '{':
                    stk.pop()
                else:
                    ans += 1197
                    break
            if x == ">":
                if len(stk) > 0 and stk[-1] == '<':
                    stk.pop()
                else:
                    ans += 25137
                    break
        else:
            stk.append(x)
print(ans)
