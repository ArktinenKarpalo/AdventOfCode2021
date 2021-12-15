import sys
import queue
input = sys.stdin.read().strip().split("\n")

pq = queue.PriorityQueue()
pq.put([-int(input[0][0]),(0,0)])
vis = set()
while True:
    cur = pq.get()
    if cur[1] in vis or cur[1][0] < 0 or cur[1][1] < 0 or cur[1][0] >= 100 or cur[1][1] >= 100:
        continue
    cur[0] += int(input[cur[1][0]][cur[1][1]])
    vis.add(cur[1])
    pq.put([cur[0], (cur[1][0]+1, cur[1][1])])
    pq.put([cur[0], (cur[1][0]-1, cur[1][1])])
    pq.put([cur[0], (cur[1][0], cur[1][1]+1)])
    pq.put([cur[0], (cur[1][0], cur[1][1]-1)])
    if cur[1] == (100-1,100-1):
        print(cur[0])
        exit(0)
