import sys 
input = sys.stdin.readline

from heapq import heappush, heappop

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, x)
        