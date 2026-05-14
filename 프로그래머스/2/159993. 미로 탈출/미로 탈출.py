from collections import deque

def bfs(maps, queue, visited, n, m):
    flag = False
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while queue:
        x, y, t = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (0 <= nx < n and 0 <= ny < m) and (maps[nx][ny] != "X" and not visited[nx][ny]):
                if flag and maps[nx][ny] == "E":
                    return t+1
            
                queue.append([nx, ny, t+1])
                visited[nx][ny] = True
                if maps[nx][ny] == "L": 
                    flag = True
                    visited = [[False] * m for _ in range(n)]
                    queue.clear()
                    queue.append([nx, ny, t+1])
                    visited[nx][ny] = True
                    break
                    
    return -1

def solution(maps):
    answer = 0
    t = 0
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                queue.append([i,j,0])
                visited[i][j] = True
                break
    
    answer = bfs(maps, queue, visited, n, m)
    
    return answer