import sys
input = sys.stdin.readline
from itertools import *
from collections import deque

n, m = map(int, input().split())
arr = []; copyarr = []; cand = []; ans = []; q = deque(); q2 = deque()
answer = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    for k in range(m):
        if arr[i][k] == 0:
            cand.append((i,k))
        elif arr[i][k] == 2:
            q.append((i,k))
            
copyarr = [row[:] for row in arr]
q2 = deque(q)

def bfs(copyarr, q):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and copyarr[nx][ny] == 0:
                copyarr[nx][ny] = 2
                q.append((nx, ny))
                
    return copyarr
    
setup = list(combinations(cand, 3))

for i in range(len(setup)):
    
    copyarr = [row[:] for row in arr]
    cnt = 0
    q = deque(q2)
    
    for sets in setup[i]:
        copyarr[sets[0]][sets[1]] = 1 
        
    ans = bfs(copyarr, q)
    for c in ans:
        for i in range(m):
            if c[i] == 0:
                cnt += 1
    answer = max(cnt, answer)

print(answer)