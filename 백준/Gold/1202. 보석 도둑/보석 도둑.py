from heapq import heappush, heappop
import sys

input = sys.stdin.readline
dia_num, bag_num = map(int, input().split())
dia = []
bags = []
cand = []
cnt = 0
dia_idx = 0

for i in range(dia_num):
    w, val = map(int, input().split())
    dia.append((w, val))

for i in range(bag_num):
    bags.append(int(input()))

dia.sort() # 보석 무게순으로 정렬
bags.sort() # 가방 무게순으로 정렬

for b in bags:
    while dia_idx < dia_num and dia[dia_idx][0] <= b:
        heappush(cand, -dia[dia_idx][1])
        dia_idx += 1 # 다음 보석으로
        
    if cand:
        ans = -heappop(cand)
        cnt += ans
print(cnt)