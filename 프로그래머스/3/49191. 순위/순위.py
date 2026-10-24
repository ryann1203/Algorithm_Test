def win_dfs(v, win_visited, win):
    win_visited[v] = True
    cnt = 0
    
    for val in win[v]:
        if not win_visited[val]:
            cnt += 1 # 다음 노드 방문했을 때 + 1
            child = win_dfs(val, win_visited, win)
            cnt = cnt + child # 추가로 발견한 노드 수를 더함.
    
    return cnt
    
    
def lose_dfs(v, lose_visited, lose):
    lose_visited[v] = True
    cnt = 0
    
    for val in lose[v]:
        if not lose_visited[val]:
            cnt += 1 # 다음 노드 방문했을 때 + 1
            child = lose_dfs(val, lose_visited, lose)
            cnt = cnt + child # 추가로 발견한 노드 수를 더함.
    
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
        
        cnt1 = win_dfs(num, win_visited, win)
        cnt2 = lose_dfs(num, lose_visited, lose)
        
        if cnt1 + cnt2 == n-1:
            print(num)
            answer += 1
    
    return answer