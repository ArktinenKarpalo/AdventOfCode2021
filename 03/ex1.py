import sys
input = sys.stdin.read().strip().split("\n")
gamma = 0
epsilon = 0
for i in range(len(input[0])):
    if sum(1 if x[len(input[0])-i-1] == '1' else 0 for x in input) > len(input)/2:
        gamma |= (1<<i)
    else:
        epsilon |= (1<<i)
print(gamma*epsilon)
