def dfs(v, visited, graph):
    visited[v] = True
    cnt = 0

    for next_node in graph[v]:
        if not visited[next_node]:
            cnt += 1
            child = dfs(next_node, visited, graph)
            cnt += child

    return cnt
    

def solution(n, results):
    answer = 0
    win = {i : [] for i in range(1, n+1)}
    lose = {i : [] for i in range(1, n+1)}
    
    for res in results:
        win[res[0]].append(res[1])
        lose[res[1]].append(res[0])
        
        
    for num in range(1, n+1):
        win_visited = [False for _ in range(n+1)]
        lose_visited = [False for _ in range(n+1)]
        
        cnt1 = dfs(num, win_visited, win)
        cnt2 = dfs(num, lose_visited, lose)
        
        if cnt1 + cnt2 == n-1:
            print(num)
            answer += 1
    
    return answer