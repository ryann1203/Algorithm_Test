from collections import deque
n, m = map(int, input().split())
visited = [[False]*n for _ in range(m)]

graph = []
for i in range(m):
    graph.append(list(input().strip()))
   
def bfs(startx, starty, color):
    queue = deque([(startx, starty)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited[startx][starty] = True
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False:
                if graph[nx][ny] == color:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

white = 0
blue = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j] :
            team_color = graph[i][j]
            count = bfs(i, j, team_color)
            
            if team_color == 'W':
                white += count ** 2
            else:
                blue += count ** 2
                
print(white, blue)