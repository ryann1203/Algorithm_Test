def dfs(graph, v, visited):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)

def solution(n, computers):
    cnt = 0
    com = len(computers)
    visited = [False for _ in range(n)]
    graph = [[] for _ in range(n)]
    for k in range(com):
        for i in range(com):
            if i!=k and computers[k][i] and (i not in graph[k]):
                graph[k].append(i)
    
    for i in range(com):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1
    
    return cnt