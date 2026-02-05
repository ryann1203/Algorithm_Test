from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
max_cnt = 0
queue = deque()
flag = False

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True

    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while queue:
    x, y = queue.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and visited[nx][ny] == False:
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = True
            queue.append((nx, ny))

for row in graph:
    if 0 in row:
        print(-1)
        exit()            
       
# 각 행의 최댓값들을 모은 리스트를 만들고, 그 중 최댓값 출력
ans = max([max(row) for row in graph])
print(ans - 1)
            