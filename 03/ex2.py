import sys
input = sys.stdin.read().strip().split("\n")
def fil(input, b):
    for i in range(len(input[0])):
        if (sum(1 for x in input if x[i] == '1') >= len(input)/2) == b:
            input = list(filter(lambda x: x[i] == "1", input))
        else:
            input = list(filter(lambda x: x[i] == "0", input))
        if len(input) == 1:
            return input[0]
print(int(fil(list(input), False), 2)*int(fil(input, True), 2))
