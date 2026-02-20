from heapq import heappush, heappop
import sys

input = sys.stdin.readline
dia_num, bag_num = map(int, input().split())
dia = []
bags = []
cand = []
cnt = 0
dia_idx = 0 # 보석 리스트에서 가리키는 포인터

for i in range(dia_num):
    w, val = map(int, input().split())
    dia.append((w, val))

for i in range(bag_num):
    bags.append(int(input()))

dia.sort() # 보석 무게순으로 정렬
bags.sort() # 가방 무게순으로 정렬

for b in bags:
    while dia_idx < dia_num and dia[dia_idx][0] <= b:
        heappush(cand, -dia[dia_idx][1]) # 최대힙을 위해 가격 음수로.
        dia_idx += 1 # 다음 보석으로 포인터를 옮김
        
    if cand:
        ans = -heappop(cand) #heap에는 가격만 들어가있음.
        cnt += ans
print(cnt)