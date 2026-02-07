from collections import deque
n, m = map(int, input().split())
queue = deque()
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

def bfs(x, y):
    queue.append((x, y, 0))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while queue:
        x, y, broken = queue.popleft()
        
        if x == n-1 and y == m-1:
            return visited[x][y][broken]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if graph[nx][ny] == 0 and visited[nx][ny][broken] == 0:
                    
                    # 현 상태가 무엇이든 그 상태를 유지하며 진행(벽을 안 부쉈으면 그 상태로,
                    # 부순 상태면 그대로.
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                    
                elif graph[nx][ny] == 1 and broken == 0:

                    # 벽을 만났으니 '벽을 부순 세계'로 이동.
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    queue.append((nx, ny, 1))


    return (-1)

print(bfs(0, 0))