from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(startx, starty):
    queue = deque([(startx, starty)])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            print(graph[x][y])
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1 #중복 큐 추가 방지를 위해 +1을 미리 해둔다.
                
               
bfs(0,0)