import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
q = list(map(int, input().split()))
deq = deque()

for i in range(n):
    new_val = q[i] # 현재 숫자
    
    # 나보다 큰 애들 다 제거
    while deq and deq[-1][0] > new_val:
        deq.pop()
    
    # 내 값과 인덱스를 저장
    deq.append((new_val, i))
    
    # 가장 오래된 애 제거
    if deq[0][1] <= i - m:
        deq.popleft()
        
    # 이제 덱의 맨 앞이 무조건 최솟값!
    print(deq[0][0], end=' ')