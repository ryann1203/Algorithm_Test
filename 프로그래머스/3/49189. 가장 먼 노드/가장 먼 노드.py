from collections import deque

def bfs(graph, start, visited, cnt):
    queue = deque([start])
    visited[start] = True
    
    dist = [0]*len(visited)
    
    while queue:  
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                dist[i] = dist[v] + 1
                visited[i] = True
                
    maxd = max(dist)
    
    for d in dist:
        if d == maxd:
            cnt += 1
    
    return cnt
        

def solution(n, edge):
    answer = 0
    cnt = 0
    max_cnt = 0
    graph = {i+1: [] for i in range(n)}
    visited = [False for _ in range(n+1)]
    
    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])    
    answer = bfs(graph, 1, visited, cnt)
    
    return answer