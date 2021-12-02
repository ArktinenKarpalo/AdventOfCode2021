import sys
input = list(map(lambda x: x.split(" "), sys.stdin.read().strip().split("\n")))
depth = 0
h_pos = 0
for d in input:
    if d[0] == "forward":
        h_pos += int(d[1])
    elif d[0] == "up":
        depth -= int(d[1])
    else:
        depth += int(d[1])
print(depth*h_pos)
