import sys
input = list(map(int, sys.stdin.read().split(",")))
print(min(sum(abs(x-i)*(abs(x-i)+1)/2 for x in input) for i in range(0, max(input)+1)))
