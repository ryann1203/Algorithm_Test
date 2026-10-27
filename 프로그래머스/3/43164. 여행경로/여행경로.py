def dfs(visited, dic, start, ans, tickets):
    if len(tickets) + 1 == len(ans): # 만약 tickets보다 1이 더 크다면
        return True # 완주 성공
    
    for i, val in enumerate(dic[start]):
        if not visited[start][i]: # 지금 노드에서 가려는 곳 안 들렀니? -> True
            visited[start][i] = True # True 하고 호출.     
            ans.append(val)
            
            if dfs(visited, dic, val, ans, tickets):
                return True  # 성공했으면 취소하지 않고 종료
    
            # 실패해서 돌아왔으므로 여기서 했던 거 취소.
            ans.pop()
            visited[start][i] = False
            
    return False
        
def solution(tickets):
    sets = set()

    for val in tickets:
        for items in val:
            sets.add(items)

    dic = {s: [] for s in sets}
    visited = {s: [] for s in sets}

    for val in tickets:
        dic[val[0]].append(val[1])
        visited[val[0]].append(False) # dic과 visited 초기화까진 됨.

    # 알파벳 순서가 앞선 경로부터 탐색
    for key in dic:
        dic[key].sort()
        
    ans = ["ICN"]
    dfs(visited, dic, "ICN", ans, tickets) # ICN 노드에서 시작하겠다!

    return ans