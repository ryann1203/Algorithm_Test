n = int(input())

graph = []
result = []
ans = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    graph.append(list(map(int, input().strip())))
    
def dfs(x, y):
    visited[x][y] = True
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
            if not visited[nx][ny]:
                count += dfs(nx, ny)
              
    return count
                

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            result.append(dfs(i, j))
            ans += 1

result.sort()
print(ans)
for r in result:
    print(r)
        