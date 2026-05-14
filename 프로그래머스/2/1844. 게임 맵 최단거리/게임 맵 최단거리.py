from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append([0,0,1])
    visited[0][0] = True
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while queue:
        x, y, d = queue.popleft()
        if x == n-1 and y == m-1: return d
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]:
                queue.append([nx, ny, d+1])
                visited[nx][ny] = True          
    
    return -1