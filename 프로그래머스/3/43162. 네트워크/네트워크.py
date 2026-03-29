def dfs(n, node, computers, visited):
    visited[node] = True # 현재 노드는 visited
    for i in range(n):
        if i != node and computers[node][i] == 1 and not visited[i]:
            dfs(n, i, computers, visited)

            
def solution(n, computers):
    count = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(n, i, computers, visited)
            count += 1
    
    return count