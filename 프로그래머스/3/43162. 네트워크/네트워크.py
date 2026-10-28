def dfs(dic, start, visited):
    visited[start] = True
    
    for nodes in dic[start]:
        if not visited[nodes]:
            dfs(dic, nodes, visited)
    
    return 1

def solution(n, computers):
    answer = 0
    dic = {i : [] for i in range(n)}
    visited = [False for _ in range(n)]
    
    # dictionary 설정
    for idx, com in enumerate(computers):
        for i in range(n):
            if idx != i and com[i]:
                dic[idx].append(i)
    
    for dics in dic:
        for val in dic[dics]:
            if not visited[val]: 
                answer += dfs(dic, val, visited) 
    
    answer += visited.count(False)
                
    return answer