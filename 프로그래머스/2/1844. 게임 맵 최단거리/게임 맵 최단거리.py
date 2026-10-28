from collections import deque

def solution(maps):
    answer = 1
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    queue = deque([(0,0,1)])
    
    while queue:
        x, y, d = queue.popleft()
        answer += 1
        if x == n-1 and y == m-1 :
            return d
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                
                queue.append((nx, ny, d+1))

    return -1