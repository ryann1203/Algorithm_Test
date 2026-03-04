from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n + 1)
cnt = 0
q = deque()

for i in range(1, n + 1):
    # 새로운 덩어리 발견
    if not visited[i]:
        cnt += 1 # 덩어리 개수 추가
        
        # bfs 시작
        q = deque([i])
        visited[i] = True
        
        while q:
            current = q.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

print(cnt)