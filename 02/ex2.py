import sys
input = list(map(lambda x: x.split(" "), sys.stdin.read().strip().split("\n")))
depth = 0
h_pos = 0
aim = 0
for d in input:
    if d[0] == "forward":
         h_pos += int(d[1])
         depth += int(d[1])*aim
    elif d[0] == "up":
        aim -= int(d[1])
    else:
        aim += int(d[1])
print(depth*h_pos)
