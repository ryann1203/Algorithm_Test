# 그룹의 개수 구하기
from collections import deque
import sys
input = sys.stdin.readline
arr = []

def bfs(x, y, n, m, graph, visited):
    q = deque()
    q.append((x, y))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] == 1:
                q.append((nx, ny)) # 1이면 q에 추가한다.
                visited[nx][ny] = True


def set_graph():
    ans = 0
    m, n, k = map(int, input().split()) # m이 열, n이 행
    graph = [[0]*(m+1) for _ in range(n+1) ]
    visited = [[False]*(m+1) for _ in range(n+1)]
    
    for i in range(k):
        a,b=map(int, input().split())
        graph[b][a] = 1

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1 and not visited[x][y]:
                ans += 1
                visited[x][y] = True
                bfs(x, y, n, m, graph, visited)

    return ans


cnt = int(input())
while cnt:
    print(set_graph())
    cnt -= 1